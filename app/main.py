from fastapi import FastAPI
from app.routes import products  
from app.routes import products, admin, general, profile 
from app.database import supabase

app = FastAPI()

# Include the product routes
app.include_router(products.router)
app.include_router(admin.router)      
app.include_router(general.router) 
app.include_router(profile.router)

@app.get("/")
def home():
    return {"message": "x-MED Pharmacy API"}


# @app.get("/test-products")
# async def test_products():
#     response = supabase.table("products").select("*").execute()
#     print("Raw Supabase response:", response)  # Check console output
#     return response