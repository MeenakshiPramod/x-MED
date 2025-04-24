from fastapi import APIRouter
from app.database import supabase

router = APIRouter(tags=["general"])

# Get contact info
@router.get("/contact")
async def get_contact():
    response = supabase.table("settings").select("*").in_(
        "key", ["email", "phone1", "phone2"]
    ).execute()
    
   
    print("Supabase response:", response)
    
    if not response.data:
        return {"email": "", "phone1": "", "phone2": ""}
    
    # Safely extract values
    contact_info = {item["key"]: item["value"] for item in response.data}
    return {
        "email": contact_info.get("email", ""),
        "phone1": contact_info.get("phone1", ""),
        "phone2": contact_info.get("phone2", "")
    }

# Get about info
@router.get("/about")
async def get_about():
    response = supabase.table("settings").select("value").eq(
        "key", "about"
    ).execute()
    return {"about": response.data[0]["value"]}