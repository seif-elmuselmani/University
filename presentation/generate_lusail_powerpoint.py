# -*- coding: utf-8 -*-
"""
Lusail University Digital Transformation Executive Pitch Deck Generator (Premium Edition)
Generates an ultra-premium, 16:9 widescreen PowerPoint presentation (.pptx).
Features:
- Dual-theme architecture: Deep Royal Navy (#004876) for Hero slides, Ultra-clean snow (#F8FAFC) for Content.
- Realistic 3D-styled browser window mockups with traffic light dots (Red/Yellow/Green) and official URLs.
- Big Stat Callouts, color-coded college badges, elevated card structures, and gold accent borders.
- 100% authentic Lusail University identity with real embedded screenshots and realistic academic scope.
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# ----------------- PALETTE & CONSTANTS -----------------
NAVY = RGBColor(0, 72, 118)          # #004876 (Lusail Royal Navy)
DARK_NAVY = RGBColor(0, 45, 74)      # #002D4A (Deep Dark Navy)
MID_NAVY = RGBColor(0, 95, 158)      # #005F9E
GOLD = RGBColor(190, 156, 121)       # #be9c79 (Lusail Warm Gold)
LIGHT_GOLD = RGBColor(245, 238, 227) # #F5EEE3
BG_LIGHT = RGBColor(248, 250, 252)   # #F8FAFC (Snow Canvas)
CARD_BG = RGBColor(255, 255, 255)    # #FFFFFF
CARD_SHADOW = RGBColor(226, 232, 240)# #E2E8F0
TEXT_DARK = RGBColor(15, 23, 42)     # #0F172A
TEXT_MUTED = RGBColor(71, 85, 105)   # #475569
BORDER_COLOR = RGBColor(226, 232, 240) # #E2E8F0

# Traffic light dots for browser frames
DOT_RED = RGBColor(248, 113, 113)    # #F87171
DOT_YELLOW = RGBColor(251, 191, 36)  # #FBBF24
DOT_GREEN = RGBColor(52, 211, 153)   # #34D399
BROWSER_BAR = RGBColor(241, 245, 249)# #F1F5F9

# College Accent Colors
COL_LAW = RGBColor(73, 170, 118)     # #49AA76
COL_BIZ = RGBColor(150, 45, 63)      # #962D3F
COL_IT = RGBColor(95, 18, 89)        # #5F1259
COL_EDU = RGBColor(0, 59, 77)        # #003B4D
ACCENT_GREEN = RGBColor(22, 163, 74) # #16A34A

FONT_TITLE = "Segoe UI"
FONT_BODY = "Segoe UI"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "img")

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Helper: Base light content slide
    def add_base_slide(title_text="", category_text="جامعة لوسيل | المنظومة الرقمية الشاملة 2026/2027", slide_num=""):
        slide = prs.slides.add_slide(blank_layout)
        
        # Background canvas
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_LIGHT
        bg.line.fill.background()
        
        # Elegant Top Header Ribbon (Gold + Navy dual line)
        top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.12))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = NAVY
        top_bar.line.fill.background()
        
        top_gold = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(10.0), 0, Inches(3.333), Inches(0.12))
        top_gold.fill.solid()
        top_gold.fill.fore_color.rgb = GOLD
        top_gold.line.fill.background()

        if title_text:
            header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.28), Inches(11.733), Inches(1.15))
            tf = header_box.text_frame
            tf.word_wrap = True
            tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
            
            p_cat = tf.paragraphs[0]
            p_cat.text = category_text
            p_cat.font.size = Pt(10.5)
            p_cat.font.bold = True
            p_cat.font.color.rgb = GOLD
            p_cat.font.name = FONT_TITLE
            p_cat.alignment = PP_ALIGN.RIGHT

            p_title = tf.add_paragraph()
            p_title.text = title_text
            p_title.font.size = Pt(21)
            p_title.font.bold = True
            p_title.font.color.rgb = NAVY
            p_title.font.name = FONT_TITLE
            p_title.alignment = PP_ALIGN.RIGHT

        # Polished Footer Bar
        foot_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(7.0), Inches(11.733), Inches(0.02))
        foot_line.fill.solid()
        foot_line.fill.fore_color.rgb = BORDER_COLOR
        foot_line.line.fill.background()

        footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(11.733), Inches(0.35))
        ft_tf = footer_box.text_frame
        ft_tf.word_wrap = True
        ft_tf.margin_left = ft_tf.margin_top = ft_tf.margin_right = ft_tf.margin_bottom = 0
        p_ft = ft_tf.paragraphs[0]
        p_ft.text = f"جامعة لوسيل - المقترح التنفيذي الرسمي للتحول الأكاديمي الشامل 2026/2027 | وثيقة سرية لمجلس الأمناء      {slide_num}"
        p_ft.font.size = Pt(9)
        p_ft.font.color.rgb = TEXT_MUTED
        p_ft.font.name = FONT_BODY
        p_ft.alignment = PP_ALIGN.RIGHT

        return slide

    # Helper: Elevated Card with simulated shadow
    def add_card(slide, left, top, width, height, title="", subtitle="", bg_color=CARD_BG, border=BORDER_COLOR, title_color=NAVY):
        # Card body
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        if border:
            shape.line.color.rgb = border
            shape.line.width = Pt(1.2)
        else:
            shape.line.fill.background()
            
        if title or subtitle:
            tf = shape.text_frame
            tf.word_wrap = True
            tf.margin_left = Inches(0.2)
            tf.margin_right = Inches(0.2)
            tf.margin_top = Inches(0.15)
            tf.margin_bottom = Inches(0.15)
            if title:
                p = tf.paragraphs[0]
                p.text = title
                p.font.bold = True
                p.font.size = Pt(12)
                p.font.color.rgb = title_color
                p.font.name = FONT_TITLE
                p.alignment = PP_ALIGN.RIGHT
            if subtitle:
                p2 = tf.add_paragraph()
                p2.text = subtitle
                p2.font.size = Pt(10)
                p2.font.color.rgb = TEXT_MUTED
                p2.font.name = FONT_BODY
                p2.alignment = PP_ALIGN.RIGHT
        return shape

    # Helper: Realistic 3D Browser Mockup Window
    def add_browser_window(slide, img_name, left, top, width, height, url="https://lu.edu.qa", caption=""):
        img_path = os.path.join(IMG_DIR, img_name)
        bar_h = Inches(0.35)
        
        # Outer container
        container = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        container.fill.solid()
        container.fill.fore_color.rgb = CARD_BG
        container.line.color.rgb = BORDER_COLOR
        container.line.width = Pt(1.5)
        
        # Browser top bar
        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, bar_h)
        bar.fill.solid()
        bar.fill.fore_color.rgb = BROWSER_BAR
        bar.line.color.rgb = BORDER_COLOR
        bar.line.width = Pt(1)
        
        # 3 Traffic dots
        dot_y = top + Inches(0.12)
        d_rad = Inches(0.1)
        
        d1 = slide.shapes.add_shape(MSO_SHAPE.OVAL, left + Inches(0.15), dot_y, d_rad, d_rad)
        d1.fill.solid(); d1.fill.fore_color.rgb = DOT_RED; d1.line.fill.background()
        
        d2 = slide.shapes.add_shape(MSO_SHAPE.OVAL, left + Inches(0.32), dot_y, d_rad, d_rad)
        d2.fill.solid(); d2.fill.fore_color.rgb = DOT_YELLOW; d2.line.fill.background()
        
        d3 = slide.shapes.add_shape(MSO_SHAPE.OVAL, left + Inches(0.49), dot_y, d_rad, d_rad)
        d3.fill.solid(); d3.fill.fore_color.rgb = DOT_GREEN; d3.line.fill.background()
        
        # URL pill box in center
        url_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left + Inches(0.7), top + Inches(0.06), width - Inches(0.9), Inches(0.23))
        url_box.fill.solid(); url_box.fill.fore_color.rgb = CARD_BG
        url_box.line.color.rgb = BORDER_COLOR; url_box.line.width = Pt(0.75)
        utf = url_box.text_frame
        utf.margin_top = utf.margin_bottom = utf.margin_left = utf.margin_right = 0
        up = utf.paragraphs[0]
        up.text = f"🔒 {url}"
        up.font.size = Pt(8)
        up.font.color.rgb = TEXT_MUTED
        up.alignment = PP_ALIGN.CENTER
        
        # Embedded image
        if os.path.exists(img_path):
            img_top = top + bar_h + Inches(0.04)
            img_h = height - bar_h - Inches(0.32 if caption else 0.08)
            img_w = width - Inches(0.08)
            slide.shapes.add_picture(img_path, left + Inches(0.04), img_top, img_w, img_h)
            
        if caption:
            c_box = slide.shapes.add_textbox(left, top + height - Inches(0.28), width, Inches(0.28))
            ctf = c_box.text_frame
            ctf.margin_top = ctf.margin_bottom = ctf.margin_left = ctf.margin_right = 0
            cp = ctf.paragraphs[0]
            cp.text = caption
            cp.font.size = Pt(8.5)
            cp.font.bold = True
            cp.font.color.rgb = NAVY
            cp.alignment = PP_ALIGN.CENTER

    # Helper: Big Stat Callout Card
    def add_stat_callout(slide, left, top, width, height, number, label, subtext="", border_col=GOLD):
        card = add_card(slide, left, top, width, height, border=border_col)
        tf = card.text_frame
        tf.margin_left = tf.margin_right = Inches(0.15)
        tf.margin_top = Inches(0.1)
        
        p0 = tf.paragraphs[0]
        p0.text = number
        p0.font.bold = True
        p0.font.size = Pt(26)
        p0.font.color.rgb = NAVY
        p0.alignment = PP_ALIGN.CENTER
        
        p1 = tf.add_paragraph()
        p1.text = label
        p1.font.bold = True
        p1.font.size = Pt(10.5)
        p1.font.color.rgb = TEXT_DARK
        p1.alignment = PP_ALIGN.CENTER
        
        if subtext:
            p2 = tf.add_paragraph()
            p2.text = subtext
            p2.font.size = Pt(8.5)
            p2.font.color.rgb = GOLD
            p2.alignment = PP_ALIGN.CENTER

    # ==================== SLIDE 1: ULTRA-LUXURY EXECUTIVE COVER ====================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid(); bg1.fill.fore_color.rgb = NAVY; bg1.line.fill.background()

    # Right side decorative geometric bar
    deco1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.0), Inches(0.12), Inches(5.5))
    deco1.fill.solid(); deco1.fill.fore_color.rgb = GOLD; deco1.line.fill.background()

    # Left content box
    c_box = s1.shapes.add_textbox(Inches(1.1), Inches(1.0), Inches(6.3), Inches(5.5))
    c_tf = c_box.text_frame
    c_tf.word_wrap = True

    p0 = c_tf.paragraphs[0]
    p0.text = "المقترح الاستراتيجي المعتمد للتطوير المؤسسي | جامعة لوسيل"
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = GOLD
    p0.alignment = PP_ALIGN.RIGHT

    p1 = c_tf.add_paragraph()
    p1.text = "منظومة تشغيل جامعة لوسيل الأكاديمية الموحدة"
    p1.font.size = Pt(28)
    p1.font.bold = True
    p1.font.color.rgb = CARD_BG
    p1.alignment = PP_ALIGN.RIGHT

    p2 = c_tf.add_paragraph()
    p2.text = "Lusail University OS (2026/2027) - Executive Showcase"
    p2.font.size = Pt(14)
    p2.font.color.rgb = LIGHT_GOLD
    p2.alignment = PP_ALIGN.RIGHT

    p3 = c_tf.add_paragraph()
    p3.text = "\nبوابة أكاديمية سيادية موحدة تضم 21 صفحة تخصصية جاهزة للعمل، تدعم الكليات الـ 4 والبرامج الـ 17 المعتمدة، وأتمتة 16 خدمة ذاتية بالـ QR Code، مع لوحة تحكم المسجل العام (Desk OS) ومحرك احتساب المعدل 4.00."
    p3.font.size = Pt(11)
    p3.font.color.rgb = RGBColor(226, 232, 240)
    p3.alignment = PP_ALIGN.RIGHT

    p4 = c_tf.add_paragraph()
    p4.text = "\nمجلس الأمناء: سعادة د. علي بن فطيس المري | رئيس الجامعة: أ.د. نظام هندي"
    p4.font.size = Pt(10)
    p4.font.bold = True
    p4.font.color.rgb = GOLD
    p4.alignment = PP_ALIGN.RIGHT

    # Real Screenshot embedded in a realistic browser frame on the cover
    add_browser_window(s1, "screen_home.png", Inches(7.7), Inches(1.0), Inches(4.8), Inches(5.5), 
                       url="https://lu.edu.qa", caption="الواجهة الرئيسية الحية لمنظومة جامعة لوسيل")

    # ==================== SLIDE 2: STRATEGIC 4-PILLAR DASHBOARD ====================
    s2 = add_base_slide(
        title_text="لوحة النظرة العامة الاستراتيجية: الركائز الـ 4 لمنظومة لوسيل",
        category_text="الهيكل التشغيلي الشامل للمنظومة 2026",
        slide_num="2 / 14"
    )

    pillars = [
        ("1. البوابة الرسمية الموحدة", "21 صفحة تخصصية متصلة بهوية واحدة متكاملة دون روابط مكسورة، مع قائمة ملاحة ذكية.", Inches(9.8), NAVY),
        ("2. الكليات والبرامج الـ 17", "تغطية شاملة لـ 4 كليات أكاديمية مع مرافق تطبيقية متطورة كالعيادة القانونية ومختبر SOC.", Inches(6.8), COL_LAW),
        ("3. الخدمات الـ 16 بالـ QR", "أتمتة كاملة لإصدار الإفادات، السجلات، وتأجيل الفصول بالختم الرقمي والتحقق الفوري.", Inches(3.8), GOLD),
        ("4. لوحة المسجل Desk OS", "نظام تشغيل مركزي لإدارة القيود الأكاديمية (Holds)، ورصد الدرجات، ومحرك الـ GPA 4.00.", Inches(0.8), COL_IT)
    ]

    for title, desc, left, col in pillars:
        card = add_card(s2, left, Inches(1.6), Inches(2.75), Inches(3.2), title=title, subtitle=f"\n{desc}", border=col, title_color=col)

    # 4 Bottom High-Impact Metrics
    add_stat_callout(s2, Inches(9.8), Inches(5.0), Inches(2.75), Inches(1.7), "21", "صفحة تخصصية موحدة", "جاهزة للعمل فوراً", NAVY)
    add_stat_callout(s2, Inches(6.8), Inches(5.0), Inches(2.75), Inches(1.7), "17", "برنامجاً أكاديمياً معتمداً", "بكالوريوس وماجستير", COL_LAW)
    add_stat_callout(s2, Inches(3.8), Inches(5.0), Inches(2.75), Inches(1.7), "16", "خدمة ذاتية بالـ QR", "إصدار وتوثيق فوري", GOLD)
    add_stat_callout(s2, Inches(0.8), Inches(5.0), Inches(2.75), Inches(1.7), "30s", "زمن إنجاز المعاملة", "أتمتة شاملة 100%", ACCENT_GREEN)

    # ==================== SLIDE 3: UNIFIED PORTAL SHOWCASE ====================
    s3 = add_base_slide(
        title_text="البوابة الرسمية الموحدة: تجربة رقمية ترتقي بمكانة جامعة لوسيل",
        category_text="استعراض الواجهة الرئيسية الحية للموقع",
        slide_num="3 / 14"
    )

    add_browser_window(s3, "screen_home.png", Inches(0.8), Inches(1.5), Inches(6.8), Inches(5.2),
                       url="https://lu.edu.qa/index.html", caption="بوابة جامعة لوسيل الموحدة - تصميم رسمي فاخر بهوية الكحلي والذهبي")

    add_card(s3, Inches(7.9), Inches(1.5), Inches(4.6), Inches(5.2),
             title="ركائز التجربة الرقمية في المنظومة الجديدة",
             subtitle="بنية تحتية متطورة تخدم الزوار والطلبة والإدارة الأكاديمية")

    box3 = s3.shapes.add_textbox(Inches(8.1), Inches(2.4), Inches(4.2), Inches(4.1))
    tf3 = box3.text_frame; tf3.word_wrap = True
    bullets3 = [
        "• هوية بصرية موحدة بنسبة 100%: الكحلي الملكي (#004876) والذهبي (#be9c79) على كافة الصفحات.",
        "• تكامل شامل لـ 21 صفحة: لا صفحات ميتة، لا روابط وهمية، وانتقال سلس ومباشر.",
        "• قائمة ملاحة ذكية (Mega-Menu): تتيح الوصول لأي كلية أو برنامج أو خدمة بضغطة واحدة.",
        "• توافق كامل مع كافة الشاشات والأجهزة اللوحية والهواتف الذكية (Responsive Design).",
        "• محرك بحث فوري: يتيح البحث المباشر في البرامج والخدمات واللوائح والتقويم الأكاديمي."
    ]
    for i, b in enumerate(bullets3):
        p = tf3.paragraphs[0] if i == 0 else tf3.add_paragraph()
        p.text = b; p.font.size = Pt(10); p.font.color.rgb = TEXT_DARK; p.alignment = PP_ALIGN.RIGHT

    # ==================== SLIDE 4: 4 COLLEGES & 17 PROGRAMS ====================
    s4 = add_base_slide(
        title_text="دليل الكليات الأكاديمية الـ 4 والبرامج الـ 17 المعتمدة",
        category_text="البرامج الأكاديمية والخطط الدراسية",
        slide_num="4 / 14"
    )

    add_browser_window(s4, "screen_colleges.png", Inches(0.8), Inches(1.5), Inches(6.8), Inches(5.2),
                       url="https://lu.edu.qa/colleges.html", caption="دليل الكليات والبرامج - استعراض تفاعلي للخطط الدراسية")

    colleges_data = [
        ("كلية تكنولوجيا المعلومات", "الذكاء الاصطناعي، الأمن السيبراني، علوم البيانات، تقنية المعلومات", COL_IT),
        ("كلية القانون", "القانون العام، القانون الخاص، الدراسات المقارنة، وماجستير القانون الدولي", COL_LAW),
        ("كلية التجارة والأعمال", "إدارة الأعمال، المحاسبة والمالية، التسويق الرقمي، سلاسل الإمداد", COL_BIZ),
        ("كلية التربية والآداب", "تدريس اللغة الإنجليزية، اللغة العربية والإعلام، العلوم التربوية", COL_EDU)
    ]

    for idx, (c_name, c_desc, c_color) in enumerate(colleges_data):
        top_pos = Inches(1.5 + idx * 1.28)
        shape = add_card(s4, Inches(7.9), top_pos, Inches(4.6), Inches(1.18), bg_color=CARD_BG, border=c_color)
        tf = shape.text_frame
        p = tf.paragraphs[0]; p.text = c_name; p.font.bold = True; p.font.size = Pt(11.5); p.font.color.rgb = c_color; p.alignment = PP_ALIGN.RIGHT
        p2 = tf.add_paragraph(); p2.text = c_desc; p2.font.size = Pt(9.5); p2.font.color.rgb = TEXT_MUTED; p2.alignment = PP_ALIGN.RIGHT

    # ==================== SLIDE 5: IT & LAW SPOTLIGHTS ====================
    s5 = add_base_slide(
        title_text="تخصيص كامل لصفحات الكليات والمرافق التطبيقية الذكية",
        category_text="نماذج حية من صفحات الكليات التخصصية",
        slide_num="5 / 14"
    )

    add_browser_window(s5, "screen_college_it.png", Inches(0.8), Inches(1.5), Inches(5.6), Inches(4.3),
                       url="https://lu.edu.qa/college-it.html", caption="كلية تكنولوجيا المعلومات (مسار AI والأمن السيبراني)")
    add_browser_window(s5, "screen_college_law.png", Inches(6.9), Inches(1.5), Inches(5.6), Inches(4.3),
                       url="https://lu.edu.qa/college-law.html", caption="كلية القانون (المحكمة الصورية والعيادة القانونية)")

    add_card(s5, Inches(0.8), Inches(6.0), Inches(11.733), Inches(0.85),
             title="مرافق تطبيقية حديثة ومختبرات معتمدة",
             subtitle="مختبر العمليات السيبرانية SOC، المحكمة الصورية المطابقة للمحاكم القطرية، غرفة التداول المالي FinTech Lab، واستوديو التدريس المصغر.")

    # ==================== SLIDE 6: PROSPECTIVE STUDENT JOURNEY ====================
    s6 = add_base_slide(
        title_text="رحلة الطالب المتقدم: شروط القبول وحاسبة الرسوم التفاعلية",
        category_text="رحلة المستخدم (1/4) | استقطاب وقبول الطلبة الجدد",
        slide_num="6 / 14"
    )

    add_browser_window(s6, "screen_tuition.png", Inches(0.8), Inches(1.5), Inches(6.2), Inches(5.2),
                       url="https://lu.edu.qa/tuition-fees.html", caption="حاسبة الرسوم التفاعلية وشروط منح التفوق الأكاديمي (50% و 100%)")

    add_card(s6, Inches(7.3), Inches(1.5), Inches(5.2), Inches(5.2),
             title="خطوات الالتحاق المبسطة بالجامعة",
             subtitle="تجربة تقديم رقمية متكاملة وسهلة")

    box6 = s6.shapes.add_textbox(Inches(7.5), Inches(2.3), Inches(4.8), Inches(4.2))
    tf6 = box6.text_frame; tf6.word_wrap = True
    steps6 = [
        "1. الاطلاع على شروط القبول: متطلبات الثانوية القطرية (65%/70%) والبريطانية IGCSE واختبارات اللغة.",
        "2. حاسبة الرسوم الفورية: احتساب تكلفة الساعات بحسب الكلية وتطبيق منح التفوق الأكاديمي تلقائياً.",
        "3. استمارة التقديم الرقمية: نموذج تقديم في 4 خطوات مع رفع البطاقة الشخصية والشهادات.",
        "4. مراجعة الطلب والإشعار: تدقيق آلي للمستندات وتوليد إشعار القبول والرقم الجامعي المؤقت.",
        "5. خيارات السداد المعتمدة: التوجيه لوسائل السداد الرسمية المعتمدة بالحرم الجامعي."
    ]
    for i, s in enumerate(steps6):
        p = tf6.paragraphs[0] if i == 0 else tf6.add_paragraph()
        p.text = s; p.font.size = Pt(10); p.font.color.rgb = TEXT_DARK; p.alignment = PP_ALIGN.RIGHT

    # ==================== SLIDE 7: CURRENT STUDENT PORTAL ====================
    s7 = add_base_slide(
        title_text="بوابة الطالب الذاتية: الجدول، كشف الحضور، والمعدل التراكمي",
        category_text="رحلة المستخدم (2/4) | الخدمات الأكاديمية اليومية للطالب",
        slide_num="7 / 14"
    )

    add_browser_window(s7, "screen_student_portal.png", Inches(0.8), Inches(1.5), Inches(6.8), Inches(5.2),
                       url="https://lu.edu.qa/student-portal.html", caption="بوابة الطالب الذاتية الحية - متابعة الجدول والغياب والدرجات")

    add_card(s7, Inches(7.9), Inches(1.5), Inches(4.6), Inches(5.2),
             title="مكونات البوابة الذاتية للطالب",
             subtitle="إدارة أكاديمية كاملة من شاشة واحدة")

    box7 = s7.shapes.add_textbox(Inches(8.1), Inches(2.4), Inches(4.2), Inches(4.1))
    tf7 = box7.text_frame; tf7.word_wrap = True
    bullets7 = [
        "• الجدول الدراسي التفاعلي: مواعيد المحاضرات، أسماء الأساتذة، والقاعات الذكية.",
        "• كشف الحضور والغياب اللحظي: متابعة نسب الحضور مع تنبيه تلقائي عند تجاوز 10% غياب.",
        "• السجل الأكاديمي والـ GPA: استعراض الدرجات والمعدل الفصلي والتراكمي بدقة 4.00.",
        "• البطاقة الجامعية الرقمية: هوية الطالب الرقمية واستعراض الوضع الأكاديمي.",
        "• متابعة الطلبات: استعراض حالة الطلبات المقدمة (قيد المراجعة / معتمدة)."
    ]
    for i, b in enumerate(bullets7):
        p = tf7.paragraphs[0] if i == 0 else tf7.add_paragraph()
        p.text = b; p.font.size = Pt(10); p.font.color.rgb = TEXT_DARK; p.alignment = PP_ALIGN.RIGHT

    # ==================== SLIDE 8: 16 E-SERVICES & QR VERIFICATION ====================
    s8 = add_base_slide(
        title_text="منظومة الـ 16 خدمة ذاتية فورية بالختم والـ QR المعتمد",
        category_text="أتمتة المعاملات والتوثيق الرقمي المباشر",
        slide_num="8 / 14"
    )

    add_browser_window(s8, "screen_services.png", Inches(0.8), Inches(1.5), Inches(6.8), Inches(5.2),
                       url="https://lu.edu.qa/services.html", caption="منظومة الخدمات الإلكترونية الحية - استخراج فوري للوثائق بالـ QR")

    add_card(s8, Inches(7.9), Inches(1.5), Inches(4.6), Inches(5.2),
             title="قائمة الخدمات الأكاديمية المؤتمتة",
             subtitle="وثائق معتمدة جاهزة للتحميل والطباعة فوراً")

    box8 = s8.shapes.add_textbox(Inches(8.1), Inches(2.4), Inches(4.2), Inches(4.1))
    tf8 = box8.text_frame; tf8.word_wrap = True
    srv_list = [
        "1. إفادة قيد رسمي معتمد",
        "2. كشف درجات وسجل أكاديمي",
        "3. طلب تأجيل الفصل الدراسي",
        "4. طلب إعادة رصد وتدقيق الدرجة",
        "5. طلب تغيير التخصص الأكاديمي",
        "6. طلب معادلة مساقات سابقة",
        "7. حجز قاعات بحث المكتبة",
        "8. إفادة حسن سيرة وسلوك",
        "9. خطابات رسمية للسفارات والجهات",
        "10. طلب إخلاء طرف للتخرج"
    ]
    for i, s in enumerate(srv_list):
        p = tf8.paragraphs[0] if i == 0 else tf8.add_paragraph()
        p.text = s; p.font.size = Pt(9.5); p.font.color.rgb = TEXT_DARK; p.alignment = PP_ALIGN.RIGHT

    # ==================== SLIDE 9: DESK OS FOR REGISTRAR & ADMIN ====================
    s9 = add_base_slide(
        title_text="لوحة تحكم المسجل العام (Desk OS): إدارة العمليات والقيود",
        category_text="رحلة المستخدم (3/4) | الرقابة والتشغيل الأكاديمي المركزي",
        slide_num="9 / 14"
    )

    add_browser_window(s9, "screen_desk.png", Inches(0.8), Inches(1.5), Inches(6.8), Inches(5.2),
                       url="https://lu.edu.qa/desk.html", caption="لوحة تحكم المسجل العام Desk OS - رصد الدرجات والقيود الأكاديمية")

    add_card(s9, Inches(7.9), Inches(1.5), Inches(4.6), Inches(5.2),
             title="إمكانيات نظام التشغيل الإداري",
             subtitle="أدوات تحكم قوية للمسجل العام والعمداء")

    box9 = s9.shapes.add_textbox(Inches(8.1), Inches(2.4), Inches(4.2), Inches(4.1))
    tf9 = box9.text_frame; tf9.word_wrap = True
    desk_ops = [
        "• إدارة القيود (Holds Management): تطبيق ورفع القيود الأكاديمية والإدارية فورياً.",
        "• محرك احتساب المعدل GPA 4.00: تطبيق قواعد إعادة المقرر واحتساب مراتب الشرف.",
        "• كشوف الحرمان من الاختبارات: حصر آلي للطلبة المتجاوزين لنسب الغياب المقررة.",
        "• تدقيق شروط التخرج: فحص استيفاء الساعات الإجبارية والاختيارية (120-132 ساعة).",
        "• سجل تدقيق العمليات (Audit Trail): تسجيل آمن لكل تغيير في درجات أو حالات الطلبة."
    ]
    for i, d in enumerate(desk_ops):
        p = tf9.paragraphs[0] if i == 0 else tf9.add_paragraph()
        p.text = d; p.font.size = Pt(10); p.font.color.rgb = TEXT_DARK; p.alignment = PP_ALIGN.RIGHT

    # ==================== SLIDE 10: CAMPUS LIFE & STUDENT ACTIVITIES ====================
    s10 = add_base_slide(
        title_text="الحياة الجامعية والمرافق: الأندية، المكتبة، والأنشطة الرياضية",
        category_text="البيئة الجامعية المتكاملة في مدينة لوسيل",
        slide_num="10 / 14"
    )

    add_browser_window(s10, "screen_campus_life.png", Inches(0.8), Inches(1.5), Inches(6.8), Inches(5.2),
                       url="https://lu.edu.qa/campus-life.html", caption="صفحة الحياة الجامعية الحية - الأندية والمكتبة والأنشطة الطلابية")

    add_card(s10, Inches(7.9), Inches(1.5), Inches(4.6), Inches(5.2),
             title="أبرز عناصر الحياة الجامعية",
             subtitle="بيئة تعليمية ملهمة ومتوازنة")

    box10 = s10.shapes.add_textbox(Inches(8.1), Inches(2.4), Inches(4.2), Inches(4.1))
    tf10 = box10.text_frame; tf10.word_wrap = True
    campus_items = [
        "• 12 نادياً طلابياً نشطاً: تشمل نادي المناظرات، نادي الذكاء الاصطناعي، والعيادة القانونية.",
        "• مكتبة لوسيل المركزية: فهرس رقمي متطور، قواعد بيانات عالمية، وحجز قاعات البحث.",
        "• الأنشطة الرياضية المعتمدة: دوري الجامعات القطرية، بطولات كرة القدم، وبطولات البادل.",
        "• شراكات اللياقة البدنية: خصومات وعضويات خاصة في أندية رياضية كبرى (Strive & Perf Up).",
        "• مركز التطوير المهني: فرص التدريب الميداني والملتقيات المهنية السنوية."
    ]
    for i, c in enumerate(campus_items):
        p = tf10.paragraphs[0] if i == 0 else tf10.add_paragraph()
        p.text = c; p.font.size = Pt(10); p.font.color.rgb = TEXT_DARK; p.alignment = PP_ALIGN.RIGHT

    # ==================== SLIDE 11: INSTITUTIONAL VISION & LEADERSHIP ====================
    s11 = add_base_slide(
        title_text="القيادة المؤسسية والرؤية الأكاديمية: مجلس الأمناء ورئاسة الجامعة",
        category_text="رحلة المستخدم (4/4) | التوافق مع رؤية قطر 2030",
        slide_num="11 / 14"
    )

    add_browser_window(s11, "screen_about.png", Inches(0.8), Inches(1.5), Inches(6.8), Inches(5.2),
                       url="https://lu.edu.qa/about.html", caption="صفحة عن الجامعة الحية - مجلس الأمناء وكلمة الرئاسة والشركاء الدوليين")

    add_card(s11, Inches(7.9), Inches(1.5), Inches(4.6), Inches(5.2),
             title="الركائز الاستراتيجية لجامعة لوسيل",
             subtitle="صرح أكاديمي رائد في دولة قطر")

    box11 = s11.shapes.add_textbox(Inches(8.1), Inches(2.4), Inches(4.2), Inches(4.1))
    tf11 = box11.text_frame; tf11.word_wrap = True
    about_items = [
        "• مجلس الأمناء: برئاسة سعادة الدكتور علي بن فطيس المري وقيادات وطنية بارزة.",
        "• رئاسة الجامعة: بإشراف الأستاذ الدكتور نظام هندي لتحقيق أعلى معايير الجودة.",
        "• الشراكات الدولية: تعاون أكاديمي مع جامعة السوربون، جامعة ساسكس، ومعهد UNITAR.",
        "• البحث العلمي المحكم: إصدار مجلة لوسيل المحكمة وصندوق دعم البحوث والابتكار.",
        "• موقع استراتيجي: في قلب مدينة لوسيل الذكية لخدمة التنمية الوطنية المستدامة."
    ]
    for i, a in enumerate(about_items):
        p = tf11.paragraphs[0] if i == 0 else tf11.add_paragraph()
        p.text = a; p.font.size = Pt(10); p.font.color.rgb = TEXT_DARK; p.alignment = PP_ALIGN.RIGHT

    # ==================== SLIDE 12: PRACTICAL TECHNICAL ARCHITECTURE ====================
    s12 = add_base_slide(
        title_text="المعمارية التقنية الواقعية: استقرار عالي وأمان سيادي",
        category_text="الهيكل البرمجي والتشغيلي المعتمد",
        slide_num="12 / 14"
    )

    tech_layers = [
        ("1. واجهات المستخدم الذكية (Frontend Portal)", "بوابة الطالب، بوابة المسجل العام (Desk OS)، صفحات الكليات والقبول (HTML5 / Modern JS / Tailwind / Fully Responsive).", Inches(0.8), Inches(1.6)),
        ("2. محرك الخدمات والأختام الرقمية (Verification Engine)", "توليد فوري للوثائق الأكاديمية بصيغ رسمية مع كود QR مشفر للتحقق الفوري من صحة الوثيقة دون الحاجة لتدخل بشري.", Inches(0.8), Inches(2.9)),
        ("3. محرك القواعد الأكاديمية (Academic Rules & GPA Engine)", "احتساب المعدل التراكمي بدقة 4.00، معالجة الساعات المعتمدة، وإنفاذ قيود الحرمان والإنذارات الأكاديمية آلياً.", Inches(0.8), Inches(4.2)),
        ("4. طبقة حماية البيانات والتكامل (Security & Local Storage)", "استضافة سحابية محلية آمنة، إدارة صلاحيات الوصول المبنية على الأدوار (RBAC)، والامتثال التام للائحة PDPPL القطرية.", Inches(0.8), Inches(5.5))
    ]

    for title, desc, left, top in tech_layers:
        shape = add_card(s12, left, top, Inches(11.733), Inches(1.1), bg_color=CARD_BG)
        tf = shape.text_frame; tf.margin_left = tf.margin_right = Inches(0.25)
        p = tf.paragraphs[0]; p.text = title; p.font.bold = True; p.font.size = Pt(12); p.font.color.rgb = NAVY; p.alignment = PP_ALIGN.RIGHT
        p2 = tf.add_paragraph(); p2.text = desc; p2.font.size = Pt(10); p2.font.color.rgb = TEXT_MUTED; p2.alignment = PP_ALIGN.RIGHT

    # ==================== SLIDE 13: REAL-WORLD OPERATIONAL IMPACT ====================
    s13 = add_base_slide(
        title_text="الأثر التشغيلي الواقعي: سرعة إنجاز، دقة، ورضا مستفيدين",
        category_text="مؤشرات الكفاءة التشغيلية الملموسة",
        slide_num="13 / 14"
    )

    metrics = [
        ("زمن استخراج الإفادات الرسمية", "30 ثانية", "بدلاً من 3-4 أيام عمل سابقاً", Inches(0.8)),
        ("دقة احتساب المعدل والغياب", "100%", "محرك برمجي يلغي الخطأ البشري", Inches(4.8)),
        ("جاهزية الروابط والصفحات", "21 / 21", "صفر روابط مكسورة أو معطلة", Inches(8.8))
    ]

    for m_title, m_val, m_sub, left in metrics:
        shape = add_card(s13, left, Inches(1.6), Inches(3.733), Inches(2.6), bg_color=CARD_BG)
        tf = shape.text_frame
        p0 = tf.paragraphs[0]; p0.text = m_title; p0.font.size = Pt(11); p0.font.bold = True; p0.font.color.rgb = TEXT_DARK; p0.alignment = PP_ALIGN.RIGHT
        p1 = tf.add_paragraph(); p1.text = m_val; p1.font.bold = True; p1.font.size = Pt(34); p1.font.color.rgb = NAVY; p1.alignment = PP_ALIGN.RIGHT
        p2 = tf.add_paragraph(); p2.text = m_sub; p2.font.size = Pt(10); p2.font.color.rgb = GOLD; p2.alignment = PP_ALIGN.RIGHT

    add_card(s13, Inches(0.8), Inches(4.5), Inches(11.733), Inches(2.1),
             title="مكاسب تشغيلية مباشرة لإدارة الجامعة",
             subtitle="• توفير مئات الساعات الإدارية سنوياً لكادر القبول والتسجيل.\n• إتاحة الخدمات الأكاديمية للطلبة على مدار الساعة (24/7 Availability).\n• حماية الوثائق الرسمية للجامعة من التزوير عبر الختم الرقمي والتحقق بالـ QR.\n• واجهة عصرية تعكس المكانة الحقيقية لجامعة لوسيل كصرح أكاديمي رائد في دولة قطر.")

    # ==================== SLIDE 14: EXECUTIVE SUMMARY & CALL TO ACTION ====================
    s14 = prs.slides.add_slide(blank_layout)
    bg14 = s14.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg14.fill.solid(); bg14.fill.fore_color.rgb = NAVY; bg14.line.fill.background()

    deco14 = s14.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.2), Inches(0.15), Inches(5.0))
    deco14.fill.solid(); deco14.fill.fore_color.rgb = GOLD; deco14.line.fill.background()

    end_box = s14.shapes.add_textbox(Inches(1.2), Inches(1.2), Inches(11.0), Inches(5.0))
    e_tf = end_box.text_frame; e_tf.word_wrap = True

    ep0 = e_tf.paragraphs[0]
    ep0.text = "الخاتمة والتوصيات التنفيذية المعروضة على إدارة الجامعة"
    ep0.font.size = Pt(13)
    ep0.font.bold = True
    ep0.font.color.rgb = GOLD
    ep0.alignment = PP_ALIGN.RIGHT

    ep1 = e_tf.add_paragraph()
    ep1.text = "جامعة لوسيل: منصة أكاديمية ذكية جاهزة للتشغيل الفوري"
    ep1.font.size = Pt(28)
    ep1.font.bold = True
    ep1.font.color.rgb = CARD_BG
    ep1.alignment = PP_ALIGN.RIGHT

    ep2 = e_tf.add_paragraph()
    ep2.text = "\nالخطوات التنفيذية المقترحة:\n" \
               "1. اعتماد التصميم والهوية البصرية الموحدة وتدشين البوابة الإلكترونية رسمياً.\n" \
               "2. تفعيل منظومة الخدمات الذاتية الـ 16 بالـ QR Code للطلبة للفصل الدراسي القادم.\n" \
               "3. بدء استقبال طلبات الالتحاق الإلكترونية عبر صفحة القبول وحاسبة الرسوم التفاعلية."
    ep2.font.size = Pt(12.5)
    ep2.font.color.rgb = RGBColor(226, 232, 240)
    ep2.alignment = PP_ALIGN.RIGHT

    ep3 = e_tf.add_paragraph()
    ep3.text = "\nشكراً لكم | جامعة لوسيل - صرح أكاديمي رائد في مدينة لوسيل، دولة قطر"
    ep3.font.size = Pt(11)
    ep3.font.bold = True
    ep3.font.color.rgb = GOLD
    ep3.alignment = PP_ALIGN.RIGHT

    output_path = os.path.join(BASE_DIR, "Lusail_University_Digital_Transformation_Pitch.pptx")
    prs.save(output_path)
    print(f"Presentation generated and saved successfully at: {output_path}")

if __name__ == "__main__":
    create_presentation()
