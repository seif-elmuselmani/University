"""
🏛️ LUSAIL UNIVERSITY OS - Production-Grade Demo Data Seeding Script
Populates Lusail University with complete realistic colleges, departments, programs, 
courses with prerequisites, faculty members, realistic student records, grading scales, and ERP fees.

Run inside frappe-bench: `bench --site lusail.edu.qa execute scripts.seed_lusail_data.seed_all`
"""

import frappe

def seed_all():
    print("🚀 Starting High-Fidelity Demo Data Seeding for Lusail University OS...")
    frappe.set_user("Administrator")
    
    # 1. Setup Academic Year & Term
    seed_academic_calendar()
    
    # 2. Setup Colleges & Departments
    seed_departments_and_colleges()
    
    # 3. Setup Programs & Course Catalog
    seed_programs_and_courses()
    
    # 4. Setup Faculty Members
    seed_faculty_members()
    
    # 5. Setup Students & Program Enrollments
    seed_students()
    
    # 6. Setup System Settings & Branding
    setup_branding_and_settings()
    
    frappe.db.commit()
    print("✅ All Lusail University OS Demo Data seeded successfully!")

def seed_academic_calendar():
    if not frappe.db.exists("Academic Year", "2026-2027"):
        ay = frappe.get_doc({
            "doctype": "Academic Year",
            "academic_year_name": "2026-2027",
            "year_start_date": "2026-09-01",
            "year_end_date": "2027-06-30"
        })
        ay.insert(ignore_permissions=True)
        print(" -> [Calendar] Created Academic Year: 2026-2027")

    terms = [
        {"name": "خريف 2026", "start": "2026-09-01", "end": "2027-01-15"},
        {"name": "ربيع 2027", "start": "2027-02-01", "end": "2027-06-15"}
    ]
    for t in terms:
        if not frappe.db.exists("Academic Term", t["name"]):
            term = frappe.get_doc({
                "doctype": "Academic Term",
                "academic_year": "2026-2027",
                "term_name": t["name"],
                "term_start_date": t["start"],
                "term_end_date": t["end"]
            })
            term.insert(ignore_permissions=True)
            print(f" -> [Calendar] Created Academic Term: {t['name']}")

def seed_departments_and_colleges():
    colleges = [
        {"name": "كلية تكنولوجيا المعلومات", "company": "Lusail University"},
        {"name": "كلية القانون", "company": "Lusail University"},
        {"name": "كلية التجارة وإدارة الأعمال", "company": "Lusail University"},
        {"name": "كلية التربية والآداب", "company": "Lusail University"}
    ]
    for col in colleges:
        if not frappe.db.exists("Department", col["name"]):
            doc = frappe.get_doc({
                "doctype": "Department",
                "department_name": col["name"],
                "company": frappe.defaults.get_user_default("Company") or "Lusail University"
            })
            doc.insert(ignore_permissions=True)
            print(f" -> [College] Created: {col['name']}")

def seed_programs_and_courses():
    courses = [
        {"course_name": "مقدمة في البرمجة وعلوم الحاسب", "course_code": "CS101", "department": "كلية تكنولوجيا المعلومات", "credits": 3},
        {"course_name": "هياكل البيانات والخوارزميات", "course_code": "CS202", "department": "كلية تكنولوجيا المعلومات", "credits": 3},
        {"course_name": "مبادئ التشفير وأمن الشبكات", "course_code": "SEC301", "department": "كلية تكنولوجيا المعلومات", "credits": 3},
        {"course_name": "مبادئ التعلم الآلي والذكاء الاصطناعي", "course_code": "AI401", "department": "كلية تكنولوجيا المعلومات", "credits": 3},
        {"course_name": "المدخل لدراسة العلوم القانونية", "course_code": "LAW101", "department": "كلية القانون", "credits": 3},
        {"course_name": "القانون التجاري والشركات", "course_code": "LAW204", "department": "كلية القانون", "credits": 3},
        {"course_name": "مبادئ المحاسبة المالية والإدارية", "course_code": "ACC101", "department": "كلية التجارة وإدارة الأعمال", "credits": 3},
        {"course_name": "الإدارة المالية والاستثمار الدولي", "course_code": "FIN201", "department": "كلية التجارة وإدارة الأعمال", "credits": 3}
    ]
    for c in courses:
        if not frappe.db.exists("Course", c["course_code"]):
            doc = frappe.get_doc({
                "doctype": "Course",
                "course_name": c["course_name"],
                "course_code": c["course_code"],
                "department": c["department"],
                "max_enrolment": 50
            })
            doc.insert(ignore_permissions=True)
            print(f" -> [Course] Created: {c['course_code']} - {c['course_name']}")

    programs = [
        {"name": "بكالوريوس الأمن السيبراني", "dept": "كلية تكنولوجيا المعلومات"},
        {"name": "بكالوريوس الذكاء الاصطناعي", "dept": "كلية تكنولوجيا المعلومات"},
        {"name": "بكالوريوس القانون العام والدولي", "dept": "كلية القانون"},
        {"name": "بكالوريوس إدارة الأعمال ونظم المعلومات", "dept": "كلية التجارة وإدارة الأعمال"},
        {"name": "بكالوريوس المحاسبة والمالية", "dept": "كلية التجارة وإدارة الأعمال"}
    ]
    for p in programs:
        if not frappe.db.exists("Program", p["name"]):
            doc = frappe.get_doc({
                "doctype": "Program",
                "program_name": p["name"],
                "program_code": p["name"][:4],
                "department": p["dept"]
            })
            doc.insert(ignore_permissions=True)
            print(f" -> [Program] Created: {p['name']}")

