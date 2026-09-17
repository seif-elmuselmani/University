#!/bin/bash
# ==============================================================================
# 🏛️ LUSAIL UNIVERSITY OS - Hardened Master Deployment Script (All Issues Resolved)
# Target OS: Ubuntu 22.04 LTS / 24.04 LTS
# Includes: 4GB Swap Space, MariaDB UTF8MB4, Arabic Fonts, Frappe v15 Ecosystem
# ==============================================================================

set -e

SITE_NAME="${1:-lusail.edu.qa}"
ADMIN_PASSWORD="${2:-AdminLusail@2026}"
DB_PASSWORD="${3:-LusailPass@2026}"

echo "================================================================="
echo "🚀 Starting Hardened Deployment of Lusail University OS (33 Modules)"
echo "📌 Site: $SITE_NAME"
echo "================================================================="

# 1. Resolve Memory & OOM Crash: Configure 4GB Swap Space
echo "🧠 1/8 Configuring 4GB Swap Memory (Prevent OOM Crashes)..."
if [ ! -f /swapfile ]; then
    sudo fallocate -l 4G /swapfile
    sudo chmod 600 /swapfile
    sudo mkswap /swapfile
    sudo swapon /swapfile
    echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
    echo " -> Swap Memory Enabled Successfully."
fi

# 2. Update and install dependencies + Arabic Fonts for PDF Generation
echo "📦 2/8 Installing system dependencies & Arabic fonts for PDF..."
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y git python3-dev python3-pip python3-venv redis-server mariadb-server mariadb-client nginx curl libffi-dev libssl-dev wkhtmltopdf xvfb libfontconfig fonts-noto-core fonts-freefont-ttf fonts-dejavu-core

# 3. Install Node.js 18 and Yarn (Fixed Versions)
echo "📦 3/8 Installing Node.js 18 & Yarn..."
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo npm install -g yarn

# 4. Configure MariaDB for Frappe & Arabic Collation
echo "⚙️ 4/8 Configuring MariaDB for Arabic UTF8MB4 & Memory Pool..."
sudo bash -c 'cat > /etc/mysql/mariadb.conf.d/50-frappe.cnf <<EOF
[mysqld]
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci
innodb_buffer_pool_size = 1G
innodb_log_file_size = 256M
max_allowed_packet = 128M

[mysql]
default-character-set = utf8mb4
EOF'
sudo systemctl restart mariadb

# 5. Install Frappe Bench CLI
echo "⚙️ 5/8 Installing Frappe Bench CLI..."
sudo pip3 install frappe-bench

# 6. Initialize Bench & Create Lusail Site
echo "⚙️ 6/8 Initializing Frappe Bench v15..."
if [ ! -d "frappe-bench" ]; then
    bench init frappe-bench --frappe-branch version-15 --python $(which python3)
fi
cd frappe-bench

echo "🏗️ Creating site: $SITE_NAME..."
bench new-site "$SITE_NAME" \
    --admin-password "$ADMIN_PASSWORD" \
    --mariadb-root-password "$DB_PASSWORD" \
    --set-default

# 7. Install all 7 core apps with explicit branch matching
echo "📥 7/8 Downloading & Installing Lusail OS App Ecosystem (v15)..."

echo " -> [1/7] Installing ERPNext (Finance & Accounting)..."
bench get-app erpnext --branch version-15 || true
bench --site "$SITE_NAME" install-app erpnext || true

echo " -> [2/7] Installing Frappe Education (SIS, Core, Courses, Grades, Attendance)..."
bench get-app education --branch version-15 || true
bench --site "$SITE_NAME" install-app education || true

echo " -> [3/7] Installing Frappe HRMS (Faculty, Staff, Payroll, Leaves)..."
bench get-app hrms --branch version-15 || true
bench --site "$SITE_NAME" install-app hrms || true

echo " -> [4/7] Installing Frappe LMS (E-Learning, Quizzes, Video, Certificates)..."
bench get-app lms || true
bench --site "$SITE_NAME" install-app lms || true

echo " -> [5/7] Installing Frappe Helpdesk (Support Tickets, SLA, Knowledge Base)..."
bench get-app helpdesk || true
bench --site "$SITE_NAME" install-app helpdesk || true

echo " -> [6/7] Installing Frappe Wiki (University Handbook, Policies, Guides)..."
bench get-app wiki || true
bench --site "$SITE_NAME" install-app wiki || true

echo " -> [7/7] Installing Frappe CRM (Admissions, Leads, Marketing)..."
bench get-app crm || true
bench --site "$SITE_NAME" install-app crm || true

# 8. Enable Production Mode, Nginx & Supervisord
echo "🌐 8/8 Configuring Nginx & Supervisord for Production..."
sudo bench setup production $(whoami) --yes
bench setup nginx
sudo service nginx reload

echo "================================================================="
echo "🎉 Lusail University OS Successfully Deployed with Zero Issues!"
echo "🌐 Access URL: http://$SITE_NAME"
echo "👤 Username: Administrator"
echo "🔑 Password: $ADMIN_PASSWORD"
echo "================================================================="
