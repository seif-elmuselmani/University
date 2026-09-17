# -*- coding: utf-8 -*-
"""
Portal Stage Manager - إدارة إظهار وإخفاء الصفحات المتقدمة
"""

import os
import shutil
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PORTAL_DIR = os.path.join(BASE_DIR, "portal")
STAGED_DIR = os.path.join(BASE_DIR, "portal_staged_advanced")

ADVANCED_PAGES = [
    "desk.html",              # لوحة التحكم الإدارية
    "student-portal.html",    # بوابة الطالب الكاملة
    "research.html",          # بوابة البحث العلمي
    "career-center.html",     # مركز التوظيف والتدريب
    "library.html",           # المكتبة الرقمية
    "student-clubs.html",     # الأنشطة والنوادي الطلابية
    "services.html",          # بوابة الـ 16 خدمة الذاتية
    "campus-life.html",       # الحياة الجامعية المفصلة
    "admissions.html",        # محرك التقديم التفاعلي الكامل
    "tuition-fees.html",      # حاسبة الرسوم التفاعلية
    "architecture.html",      # المعمارية الداخلية
    "college-it.html",        # تفاصيل كلية تكنولوجيا المعلومات
    "college-business.html",  # تفاصيل كلية التجارة
    "college-education.html", # تفاصيل كلية التربية
    "college-law.html",       # تفاصيل كلية القانون
]

def ensure_staged_dir():
    if not os.path.exists(STAGED_DIR):
        os.makedirs(STAGED_DIR)

def hide_advanced_pages():
    ensure_staged_dir()
    hidden_count = 0
    for page in ADVANCED_PAGES:
        src = os.path.join(PORTAL_DIR, page)
        dst = os.path.join(STAGED_DIR, page)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            os.remove(src)
            hidden_count += 1
            print(f"[HIDDEN & SAVED] {page}")
    
    print(f"\nSuccessfully hidden {hidden_count} advanced pages.")
    print("Active on server now: (index, about, colleges, admission-requirements, academic-calendar, contact, faq)")

def restore_all_pages():
    if not os.path.exists(STAGED_DIR):
        print("No staged backup folder found.")
        return
    
    restored_count = 0
    for page in os.listdir(STAGED_DIR):
        src = os.path.join(STAGED_DIR, page)
        dst = os.path.join(PORTAL_DIR, page)
        if os.path.isfile(src):
            shutil.copy2(src, dst)
            os.remove(src)
            restored_count += 1
            print(f"[RESTORED] {page}")
    
    print(f"\nSuccessfully restored all {restored_count} pages 100%.")

def check_status():
    portal_files = [f for f in os.listdir(PORTAL_DIR) if f.endswith(".html")] if os.path.exists(PORTAL_DIR) else []
    staged_files = [f for f in os.listdir(STAGED_DIR) if f.endswith(".html")] if os.path.exists(STAGED_DIR) else []
    
    print("=" * 50)
    print(f"Active pages on portal ({len(portal_files)}):")
    for f in sorted(portal_files):
        print(f"  * {f}")
    
    print("-" * 50)
    print(f"Hidden/Staged pages ({len(staged_files)}):")
    for f in sorted(staged_files):
        print(f"  * {f}")
    print("=" * 50)

if __name__ == "__main__":
    action = sys.argv[1].lower() if len(sys.argv) > 1 else "status"
    if action == "hide":
        hide_advanced_pages()
    elif action == "restore":
        restore_all_pages()
    elif action == "status":
        check_status()
    else:
        print("Unknown action. Use: hide / restore / status")
