from fastapi import APIRouter, HTTPException
from app.models.product import Product, ProductCreate
from app.database import supabase

router = APIRouter(prefix="/products", tags=["products"])

# Get all products
@router.get("/", response_model=list[Product])
async def get_products():
    response = supabase.table("products").select("*").execute()
    return response.data

# Get featured products (for homepage)
@router.get("/featured", response_model=list[Product])
async def get_featured_products():
    response = supabase.table("products").select("*").eq("is_featured", True).limit(6).execute()
    return response.data

# Search products by name/category/diagnosis
@router.get("/search")
async def search_products(query: str):
    response = supabase.table("products").select("*").or_(
        f"name.ilike.%{query}%,category.ilike.%{query}%,diagnosis.ilike.%{query}%"
    ).execute()
    return response.data

@router.get("/{product_id}", response_model=Product)
async def get_product(product_id: int):
    response = supabase.table("products").select("*").eq("id", product_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Product not found")
    return response.data[0]