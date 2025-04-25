from fastapi import APIRouter, HTTPException
from app.models.user import User
from app.database import supabase
from app.models.user import User, UserUpdate  # Import the new model

router = APIRouter(prefix="/profile", tags=["profile"])

# Get user profile
@router.get("/{user_id}", response_model=User)
async def get_profile(user_id: int):
    response = supabase.table("users").select("*").eq("id", user_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="User not found")
    return response.data[0]



@router.put("/{user_id}")
async def update_profile(
    user_id: int, 
    user: UserUpdate  # Use UserUpdate instead of User
):
    update_data = user.dict(exclude_unset=True)  # Only include provided fields
    response = supabase.table("users").update(update_data).eq("id", user_id).execute()
    if not response.data:
        raise HTTPException(status_code=400, detail="Update failed")
    return {"status": "success", "updated_data": response.data[0]}