# -*- coding: utf-8 -*-
"""
Lusail University Clean Architecture - SQLite Database & Persistence Layer
Provides lightweight, reliable relational database storage and automatic seeding for:
- Users & Roles (Students, Faculty, Staff)
- Students, Programs & Academics
- Courses & Registrations
- Invoices & Financial Ledgers
- Admissions Applications
- Service Tickets
"""

import sqlite3
import os
import json
from typing import Dict, List, Any, Optional

DB_PATH = os.path.join(os.path.dirname(__file__), "lusail_university.db")

def get_db_connection() -> sqlite3.Connection:
    """Create and return a connection with row factory enabled."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize database tables and seed initial Lusail University dataset."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Enable foreign keys
    cursor.execute("PRAGMA foreign_keys = ON;")

    # 1. Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        full_name TEXT NOT NULL,
        role TEXT NOT NULL, -- 'student', 'faculty', 'admin', 'registrar', 'bursar'
        email TEXT UNIQUE NOT NULL,
        national_id TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 2. Students profile & academic status
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id TEXT PRIMARY KEY,
        user_id INTEGER,
        full_name TEXT NOT NULL,
        college TEXT NOT NULL,
        major TEXT NOT NULL,
        gpa REAL DEFAULT 0.00,
        earned_credits INTEGER DEFAULT 0,
        registered_credits INTEGER DEFAULT 0,
        academic_standing TEXT DEFAULT 'منتظم',
        active_holds TEXT DEFAULT '[]', -- JSON array of holds
        balance_due_qar REAL DEFAULT 0.0,
        scholarship_type TEXT DEFAULT 'NONE',
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    """)

    # 3. Courses catalog
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        course_code TEXT PRIMARY KEY,
        title_ar TEXT NOT NULL,
        title_en TEXT NOT NULL,
        college TEXT NOT NULL,
        credits INTEGER DEFAULT 3,
        prerequisites TEXT DEFAULT '[]', -- JSON array of codes
        tuition_qar REAL DEFAULT 4500.0 -- (3 credits * 1500 QAR)
    );
    """)

    # 4. Enrollments / Grades
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS enrollments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT NOT NULL,
        course_code TEXT NOT NULL,
        semester TEXT NOT NULL, -- e.g. 'خريف 2026'
        score REAL,
        letter_grade TEXT,
        grade_points REAL,
        status TEXT DEFAULT 'مسجل', -- 'مسجل', 'ناجح', 'راسب', 'منسحب'
        FOREIGN KEY (student_id) REFERENCES students(student_id),
        FOREIGN KEY (course_code) REFERENCES courses(course_code)
    );
    """)

    # 5. Invoices & Financial transactions
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS invoices (
        invoice_number TEXT PRIMARY KEY,
        student_id TEXT NOT NULL,
        semester TEXT NOT NULL,
        credits INTEGER NOT NULL,
        base_amount_qar REAL NOT NULL,
        discount_amount_qar REAL DEFAULT 0.0,
        services_fee_qar REAL DEFAULT 750.0,
        total_payable_qar REAL NOT NULL,
        paid_amount_qar REAL DEFAULT 0.0,
        payment_status TEXT DEFAULT 'مستحق', -- 'مستحق', 'مدفوع كلياً', 'مدفوع جزئياً'
        payment_reference TEXT,
        payment_date TIMESTAMP,
        FOREIGN KEY (student_id) REFERENCES students(student_id)
    );
    """)

    # 6. Admissions Applications
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admission_applications (
        application_id TEXT PRIMARY KEY,
        full_name TEXT NOT NULL,
        national_id TEXT NOT NULL,
        nationality TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        first_choice_college TEXT NOT NULL,
        first_choice_major TEXT NOT NULL,
        high_school_gpa REAL NOT NULL,
        status TEXT DEFAULT 'قيد المراجعة', -- 'قيد المراجعة', 'مقبول مبدئياً', 'مقبول نهائياً', 'مرفوض'
        submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 7. Service Tickets
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS service_tickets (
        ticket_id TEXT PRIMARY KEY,
        student_id TEXT NOT NULL,
        service_code TEXT NOT NULL,
        service_name TEXT NOT NULL,
        details TEXT,
        status TEXT DEFAULT 'قيد المعالجة', -- 'جديد', 'قيد المعالجة', 'مكتمل', 'مرفوض'
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (student_id) REFERENCES students(student_id)
    );
    """)

    conn.commit()

    # Seed Initial Data if table is empty
    cursor.execute("SELECT COUNT(*) as cnt FROM courses;")
    if cursor.fetchone()['cnt'] == 0:
        seed_data(cursor)
        conn.commit()

    conn.close()

