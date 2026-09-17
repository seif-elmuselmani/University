# -*- coding: utf-8 -*-
"""
Capture 1920x1080 High-Res Screenshots for each of the 14 Slides
"""
import os
import subprocess
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RENDER_HTML = os.path.join(BASE_DIR, "presentation", "render_slides.html")
OUTPUT_DIR = os.path.join(BASE_DIR, "presentation", "slides_rendered")
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(RENDER_HTML, "r", encoding="utf-8") as f:
    full_html = f.read()

# For each slide 1 to 14, create a focused single-slide HTML
for i in range(1, 15):
    slide_id = f"slide-{i}"
    # Replace other slides or hide them with CSS
    custom_css = f"""
    <style>
        .slide-canvas {{ display: none !important; }}
        #{slide_id} {{ display: flex !important; margin: 0 !important; width: 1920px !important; height: 1080px !important; }}
        body {{ padding: 0 !important; margin: 0 !important; overflow: hidden !important; }}
    </style>
    """
    slide_html = full_html.replace("</head>", f"{custom_css}\n</head>")
    
    temp_file = os.path.join(OUTPUT_DIR, f"temp_slide_{i}.html")
    with open(temp_file, "w", encoding="utf-8") as tf:
        tf.write(slide_html)
    
    out_png = os.path.join(OUTPUT_DIR, f"slide_{i}.png")
    
    cmd = [
        EDGE_PATH,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=1920,1080",
        f"--screenshot={out_png}",
        f"file:///{temp_file.replace(os.sep, '/')}"
    ]
    subprocess.run(cmd, check=True)
    print(f"Captured Slide {i} -> {out_png}")
    
    if os.path.exists(temp_file):
        os.remove(temp_file)

print("All 14 slides captured successfully!")