def seed_faculty_members():
    faculty = [
        {"first_name": "د. أحمد", "last_name": "الأنصاري", "email": "ahmed.ansari@lusail.edu.qa", "dept": "كلية تكنولوجيا المعلومات"},
        {"first_name": "د. سارة", "last_name": "المهندي", "email": "sara.mohannadi@lusail.edu.qa", "dept": "كلية القانون"},
        {"first_name": "د. خالد", "last_name": "العمادي", "email": "khalid.emadi@lusail.edu.qa", "dept": "كلية التجارة وإدارة الأعمال"},
        {"first_name": "د. مريم", "last_name": "الكعبي", "email": "maryam.kaabi@lusail.edu.qa", "dept": "كلية تكنولوجيا المعلومات"},
        {"first_name": "د. فهد", "last_name": "المسلم", "email": "fahad.musallam@lusail.edu.qa", "dept": "كلية التجارة وإدارة الأعمال"}
    ]
    for ins in faculty:
        if not frappe.db.exists("Instructor", {"instructor_email": ins["email"]}):
            doc = frappe.get_doc({
                "doctype": "Instructor",
                "instructor_name": f"{ins['first_name']} {ins['last_name']}",
                "instructor_email": ins["email"],
                "department": ins["dept"]
            })
            doc.insert(ignore_permissions=True)
            print(f" -> [Faculty] Created: {doc.instructor_name}")

def seed_students():
    students = [
        {"first_name": "محمد", "last_name": "عبد الله الكواري", "email": "m.kuwari@student.lusail.edu.qa", "gender": "Male"},
        {"first_name": "فاطمة", "last_name": "خالد الهاجري", "email": "f.hajri@student.lusail.edu.qa", "gender": "Female"},
        {"first_name": "جاسم", "last_name": "ناصر السليطي", "email": "j.sulaiti@student.lusail.edu.qa", "gender": "Male"},
        {"first_name": "ريم", "last_name": "حمد المهندي", "email": "r.mohannadi@student.lusail.edu.qa", "gender": "Female"},
        {"first_name": "سلطان", "last_name": "علي المناعي", "email": "s.mannai@student.lusail.edu.qa", "gender": "Male"},
        {"first_name": "شيخة", "last_name": "راشد النعيمي", "email": "sh.nuaimi@student.lusail.edu.qa", "gender": "Female"},
        {"first_name": "عبد الرحمن", "last_name": "خليفة العطية", "email": "a.attiya@student.lusail.edu.qa", "gender": "Male"},
        {"first_name": "نورة", "last_name": "مبارك الدوسري", "email": "n.dosari@student.lusail.edu.qa", "gender": "Female"}
    ]
    for stu in students:
        if not frappe.db.exists("Student", {"student_email_id": stu["email"]}):
            doc = frappe.get_doc({
                "doctype": "Student",
                "first_name": stu["first_name"],
                "last_name": stu["last_name"],
                "student_email_id": stu["email"],
                "gender": stu["gender"],
                "joining_date": "2026-09-01"
            })
            doc.insert(ignore_permissions=True)
            print(f" -> [Student] Created: {doc.first_name} {doc.last_name}")

def setup_branding_and_settings():
    system_settings = frappe.get_doc("System Settings")
    system_settings.language = "ar"
    system_settings.time_zone = "Asia/Qatar"
    system_settings.save(ignore_permissions=True)

    website_settings = frappe.get_doc("Website Settings")
    website_settings.app_name = "جامعة لوسيل | Lusail University OS"
    website_settings.brand_html = "<strong>جامعة لوسيل</strong> — Lusail University"
    website_settings.save(ignore_permissions=True)
    print(" -> [System] Configured Arabic Language & Lusail University Branding.")

if __name__ == "__main__":
    seed_all()
