/**
 * Lusail University - Unified Institutional Navigation, Header, Mega-Menu & Footer Hub
 * Standardized across all 22 pages for 100% brand consistency.
 */

window.LusailNav = {
    // Searchable index of all portals, pages, majors, and services
    searchIndex: [
        // Colleges & Programs
        { title: "كلية تكنولوجيا المعلومات (College of IT)", category: "الكليات الأكاديمية", url: "college-it.html", desc: "الذكاء الاصطناعي، الأمن السيبراني، علوم البيانات، تقنية المعلومات", icon: "cpu" },
        { title: "مسار الذكاء الاصطناعي وتعلم الآلة", category: "الكليات الأكاديمية", url: "college-it.html#ai", desc: "بكالوريوس الذكاء الاصطناعي والتعلم العميق والرؤية الحاسوبية", icon: "bot" },
        { title: "مسار الأمن السيبراني والتحقيق الرقمي", category: "الكليات الأكاديمية", url: "college-it.html#cyber", desc: "بكالوريوس الأمن السيبراني ومختبر العمليات الأمنية SOC", icon: "shield-check" },
        { title: "كلية القانون (College of Law)", category: "الكليات الأكاديمية", url: "college-law.html", desc: "القانون العام، القانون الخاص، الدراسات القانونية المقارنة، المحكمة الصورية", icon: "scale" },
        { title: "المحكمة الصورية والعيادة القانونية التطبيقية", category: "الكليات الأكاديمية", url: "college-law.html#moot", desc: "قاعة محاكمة مطابقة للمحاكم القطرية والدولية للتدريب العملي", icon: "gavel" },
        { title: "كلية التجارة والأعمال (College of Commerce & Business)", category: "الكليات الأكاديمية", url: "college-business.html", desc: "إدارة الأعمال، المحاسبة والمالية، التسويق الرقمي، سلاسل الإمداد", icon: "briefcase" },
        { title: "معمل المحاكاة المالية وغرفة التداول (FinTech Lab)", category: "الكليات الأكاديمية", url: "college-business.html#fintech", desc: "40 محطة عمل متصلة ببيانات بورصة قطر وشاشات بلومبرغ", icon: "line-chart" },
        { title: "كلية التربية والآداب (College of Education & Arts)", category: "الكليات الأكاديمية", url: "college-education.html", desc: "تدريس اللغة الإنجليزية، اللغة العربية والإعلام، العلوم التربوية", icon: "book-open" },
        { title: "معمل التدريس المصغر والصوتيات اللغوية", category: "الكليات الأكاديمية", url: "college-education.html#microteaching", desc: "استوديو محاكاة الحصص المدرسية المزود بكاميرات تحليل الأداء", icon: "mic" },
        { title: "دليل الكليات والبرامج الـ 17 الشامل (All Colleges)", category: "الكليات الأكاديمية", url: "colleges.html", desc: "استعراض كافة الكليات الـ 4 والبرامج الأكاديمية الـ 17 بكالوريوس و5 ماجستير", icon: "building-2" },

        // Admissions & Fees
        { title: "بوابة التقديم والقبول الإلكتروني الفوري", category: "القبول والتسجيل", url: "admissions.html", desc: "استمارة التسجيل الإلكترونية لخريف 2026 ورفع المستندات الرسمية", icon: "send" },
        { title: "خطوات استكمال طلب الالتحاق الأربعة", category: "القبول والتسجيل", url: "admissions.html#steps", desc: "دليل خطوات التسجيل ورفع الشهادات والمراجعة الفورية", icon: "check-square" },
        { title: "شروط القبول ومعادلة الشهادات الثانوية", category: "القبول والتسجيل", url: "admission-requirements.html", desc: "متطلبات الثانوية القطرية (65% / 70%)، البريطانية IGCSE، الأمريكية IB", icon: "award" },
        { title: "شروط الثانوية العامة القطرية", category: "القبول والتسجيل", url: "admission-requirements.html#qatari", desc: "نسبة 65% كحد أدنى أو 70% في مقرر اللغة العربية", icon: "file-text" },
        { title: "الشهادات البريطانية IGCSE و A-Level", category: "القبول والتسجيل", url: "admission-requirements.html#british", desc: "النجاح في 5 مواد IGCSE ومادتين AS أو مادة A-Level", icon: "globe" },
        { title: "اختبارات الكفاءة اللغوية (IELTS / TOEFL)", category: "القبول والتسجيل", url: "admission-requirements.html#ielts", desc: "درجة IELTS 5.5 أو اختبار تحديد المستوى بجامعة لوسيل (150 ر.ق)", icon: "languages" },
        { title: "دليل وحاسبة الرسوم الدراسية والمنح", category: "القبول والتسجيل", url: "tuition-fees.html", desc: "حاسبة الرسوم التفاعلية، منح التفوق 50% و100% وبوابة الدفع QPay", icon: "calculator" },
        { title: "منح التفوق الأكاديمي (50% و 100%)", category: "القبول والتسجيل", url: "tuition-fees.html#scholarships", desc: "شروط منح التفوق للطلبة الحاصلين على 90% و95% فأعلى", icon: "star" },
        { title: "منظومة الدفع الإلكتروني المعتمدة QPay", category: "القبول والتسجيل", url: "tuition-fees.html#payment", desc: "تسديد الرسوم الدراسية بالريال القطري عبر بطاقات الخصم والائتمان", icon: "credit-card" },
        { title: "التقويم الأكاديمي الرسمي 2026/2027", category: "القبول والتسجيل", url: "academic-calendar.html", desc: "مواعيد الفصول الدراسية (خريف، ربيع، صيف) وفترات الحذف والإضافة", icon: "calendar" },

        // Campus Life & Facilities
        { title: "الحرم الجامعي والمرافق الحيوية بمدينة لوسيل", category: "الحياة الجامعية", url: "campus-life.html", desc: "مباني الجامعة، القاعات الذكية، بيئة التعلم الحديثة في لوسيل", icon: "map-pin" },
        { title: "الأندية والأنشطة الطلابية (Student Clubs)", category: "الحياة الجامعية", url: "student-clubs.html", desc: "12 نادي طلابي، الأنشطة الثقافية والرياضية ونموذج الانضمام الفوري", icon: "users" },
        { title: "مكتبة لوسيل المركزية وقواعد البيانات الرقمية", category: "الحياة الجامعية", url: "library.html", desc: "الفهرس الرقمي (مداد)، حجز قاعات البحث، قواعد بيانات IEEE ودار المنظومة", icon: "library" },
        { title: "الأنشطة والبطولات الرياضية الطلابية", category: "الحياة الجامعية", url: "campus-life.html#sports", desc: "دوري الجامعات القطرية، فعاليات اليوم الرياضي، والبطولات الداخلية", icon: "trophy" },
        { title: "شراكات وعضويات أندية اللياقة البدنية (Strive & Perf Up)", category: "الحياة الجامعية", url: "campus-life.html#fitness", desc: "خصومات وعضويات رياضية خاصة لطلبة وموظفي جامعة لوسيل", icon: "activity" },
        { title: "مركز التطوير المهني وشبكة الخريجين", category: "الحياة الجامعية", url: "career-center.html", desc: "التدريب الميداني، ملتقيات التوظيف، وفرص العمل لخريجي لوسيل", icon: "award" },

        // Research & Institutional
        { title: "عن جامعة لوسيل ومجلس الأمناء", category: "عن الجامعة", url: "about.html", desc: "الرؤية والرسالة 2030، رئيس مجلس الأمناء د. علي بن فطيس المري، ورئيس الجامعة أ.د. نظام هندي", icon: "shield" },
        { title: "مجلس الأمناء والقيادة المؤسسية", category: "عن الجامعة", url: "about.html#trustees", desc: "سعادة الدكتور علي بن فطيس المري رئيس مجلس الأمناء والقيادات الأكاديمية", icon: "users" },
        { title: "كلمة رئيس الجامعة (أ.د. نظام هندي)", category: "عن الجامعة", url: "about.html#president", desc: "الرؤية الاستراتيجية لجودة التعليم العالي والاعتماد المؤسسي", icon: "user-check" },
        { title: "الشراكات الدولية (سوربون، ساسكس، UNITAR)", category: "عن الجامعة", url: "about.html#partners", desc: "اتفاقيات التعاون الأكاديمي والشهادات المزدوجة مع أعرق الجامعات العالمية", icon: "globe" },
        { title: "عمادة البحث العلمي والدراسات العليا", category: "البحث العلمي", url: "research.html", desc: "المراكز البحثية، الكراسي العلمية، ومجلة لوسيل المحكمة", icon: "microscope" },
        { title: "مجلة لوسيل للدراسات المحكمة (ISSN 2789-5544)", category: "البحث العلمي", url: "research.html#journal", desc: "دورية علمية محكمة خاضعة للتحكيم المزدوج الأعمى ومفهرسة دولياً", icon: "book-marked" },
        { title: "صندوق دعم البحوث والابتكارات الطلابية", category: "البحث العلمي", url: "research.html#grants", desc: "منح تمويلية تصل إلى 25,000 ر.ق لمشاريع التخرج والابتكارات", icon: "gift" },
        { title: "الأسئلة الشائعة والمكررة (FAQ)", category: "عن الجامعة", url: "faq.html", desc: "إجابات وافية لكافة استفسارات القبول والتسجيل والرسوم والخدمات", icon: "help-circle" },
        { title: "تواصل معنا ودليل الهواتف وخريطة الحرم", category: "عن الجامعة", url: "contact.html", desc: "المنطقة 69، شارع 100، مبنى 333، جبل ثعيلب، لوسيل | +974 4401 1111", icon: "phone" },

        // Portals & Systems
        { title: "بوابة الطالب الذاتية (Student Portal)", category: "الأنظمة الذكية", url: "student-portal.html", desc: "الجدول الدراسي، السجل الأكاديمي، كشف الغياب، والبطاقة الجامعية", icon: "layout-dashboard" },
        { title: "الجدول الدراسي الأسبوعي وسجل الحضور", category: "الأنظمة الذكية", url: "student-portal.html#schedule", desc: "مواعيد المحاضرات والقاعات ونسب الحضور والغياب اللحظية", icon: "calendar" },
        { title: "منظومة الخدمات الإلكترونية (16 خدمة)", category: "الأنظمة الذكية", url: "services.html", desc: "إفادة القيد، السجل الأكاديمي، تأجيل الفصل، إعادة الرصد، والمزيد", icon: "layers" },
        { title: "إفادات القيد والسجل الأكاديمي الرسمي", category: "الأنظمة الذكية", url: "services.html#service-enrollment", desc: "استخراج إفادة القيد المعتمدة رقمياً بالـ QR Code", icon: "file-check" },
        { title: "طلب تأجيل الفصل الدراسي أو الانسحاب", category: "الأنظمة الذكية", url: "services.html#service-defer", desc: "تقديم طلب رسمي لتأجيل القيد وفق اللائحة الأكاديمية", icon: "clock" },
        { title: "طلب إعادة رصد وتدقيق الدرجة", category: "الأنظمة الذكية", url: "services.html#service-regrade", desc: "التظلم الأكاديمي وإعادة تدقيق كراسة الإجابة", icon: "edit-3" },
        { title: "لوحة تحكم الإدارة والمسجل العام (Desk OS)", category: "الأنظمة الذكية", url: "desk.html", desc: "نظام التشغيل الإداري، رصد الدرجات، القيود الأكاديمية والمالية", icon: "layout-grid" },
        { title: "محرك احتساب المعدل التراكمي (GPA Engine)", category: "الأنظمة الذكية", url: "desk.html#grades", desc: "سلم الدرجات 4.00 Scale وحساب مراتب الشرف والتخرج", icon: "calculator" },
        { title: "نظام إدارة القيود الأكاديمية والمالية (Holds Engine)", category: "الأنظمة الذكية", url: "desk.html#holds", desc: "إدارة الحظر الأكاديمي، القيود المالية، وتصديق المستندات", icon: "lock" }
    ],

    // Return the standard unified Top Utility Bar HTML
    getTopBarHTML() {
        return `
        <div class="bg-slate-100 text-slate-700 text-[11px] py-1.5 px-4 sm:px-6 border-b border-slate-200">
            <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-2">
                <div class="flex items-center gap-1 sm:gap-2">
                    <span class="text-slate-400 font-bold hidden sm:inline">مسارات سريعة:</span>
                    <a href="admissions.html" class="px-2.5 py-0.5 rounded-lg bg-white border border-slate-200 hover:border-[#be9c79] hover:text-[#004876] font-bold text-slate-700 transition">للطلاب الجدد</a>
                    <a href="student-portal.html" class="px-2.5 py-0.5 rounded-lg bg-emerald-50 border border-emerald-200 text-emerald-800 font-bold transition flex items-center gap-1"><i data-lucide="user" class="w-3 h-3"></i> للطلاب الحاليين</a>
                    <a href="desk.html" class="px-2.5 py-0.5 rounded-lg bg-white border border-slate-200 hover:border-[#be9c79] hover:text-[#004876] font-bold text-slate-700 transition">لهيئة التدريس والإدارة</a>
                    <a href="about.html" class="px-2.5 py-0.5 rounded-lg bg-white border border-slate-200 hover:border-[#be9c79] hover:text-[#004876] font-bold text-slate-700 transition hidden md:inline">للزوار والشركاء</a>
                </div>
                <div class="flex items-center gap-3 sm:gap-4 font-bold text-xs">
                    <a href="https://stus.lu.edu.qa/StudentSelfService" target="_blank" class="text-[#004876] hover:text-[#be9c79] transition flex items-center gap-1">
                        <span class="w-2 h-2 rounded-full bg-[#be9c79]"></span> BANNER
                    </a>
                    <a href="https://lms.lu.edu.qa" target="_blank" class="text-[#004876] hover:text-[#be9c79] transition flex items-center gap-1">
                        <span class="w-2 h-2 rounded-full bg-emerald-500"></span> BLACKBOARD
                    </a>
                    <button onclick="window.LusailNav.openSpotlight()" class="hover:text-[#004876] transition flex items-center gap-1.5 text-slate-600 bg-white px-2.5 py-0.5 rounded-lg border border-slate-200 shadow-2xs">
                        <i data-lucide="search" class="w-3 h-3 text-[#004876]"></i>
                        <span class="hidden sm:inline">بحث سريع <kbd class="px-1 text-[9px] bg-slate-100 rounded font-mono border border-slate-300">Ctrl+K</kbd></span>
                    </button>
                </div>
            </div>
        </div>`;
    },

    // Return the standard unified Main Header HTML
    getMainHeaderHTML() {
        return `
        <header class="bg-white border-b border-slate-200 py-3 px-4 sm:px-6 sticky top-0 z-40 shadow-sm">
            <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
                <div class="flex items-center gap-3 sm:gap-4">
                    <button onclick="window.LusailNav.toggleMobileDrawer()" class="p-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-800 lg:hidden transition">
                        <i data-lucide="menu" class="w-5 h-5"></i>
                    </button>
                    <a href="index.html" class="flex items-center gap-3 group">
                        <img src="https://lu.edu.qa/img/lu-logo.webp" alt="جامعة لوسيل - Lusail University" class="h-11 sm:h-13 w-auto object-contain transition group-hover:scale-102">
                    </a>
                    <div class="hidden xl:block border-r border-slate-200 pr-4">
                        <div class="flex items-center gap-2">
                            <span class="text-xs font-black text-[#004876]">جامعة وطنية رائدة</span>
                            <span class="text-[9px] px-1.5 py-0.5 rounded-full font-bold bg-[#be9c79]/15 text-[#856545] border border-[#be9c79]/30">دولة قطر</span>
                        </div>
                        <p class="text-[10px] text-slate-500 font-medium">تحت إشراف وزارة التربية والتعليم والتعليم العالي</p>
                    </div>
                </div>

                <div class="flex items-center gap-2 sm:gap-3">
                    <button onclick="window.LusailNav.openSignModal()" class="px-3 py-1.5 bg-[#be9c79]/15 hover:bg-[#be9c79]/30 text-[#004876] text-xs font-bold rounded-xl transition flex items-center gap-1.5 border border-[#be9c79]/40 shadow-xs">
                        <i data-lucide="hand" class="w-4 h-4 text-[#be9c79]"></i>
                        <span class="hidden sm:inline">لغة الإشارة</span>
                    </button>
                    <a href="admissions.html" class="px-3.5 py-1.5 bg-[#004876] hover:bg-[#003354] text-white text-xs font-bold rounded-xl transition flex items-center gap-1.5 shadow-sm border border-[#004876]">
                        <i data-lucide="user-plus" class="w-3.5 h-3.5 text-[#be9c79]"></i>
                        <span>القبول والتسجيل</span>
                    </a>
                    <a href="student-portal.html" class="px-3.5 py-1.5 bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold rounded-xl transition flex items-center gap-1.5 shadow-sm hidden md:flex">
                        <i data-lucide="layout-dashboard" class="w-3.5 h-3.5"></i>
                        <span>بوابة الطالب</span>
                    </a>
                    <a href="desk.html" class="px-3.5 py-1.5 bg-slate-100 hover:bg-slate-200 text-[#004876] text-xs font-bold rounded-xl transition flex items-center gap-1 border border-slate-300">
                        <i data-lucide="shield" class="w-3.5 h-3.5 text-[#be9c79]"></i>
                        <span class="hidden sm:inline">Desk OS</span>
                    </a>
                </div>
            </div>
        </header>`;
    },

    // Return the standard unified Mega Menu Ribbon HTML
    getMegaMenuHTML(activeSectorId) {
        const sectors = window.LusailMegaMenuData ? window.LusailMegaMenuData.sectors : [];
        let sectorButtons = '';
        let sectorPanels = '';

        sectors.forEach(sec => {
            sectorButtons += `
                <div class="static">
                    <button data-mega-sector-btn="${sec.id}"
                            @mouseenter="activeMegaSector = '${sec.id}'" 
                            @click="activeMegaSector = (activeMegaSector === '${sec.id}' ? null : '${sec.id}')"
                            class="py-3.5 px-4 hover:bg-white/10 text-white transition flex items-center gap-1.5 focus:outline-none"
                            :class="activeMegaSector === '${sec.id}' ? 'bg-white/20 text-[#be9c79]' : ''">
                        <span>${sec.title}</span>
                        <i data-lucide="chevron-down" class="w-3 h-3 transition-transform" :class="activeMegaSector === '${sec.id}' ? 'rotate-180 text-[#be9c79]' : 'text-white/70'"></i>
                    </button>
                </div>
            `;

            let columnsHTML = '';
            sec.columns.forEach(col => {
                let linksHTML = '';
                col.links.forEach(lnk => {
                    linksHTML += `
                        <li>
                            <a href="${lnk.url}" class="group flex items-start gap-2.5 p-1.5 rounded-xl hover:bg-slate-50 transition text-slate-700 hover:text-[#004876]">
                                <div class="w-6 h-6 rounded-lg bg-slate-100 text-[#004876] group-hover:bg-[#be9c79]/20 group-hover:text-[#004876] flex items-center justify-center shrink-0 transition">
                                    <i data-lucide="${lnk.icon}" class="w-3.5 h-3.5"></i>
                                </div>
                                <span class="text-xs font-semibold leading-snug pt-0.5">${lnk.text}</span>
                            </a>
                        </li>
                    `;
                });

                columnsHTML += `
                    <div class="space-y-4">
                        <h4 class="font-black text-sm text-[#004876] pb-2 border-b border-slate-200 flex items-center justify-between">
                            <span>${col.heading}</span>
                            <span class="w-2 h-2 rounded-full bg-[#be9c79]"></span>
                        </h4>
                        <ul class="space-y-2.5">
                            ${linksHTML}
                        </ul>
                    </div>
                `;
            });

            sectorPanels += `
                <div data-mega-sector-panel="${sec.id}" 
                     class="grid grid-cols-1 md:grid-cols-3 gap-8"
                     style="display: none;">
                    ${columnsHTML}
                </div>
            `;
        });

        return `
        <nav id="lusail-mega-nav"
             class="bg-gradient-to-r from-[#004876] to-[#003354] text-white text-xs font-bold hidden lg:block shadow-md relative border-b-2 border-[#be9c79]" 
             x-data="{ activeMegaSector: null }"
             @mouseleave="activeMegaSector = null">
            <div class="max-w-7xl mx-auto px-6 flex items-center justify-between">
                <div class="flex items-center divide-x divide-x-reverse divide-white/10">
                    <a href="index.html" class="py-3.5 px-4 bg-white/20 text-[#be9c79] font-bold transition flex items-center gap-1.5"><i data-lucide="home" class="w-3.5 h-3.5"></i> الرئيسية</a>
                    ${sectorButtons}
                </div>
                <div class="flex items-center gap-4 text-[11px] text-white/90">
                    <a href="tel:44011111" class="hover:text-[#be9c79] transition flex items-center gap-1"><i data-lucide="phone" class="w-3 h-3 text-[#be9c79]"></i> +974 4401 1111</a>
                    <a href="mailto:info@lu.edu.qa" class="hover:text-[#be9c79] transition flex items-center gap-1"><i data-lucide="mail" class="w-3 h-3 text-[#be9c79]"></i> info@lu.edu.qa</a>
                </div>
            </div>

            <div id="lusail-mega-panels-container"
                 class="absolute top-full left-0 right-0 bg-white text-slate-800 shadow-2xl border-t border-b border-slate-200 z-50 py-8 px-6"
                 style="display: none;">
                <div class="max-w-7xl mx-auto">
                    ${sectorPanels}
                </div>
            </div>
        </nav>`;
    },

    // Return the standard unified Institutional Footer HTML
    getFooterHTML() {
        return `
        <footer class="bg-white text-slate-600 text-xs border-t border-slate-200 mt-16">
            <div class="max-w-7xl mx-auto p-6 sm:p-8 lg:p-10 grid grid-cols-1 md:grid-cols-4 gap-8">
                <!-- Col 1: About & Accreditation -->
                <div class="space-y-3.5">
                    <div class="flex items-center gap-3">
                        <img src="https://lu.edu.qa/img/lu-logo.webp" alt="جامعة لوسيل" class="h-10 w-auto object-contain">
                    </div>
                    <p class="text-[11px] leading-relaxed text-slate-500">
                        جامعة لوسيل صرح أكاديمي وطني رائد بدولة قطر يقدم برامج جامعية نوعية معتمدة تلبي احتياجات سوق العمل وتدعم رؤية قطر الوطنية 2030.
                    </p>
                    <div class="pt-1 flex items-center gap-2 text-[10px] text-slate-400 font-bold">
                        <i data-lucide="shield-check" class="w-4 h-4 text-emerald-600"></i>
                        <span>معتمدة من وزارة التربية والتعليم والتعليم العالي</span>
                    </div>
                </div>

                <!-- Col 2: Academic Colleges -->
                <div>
                    <h4 class="font-black text-slate-900 mb-3.5 text-xs flex items-center gap-1.5">
                        <span class="w-1.5 h-3 bg-[#004876] rounded-full"></span>
                        <span>الكليات الأكاديمية (4)</span>
                    </h4>
                    <ul class="space-y-2 text-[11px]">
                        <li><a href="college-it.html" class="hover:text-[#004876] font-medium transition">كلية تكنولوجيا المعلومات (IT)</a></li>
                        <li><a href="college-law.html" class="hover:text-[#004876] font-medium transition">كلية القانون والعلوم القضائية</a></li>
                        <li><a href="college-business.html" class="hover:text-[#004876] font-medium transition">كلية التجارة والأعمال (Business)</a></li>
                        <li><a href="college-education.html" class="hover:text-[#004876] font-medium transition">كلية التربية والآداب (Education)</a></li>
                        <li><a href="colleges.html" class="text-[#004876] font-bold hover:underline">دليل الكليات الـ 4 الشامل ←</a></li>
                    </ul>
                </div>

                <!-- Col 3: Quick Portals -->
                <div>
                    <h4 class="font-black text-slate-900 mb-3.5 text-xs flex items-center gap-1.5">
                        <span class="w-1.5 h-3 bg-[#be9c79] rounded-full"></span>
                        <span>بوابات سريعة</span>
                    </h4>
                    <ul class="space-y-2 text-[11px]">
                        <li><a href="admissions.html" class="hover:text-[#004876] font-medium transition">بوابة القبول والتسجيل الفوري</a></li>
                        <li><a href="admission-requirements.html" class="hover:text-[#004876] font-medium transition">شروط القبول ومعادلة الشهادات</a></li>
                        <li><a href="tuition-fees.html" class="hover:text-[#004876] font-medium transition">حاسبة الرسوم والمنح 50%-100%</a></li>
                        <li><a href="academic-calendar.html" class="hover:text-[#004876] font-medium transition">التقويم الأكاديمي 2026/2027</a></li>
                        <li><a href="services.html" class="hover:text-[#004876] font-medium transition">منظومة الخدمات الإلكترونية (16)</a></li>
                        <li><a href="library.html" class="hover:text-[#004876] font-medium transition">مكتبة لوسيل المركزية (مداد)</a></li>
                    </ul>
                </div>

                <!-- Col 4: Official Contact -->
                <div>
                    <h4 class="font-black text-slate-900 mb-3.5 text-xs flex items-center gap-1.5">
                        <span class="w-1.5 h-3 bg-emerald-600 rounded-full"></span>
                        <span>العنوان والتواصل الرسمي</span>
                    </h4>
                    <p class="text-[11px] text-slate-600 mb-2 leading-relaxed">
                        المنطقة 69، شارع 100، مبنى 333، جبل ثعيلب، مدينة لوسيل، دولة قطر
                    </p>
                    <p class="text-[11px] text-slate-600 mb-1">
                        مركز الاتصال الموحد: <strong class="text-slate-900" dir="ltr">+974 4401 1111</strong>
                    </p>
                    <p class="text-[11px] text-slate-600 mb-2">
                        البريد الرسمي: <a href="mailto:info@lu.edu.qa" class="text-[#004876] font-bold">info@lu.edu.qa</a>
                    </p>
                    <div class="flex items-center gap-2 pt-1 text-slate-400">
                        <a href="https://x.com/Lusail_Uni" target="_blank" class="w-7 h-7 rounded-lg bg-slate-100 hover:bg-[#004876] hover:text-white flex items-center justify-center transition"><i data-lucide="twitter" class="w-3.5 h-3.5"></i></a>
                        <a href="https://www.instagram.com/lusail_uni" target="_blank" class="w-7 h-7 rounded-lg bg-slate-100 hover:bg-[#004876] hover:text-white flex items-center justify-center transition"><i data-lucide="instagram" class="w-3.5 h-3.5"></i></a>
                        <a href="https://www.linkedin.com/school/lusail-university" target="_blank" class="w-7 h-7 rounded-lg bg-slate-100 hover:bg-[#004876] hover:text-white flex items-center justify-center transition"><i data-lucide="linkedin" class="w-3.5 h-3.5"></i></a>
                    </div>
                </div>
            </div>

            <!-- Copyright Bar -->
            <div class="bg-slate-50 py-3.5 px-6 text-center text-[10px] text-slate-500 border-t border-slate-200">
                <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-2">
                    <span>© 2026 جامعة لوسيل. جميع الحقوق محفوظة. صرح وطني للتعليم العالي، دولة قطر.</span>
                    <div class="flex items-center gap-4 text-slate-400">
                        <a href="about.html" class="hover:text-slate-700">عن الجامعة</a>
                        <span>•</span>
                        <a href="contact.html" class="hover:text-slate-700">سياسة الخصوصية</a>
                        <span>•</span>
                        <a href="faq.html" class="hover:text-slate-700">الأسئلة الشائعة</a>
                    </div>
                </div>
            </div>
        </footer>`;
    },

    // Mobile Drawer Toggle
    toggleMobileDrawer() {
        let drawer = document.getElementById('lusail-mobile-drawer');
        if (!drawer) {
            this.injectModals();
            drawer = document.getElementById('lusail-mobile-drawer');
        }
        if (drawer) {
            drawer.classList.toggle('hidden');
        }
    },

    // Spotlight Search Modal Handling & Real-time Filtering
    openSpotlight() {
        let modal = document.getElementById('lusail-spotlight-modal');
        if (!modal) {
            this.injectModals();
            modal = document.getElementById('lusail-spotlight-modal');
        }
        if (modal) {
            modal.classList.remove('hidden');
            const input = document.getElementById('lusail-spotlight-input');
            if (input) {
                input.value = '';
                input.focus();
                this.filterSpotlight('');
            }
        }
    },

    closeSpotlight() {
        const modal = document.getElementById('lusail-spotlight-modal');
        if (modal) {
            modal.classList.add('hidden');
        }
    },

    filterSpotlight(query) {
        const resultsContainer = document.getElementById('lusail-spotlight-results');
        if (!resultsContainer) return;

        const q = (query || '').trim().toLowerCase();
        const matches = this.searchIndex.filter(item => {
            if (!q) return true;
            return item.title.toLowerCase().includes(q) ||
                   item.category.toLowerCase().includes(q) ||
                   (item.desc && item.desc.toLowerCase().includes(q));
        }).slice(0, 10);

        if (matches.length === 0) {
            resultsContainer.innerHTML = `
                <div class="py-12 text-center text-slate-400">
                    <p class="text-sm font-medium">لم يتم العثور على نتائج مطابقة لـ "${query}"</p>
                    <p class="text-xs text-slate-400 mt-1">جرّب البحث بكلمات أخرى مثل: ذكاء اصطناعي، قبول، رسوم، تقويم، قانون</p>
                </div>
            `;
            return;
        }

        resultsContainer.innerHTML = matches.map(item => `
            <a href="${item.url}" class="flex items-start gap-3.5 p-3 rounded-2xl hover:bg-slate-50 transition border border-transparent hover:border-slate-200 group">
                <div class="w-9 h-9 rounded-xl bg-slate-100 text-[#004876] group-hover:bg-[#be9c79]/20 group-hover:text-[#004876] flex items-center justify-center shrink-0 transition">
                    <i data-lucide="${item.icon || 'arrow-left'}" class="w-4 h-4"></i>
                </div>
                <div class="flex-1 min-w-0">
                    <div class="flex items-center justify-between gap-2">
                        <span class="text-xs font-bold text-slate-900 group-hover:text-[#004876]">${item.title}</span>
                        <span class="text-[10px] px-2 py-0.5 rounded-md bg-slate-100 text-slate-500 font-semibold shrink-0">${item.category}</span>
                    </div>
                    <p class="text-[11px] text-slate-500 truncate mt-0.5">${item.desc || ''}</p>
                </div>
            </a>
        `).join('');

        if (window.lucide) {
            window.lucide.createIcons();
        }
    },

    openSignModal() {
        let modal = document.getElementById('lusail-sign-modal');
        if (!modal) {
            this.injectModals();
            modal = document.getElementById('lusail-sign-modal');
        }
        if (modal) {
            modal.classList.remove('hidden');
        } else {
            alert('مرحباً بك في خدمة لغة الإشارة المعتمدة بجامعة لوسيل للطلبة والمراجعين من ذوي الإعاقة السمعية.');
        }
    },

    closeSignModal() {
        const modal = document.getElementById('lusail-sign-modal');
        if (modal) modal.classList.add('hidden');
    },

    // Inject Search Modal, Sign Modal, and Mobile Drawer if not already in document
    injectModals() {
        if (!document.getElementById('lusail-spotlight-modal')) {
            const spotlightDiv = document.createElement('div');
            spotlightDiv.id = 'lusail-spotlight-modal';
            spotlightDiv.className = 'fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex items-start justify-center pt-20 p-4 hidden';
            spotlightDiv.innerHTML = `
                <div class="bg-white w-full max-w-2xl rounded-3xl shadow-2xl border border-slate-200 overflow-hidden" onclick="event.stopPropagation()">
                    <div class="p-4 border-b border-slate-200 flex items-center gap-3">
                        <i data-lucide="search" class="w-5 h-5 text-[#004876] shrink-0"></i>
                        <input id="lusail-spotlight-input" 
                               type="text" 
                               placeholder="ابحث عن كلية، تخصص، شروط القبول، الرسوم، الخدمات، أو بوابة..." 
                               class="w-full text-sm font-semibold focus:outline-none placeholder:text-slate-400"
                               oninput="window.LusailNav.filterSpotlight(this.value)">
                        <button onclick="window.LusailNav.closeSpotlight()" class="p-1 rounded-lg hover:bg-slate-100 text-slate-400">
                            <i data-lucide="x" class="w-5 h-5"></i>
                        </button>
                    </div>
                    <div id="lusail-spotlight-results" class="max-h-[60vh] overflow-y-auto p-3 space-y-1 divide-y divide-slate-50">
                        <!-- Dynamic items -->
                    </div>
                    <div class="bg-slate-50 px-4 py-2.5 border-t border-slate-200 flex items-center justify-between text-[11px] text-slate-500 font-medium">
                        <span>انقر على أي نتيجة للانتقال المباشر</span>
                        <div class="flex items-center gap-2">
                            <span>للإغلاق</span>
                            <kbd class="px-1.5 py-0.5 bg-white border border-slate-200 rounded font-mono text-[9px]">ESC</kbd>
                        </div>
                    </div>
                </div>
            `;
            spotlightDiv.addEventListener('click', () => this.closeSpotlight());
            document.body.appendChild(spotlightDiv);
        }

        if (!document.getElementById('lusail-sign-modal')) {
            const signDiv = document.createElement('div');
            signDiv.id = 'lusail-sign-modal';
            signDiv.className = 'fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-4 hidden';
            signDiv.innerHTML = `
                <div class="bg-white max-w-md w-full rounded-3xl p-6 shadow-2xl border border-slate-200 text-center space-y-4" onclick="event.stopPropagation()">
                    <div class="w-16 h-16 bg-[#be9c79]/15 text-[#004876] rounded-2xl flex items-center justify-center mx-auto">
                        <i data-lucide="hand" class="w-8 h-8 text-[#be9c79]"></i>
                    </div>
                    <h3 class="text-base font-black text-[#004876]">خدمة لغة الإشارة والوصول الرقمي</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        توفر جامعة لوسيل ترجمة فورية بلغة الإشارة المعتمدة للطلبة والمراجعين من ذوي الإعاقة السمعية في كافة مكاتب القبول، والتسجيل، والخدمات الطلابية.
                    </p>
                    <div class="p-3 bg-emerald-50 text-emerald-800 text-xs rounded-xl font-bold flex items-center justify-center gap-2 border border-emerald-200">
                        <i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-600"></i>
                        <span>متوافق مع المعايير الدولية للنفاذ الرقمي WCAG 2.1</span>
                    </div>
                    <button onclick="window.LusailNav.closeSignModal()" class="w-full py-2.5 bg-[#004876] hover:bg-[#003354] text-white text-xs font-bold rounded-xl transition shadow-md">
                        إغلاق
                    </button>
                </div>
            `;
            signDiv.addEventListener('click', () => this.closeSignModal());
            document.body.appendChild(signDiv);
        }

        if (!document.getElementById('lusail-mobile-drawer')) {
            const drawerDiv = document.createElement('div');
            drawerDiv.id = 'lusail-mobile-drawer';
            drawerDiv.className = 'fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex justify-end lg:hidden hidden';
            drawerDiv.innerHTML = `
                <div class="bg-white w-full max-w-xs h-full shadow-2xl flex flex-col justify-between overflow-y-auto" onclick="event.stopPropagation()">
                    <div class="p-4 border-b border-slate-200 flex items-center justify-between bg-slate-50">
                        <img src="https://lu.edu.qa/img/lu-logo.webp" alt="جامعة لوسيل" class="h-9 w-auto">
                        <button onclick="window.LusailNav.toggleMobileDrawer()" class="p-1 rounded-lg hover:bg-slate-200 text-slate-600">
                            <i data-lucide="x" class="w-5 h-5"></i>
                        </button>
                    </div>
                    <div class="p-4 space-y-4 flex-1">
                        <div class="space-y-1">
                            <span class="text-[10px] font-black text-slate-400 uppercase tracking-wider block px-2">الكليات الأكاديمية</span>
                            <a href="college-it.html" class="flex items-center gap-2.5 p-2 rounded-xl text-xs font-bold text-slate-700 hover:bg-slate-100 hover:text-[#004876]"><i data-lucide="cpu" class="w-4 h-4 text-[#004876]"></i> كلية تكنولوجيا المعلومات</a>
                            <a href="college-law.html" class="flex items-center gap-2.5 p-2 rounded-xl text-xs font-bold text-slate-700 hover:bg-slate-100 hover:text-[#004876]"><i data-lucide="scale" class="w-4 h-4 text-[#004876]"></i> كلية القانون</a>
                            <a href="college-business.html" class="flex items-center gap-2.5 p-2 rounded-xl text-xs font-bold text-slate-700 hover:bg-slate-100 hover:text-[#004876]"><i data-lucide="briefcase" class="w-4 h-4 text-[#004876]"></i> كلية التجارة والأعمال</a>
                            <a href="college-education.html" class="flex items-center gap-2.5 p-2 rounded-xl text-xs font-bold text-slate-700 hover:bg-slate-100 hover:text-[#004876]"><i data-lucide="book-open" class="w-4 h-4 text-[#004876]"></i> كلية التربية والآداب</a>
                            <a href="colleges.html" class="flex items-center gap-2.5 p-2 rounded-xl text-xs font-bold text-[#004876] bg-slate-50"><i data-lucide="building-2" class="w-4 h-4"></i> دليل الكليات الـ 4 والبرامج الـ 17</a>
                        </div>
                        <div class="space-y-1 pt-2 border-t border-slate-100">
                            <span class="text-[10px] font-black text-slate-400 uppercase tracking-wider block px-2">القبول والتسجيل</span>
                            <a href="admissions.html" class="flex items-center gap-2.5 p-2 rounded-xl text-xs font-bold text-slate-700 hover:bg-slate-100"><i data-lucide="send" class="w-4 h-4 text-[#be9c79]"></i> التقديم الإلكتروني الفوري</a>
                            <a href="admission-requirements.html" class="flex items-center gap-2.5 p-2 rounded-xl text-xs font-bold text-slate-700 hover:bg-slate-100"><i data-lucide="award" class="w-4 h-4 text-[#be9c79]"></i> شروط القبول والشهادات</a>
                            <a href="tuition-fees.html" class="flex items-center gap-2.5 p-2 rounded-xl text-xs font-bold text-slate-700 hover:bg-slate-100"><i data-lucide="calculator" class="w-4 h-4 text-[#be9c79]"></i> الرسوم الدراسية والمنح</a>
                            <a href="academic-calendar.html" class="flex items-center gap-2.5 p-2 rounded-xl text-xs font-bold text-slate-700 hover:bg-slate-100"><i data-lucide="calendar" class="w-4 h-4 text-[#be9c79]"></i> التقويم الأكاديمي</a>
                        </div>
                        <div class="space-y-1 pt-2 border-t border-slate-100">
                            <span class="text-[10px] font-black text-slate-400 uppercase tracking-wider block px-2">الحياة الجامعية والمرافق</span>
                            <a href="campus-life.html" class="flex items-center gap-2.5 p-2 rounded-xl text-xs font-bold text-slate-700 hover:bg-slate-100"><i data-lucide="map-pin" class="w-4 h-4 text-emerald-600"></i> الحرم الجامعي</a>
                            <a href="student-clubs.html" class="flex items-center gap-2.5 p-2 rounded-xl text-xs font-bold text-slate-700 hover:bg-slate-100"><i data-lucide="users" class="w-4 h-4 text-emerald-600"></i> الأندية الطلابية</a>
                            <a href="campus-life.html#sports" class="flex items-center gap-2.5 p-2 rounded-xl text-xs font-bold text-slate-700 hover:bg-slate-100"><i data-lucide="trophy" class="w-4 h-4 text-emerald-600"></i> الأنشطة والبطولات الرياضية</a>
                            <a href="library.html" class="flex items-center gap-2.5 p-2 rounded-xl text-xs font-bold text-slate-700 hover:bg-slate-100"><i data-lucide="library" class="w-4 h-4 text-emerald-600"></i> مكتبة لوسيل المركزية</a>
                        </div>
                        <div class="space-y-1 pt-2 border-t border-slate-100">
                            <span class="text-[10px] font-black text-slate-400 uppercase tracking-wider block px-2">الأنظمة والبوابات</span>
                            <a href="student-portal.html" class="flex items-center gap-2.5 p-2 rounded-xl text-xs font-bold text-emerald-800 bg-emerald-50"><i data-lucide="layout-dashboard" class="w-4 h-4 text-emerald-600"></i> بوابة الطالب الذاتية</a>
                            <a href="services.html" class="flex items-center gap-2.5 p-2 rounded-xl text-xs font-bold text-slate-700 hover:bg-slate-100"><i data-lucide="layers" class="w-4 h-4 text-[#004876]"></i> منظومة الخدمات الإلكترونية</a>
                            <a href="desk.html" class="flex items-center gap-2.5 p-2 rounded-xl text-xs font-bold text-[#004876] bg-slate-50"><i data-lucide="shield" class="w-4 h-4"></i> لوحة تشغيل Desk OS</a>
                        </div>
                    </div>
                    <div class="p-4 bg-slate-50 border-t border-slate-200 text-center">
                        <a href="tel:44011111" class="text-xs font-bold text-[#004876] flex items-center justify-center gap-1.5"><i data-lucide="phone" class="w-3.5 h-3.5 text-[#be9c79]"></i> +974 4401 1111</a>
                    </div>
                </div>
            `;
            drawerDiv.addEventListener('click', () => this.toggleMobileDrawer());
            document.body.appendChild(drawerDiv);
        }
    },

    // Attach Vanilla JS fallback events to Mega Menu buttons so it works with or without Alpine.js
    initMegaMenuEvents() {
        const nav = document.getElementById('lusail-mega-nav');
        if (!nav) return;

        const buttons = nav.querySelectorAll('[data-mega-sector-btn]');
        const panelsContainer = document.getElementById('lusail-mega-panels-container');
        const panels = nav.querySelectorAll('[data-mega-sector-panel]');

        const showSector = (sectorId) => {
            buttons.forEach(btn => {
                if (btn.getAttribute('data-mega-sector-btn') === sectorId) {
                    btn.classList.add('bg-white/20', 'text-[#be9c79]');
                } else {
                    btn.classList.remove('bg-white/20', 'text-[#be9c79]');
                }
            });

            let anyOpen = false;
            panels.forEach(p => {
                if (p.getAttribute('data-mega-sector-panel') === sectorId) {
                    p.style.display = 'grid';
                    anyOpen = true;
                } else {
                    p.style.display = 'none';
                }
            });

            if (panelsContainer) {
                panelsContainer.style.display = anyOpen ? 'block' : 'none';
            }
        };

        const hideAll = () => {
            buttons.forEach(btn => btn.classList.remove('bg-white/20', 'text-[#be9c79]'));
            panels.forEach(p => p.style.display = 'none');
            if (panelsContainer) panelsContainer.style.display = 'none';
        };

        buttons.forEach(btn => {
            const secId = btn.getAttribute('data-mega-sector-btn');
            btn.addEventListener('mouseenter', () => showSector(secId));
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                showSector(secId);
            });
        });

        nav.addEventListener('mouseleave', hideAll);
    },

    // Inject Unified Navigation into Containers or document
    renderAll() {
        this.injectModals();

        const headerContainer = document.getElementById('lusail-header-mount');
        if (headerContainer) {
            headerContainer.innerHTML = this.getTopBarHTML() + this.getMainHeaderHTML() + this.getMegaMenuHTML();
            this.initMegaMenuEvents();
        }

        const footerContainer = document.getElementById('lusail-footer-mount');
        if (footerContainer) {
            footerContainer.innerHTML = this.getFooterHTML();
        }

        if (window.lucide) {
            window.lucide.createIcons();
        }
    },

    initSpotlight() {
        document.addEventListener('keydown', (e) => {
            if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
                e.preventDefault();
                this.openSpotlight();
            }
            if (e.key === 'Escape') {
                this.closeSpotlight();
                this.closeSignModal();
            }
        });
    }
};

document.addEventListener('DOMContentLoaded', () => {
    window.LusailNav.initSpotlight();
    window.LusailNav.renderAll();
    if (window.lucide) {
        window.lucide.createIcons();
    }
});
