# -*- coding: utf-8 -*-
"""
Lusail University Unified OS - FastAPI Backend Entrypoint
Provides high-performance REST API services with clean layered architecture:
- Auth, Academics, GPA & Holds, Finance & Bursar, Admissions, and E-Services.
"""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import init_db
from .routers import auth, academic, finance, admissions, services

# Initialize Database on startup
init_db()

app = FastAPI(
    title="جامعة لوسيل - خادم المنظومة الرقمية الموحدة (Lusail University OS API)",
    description="RESTful Backend API powering Academic, Financial, Admissions, and E-Services portals.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Enable CORS for frontend portals (port 8085 and localhost)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount Routers
app.include_router(auth.router)
app.include_router(academic.router)
app.include_router(finance.router)
app.include_router(admissions.router)
app.include_router(services.router)

@app.get("/")
def root():
    return {
        "status": "online",
        "system": "جامعة لوسيل - المنظومة الرقمية الشاملة (Lusail University OS)",
        "version": "1.0.0",
        "endpoints": {
            "docs": "/docs",
            "auth": "/api/auth",
            "academic": "/api/academic",
            "finance": "/api/finance",
            "admissions": "/api/admissions",
            "services": "/api/services"
        }
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