def seed_data(cursor: sqlite3.Cursor):
    """Seed authentic initial data for Lusail University demo."""
    
    # 1. Seed Users
    users = [
        ('student1', 'pass123', 'مريم الكواري', 'student', 'maryam.k@lu.edu.qa', '29863401298'),
        ('student2', 'pass123', 'راشد الهاجري', 'student', 'rashid.h@lu.edu.qa', '29963408712'),
        ('student3', 'pass123', 'نورة الدوسري', 'student', 'noura.d@lu.edu.qa', '30063404521'),
        ('faculty1', 'pass123', 'د. خالد المناعي', 'faculty', 'k.mannai@lu.edu.qa', '28563401122'),
        ('admin1', 'admin123', 'إدارة التسجيل والقبول', 'admin', 'registrar@lu.edu.qa', '28063409988'),
        ('bursar1', 'admin123', 'الإدارة المالية والمحاسبة', 'bursar', 'finance@lu.edu.qa', '28163407766')
    ]
    cursor.executemany("""
    INSERT INTO users (username, password_hash, full_name, role, email, national_id)
    VALUES (?, ?, ?, ?, ?, ?);
    """, users)

    # 2. Seed Courses
    courses = [
        ('IT101', 'مقدمة في الحوسبة والبرمجة', 'Intro to Computing & Python', 'كلية تكنولوجيا المعلومات', 3, '[]', 4500.0),
        ('IT201', 'هياكل البيانات والخوارزميات', 'Data Structures & Algorithms', 'كلية تكنولوجيا المعلومات', 3, '["IT101"]', 4500.0),
        ('AI301', 'الذكاء الاصطناعي وتعلم الآلة', 'Artificial Intelligence & ML', 'كلية تكنولوجيا المعلومات', 3, '["IT201"]', 4500.0),
        ('LAW101', 'المدخل للعلوم القانونية', 'Intro to Legal Studies', 'كلية القانون', 3, '[]', 4500.0),
        ('LAW202', 'القانون التجاري والشركات', 'Commercial & Corporate Law', 'كلية القانون', 3, '["LAW101"]', 4500.0),
        ('BUS101', 'مبادئ إدارة الأعمال والتسويق', 'Principles of Management', 'كلية التجارة والأعمال', 3, '[]', 4500.0),
        ('FIN201', 'الإدارة المالية والمصرفية', 'Financial Management', 'كلية التجارة والأعمال', 3, '["BUS101"]', 4500.0),
        ('EDU101', 'أصول التربية والتعليم الحديث', 'Foundations of Education', 'كلية التربية والآداب', 3, '[]', 4500.0)
    ]
    cursor.executemany("""
    INSERT INTO courses (course_code, title_ar, title_en, college, credits, prerequisites, tuition_qar)
    VALUES (?, ?, ?, ?, ?, ?, ?);
    """, courses)

    # 3. Seed Students
    students = [
        ('LU-2024-0891', 1, 'مريم الكواري', 'كلية تكنولوجيا المعلومات', 'بكالوريوس الذكاء الاصطناعي', 3.92, 45, 15, 'Honor Roll (لوحة الشرف)', '[]', 0.0, 'ACADEMIC_EXCELLENCE_50'),
        ('LU-2023-1420', 2, 'راشد الهاجري', 'كلية التجارة والأعمال', 'بكالوريوس إدارة الأعمال', 3.45, 60, 15, 'Good Standing (وضع سليم)', '[]', 0.0, 'NONE'),
        ('LU-2024-0312', 3, 'نورة الدوسري', 'كلية القانون', 'بكالوريوس القانون الخاص', 3.88, 30, 15, 'Honor Roll (لوحة الشرف)', '["Financial"]', 4500.0, 'NONE')
    ]
    cursor.executemany("""
    INSERT INTO students (student_id, user_id, full_name, college, major, gpa, earned_credits, registered_credits, academic_standing, active_holds, balance_due_qar, scholarship_type)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, students)

    # 4. Seed Enrollments for Maryam Al-Kuwari
    enrollments = [
        ('LU-2024-0891', 'IT101', 'خريف 2024', 96.0, 'A+', 4.00, 'ناجح'),
        ('LU-2024-0891', 'IT201', 'ربيع 2025', 94.0, 'A', 3.75, 'ناجح'),
        ('LU-2024-0891', 'AI301', 'خريف 2026', 98.0, 'A+', 4.00, 'ناجح'),
        ('LU-2024-0891', 'BUS101', 'خريف 2026', 95.0, 'A+', 4.00, 'ناجح')
    ]
    cursor.executemany("""
    INSERT INTO enrollments (student_id, course_code, semester, score, letter_grade, grade_points, status)
    VALUES (?, ?, ?, ?, ?, ?, ?);
    """, enrollments)

    # 5. Seed Invoices
    invoices = [
        ('INV-2026-001', 'LU-2024-0891', 'خريف 2026', 15, 22500.0, 11250.0, 750.0, 12000.0, 12000.0, 'مدفوع كلياً', 'QPAY-TXN-8849102', '2026-09-01 10:30:00'),
        ('INV-2026-002', 'LU-2024-0312', 'خريف 2026', 15, 22500.0, 0.0, 750.0, 23250.0, 18750.0, 'مستحق', None, None)
    ]
    cursor.executemany("""
    INSERT INTO invoices (invoice_number, student_id, semester, credits, base_amount_qar, discount_amount_qar, services_fee_qar, total_payable_qar, paid_amount_qar, payment_status, payment_reference, payment_date)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, invoices)

    # 6. Seed Sample Admission Applications
    admissions = [
        ('APP-2026-901', 'جاسم محمد السليطي', '30263409981', 'قطري', 'jassim.s@example.qa', '+974 5512 3456', 'كلية تكنولوجيا المعلومات', 'بكالوريوس الذكاء الاصطناعي', 94.5, 'مقبول مبدئياً'),
        ('APP-2026-902', 'فاطمة أحمد الكعبي', '30163401123', 'قطرية', 'fatima.k@example.qa', '+974 6698 7711', 'كلية القانون', 'بكالوريوس القانون العام', 96.0, 'مقبول نهائياً')
    ]
    cursor.executemany("""
    INSERT INTO admission_applications (application_id, full_name, national_id, nationality, email, phone, first_choice_college, first_choice_major, high_school_gpa, status)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, admissions)

if __name__ == "__main__":
    init_db()
    print("Lusail University Database initialized successfully.")
