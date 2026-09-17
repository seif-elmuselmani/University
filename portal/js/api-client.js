/**
 * Lusail University Unified API Client Bridge (JavaScript)
 * Full Two-Way Synchronization with SQLite Database via FastAPI Backend (http://127.0.0.1:8000).
 */

const LUSAIL_API_BASE = 'http://127.0.0.1:8000';

window.LusailAPI = {
    baseUrl: LUSAIL_API_BASE,

    // Helper fetch wrapper
    async request(endpoint, options = {}) {
        const url = `${this.baseUrl}${endpoint}`;
        const defaultHeaders = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        };

        const config = {
            ...options,
            headers: {
                ...defaultHeaders,
                ...options.headers
            }
        };

        try {
            const response = await fetch(url, config);
            const data = await response.json();
            if (!response.ok) {
                throw new Error(data.detail || 'حدث خطأ في معالجة الطلب');
            }
            return data;
        } catch (err) {
            console.warn(`[LusailAPI] Request to ${url} failed:`, err.message);
            throw err;
        }
    },

    // 1. Authentication
    async login(username, password) {
        return this.request('/api/auth/login', {
            method: 'POST',
            body: JSON.stringify({ username, password })
        });
    },

    // 2. Students & Academics
    async getStudents() {
        return this.request('/api/academic/students');
    },

    async getTranscript(studentId = 'LU-2024-0891') {
        return this.request(`/api/academic/students/${studentId}/transcript`);
    },

    async recordGrade(studentId, courseCode, score, semester = 'خريف 2026') {
        return this.request('/api/academic/grades/record', {
            method: 'POST',
            body: JSON.stringify({
                student_id: studentId,
                course_code: courseCode,
                score: parseFloat(score),
                semester: semester
            })
        });
    },

    // 3. Tuition & Financial
    async calculateTuition(credits = 15, scholarshipType = 'NONE') {
        return this.request('/api/finance/calculate-tuition', {
            method: 'POST',
            body: JSON.stringify({
                credits: parseInt(credits),
                scholarship_type: scholarshipType,
                include_services_fee: true
            })
        });
    },

    async getAllInvoices() {
        return this.request('/api/finance/invoices');
    },

    async payInvoice(invoiceNumber, studentId, amount) {
        return this.request('/api/finance/pay-invoice', {
            method: 'POST',
            body: JSON.stringify({
                invoice_number: invoiceNumber,
                student_id: studentId,
                amount: parseFloat(amount)
            })
        });
    },

    // 4. Admissions
    async submitAdmission(applicationData) {
        return this.request('/api/admissions/apply', {
            method: 'POST',
            body: JSON.stringify(applicationData)
        });
    },

    async getAllAdmissionApplications() {
        return this.request('/api/admissions/applications');
    },

    // 5. E-Services & Tickets
    async submitService(studentId, serviceCode, details = '') {
        return this.request('/api/services/submit', {
            method: 'POST',
            body: JSON.stringify({
                student_id: studentId,
                service_code: serviceCode,
                details: details
            })
        });
    },

    async getAllServiceTickets() {
        return this.request('/api/services/tickets');
    }
};

console.log('✅ Lusail University Real-Time API Client Bridge Active (http://127.0.0.1:8000)');
