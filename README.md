# x-MED

# x-MED Backend API  

## **📌 Project Overview**  
FastAPI backend for an online pharmacy demo. Features product management, user profiles, and admin controls.  

## **Endpoints**  

### **Products**  
| Endpoint | Method | Description |  
|----------|--------|-------------|  
| `/products/` | GET | List all medicines |  
| `/products/featured` | GET | Get featured products |  
| `/products/search?query=` | GET | Search by name/category/diagnosis |  

### **Admin**  
| Endpoint | Method | Description |  
|----------|--------|-------------|  
| `/admin/products/` | POST | Add new product (Admin-only) |  
| `/admin/banner/` | PUT | Update homepage banner (Admin-only) |  

### **General**  
| Endpoint | Method | Description |  
|----------|--------|-------------|  
| `/contact` | GET | Get pharmacy contact details |  
| `/about` | GET | Get company info |  


### **Profile**  
| Endpoint | Method | Description |  
|----------|--------|-------------|  
| `/profile/{id}` | GET | Get user profile details |  
| `/profile/{id}` | PUT | Update user nfo |  

## **Environment Variables**  
- `SUPABASE_URL`: Your Supabase project URL  
- `SUPABASE_KEY`: Your Supabase anon key  

## **🛠 Tech Stack**  
- **Backend**: FastAPI (Python)  
- **Database**: Supabase (PostgreSQL)  
- **Auth**: (Planned for future)  

## **⚙️ Setup**  
1. Clone the repo:  
   ```bash  
   git clone https://github.com/yourusername/x-med-backend.git  

