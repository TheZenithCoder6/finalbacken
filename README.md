# 🎨 Art Gallery – Full Stack Art E‑commerce Platform

A modern, full‑stack web application for an art gallery that allows users to browse artworks, view artist profiles, make purchases, and manage inventory. The platform features a rich, interactive frontend with visualisations and a robust backend API with authentication, product management, and payment readiness.

## ✨ Key Features

### 🖥️ Frontend (Next.js)
- **Smooth UI/UX**: Built with Next.js 16 (App Router) and Tailwind CSS for responsive, mobile‑first design.
- **Advanced Animations**: GSAP and Framer Motion power scroll‑triggered effects, parallax, and micro‑interactions.
- **Touch‑Friendly Carousels**: Swiper.js for smooth, responsive sliders.
- **Dark / Light Mode**: Toggle themes instantly with `next-themes`.
- **AI Integration**: Google Generative AI (Gemini) and Groq SDK provide smart recommendations or art descriptions.
- **Payment Gateway**: Razorpay integration for secure checkout.

### ⚙️ Backend (Django REST Framework)
- **RESTful API**: Built with Django 5.2 and DRF 3.15 – serves product, artist, and order data.
- **User Authentication**: JWT authentication via `djangorestframework-simplejwt` (login, signup, token refresh).
- **Admin Panel**: Full Django admin to manage products, artists, users, and orders.
- **Database**: PostgreSQL (production) – scalable and reliable.
- **CORS Support**: Configured to allow requests from the Next.js frontend.
- **Static Files**: Served via Whitenoise, ready for deployment.
- **Deployment Ready**: Configured for Vercel (frontend) and Python‑compatible hosts (backend).

## 🛠️ Tech Stack

| Area | Technology |
|------|------------|
| **Frontend Framework** | Next.js 16 (React 19) |
| **Styling** | Tailwind CSS, `clsx`, PostCSS |
| **Animations / 3D** | GSAP, Framer Motion, |
| **Carousels** | Swiper.js, Lenis (smooth scroll) |
| **Backend** | Django 5.2, Django REST Framework |
| **Database** | PostgreSQL (with psycopg2) |
| **Authentication** | JWT (SimpleJWT) |
| **Payment** | Razorpay SDK |
| **AI Services** | Google Gemini AI, Groq SDK |
| **Deployment** | Vercel (frontend) + Python host (backend) |
| **Other Tools** | Whitenoise, Gunicorn, Python‑dotenv |

## 📁 Project Structure (Simplified)
finalfrontend/ # Next.js frontend
├── app/ # App Router pages
├── components/ # Reusable UI components
├── public/ # Static assets
├── styles/ # Global styles
├── next.config.ts # Image domains & Swiper transpilation
├── tailwind.config.js # Custom animations
└── package.json

finalbacken/ # Django backend
├── backend/ # Project settings (settings.py, wsgi.py)
├── shop/ # Main app (models, views, admin)
│ ├── models.py # Product, Artist, User models
│ ├── views.py # API endpoints (DRF)
│ ├── admin.py # Admin panel customisations
│ └── ...
├── manage.py
├── requirements.txt # Django, DRF, PostgreSQL driver, etc.
├── vercel.json # Vercel deployment config for Python
└── runtime.txt # Python 3.11


## 🚀 Getting Started

### Prerequisites
- Node.js 20+ (for frontend)
- Python 3.11 (for backend)
- PostgreSQL (or use SQLite for local testing)

### Frontend Setup

```bash
# Clone frontend repo
git clone https://github.com/TheZenithCoder6/finalfrontend.git
cd finalfrontend

# Install dependencies
npm install

# Create .env.local (add API keys for AI, Razorpay, backend URL)
# Example:
# NEXT_PUBLIC_BACKEND_URL=http://localhost:8000/api
# RAZORPAY_KEY_ID=your_key

# Run dev server
npm run dev

Backend setup

# Clone backend repo (if separate)
git clone https://github.com/TheZenithCoder6/finalbacken.git
cd finalbacken

# Create virtual environment
python -m venv venv
source venv/bin/activate   # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt

# Set up environment variables – create .env file
# Example:
# DATABASE_URL=postgresql://user:pass@localhost:5432/artgallery
# SECRET_KEY=your-secret-key

# Run migrations
python manage.py migrate

# Load sample data (optional)
python manage.py loaddata data_utf8.json   # products, artists, users

# Create superuser for admin panel
python manage.py createsuperuser

# Start backend server
python manage.py runserver


📦 Important Backend Models (from data_utf8.json)
User – custom fields; supports admin and regular users.

Product – fields: name, description, price, image URL, category, artist, dimensions, stock, availability.

Artist – fields: name, genre, DOB, image, about, short bio, featured (is_top).

Session – for user login sessions

🔗 API Endpoints (Examples)
Endpoint	Method	Description
/api/products/	GET	List all products
/api/products/<id>/	GET	Retrieve single product
/api/artists/	GET	List all artists
/api/token/	POST	Obtain JWT token (login)
/api/token/refresh/	POST	Refresh JWT token
Note: Full API documentation (if implemented) would go here.

🌐 Deployment
Frontend (Vercel)
Connect GitHub repo to Vercel.

Set environment variables (NEXT_PUBLIC_BACKEND_URL, etc.).

Deploy automatically on push.

Backend (Vercel / Python host)
The included vercel.json is configured to serve the Django app via @vercel/python.

Environment variables (DATABASE_URL, SECRET_KEY) must be set in Vercel dashboard.

For production, consider using Heroku, Railway, or a VPS for better performance with PostgreSQL.
