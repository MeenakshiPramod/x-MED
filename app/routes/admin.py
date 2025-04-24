from fastapi import APIRouter, HTTPException
from app.models.product import ProductCreate
from app.database import supabase

router = APIRouter(prefix="/admin", tags=["admin"])

# Add new product
@router.post("/products/", response_model=dict)
async def add_product(product: ProductCreate):
    response = supabase.table("products").insert(product.dict()).execute()
    if not response.data:
        raise HTTPException(status_code=400, detail="Insert failed")
    return {"status": "success", "data": response.data[0]}

# Update homepage banner
@router.put("/banner/")
async def update_banner(banner_url: str):
    response = supabase.table("settings").upsert(
        {"key": "banner", "value": banner_url}
    ).execute()
    return {"status": "banner updated"}