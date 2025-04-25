# x-MED

# x-MED Backend API  

## **📌 Project Overview**  
FastAPI backend for an online pharmacy demo. Features product management, user profiles, and admin controls.  

## **🗃️ Database Structure**  
All tables are stored in **Supabase (PostgreSQL)**.  

### **1. `products` Table**  
| Column | Type | Description |  
|--------|------|-------------|  
| `id` | `int8` | Auto-incremented primary key |  
| `name` | `text` | Medicine name (e.g., "Aspirin") |  
| `description` | `text` | Short description |  
| `price` | `float8` | Price (e.g., `5.99`) |  
| `category` | `text` | E.g., "Painkiller", "Antibiotic" |  
| `diagnosis` | `text` | E.g., "Headache", "Fever" |  
| `image_url` | `text` | URL of product image |  
| `is_featured` | `bool` | `true` for homepage display |  

### **2. `users` Table**  
| Column | Type | Description |  
|--------|------|-------------|  
| `id` | `int8` | Auto-incremented primary key |  
| `name` | `text` | User's full name |  
| `email` | `text` | Unique user email |  
| `phone` | `text` | Contact number |  
| `place` | `text` | User's location |  
| `profile_pic_url` | `text` | Optional profile image URL |  

### **3. `settings` Table**  
| Column | Type | Description |  
|--------|------|-------------|  
| `key` | `text` | Primary key (e.g., "banner", "email") |  
| `value` | `text` | Stored data (e.g., URLs, contact info) |  

**Example Settings Data**:  
| `key` | `value` |  
|-------|---------|  
| `about` | `x-MED is a demo...` |  
| `banner` | `https://example.com/banner.jpg` |  
| `email` | `contact@xmed.example` |  
| `phone1` | `+1 123-456-7890` |  


---

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

