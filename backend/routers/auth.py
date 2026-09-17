# -*- coding: utf-8 -*-
"""
Authentication & User Sessions Router
"""

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
import sqlite3
from ..database import get_db_connection

router = APIRouter(prefix="/api/auth", tags=["Authentication"])

class LoginRequest(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    full_name: str
    role: str
    email: str
    student_id: Optional[str] = None

@router.post("/login")
def login(req: LoginRequest):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT u.id, u.username, u.full_name, u.role, u.email, u.password_hash, s.student_id
    FROM users u
    LEFT JOIN students s ON u.id = s.user_id
    WHERE u.username = ?;
    """, (req.username.strip(),))
    user = cursor.fetchone()
    conn.close()

    if not user or user["password_hash"] != req.password.strip():
        raise HTTPException(status_code=401, detail="اسم المستخدم أو كلمة المرور غير صحيحة")

    return {
        "status": "success",
        "message": f"مرحباً بك، {user['full_name']}",
        "user": {
            "id": user["id"],
            "username": user["username"],
            "full_name": user["full_name"],
            "role": user["role"],
            "email": user["email"],
            "student_id": user["student_id"]
        },
        "token": f"lusail-auth-token-{user['id']}-xyz"
    }

@router.get("/me/{user_id}")
def get_current_user(user_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT u.id, u.username, u.full_name, u.role, u.email, s.student_id, s.college, s.major, s.gpa
    FROM users u
    LEFT JOIN students s ON u.id = s.user_id
    WHERE u.id = ?;
    """, (user_id,))
    user = cursor.fetchone()
    conn.close()

    if not user:
        raise HTTPException(status_code=404, detail="المستخدم غير موجود")

    return dict(user)
