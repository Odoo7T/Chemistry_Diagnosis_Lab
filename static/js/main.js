document.addEventListener("DOMContentLoaded", () => {
    // Language Switcher Elements & State
    const langBtnAr = document.getElementById("lang-btn-ar");
    const langBtnEn = document.getElementById("lang-btn-en");
    let currentLang = localStorage.getItem("chemlab_lang") || "ar";

    // Bilingual Localization (Arabic & English)
    const TRANSLATIONS = {
        ar: {
            header_logo_sub: "نظام تشخيص العينات العضوية وغير العضوية",
            header_salt_btn: "🧂 تشخيص ملح كامل",
            header_new_btn: "↺ عينة جديدة",
            header_predictor_btn: "⚗ محاكي التفاعلات",
            header_flame_btn: "دليل اللهب",
            header_status: "النظام جاهز",
            workspace_eyebrow: "CHEMISTRY DIAGNOSIS LAB — EXPERT SYSTEM",
            workspace_title: "فحص وتشخيص العينة المجهولة (عضوي / غير عضوي)",
            workspace_desc: "حدد مسار الفحص التحليلي المناسب: كشف المركبات العضوية، تشخيص الأملاح غير العضوية الكاملة، كشف الأيونات المنفردة، أو فحص التسخين المبدئي للعينة المجهولة.",
            tab_all_text: "🔀 تحديد مسار التحليل (عضوي / غير عضوي)",
            tab_salt_text: "🧂 تشخيص ملح كامل (30 ملحاً)",
            tab_organic_text: "🧪 كشف المركبات العضوية (25 مركباً)",
            tab_ions_text: "⚗️ كشف أيونات منفردة",
            step_back: "← الرجوع للسؤال السابق",
            stage4_eyebrow: "CONFIRMATORY PROTOCOL",
            stage4_title: "النتيجة المحتملة والاختبار التأكيدي",
            stage4_desc: "التأكيد المعملي النهائي لهوية الأيون المشخص لضمان صحة النتيجة علمياً.",
            stage4_structure_badge: "🧪 الصيغة البنائية للمركب",
            stage4_yes: "نعم، إجراء الاختبار التأكيدي (Recommended)",
            stage4_skip: "لا، الاكتفاء بهذه النتيجة وعرض التقرير",
            confirmatory_confirmed: "✓ نعم، ظهرت العلامة التأكيدية بنجاح",
            confirmatory_failed: "✗ لا، لم تظهر العلامة المتوقعة",
            stage4_failure_title: "لم يتم تأكيد هوية الأيون (التوقع غير صحيح)",
            stage4_failure_how: "كيف تريد المتابعة الآن؟",
            failure_restart: "↺ نعيد من الأول (البدء من الكاشف الأول مع الاحتفاظ باللون والحالة)",
            failure_resume: "⤺ نكمل من اللي وصلنا له (متابعة البحث من الخطوة السابقة كمسألة جديدة)",
            user_error_title: "⚠️ تنبيه: خطأ في المشاهدات المعملية لديك!",
            user_error_resume: "⤺ تغيير المشاهدة وتجربة مسار آخر",
            user_error_restart: "↺ بدء فحص عينة جديدة من الصفر",
            report_banner_sub: "تقرير التحليل الكيميائي النوعي غير العضوي — Qualitative Unknown Analysis Report",
            report_box1_title: "1. الخواص الأولية للعينة (Physical Properties)",
            report_label_color: "لون العينة الأصلي:",
            report_label_state: "الحالة الفيزيائية:",
            report_label_type: "تصنيف المادة:",
            report_box2_title: "2. التشخيص الكيميائي النهائي (Identified Species)",
            report_label_formula: "الصيغة الكيميائية:",
            report_label_name: "الاسم العلمي:",
            report_label_confirm: "حالة الاختبار التأكيدي:",
            report_structure_badge: "🧪 الصيغة البنائية للمركب (Chemical Structure)",
            salt_how_btn: "كيف وصلت لهذه النتيجة؟ (How did we deduce this salt?)",
            report_box3_title: "3. مسار الفحوصات والكواشف المضافة وملاحظاتها (Analytical Trail)",
            report_box4_title: "4. المعادلات الكيميائية الموزونة (Verified Equations)",
            report_box5_title: "5. ملاحظات السلامة والاستدلال المعملي (Safety & Diagnostic Notes)",
            report_action_prompt: "هل تريد حفظ التقرير النهائي أو بدء عينة جديدة؟",
            report_print: "🖨️ حفظ / طباعة التقرير النهائي (Print / Save Report)",
            report_new_sample: "↺ بدء فحص عينة جديدة (New Sample)",
            predictor_eyebrow: "AUXILIARY LAB TOOL",
            predictor_title: "محاكي التفاعلات الكيميائية (50 تفاعلاً خبيراً)",
            predictor_desc: "استكشف النواتج وتغيرات الألوان والمعادلات الكيميائية باختيار أي أيون وكاشف مباشرة من قاعدة البيانات.",
            predictor_label_ion: "1. اختر الأيون (Ion):",
            predictor_sublabel_cations: "كاتيونات (Cations):",
            predictor_sublabel_anions: "أنيونات (Anions):",
            predictor_label_reagent: "2. اختر الكاشف (Reagent):",
            predictor_label_combos: "أمثلة سريعة مؤكدة:",
            predict_btn: "مــزج وتوقع التفاعل الكيميائي",
            tube_label: "جاهز للاختبار",
            predict_placeholder: "اختر أيوناً وكاشفاً ثم اضغط مـزج وتوقع التفاعل لمعاينة النتيجة والمعادلة الكيميائية.",
            predict_eq_title: "المعادلات الكيميائية — EQUATIONS",
            predict_notes_title: "الملاحظات والشروط المعملية — NOTES",
            ref_modal_title: "الملاحظات المرجعية وكشوفات اللهب الجافة",
            ref_modal_desc: "دليل كشف اللهب للفلزات القلوية وملاحظات التحليل النوعي.",
            structure_modal_title: "الصيغة البنائية للمركب (Chemical Structure)",
            page_footer: "CHEMLAB — نظام خبير الكيمياء غير العضوية الاستدلالي وتشخيص العينات المجهولة"
        },
        en: {
            header_logo_sub: "Organic & Inorganic Qualitative Diagnostic System",
            header_salt_btn: "🧂 Complete Salt Diagnosis",
            header_new_btn: "↺ New Sample",
            header_predictor_btn: "⚗ Reaction Simulator",
            header_flame_btn: "Flame Guide",
            header_status: "SYSTEM READY",
            workspace_eyebrow: "CHEMISTRY DIAGNOSIS LAB — EXPERT SYSTEM",
            workspace_title: "Unknown Sample Chemical Diagnosis (Organic / Inorganic)",
            workspace_desc: "Select the diagnostic pathway: Organic Compounds, Complete Inorganic Salts, Single Ions, or Preliminary Heating Test.",
            tab_all_text: "🔀 Select Route (Organic / Inorganic)",
            tab_salt_text: "🧂 Complete Salt Diagnosis (30 Salts)",
            tab_organic_text: "🧪 Organic Analysis (25 Compounds)",
            tab_ions_text: "⚗️ Single Ion Analysis",
            step_back: "← Back to Previous Question",
            stage4_eyebrow: "CONFIRMATORY PROTOCOL",
            stage4_title: "Suspected Outcome & Confirmatory Test",
            stage4_desc: "Final experimental verification of the identified species to ensure scientific accuracy.",
            stage4_structure_badge: "🧪 Chemical Structure",
            stage4_yes: "Yes, Run Confirmatory Test (Recommended)",
            stage4_skip: "No, Skip to Final Report",
            confirmatory_confirmed: "✓ Yes, Confirmatory Sign Appeared",
            confirmatory_failed: "✗ No, Expected Sign Did Not Appear",
            stage4_failure_title: "Identity Not Confirmed (Hypothesis Disproved)",
            stage4_failure_how: "How would you like to proceed?",
            failure_restart: "↺ Restart from First Reagent (Keep color & physical state)",
            failure_resume: "⤺ Resume from Previous Step (Re-examine branch)",
            user_error_title: "⚠️ Warning: Inconsistent Laboratory Observations!",
            user_error_resume: "⤺ Adjust Observation & Try Another Path",
            user_error_restart: "↺ Start Fresh with New Sample",
            report_banner_sub: "Qualitative Unknown Chemical Analysis Report",
            report_box1_title: "1. Initial Sample Properties (Physical)",
            report_label_color: "Original Color:",
            report_label_state: "Physical State:",
            report_label_type: "Classification:",
            report_box2_title: "2. Final Chemical Diagnosis (Identified Species)",
            report_label_formula: "Chemical Formula:",
            report_label_name: "Scientific Name:",
            report_label_confirm: "Confirmatory Status:",
            report_structure_badge: "🧪 Chemical Structure",
            salt_how_btn: "How did we deduce this salt? (Inference Reasoning)",
            report_box3_title: "3. Analytical Progression Trail & Observations",
            report_box4_title: "4. Verified Balanced Chemical Equations",
            report_box5_title: "5. Safety & Diagnostic Laboratory Notes",
            report_action_prompt: "Would you like to print/save the final report or test a new sample?",
            report_print: "🖨️ Print / Save Final Report",
            report_new_sample: "↺ Start New Unknown Sample",
            predictor_eyebrow: "AUXILIARY LAB TOOL",
            predictor_title: "Chemical Reaction Simulator (50 Expert Reactions)",
            predictor_desc: "Explore reaction products, color changes, and chemical equations by selecting any ion and reagent directly from the database.",
            predictor_label_ion: "1. Select Ion:",
            predictor_sublabel_cations: "Cations:",
            predictor_sublabel_anions: "Anions:",
            predictor_label_reagent: "2. Select Reagent:",
            predictor_label_combos: "Quick Reference Combos:",
            predict_btn: "Mix & Predict Reaction",
            tube_label: "Ready for test",
            predict_placeholder: "Select an ion and a reagent, then click Mix & Predict Reaction to view products and balanced equations.",
            predict_eq_title: "BALANCED CHEMICAL EQUATIONS",
            predict_notes_title: "LABORATORY OBSERVATIONS & CONDITIONS",
            ref_modal_title: "Reference Notes & Dry Flame Tests",
            ref_modal_desc: "Flame test guide for alkali/alkaline earth metals and qualitative analysis notes.",
            structure_modal_title: "Chemical Structure",
            page_footer: "CHEMLAB — Expert Diagnostic System for Qualitative Chemical Analysis"
        }
    };

    const ELEMENT_TRANSLATION_MAP = {
        "header-logo-sub": "header_logo_sub",
        "header-salt-btn-text": "header_salt_btn",
        "header-new-btn-text": "header_new_btn",
        "header-predictor-btn-text": "header_predictor_btn",
        "header-flame-btn-text": "header_flame_btn",
        "header-status-text": "header_status",
        "workspace-eyebrow": "workspace_eyebrow",
        "workspace-title": "workspace_title",
        "workspace-description": "workspace_desc",
        "tab-all-text": "tab_all_text",
        "tab-salt-text": "tab_salt_text",
        "tab-organic-text": "tab_organic_text",
        "tab-ions-text": "tab_ions_text",
        "step-back-text": "step_back",
        "stage4-eyebrow": "stage4_eyebrow",
        "stage4-title": "stage4_title",
        "stage4-desc": "stage4_desc",
        "stage4-structure-badge": "stage4_structure_badge",
        "stage4-yes-text": "stage4_yes",
        "stage4-skip-text": "stage4_skip",
        "confirmatory-confirmed-text": "confirmatory_confirmed",
        "confirmatory-failed-text": "confirmatory_failed",
        "stage4-failure-title": "stage4_failure_title",
        "stage4-failure-how": "stage4_failure_how",
        "failure-restart-text": "failure_restart",
        "failure-resume-text": "failure_resume",
        "user-error-title": "user_error_title",
        "user-error-resume-text": "user_error_resume",
        "user-error-restart-text": "user_error_restart",
        "report-banner-sub": "report_banner_sub",
        "report-box1-title": "report_box1_title",
        "report-label-color": "report_label_color",
        "report-label-state": "report_label_state",
        "report-label-type": "report_label_type",
        "report-box2-title": "report_box2_title",
        "report-label-formula": "report_label_formula",
        "report-label-name": "report_label_name",
        "report-label-confirm": "report_label_confirm",
        "report-structure-badge": "report_structure_badge",
        "salt-how-btn-text": "salt_how_btn",
        "report-box3-title": "report_box3_title",
        "report-box4-title": "report_box4_title",
        "report-box5-title": "report_box5_title",
        "report-action-prompt": "report_action_prompt",
        "report-print-text": "report_print",
        "report-new-sample-text": "report_new_sample",
        "predictor-eyebrow": "predictor_eyebrow",
        "predictor-title": "predictor_title",
        "predictor-desc": "predictor_desc",
        "predictor-label-ion": "predictor_label_ion",
        "predictor-sublabel-cations": "predictor_sublabel_cations",
        "predictor-sublabel-anions": "predictor_sublabel_anions",
        "predictor-label-reagent": "predictor_label_reagent",
        "predictor-label-combos": "predictor_label_combos",
        "predict-btn-text": "predict_btn",
        "tube-label": "tube_label",
        "predict-placeholder-text": "predict_placeholder",
        "predict-eq-title": "predict_eq_title",
        "predict-notes-title": "predict_notes_title",
        "ref-modal-title": "ref_modal_title",
        "ref-modal-desc": "ref_modal_desc",
        "structure-modal-title": "structure_modal_title",
        "page-footer-text": "page_footer"
    };

    function setLanguage(lang) {
        currentLang = lang;
        localStorage.setItem("chemlab_lang", lang);
        document.documentElement.lang = lang;
        document.documentElement.dir = (lang === "ar" ? "rtl" : "ltr");

        if (langBtnAr) langBtnAr.classList.toggle("active", lang === "ar");
        if (langBtnEn) langBtnEn.classList.toggle("active", lang === "en");

        const t = TRANSLATIONS[lang] || TRANSLATIONS.ar;
        for (const [id, val] of Object.entries(ELEMENT_TRANSLATION_MAP)) {
            const el = document.getElementById(id);
            if (el && t[val]) {
                el.textContent = t[val];
            }
        }

        if (typeof setActiveModeTab === "function") {
            setActiveModeTab(activeMode);
        }

        // Re-render question if active and initialized
        if (questionContainer && !questionContainer.hidden && historyStack && historyStack.length > 0) {
            renderCurrentQuestion();
        }

        // Re-render stage 4 if active
        if (stage4Container && !stage4Container.hidden) {
            updateStage4Language();
        }

        // Re-render stage 5 report if active
        if (stage5Container && !stage5Container.hidden) {
            triggerStage5Report();
        }
    }

    function setupLanguageSwitcher() {
        if (langBtnAr) {
            langBtnAr.addEventListener("click", () => {
                if (currentLang !== "ar") setLanguage("ar");
            });
        }
        if (langBtnEn) {
            langBtnEn.addEventListener("click", () => {
                if (currentLang !== "en") setLanguage("en");
            });
        }
        setLanguage(currentLang);
    }

    // Diagnostic Mode Tabs
    const modeAllBtn = document.getElementById("mode-all-btn");
    const modeSaltBtn = document.getElementById("mode-salt-btn");
    const modeOrganicBtn = document.getElementById("mode-organic-btn");
    const modeIonsBtn = document.getElementById("mode-ions-btn");
    let activeMode = "all";

    // DOM Elements - Shell
    const newSampleHeaderBtn = document.getElementById("new-sample-header-btn");
    const togglePredictorBtn = document.getElementById("toggle-predictor-btn");
    const refModalBtn = document.getElementById("ref-modal-btn");
    const refModal = document.getElementById("ref-modal");
    const refModalClose = document.getElementById("ref-modal-close");

    // Inorganic Salt Diagnosis Elements
    const saltDirectHeaderBtn = document.getElementById("salt-direct-header-btn");
    const saltHowContainer = document.getElementById("salt-how-container");
    const saltHowBtn = document.getElementById("salt-how-btn");
    const saltHowArrow = document.getElementById("salt-how-arrow");
    const saltHowPanel = document.getElementById("salt-how-panel");
    const saltHowModal = document.getElementById("salt-how-modal");
    const saltHowModalBody = document.getElementById("salt-how-modal-body");
    const saltHowModalClose = document.getElementById("salt-how-modal-close");

    // Main Workspace Containers
    const diagnosticWorkspace = document.getElementById("diagnostic-workspace");
    const questionContainer = document.getElementById("question-container");
    const questionText = document.getElementById("question-text");
    const questionTextAr = document.getElementById("question-text-ar");
    const questionHintBox = document.getElementById("question-hint-box");
    const questionHintEn = document.getElementById("question-hint-en");
    const questionHintAr = document.getElementById("question-hint-ar");
    const optionsGrid = document.getElementById("options-grid");
    const stepBackBtn = document.getElementById("step-back-btn");
    const breadcrumbTrail = document.getElementById("breadcrumb-trail");
    const qFloatBgLeft = document.getElementById("global-bg-left");
    const qFloatBgRight = document.getElementById("global-bg-right");

    const BG_IMAGES = [
        "/static/images/bg1.png",
        "/static/images/bg2.png",
        "/static/images/bg3.png",
        "/static/images/bg4.png",
        "/static/images/bg5.png",
        "/static/images/bg6.png",
        "/static/images/bg7.png",
        "/static/images/bg8.png",
        "/static/images/bg9.png",
        "/static/images/bg10.png"
    ];

    function setGlobalBackground(leftIdx, rightIdx) {
        if (!qFloatBgLeft || !qFloatBgRight) return;
        const l = BG_IMAGES[leftIdx % BG_IMAGES.length];
        const r = BG_IMAGES[rightIdx % BG_IMAGES.length];

        qFloatBgLeft.style.opacity = "0";
        qFloatBgRight.style.opacity = "0";
        setTimeout(() => {
            qFloatBgLeft.src = l;
            qFloatBgRight.src = r;
            qFloatBgLeft.style.opacity = "0.7";
            qFloatBgRight.style.opacity = "0.7";
        }, 180);
    }

    function updateQuestionBackgroundImages() {
        const stepIdx = Math.max(0, historyStack.length - 1);
        setGlobalBackground(stepIdx * 2, stepIdx * 2 + 1);
    }

    // Stage 4 Confirmatory Container & Failure Handling
    const stage4Container = document.getElementById("stage4-container");
    const stage4PromptBlock = document.getElementById("stage4-prompt-block");
    const stage4PromptText = document.getElementById("stage4-prompt-text");
    const stage4YesBtn = document.getElementById("stage4-yes-btn");
    const stage4SkipBtn = document.getElementById("stage4-skip-btn");
    const stage4ExecutionBlock = document.getElementById("stage4-execution-block");
    const confirmatoryReagentTitle = document.getElementById("confirmatory-reagent-title");
    const confirmatoryProcedure = document.getElementById("confirmatory-procedure");
    const confirmatorySignBadge = document.getElementById("confirmatory-sign-badge");
    const confirmatoryQuestionText = document.getElementById("confirmatory-question-text");
    const confirmatoryConfirmedBtn = document.getElementById("confirmatory-confirmed-btn");
    const confirmatoryFailedBtn = document.getElementById("confirmatory-failed-btn");

    // Failure & Error Blocks
    const stage4FailureBlock = document.getElementById("stage4-failure-block");
    const failedReagentName = document.getElementById("failed-reagent-name");
    const failedIonName = document.getElementById("failed-ion-name");
    const failureRestartBtn = document.getElementById("failure-restart-btn");
    const failureResumeBtn = document.getElementById("failure-resume-btn");

    const userErrorWarningBlock = document.getElementById("user-error-warning-block");
    const repeatedFailedIon = document.getElementById("repeated-failed-ion");
    const userErrorResumeBtn = document.getElementById("user-error-resume-btn");
    const userErrorRestartBtn = document.getElementById("user-error-restart-btn");

    // Stage 5 Report Container
    const stage5Container = document.getElementById("stage5-container");
    const reportId = document.getElementById("report-id");
    const reportDate = document.getElementById("report-date");
    const reportStatus = document.getElementById("report-status");
    const reportColorVal = document.getElementById("report-color-val");
    const reportStateVal = document.getElementById("report-state-val");
    const reportTypeVal = document.getElementById("report-type-val");
    const reportFormulaVal = document.getElementById("report-formula-val");
    const reportNameVal = document.getElementById("report-name-val");
    const reportConfirmVal = document.getElementById("report-confirm-val");
    const reportTimelineList = document.getElementById("report-timeline-list");
    const reportEquationList = document.getElementById("report-equation-list");
    const reportNotesList = document.getElementById("report-notes-list");
    const reportPrintBtn = document.getElementById("report-print-btn");
    const reportNewSampleBtn = document.getElementById("report-new-sample-btn");

    // Chemical Structure & Zoom Modal Elements
    const stage4StructurePreview = document.getElementById("stage4-structure-preview");
    const stage4StructureCard = document.getElementById("stage4-structure-card");
    const stage4StructureImg = document.getElementById("stage4-structure-img");
    const reportStructureCard = document.getElementById("report-structure-card");
    const reportStructureImg = document.getElementById("report-structure-img");
    const structureZoomModal = document.getElementById("structure-zoom-modal");
    const structureModalImg = document.getElementById("structure-modal-img");
    const structureModalTitle = document.getElementById("structure-modal-title");
    const structureModalClose = document.getElementById("structure-modal-close");

    function openStructureZoom(imgSrc, title) {
        if (!structureZoomModal || !structureModalImg) return;
        structureModalImg.src = imgSrc;
        if (structureModalTitle) {
            structureModalTitle.textContent = title || "الصيغة البنائية للمركب (Chemical Structure)";
        }
        structureZoomModal.classList.add("active");
    }

    if (structureModalClose) {
        structureModalClose.addEventListener("click", () => {
            if (structureZoomModal) structureZoomModal.classList.remove("active");
        });
    }

    if (structureZoomModal) {
        structureZoomModal.addEventListener("click", (e) => {
            if (e.target === structureZoomModal) {
                structureZoomModal.classList.remove("active");
            }
        });
    }

    if (stage4StructureCard) {
        stage4StructureCard.addEventListener("click", () => {
            if (stage4StructureImg && stage4StructureImg.src) {
                const title = stage4PromptText ? stage4PromptText.textContent : "الصيغة البنائية";
                openStructureZoom(stage4StructureImg.src, title);
            }
        });
    }

    if (reportStructureCard) {
        reportStructureCard.addEventListener("click", () => {
            if (reportStructureImg && reportStructureImg.src) {
                const title = reportNameVal ? `${reportFormulaVal.textContent} — ${reportNameVal.textContent}` : "الصيغة البنائية";
                openStructureZoom(reportStructureImg.src, title);
            }
        });
    }

    // Predictor Auxiliary Tool Elements
    const predictorView = document.getElementById("predictor-view");
    const cationsPills = document.getElementById("cations-pills");
    const anionsPills = document.getElementById("anions-pills");
    const reagentsPills = document.getElementById("reagents-pills");
    const predictBtn = document.getElementById("predict-btn");
    const tubeLiquid = document.getElementById("tube-liquid");
    const tubePrecipitate = document.getElementById("tube-precipitate");
    const tubeLabel = document.getElementById("tube-label");
    const predictResultPlaceholder = document.getElementById("predict-result-placeholder");
    const predictResultCard = document.getElementById("predict-result-card");
    const predictStatusBadge = document.getElementById("predict-status-badge");
    const predictResultTitle = document.getElementById("predict-result-title");
    const predictResultAr = document.getElementById("predict-result-ar");
    const predictEquationsContainer = document.getElementById("predict-equations-container");
    const predictEquationsList = document.getElementById("predict-equations-list");
    const predictNotesContainer = document.getElementById("predict-notes-container");
    const predictNotesList = document.getElementById("predict-notes-list");

    // State Variables
    let knowledgeBase = null;
    let historyStack = [];
    let sessionData = {
        color: "غير محدد",
        state: "محلول مائي",
        solubility: "غير محدد",
        stepsTrail: [],
        suspectedKey: null,
        suspectedData: null,
        confirmatory: null,
        confirmed: false,
        isSaltDiagnosis: false,
        detected_anion: null,
        detected_cation: null,
        saltOutcome: null
    };
    let selectedIon = null;
    let selectedReagent = null;
    let previousFailedAttempt = null; // remembers an ion whose confirmatory test failed

    // Fetch Knowledge Base Data & Start Immediately
    async function loadData() {
        try {
            const res = await fetch("/api/data");
            if (!res.ok) throw new Error("Failed to load knowledge base");
            knowledgeBase = await res.json();
            setupPredictorControls();
            setupSaltDiagnosisListeners();
            setupModeSelectorListeners();
            startConsultation();
            setupLanguageSwitcher();
        } catch (err) {
            console.error("Error loading knowledge base:", err);
        }
    }

    loadData();

    // ========================================================
    // UNIFIED LAB CONSULTATION (Defaults to Inorganic Salt)
    // ========================================================

    function setActiveModeTab(mode) {
        activeMode = mode;
        if (modeAllBtn) modeAllBtn.classList.toggle("active", mode === "all");
        if (modeSaltBtn) modeSaltBtn.classList.toggle("active", mode === "salt");
        if (modeOrganicBtn) modeOrganicBtn.classList.toggle("active", mode === "organic");
        if (modeIonsBtn) modeIonsBtn.classList.toggle("active", mode === "ions");

        const isEn = currentLang === "en";
        const titleEl = document.getElementById("workspace-title");
        const descEl = document.getElementById("workspace-description");

        if (mode === "all") {
            if (titleEl) titleEl.textContent = isEn ? "Unknown Sample Chemical Diagnosis (Organic / Inorganic)" : "فحص وتشخيص العينة المجهولة (عضوي / غير عضوي)";
            if (descEl) descEl.textContent = isEn
                ? "Select the diagnostic pathway: Organic Compounds, Complete Inorganic Salts, Single Ions, or Preliminary Heating Test."
                : "حدد مسار الفحص التحليلي المناسب: كشف المركبات العضوية، تشخيص الأملاح غير العضوية الكاملة، كشف الأيونات المنفردة، أو فحص التسخين المبدئي للعينة المجهولة.";
        } else if (mode === "salt") {
            if (titleEl) titleEl.textContent = isEn ? "Complete Inorganic Salt Diagnosis (30 Salts)" : "تشخيص الأملاح غير العضوية الكامل (30 ملحاً)";
            if (descEl) descEl.textContent = isEn
                ? "Expert inference system for inorganic salt diagnosis across 3 sequential stages: physical examination, acidic radical (anion) detection, and basic radical (cation) detection."
                : "نظام استدلالي خبير لتشخيص الأملاح غير العضوية عبر 3 مراحل متتالية: الفحص الفيزيائي، كشف الشق الحامضي (Anion)، وكشف الشق القاعدي (Cation) للوصول للملح ومعادلاته واستقراره.";
        } else if (mode === "organic") {
            if (titleEl) titleEl.textContent = isEn ? "Organic Chemical Analysis (25 Compounds)" : "كشف المركبات العضوية (25 مركباً)";
            if (descEl) descEl.textContent = isEn
                ? "Qualitative diagnosis of 25 organic laboratory compounds (liquids & solids) through sequential functional tests."
                : "تشخيص كيفي لـ 25 مركباً عضوياً معملياً (سوائل ومواد صلبة) عبر الفحوصات الوظيفية المتتالية.";
        } else {
            if (titleEl) titleEl.textContent = isEn ? "Single Ion Analysis (Cations & Anions)" : "كشف الأيونات المنفردة (كاتيونات وأنيونات)";
            if (descEl) descEl.textContent = isEn
                ? "Sequential precipitation and group reagent tests for isolated inorganic ions."
                : "فحوصات الترسيب وسلسلة الكواشف النوعية للأيونات غير العضوية المنفردة.";
        }
    }

    function setupModeSelectorListeners() {
        if (modeAllBtn) {
            modeAllBtn.addEventListener("click", () => {
                startConsultation();
            });
        }
        if (modeSaltBtn) {
            modeSaltBtn.addEventListener("click", () => {
                startSaltDiagnosis();
            });
        }
        if (modeOrganicBtn) {
            modeOrganicBtn.addEventListener("click", () => {
                startOrganicDiagnosis();
            });
        }
        if (modeIonsBtn) {
            modeIonsBtn.addEventListener("click", () => {
                startIonDiagnosis();
            });
        }
    }

    function startSaltDiagnosis() {
        setActiveModeTab("salt");
        previousFailedAttempt = null;
        sessionData = {
            color: "غير محدد",
            color_ar: "غير محدد",
            color_en: "Not specified",
            state: "ملح صلب / محلول مائي",
            state_ar: "ملح صلب / محلول مائي",
            state_en: "Solid salt / Aqueous solution",
            solubility: "غير محدد",
            stepsTrail: [],
            suspectedKey: null,
            suspectedData: null,
            confirmatory: null,
            confirmed: false,
            isSaltDiagnosis: true,
            detected_anion: null,
            detected_cation: null,
            saltOutcome: null
        };

        historyStack = [{
            type: "question",
            id: "SALT_START",
            label: currentLang === "en" ? "Step 1: Physical Examination of Salt" : "الخطوة 1: الفحص الفيزيائي للملح",
            label_ar: "الخطوة 1: الفحص الفيزيائي للملح",
            label_en: "Step 1: Physical Examination of Salt"
        }];

        // Show question container, hide confirmatory & report
        questionContainer.hidden = false;
        stage4Container.hidden = true;
        stage5Container.hidden = true;
        if (saltHowContainer) saltHowContainer.style.display = "none";
        if (saltHowPanel) saltHowPanel.style.display = "none";
        if (saltHowBtn) saltHowBtn.classList.remove("active");
        stepBackBtn.style.display = "none";

        renderCurrentQuestion();
        window.scrollTo({ top: 0, behavior: "smooth" });
    }

    function startOrganicDiagnosis() {
        setActiveModeTab("organic");
        previousFailedAttempt = null;
        sessionData = {
            color: "غير محدد",
            color_ar: "غير محدد",
            color_en: "Not specified",
            state: "غير محدد",
            state_ar: "غير محدد",
            state_en: "Not specified",
            solubility: "غير محدد",
            stepsTrail: [],
            suspectedKey: null,
            suspectedData: null,
            confirmatory: null,
            confirmed: false,
            isSaltDiagnosis: false,
            detected_anion: null,
            detected_cation: null,
            saltOutcome: null
        };

        historyStack = [{
            type: "question",
            id: "org_q_state",
            label: currentLang === "en" ? "Organic: Physical State" : "كشف عضوي: الحالة الفيزيائية",
            label_ar: "كشف عضوي: الحالة الفيزيائية",
            label_en: "Organic: Physical State"
        }];

        questionContainer.hidden = false;
        stage4Container.hidden = true;
        stage5Container.hidden = true;
        if (saltHowContainer) saltHowContainer.style.display = "none";
        if (saltHowPanel) saltHowPanel.style.display = "none";
        if (saltHowBtn) saltHowBtn.classList.remove("active");
        stepBackBtn.style.display = "none";

        renderCurrentQuestion();
        window.scrollTo({ top: 0, behavior: "smooth" });
    }

    function startIonDiagnosis() {
        setActiveModeTab("ions");
        previousFailedAttempt = null;
        sessionData = {
            color: "غير محدد",
            color_ar: "غير محدد",
            color_en: "Not specified",
            state: "محلول مائي",
            state_ar: "محلول مائي",
            state_en: "Aqueous Solution",
            solubility: "غير محدد",
            stepsTrail: [],
            suspectedKey: null,
            suspectedData: null,
            confirmatory: null,
            confirmed: false,
            isSaltDiagnosis: false,
            detected_anion: null,
            detected_cation: null,
            saltOutcome: null
        };

        historyStack = [{
            type: "question",
            id: "start_color",
            label: currentLang === "en" ? "Single Ion: Sample Color" : "كشف أيونات: لون العينة الأصلي",
            label_ar: "كشف أيونات: لون العينة الأصلي",
            label_en: "Single Ion: Sample Color"
        }];

        questionContainer.hidden = false;
        stage4Container.hidden = true;
        stage5Container.hidden = true;
        if (saltHowContainer) saltHowContainer.style.display = "none";
        if (saltHowPanel) saltHowPanel.style.display = "none";
        if (saltHowBtn) saltHowBtn.classList.remove("active");
        stepBackBtn.style.display = "none";

        renderCurrentQuestion();
        window.scrollTo({ top: 0, behavior: "smooth" });
    }

    function startConsultation() {
        setActiveModeTab("all");
        previousFailedAttempt = null;
        sessionData = {
            color: "غير محدد",
            color_ar: "غير محدد",
            color_en: "Not specified",
            state: "غير محدد",
            state_ar: "غير محدد",
            state_en: "Not specified",
            solubility: "غير محدد",
            stepsTrail: [],
            suspectedKey: null,
            suspectedData: null,
            confirmatory: null,
            confirmed: false,
            isSaltDiagnosis: false,
            detected_anion: null,
            detected_cation: null,
            saltOutcome: null
        };

        historyStack = [{
            type: "question",
            id: "start_mode",
            label: currentLang === "en" ? "Step 1: Select Analytical Pathway" : "الخطوة 1: تحديد مسار الفحص التحليلي",
            label_ar: "الخطوة 1: تحديد مسار الفحص التحليلي",
            label_en: "Step 1: Select Analytical Pathway"
        }];

        questionContainer.hidden = false;
        stage4Container.hidden = true;
        stage5Container.hidden = true;
        if (saltHowContainer) saltHowContainer.style.display = "none";
        if (saltHowPanel) saltHowPanel.style.display = "none";
        if (saltHowBtn) saltHowBtn.classList.remove("active");
        stepBackBtn.style.display = "none";

        renderCurrentQuestion();
        window.scrollTo({ top: 0, behavior: "smooth" });
    }

    const OPTION_TRANSLATIONS_EN = {
    "أبيض": "White",
    "عديم اللون": "Colorless",
    "أزرق": "Blue",
    "أخضر": "Green",
    "أصفر": "Yellow",
    "بني": "Brown",
    "وردي": "Pink",
    "أسود": "Black",
    "برتقالي": "Orange",
    "غير محدد": "Unspecified / Other",
    "أبيض أو بلورات عديمة اللون": "White or colorless crystals",
    "أزرق أو أزرق مخضر": "Blue or blue-green",
    "أخضر باهت": "Pale green",
    "أصفر أو بني محمر / أسود رمادي": "Yellow, reddish-brown, or grayish-black",
    "محلول مائي (Solution)": "Aqueous Solution",
    "محلول مائي": "Aqueous Solution",
    "مادة صلبة (Solid)": "Solid Substance",
    "مادة صلبة": "Solid Substance",
    "سائل (Liquid)": "Liquid",
    "سائل": "Liquid",
    "صلب (Solid)": "Solid",
    "صلب": "Solid",
    "سائل (Liquid) — يحصر البحث في 11 مركباً عضوياً": "Liquid (Narrows search to 11 organic liquids)",
    "مادة صلبة (Solid) — يحصر البحث في 14 مركباً عضوياً": "Solid (Narrows search to 14 organic solids)",
    "يمتزج تماماً مع الماء البارد (Miscible — طبقة واحدة شفافة)": "Completely miscible with cold water (Single clear layer)",
    "لا يمتزج / شحيح الذوبان (Immiscible — ينفصل في طبقتين أو قطرات زيتية)": "Immiscible / sparingly soluble (Separates into two layers or oily droplets)",
    "تذوب بسهولة وبشكل كامل في الماء البارد (Water-Soluble Organic Solids)": "Easily and completely soluble in cold water (Water-soluble organic solids)",
    "شحيحة أو عديمة الذوبان في الماء البارد (Water-Insoluble Organic Solids)": "Sparingly or insoluble in cold water (Water-insoluble organic solids)",
    "يذوب في الماء البارد مكوناً محلولاً رائقاً": "Dissolves in cold water forming a clear solution",
    "لا يذوب أو شحيح الذوبان جداً في الماء البارد": "Insoluble or sparingly soluble in cold water",
    "انصهار وتفحم وتصاعد أدخنة أو رائحة سكر محروق (مركب عضوي)": "Melting, charring, and evolution of fumes or burnt sugar smell (Organic Compound)",
    "انصهار وتفحم / رائحة سكر محروق (عضوي)": "Melting and charring / burnt sugar smell (Organic)",
    "لا تفحم، بقاء راسب معدني ثابت مع تغير اللون أثناء التسخين أو أبخرة غير متفحمة (مركب غير عضوي)": "No charring, stable mineral residue with color change on heating or non-charring vapors (Inorganic Compound)",
    "لا تفحم / بقاء مادة معدنية ثابتة (غير عضوي)": "No charring / stable mineral residue (Inorganic)",
    "فوران وتصاعد غاز": "Effervescence and gas evolution",
    "راسب أبيض": "White precipitate",
    "لا تغيير / لا يتكون راسب أو غاز": "No change / no precipitate or gas formed",
    "تغير لون المحلول": "Solution color changes",
    "أخرى": "Other observation",
    "غاز عديم اللون يعكر ماء الجير الرائق لفترة وجيزة": "Colorless gas turning clear lime water turbid temporarily (CO₂)",
    "غاز عديم اللون يعكر ماء الجير (CO₂)": "Colorless gas turning lime water turbid (CO₂)",
    "فوران سريع ولحظي بتصاعد غاز CO₂ (لا يرسب MgSO₄ على البارد)": "Rapid instantaneous effervescence with CO₂ (No MgSO₄ ppt in the cold, HCO₃⁻)",
    "فوران سريع ولحظي (HCO₃⁻)": "Rapid instantaneous effervescence (HCO₃⁻)",
    "رائحة بيض فاسد يسود ورقة مبللة بأسيتات الرصاص": "Rotten-egg odor gas turning lead acetate paper black (H₂S)",
    "رائحة بيض فاسد يسود أسيتات الرصاص (H₂S)": "Rotten-egg odor blackening lead acetate (H₂S)",
    "رائحة نفاذة خانقة تخضر ورقة مبللة بثاني كرومات البوتاسيوم": "Suffocating pungent gas turning acidified K₂Cr₂O₇ paper green (SO₂)",
    "رائحة خانقة تخضر ثاني كرومات البوتاسيوم (SO₂)": "Pungent gas turning K₂Cr₂O₇ paper green (SO₂)",
    "تصاعد غاز SO₂ مع ظهور تعكر كبريتي أصفر معلق": "SO₂ gas evolution with yellow suspended sulfur turbidity (Thiosulfate)",
    "تعكر كبريتي أصفر مع غاز SO₂ (ثيوكبريتات)": "Yellow sulfur turbidity with SO₂ gas (Thiosulfate)",
    "أبخرة بنية حمراء عند فوهة الأنبوبة": "Reddish-brown fumes at the tube mouth (NO₂)",
    "أبخرة بنية حمراء عند فوهة الأنبوبة (NO₂)": "Reddish-brown fumes at the tube mouth (NO₂)",
    "لا غاز / أخرى": "No gas / other",
    "نعم (يذوب بالماء الساخن المغلي ويعود للترسيب بالتبريد)": "Yes (dissolves in boiling hot water and recrystallizes upon cooling)",
    "نعم (يذوب بالماء الساخن)": "Yes (dissolves in hot water)",
    "لا يذوب في الماء الساخن، ولكن يذوب في محلول النشادر المخفف": "Does not dissolve in hot water, but dissolves in dilute ammonia",
    "لا (يذوب في النشادر المخفف)": "No (dissolves in dilute ammonia)",
    "لا يذوب في الماء الساخن، ويسود الراسب عند إضافة محلول النشادر": "Does not dissolve in hot water, and precipitate blackens with ammonia",
    "لا (ويسود بمحلول النشادر)": "No (blackens with ammonia)",
    "راسب أزرق": "Blue precipitate",
    "راسب أخضر": "Green precipitate",
    "راسب بني محمر جيلاتيني": "Reddish-brown gelatinous precipitate",
    "راسب أبيض يتأكسد ويتحول إلى بني بالهواء": "White precipitate oxidizing and turning brown in air",
    "يظل لونه أخضر ثابتاً": "Remains green and stable",
    "يتحول السطح تدريجياً إلى بني محمر نتيجة التأكسد": "Surface gradually turns reddish-brown due to oxidation",
    "أزرق داكن (محلول معقد أزرق ملكي ساطع)": "Deep royal blue solution (Tetraamminecopper complex)",
    "نعم، يذوب الراسب في الزيادة من NaOH مع الرج": "Yes, precipitate dissolves in excess NaOH with shaking",
    "لا، لا يذوب الراسب في الزيادة من NaOH": "No, precipitate does not dissolve in excess NaOH",
    "نعم، يذوب الراسب في زيادة الأمونيا": "Yes, precipitate dissolves in excess ammonia",
    "لا، لا يذوب الراسب في زيادة الأمونيا": "No, precipitate does not dissolve in excess ammonia",
    "لهب أحمر طوبي (brick-red flame) وراسب أبيض مع الأوكسالات": "Brick-red flame and white precipitate with ammonium oxalate (Ca²⁺)",
    "لا يوجد لون مميز للهب (راسب أبيض ثابت يعطي لوناً مع الماغنسون)": "No distinctive flame color (White precipitate giving blue color with Magneson, Mg²⁺)",
    "يذوب في الماء الساخن ويعود بالتبريد": "Dissolves in hot water and recrystallizes on cooling",
    "تصاعد غاز النشادر (رائحة نفاذة يزرق ورقة تباع الشمس المبللة)": "Evolution of ammonia gas (Pungent odor turning moist red litmus blue)",
    "يذوب الراسب في حمض HCl مع فوران وتصاعد غاز CO₂": "Precipitate dissolves in HCl with effervescence evolving CO₂ gas",
    "يذوب الراسب في حمض HCl مع تصاعد غاز SO₂ الخانق": "Precipitate dissolves in HCl evolving suffocating SO₂ gas",
    "يذوب الراسب في حمض HCl دون فوران (يعطي راسباً أصفر مع الموليبدات)": "Precipitate dissolves in HCl without gas (Forms yellow precipitate with ammonium molybdate)",
    "لا يذوب الراسب إطلاقاً في حمض HCl المخفف الساخن": "Precipitate is completely insoluble in hot dilute HCl (BaSO₄)",
    "راسب أبيض متجبن": "White curdy precipitate (AgCl)",
    "راسب كريمي / أصفر باهت": "Cream / pale-yellow precipitate (AgBr)",
    "راسب أصفر فاقع": "Bright yellow precipitate (AgI)",
    "راسب أسود من كبريتيد الفضة": "Black precipitate of silver sulfide (Ag₂S)",
    "راسب أحمر طوبي / بني محمر من كرومات الفضة": "Brick-red / reddish-brown precipitate of silver chromate",
    "نعم، يذوب تماماً وبسرعة في النشادر المخفف": "Yes, completely and rapidly dissolves in dilute ammonia",
    "لا يذوب في المخفف": "Does not dissolve in dilute ammonia",
    "يذوب بصعوبة في المخفف ويذوب في النشادر المركز": "Slowly soluble in dilute ammonia, dissolves in concentrated ammonia",
    "لا يذوب في المخفف أو المركز": "Does not dissolve in dilute or concentrated ammonia",
    "يذوب في النشادر المخفف وحمض النيتريك": "Dissolves in dilute ammonia and dilute nitric acid (Phosphate)",
    "لا يذوب نهائياً في النشادر سواء مخفف أو مركز": "Completely insoluble in both dilute and concentrated ammonia (Iodide)",
    "تكون حلقة بنية فاصلة عند السطح الفاصل بين الطبقتين (الحلقة البنية)": "Formation of a brown ring at the liquid junction (Brown Ring Test, Nitrate)",
    "حمضي قوي (تفور وتذوب في محلول بيكربونات الصوديوم NaHCO3 مع تصاعد غاز CO2)": "Strongly acidic (Effervesces with NaHCO₃ solution evolving CO₂ gas)",
    "متعادل مع عباد الشمس ولا يفور مع كربونات أو بيكربونات الصوديوم": "Neutral to litmus and does not effervesce with carbonate or bicarbonate",
    "يزيل لون KMnO4 المحمض البنفسجي، أو يكوّن مرآة فضية مع تولن (خواص اختزالية)": "Decolorizes acidified purple KMnO₄ or forms silver mirror with Tollens' (Reducing properties, Formic acid)",
    "لا يزيل لون KMnO4، وله رائحة الخل المميزة (يعطي لوناً أحمر دامي مع FeCl3 المتعادل)": "Does not decolorize KMnO₄; distinct vinegar odor (Blood-red with neutral FeCl₃, Acetic acid)",
    "يتكون راسب أصفر أو برتقالي فوري متبلور (مركب كربونيل: ألدهيد أو كيتون أليفاتي)": "Forms an immediate yellow or orange crystalline precipitate (Carbonyl compound: Aldehyde or Ketone)",
    "سلبي تماماً مع 2,4-DNP (لا يتكون راسب أصفر أو برتقالي)": "Completely negative with 2,4-DNP (No yellow or orange precipitate, Alcohol)",
    "تكوّن مرآة فضية لامعة Ag على الجدار الداخلي للأنبوبة أو راسب رمادي (ألدهيد مختزل)": "Formation of a shining silver mirror on the tube wall or grey precipitate (Reducing aldehyde)",
    "سلبي مع كاشف تولن (يبقى المحلول رائقاً ولا تتكون مرآة فضية — كيتون أليفاتي)": "Negative with Tollens' reagent (Remains clear with no silver mirror, Aliphatic ketone)",
    "تكوّن راسب أصفر متبلور من اليودوفورم CHI3 ذو رائحة مطهرة مميزة (أسيتالدهيد)": "Formation of a yellow crystalline iodoform (CHI₃) precipitate with antiseptic odor (Acetaldehyde)",
    "سلبي مع اختبار اليودوفورم (لا يتكون راسب أصفر) مع رائحة الفورمالين النفاذة (فورمالدهيد)": "Negative with iodoform test (No yellow precipitate) with pungent formalin odor (Formaldehyde)",
    "إيجابي سريع وفوري مع اختبار اليودوفورم برائحة مميزة بدون تدفئة (أسيتون)": "Rapid and immediate positive iodoform test with characteristic odor without heating (Acetone)",
    "سلبي مع اليودوفورم على البارد، ويتطلب تدفئة خفيفة لتكوين اليودوفورم (إيثيل ميثيل كيتون)": "Negative with cold iodoform, requires gentle warming to form iodoform (Ethyl methyl ketone)",
    "سائل خفيف القوام وسريع التطاير وذو رائحة كحولية معروفة (كحول أحادي الهيدروكسيل)": "Light, volatile liquid with characteristic alcohol odor (Monohydric alcohol)",
    "سائل لزج جداً وثقيل (قوام شرباتي)، غير متطاير، يزيل اللون الوردي للبوراكس-فينولفثالين على البارد": "Very viscous and heavy syrupy liquid, non-volatile; decolorizes borax-phenolphthalein in the cold (Glycerol)",
    "تكوّن راسب أصفر بلوري من اليودوفورم CHI3 برائحة مطهرة، ويخضر لون ثاني كرومات البوتاسيوم (إيثانول)": "Forms yellow crystalline iodoform precipitate with antiseptic odor; turns dichromate green (Ethanol)",
    "سلبي تماماً مع اليودوفورم، وله رائحة كحولية ويعطي رائحة الفورمالين النفاذة مع سلك النحاس الساخن (ميثانول)": "Completely negative with iodoform; alcohol odor evolving pungent formalin with hot copper spiral (Methanol)",
    "يذوب تماماً في حمض HCl المخفف؛ سائل زيتي أصفر يغمق بالهواء ولهب مدخن (قاعدة أمينية — أنيلين)": "Completely soluble in dilute HCl; yellow oily liquid darkening in air, sooty flame (Basic amine — Aniline)",
    "لا يذوب في حمض HCl المخفف؛ مركب أروماتي متعادل يتفاعل إيجابياً مع كاشف 2,4-DNP": "Insoluble in dilute HCl; neutral aromatic compound positive with 2,4-DNP (Aromatic carbonyl)",
    "له رائحة استر فواكه مميزة عطرة، يتصبن بالتسخين مع الصودا الكاوية معطياً كحولاً وأسيتات (إيثيل أسيتات)": "Pleasant fruity ester odor; hydrolyzes on heating with NaOH yielding alcohol and acetate (Ethyl acetate)",
    "رائحة اللوز المر المميزة؛ يكوّن مرآة فضية لامعة مع كاشف تولن، وسلبي مع اليودوفورم وفهلنج (بنزالدهيد)": "Distinctive bitter almond odor; forms silver mirror with Tollens', negative with iodoform and Fehling's (Benzaldehyde)",
    "رائحة زهرية عطرية قوية تشبه الفل / الياسمين؛ إيجابي مع اليودوفورم وسلبي مع تولن وفهلنج (أسيتوفينون)": "Strong sweet floral odor; positive with iodoform, negative with Tollens' and Fehling's (Acetophenone)",
    "حمضي قوي (تذوب في NaHCO3 مع فوران وتصاعد غاز CO2 وتغير لون عباد الشمس للأحمر)": "Strongly acidic (Dissolves in NaHCO₃ with effervescence evolving CO₂; turns litmus red)",
    "متعادل كيميائياً (لا يذوب في NaHCO3 ولا يعطي فوراناً؛ متعادل مع عباد الشمس)": "Chemically neutral (Insoluble in NaHCO₃ without effervescence; neutral to litmus)",
    "راسب أبيض فوري على البارد لا يذوب في حمض الخليك، ويزيل لون KMnO4 الساخن (حمض الأكساليك)": "Immediate white precipitate with CaCl₂ in the cold, insoluble in acetic acid; decolorizes warm KMnO₄ (Oxalic acid)",
    "راسب أبيض على البارد يذوب في هيدروكسيد الصوديوم، وتفاعل فنتون يعطي لوناً بنفسجياً ويتفحم برائحة سكر محروق (حمض الطرطريك)": "White precipitate with CaCl₂ soluble in NaOH; positive in Fenton's test (violet) and chars with burnt sugar odor (Tartaric acid)",
    "لا يتكون راسب على البارد، ولكن يتكون راسب أبيض فقط عند غليان المحلول بالحرارة (حمض الستريك)": "No precipitate in the cold; white precipitate forms only upon boiling the solution (Citric acid)",
    "تكوّن حلقة بنفسجية مميزة عند السطح الفاصل تتفحم بالحرارة برائحة السكر المحروق (كربوهيدرات / سكر ذائب)": "Formation of a characteristic purple ring at interface with Molisch test; chars with burnt sugar odor (Carbohydrate / Soluble sugar)",
    "سلبي مع اختبار مولش (لا تتكون حلقة بنفسجية؛ مادة صلبة غير سكرية)": "Negative with Molisch's test (No purple ring; non-sugar solid)",
    "تكوّن راسب أحمر طوبي كثيف ومباشر من Cu2O (سكر أحادي مختزل)": "Immediate dense brick-red precipitate of Cu₂O (Reducing monosaccharide)",
    "لا يتكون أي راسب أحمر طوبي مع فهلنج (محلول أزرق رائق وثابت — سكر غير مختزل)": "No brick-red precipitate with Fehling's solution (Solution remains clear blue — Non-reducing sugar)",
    "يظهر لون أحمر كريزي داكن سريع ومكثف خلال دقيقة إلى دقيقتين من الغليان (سكر كيتوزي — فركتوز)": "Rapid intense cherry-red color develops within 1-2 minutes of boiling (Ketose sugar — Fructose)",
    "لا يظهر لون أحمر خلال أول دقيقتين (يظل المحلول عديم اللون أو وردياً باهتاً جداً بعد وقت طويل) (سكر ألدوزي — جلوكوز)": "No red color within first 2 minutes; remains colorless or very faint pink after prolonged boiling (Aldose sugar — Glucose)",
    "تلوّن فوري بلون بنفسجي داكن مميز، وتفاعل الفثالين يعطي فلورسين أخضر فسفورياً مشعاً (ريسورسينول)": "Immediate deep violet coloration with FeCl₃; phthalein reaction yields fluorescent green fluorescein (Resorcinol)",
    "لا يعطي لوناً بنفسجياً مع FeCl3، وينصهر بالتسخين الجاف مع تصاعد النشادر وتفاعل البيوريت وردي بنفسجي (يوريا)": "No violet color with FeCl₃; melts on dry heating evolving ammonia, positive biuret test (violet-pink, Urea)",
    "تفور وتذوب في بيكربونات الصوديوم NaHCO3 مع تصاعد فقاعات CO2 (حمض أروماتي صلب)": "Dissolves in NaHCO₃ with effervescence evolving CO₂ bubbles (Solid aromatic acid)",
    "لا تفور ولا تذوب في بيكربونات الصوديوم (مركب فينولي أو غير حمضي)": "Does not dissolve or effervesce in NaHCO₃ (Phenolic or neutral non-acidic compound)",
    "يتكون راسب بيج / بني مصفر لحمي مميز (Buff precipitate) من بنزوات الحديديك (حمض البنزويك)": "Flesh-colored buff precipitate of ferric benzoate with neutral FeCl₃ (Benzoic acid)",
    "يتكون لون بنفسجي داكن كثيف وثابت جداً لا يزول مع FeCl3 (حمض الساليسيليك)": "Intense, deep, persistent violet coloration with neutral FeCl₃ that does not fade (Salicylic acid)",
    "بلورات متميعة وردية برائحة كربولية معروفة، تذوب جزئياً بالماء البارد وتعطي راسباً أبيض مع ماء البروم ولوناً بنفسجياً مع FeCl3 (الفينول)": "Pinkish deliquescent crystals with carbolic odor; partially soluble in cold water; white ppt with bromine water, violet with FeCl₃ (Phenol)",
    "مسحوق صلب لا يذوب في الماء البارد إطلاقاً، ذو لهب مدخن شديد (نافثولات أروماتية)": "Solid powder completely insoluble in cold water; burns with heavy smoky sooty flame (Aromatic naphthols)",
    "يعطي تلوناً بنفسجياً داكناً يتحول فورياً إلى راسب بني محمر كثيف مع مسحوق القصر (ألفا-نافثول)": "Transient deep violet color instantly turning into a dense reddish-brown precipitate with bleaching powder (Alpha-Naphthol)",
    "لا يعطي أي لون بنفسجي مع مسحوق القصر، ويعطي تلوناً أخضر باهتاً مع FeCl3 وصبغة آزو حمراء ساطعة مع الأنيلين (بيتا-نافثول)": "No violet color with bleaching powder; pale green with FeCl₃, brilliant scarlet azo dye with diazotized aniline (Beta-Naphthol)"
};


    const OPTION_TRANSLATIONS_AR = {
    "White precipitate insoluble in dilute HCl (+ white ppt with lead acetate)": "يتكون راسب أبيض لا يذوب في حمض الهيدروكلوريك المخفف (+ راسب أبيض مع أسيتات الرصاص)",
    "White precipitate soluble in dilute HCl (+ yellow ppt with silver nitrate AgNO₃)": "يتكون راسب أبيض يذوب في حمض الهيدروكلوريك المخفف (+ راسب أصفر مع نترات الفضة AgNO₃)",
    "White precipitate forms immediately in the cold": "يتكون راسب أبيض فوراً على البارد",
    "No precipitate in the cold; white precipitate forms only after boiling and heating": "لا يتكون راسب على البارد، ويتكون الراسب الأبيض بعد الغليان والتسخين",
    "Colorless gas (HCl) forming dense white fumes with ammonia-dipped rod (+ white ppt with AgNO₃)": "تصاعد غاز عديم اللون (HCl) يكون سحباً بيضاء كثيفة مع ساق مبللة بالنشادر (+ راسب أبيض مع AgNO₃)",
    "Orange-red vapors (Br₂) that turn starch-moistened paper yellow (+ cream ppt with AgNO₃)": "تصاعد أبخرة برتقالية حمراء (Br₂) تصفر ورقة مبللة بالنشا (+ راسب كريمي مع AgNO₃)",
    "Dense violet vapors (I₂) that turn starch-moistened paper blue (+ yellow ppt with AgNO₃)": "تصاعد أبخرة بنفسجية كثيفة (I₂) تزرق ورقة مبللة بالنشا (+ راسب أصفر مع AgNO₃)",
    "Reddish-brown fumes (NO₂) increasing upon adding copper turnings (+ brown ring test with FeSO₄)": "تصاعد أبخرة بنية حمراء (NO₂) تزداد كثافتها بإضافة خراطة نحاس (+ حلقة بنية مع FeSO₄)",
    "No gases or vapors evolved with concentrated sulfuric acid": "لم تتصاعد أي غازات أو أبخرة مع حمض الكبريتيك المركز",
    "Effervescence with colorless, odorless gas that turns clear lime water milky (CO₂)": "حدوث فوران وتصاعد غاز عديم اللون والرائحة يعكر ماء الجير الرائق (CO₂)",
    "Choking pungent gas (SO₂) that turns acidified potassium dichromate paper green": "تصاعد غاز ذي رائحة نفاذة خانقة (SO₂) يخضر ورقة مبللة بثاني كرومات البوتاسيوم المحمضة",
    "Foul rotten-egg odor gas (H₂S) that turns lead acetate paper black": "تصاعد غاز كريه الرائحة (رائحة البيض الفاسد H₂S) يسود ورقة مبللة بأسيتات الرصاص",
    "Colorless gas turning into reddish-brown fumes (NO₂) at the mouth of the tube": "تصاعد غاز عديم اللون يتحول عند فوهة الأنبوبة إلى أبخرة بنية حمراء (NO₂)",
    "No effervescence and no gas evolved": "لم يحدث فوران ولم يتصاعد أي غاز",
    "No yellow precipitate (solution gives white ppt with AgNO₃ turning black upon heating)": "لا يوجد راسب أصفر (والمحلول يعطي راسباً أبيض يسود بالتسخين مع AgNO₃)",
    "Yes, yellow suspended sulfur precipitate appears (solution decolorizes brown iodine)": "نعم، ظهر راسب أصفر معلق من الكبريت (والمحلول يزيل لون اليود البني)",
    "White gelatinous precipitate insoluble in excess ammonia": "يتكون راسب أبيض جيلاتيني لا يذوب في الزيادة من محلول النشادر",
    "White precipitate dissolves completely in excess ammonia": "يتكون راسب أبيض يذوب تماماً في الزيادة من محلول النشادر",
    "Brick-red flame; gives white precipitate with dilute H₂SO₄": "يلون اللهب باللون الأحمر الطوبي، ويعطي راسباً أبيض مع حمض الكبريتيك المخفف",
    "Apple-green flame; gives yellow precipitate with K₂CrO₄": "يلون اللهب باللون الأخضر التفاحي، ويعطي راسباً أصفر مع كرومات البوتاسيوم (K₂CrO₄)",
    "No distinctive flame coloration; gives white crystalline ppt with ammoniacal sodium phosphate": "لا يلون اللهب بأي لون مميز، ويعطي راسباً أبيض بلورياً مع فوسفات الصوديوم النشادرية",
    "Blue precipitate turning black on heating; dissolves in excess ammonia to royal deep blue solution": "راسب أزرق يسود بالتسخين، ويذوب في الزيادة من النشادر مكوناً محلولاً أزرق قاتماً",
    "Dirty white-green precipitate insoluble in excess; blue ppt with potassium ferricyanide": "راسب أبيض مخضر لا يذوب في الزيادة، ويعطي راسباً أزرق مع حديديسيانيد البوتاسيوم",
    "Reddish-brown gelatinous precipitate insoluble in excess; blood-red color with KSCN": "راسب جيلاتيني بني محمر لا يذوب في الزيادة، ويعطي لوناً أحمر دامياً مع ثيوسيانات البوتاسيوم (KSCN)",
    "White precipitate": "راسب أبيض",
    "No precipitate formed": "لا يتكون أي راسب",
    "Ammonia gas (NH₃) evolved, turning litmus blue and giving reddish-brown ppt with Nessler's reagent": "يتصاعد غاز النشادر (NH₃) الذي يزرق ورقة عباد الشمس ويعطي راسباً بنياً محمراً مع كاشف نيسلر",
    "No gas evolved; dry salt colors Bunsen flame persistent golden-yellow": "لا يتصاعد غاز، والملح الجاف يلون لهب بنزن باللون الأصفر الذهبي الساطع",
    "No gas evolved; dry salt colors Bunsen flame pale violet / lilac": "لا يتصاعد غاز، والملح الجاف يلون لهب بنزن باللون البنفسجي الفاتح (الليلكي)",
    "Yes, white precipitate soluble in hot water, giving bright yellow ppt with KI": "نعم، تكون راسب أبيض يذوب في الماء الساخن، ويعطي راسباً أصفر فاقعاً مع يوديد البوتاسيوم (KI)",
    "No, no precipitate formed with dilute HCl": "لا، لم يتكون أي راسب مع حمض HCl المخفف",
    "White precipitate dissolves in excess NaOH forming clear solution": "يذوب الراسب الأبيض في الزيادة من NaOH مكوناً محلولاً رائقاً",
    "White precipitate does not dissolve in excess NaOH": "لا يذوب الراسب الأبيض في الزيادة من NaOH",
    "Dissolves in cold water forming a clear solution": "يذوب في الماء البارد مكوناً محلولاً رائقاً",
    "Insoluble or sparingly soluble in cold water": "لا يذوب أو شحيح الذوبان جداً في الماء البارد",
    "White or colorless crystals": "أبيض أو بلورات عديمة اللون",
    "Blue or blue-green": "أزرق أو أزرق مخضر",
    "Pale green": "أخضر باهت",
    "Yellow, reddish-brown, or grayish-black": "أصفر أو بني محمر / أسود رمادي",
    "Decolorizes acidified purple KMnO₄ or forms silver mirror with Tollens' (Reducing properties, Formic acid)": "يختزل KMnO4 المحمضة أو كاشف تولن (فورميك)",
    "Does not decolorize KMnO₄; distinct vinegar odor (Blood-red with neutral FeCl₃, Acetic acid)": "رائحة الخل المميزة ولا يزيل KMnO4 (أسيتيك)",
    "Very viscous and heavy syrupy liquid, non-volatile; decolorizes borax-phenolphthalein in the cold (Glycerol)": "سائل لزج جداً غير متطاير (الجليسرول)",
    "Light, volatile liquid with characteristic alcohol odor (Monohydric alcohol)": "سائل خفيف سريع التطاير (كحول أحادي)",
    "Formation of a yellow crystalline iodoform (CHI₃) precipitate with antiseptic odor (Acetaldehyde)": "راسب أصفر في اختبار اليودوفورم (أسيتالدهيد)",
    "Negative with iodoform; pungent lacrimatory odor, red ppt with Fehling (Formaldehyde)": "سلبي مع اليودوفورم ورائحة خانقة (فورمالدهيد)",
    "Distinctive bitter almond odor; forms silver mirror with Tollens', negative with iodoform and Fehling's (Benzaldehyde)": "رائحة اللوز المر ومرآة فضية مع تولن (بنزالدهيد)",
    "Negative with Tollens; yellow iodoform ppt, freezes below 20°C (Acetophenone)": "راسب يودوفورم أصفر وسلبي مع تولن (أسيتوفينون)",
    "Formation of a shining silver mirror on the tube wall or grey precipitate (Reducing aldehyde)": "تكوّن مرآة فضية Ag (ألدهيد)",
    "No silver mirror forms; solution remains clear (Ketone — Acetone)": "سلبي مع تولن وفهلنج (الأسيتون)",
    "Completely soluble in dilute HCl; yellow oily liquid darkening in air, sooty flame (Basic amine — Aniline)": "يذوب في حمض HCl المخفف (الأنيلين)",
    "Insoluble in dilute HCl; neutral aromatic compound positive with 2,4-DNP (Aromatic carbonyl)": "لا يذوب في HCl ويتفاعل مع 2,4-DNP (كربونيل أروماتي)",
    "Effervescence with CO₂ bubbles (Liquid carboxylic acid)": "فوران وتصاعد غاز CO2 (حمض كربوكسيلي)",
    "No effervescence (Neutral compound: Aldehyde, Ketone, or Alcohol)": "لا يحدث فوران (متعادل)",
    "Forms yellow crystalline iodoform precipitate with antiseptic odor; turns dichromate green (Ethanol)": "راسب أصفر في اختبار اليودوفورم (إيثانول)",
    "Negative with iodoform; heating with salicylic acid yields wintergreen ester odor (Methanol)": "سلبي مع اليودوفورم ورائحة زيت الكافور (ميثانول)",
    "Forms an immediate yellow or orange crystalline precipitate (Carbonyl compound: Aldehyde or Ketone)": "راسب أصفر / برتقالي فوري (ألدهيد أو كيتون)",
    "No precipitate; solution remains clear transparent yellow (Aliphatic alcohol)": "لا يتكون راسب (كحول أليفاتي)",
    "Completely miscible with cold water (Single clear layer)": "يمتزج تماماً بالماء البارد",
    "Immiscible / sparingly soluble (Separates into two layers or oily droplets)": "لا يمتزج / شحيح الذوبان (طبقتين)",
    "Liquid": "سائل (Liquid)",
    "Solid Substance": "مادة صلبة",
    "Immediate white precipitate with CaCl₂ in the cold, insoluble in acetic acid; decolorizes warm KMnO₄ (Oxalic acid)": "راسب أبيض على البارد لا يذوب بالأسيتيك (أكساليك)",
    "White precipitate with CaCl₂ soluble in NaOH; positive in Fenton's test (violet) and chars with burnt sugar odor (Tartaric acid)": "راسب أبيض يذوب في NaOH وتفاعل فنتون بنفسجي (طرطريك)",
    "No precipitate in the cold; white ppt forms only after boiling for several minutes (Citric acid)": "راسب أبيض يتكون بالغليان فقط (ستريك)",
    "Flesh-colored buff precipitate of ferric benzoate with neutral FeCl₃ (Benzoic acid)": "راسب بيج / بني مصفر لحمي مع FeCl3 (بنزويك)",
    "Intense, deep, persistent violet coloration with neutral FeCl₃ that does not fade (Salicylic acid)": "لون بنفسجي كثيف وثابت جداً مع FeCl3 (ساليسيليك)",
    "Dissolves in NaHCO₃ with effervescence evolving CO₂ bubbles (Solid aromatic acid)": "فوران وذوبان في بيكربونات الصوديوم (حمض أروماتي)",
    "Does not effervesce with NaHCO₃ but completely dissolves in NaOH (Phenols and Naphthols)": "لا تفور مع NaHCO3 ولكن تذوب في NaOH (فينولات ونافثولات)",
    "Does not effervesce or dissolve in cold NaOH; forms colloidal solution on boiling (Starch)": "معلق غروي بالماء الساخن وأزرق مع اليود (نشا)",
    "Transient deep violet color instantly turning into a dense reddish-brown precipitate with bleaching powder (Alpha-Naphthol)": "تلون بنفسجي داكن مع مسحوق القصر / الهيبوكلوريت (ألفا-نافثول)",
    "No violet color with bleaching powder; pale green with FeCl₃, brilliant scarlet azo dye with diazotized aniline (Beta-Naphthol)": "سلبي مع مسحوق القصر وصبغة آزو حمراء قرمزية ساطعة (بيتا-نافثول)",
    "Formation of a characteristic purple ring at interface with Molisch test; chars with burnt sugar odor (Carbohydrate / Soluble sugar)": "حلقة بنفسجية مميزة وتفحم بالسكر المحروق (كربوهيدرات)",
    "No purple ring (Negative with Molisch: Resorcinol or Urea)": "سلبي مع موليش (ريسورسينول أو يوريا)",
    "Immediate deep violet coloration with FeCl₃; phthalein reaction yields fluorescent green fluorescein (Resorcinol)": "لون بنفسجي داكن مع FeCl3 وفلورسين أخضر مشع (ريسورسينول)",
    "No violet color with FeCl₃; melts on dry heating evolving ammonia, positive biuret test (violet-pink, Urea)": "تصاعد النشادر وتفاعل البيوريت وردي بنفسجي (يوريا)",
    "Pinkish deliquescent crystals with carbolic odor; partially soluble in cold water; white ppt with bromine water, violet with FeCl₃ (Phenol)": "رائحة كربولية وراسب أبيض مع ماء البروم ولون بنفسجي (الفينول)",
    "Solid powder completely insoluble in cold water; burns with heavy smoky sooty flame (Aromatic naphthols)": "مسحوق عديم الذوبان في الماء ولهب مدخن شديد (نافثولات)",
    "Easily and completely soluble in cold water (Water-soluble organic solids)": "تذوب تماماً في الماء البارد (ذائبة)",
    "Sparingly or insoluble in cold water (Insoluble / Sparingly soluble solids)": "لا تذوب / شحيحة الذوبان في الماء البارد",
    "Rapid intense cherry-red color within 1-2 minutes (Ketose sugar — Fructose)": "لون أحمر كرزي سريع خلال دقيقة أو دقيقتين (فركتوز)",
    "No red color within first 2 minutes; remains colorless or very faint pink after prolonged boiling (Aldose sugar — Glucose)": "سلبي خلال أول دقيقتين، وبلورات أوزازون إبرية (جلوكوز)",
    "Vigorous effervescence with CO₂ bubbles (Water-soluble solid aliphatic carboxylic acid)": "فوران شديد وتصاعد CO2 (حمض أليفاتي ذائب)",
    "No effervescence with NaHCO₃ (Neutral compound, sugar, or soluble phenol)": "لا يحدث فوران (متعادل أو سكر أو ريسورسينول)",
    "Immediate dense brick-red precipitate of Cu₂O (Reducing monosaccharide)": "راسب أحمر طوبي مباشر مع فهلنج (سكر مختزل)",
    "No red precipitate; solution remains clear blue (Non-reducing sugar — Sucrose)": "سلبي مع فهلنج مباشرة (السكروز)",
    "Yes, precipitate dissolves in excess ammonia": "نعم، يذوب في زيادة الأمونيا (Zn²⁺)",
    "No, precipitate does not dissolve in excess ammonia": "لا، لا يذوب في زيادة الأمونيا (Al³⁺)",
    "Precipitate is completely insoluble in dilute or concentrated HCl": "لا يذوب في حمض مخفف (كبريتات SO₄²⁻)",
    "Precipitate dissolves in HCl with effervescence evolving CO₂ gas": "يذوب في الحمض مع فوران (كربونات CO₃²⁻)",
    "Precipitate dissolves in HCl without gas (Forms yellow precipitate with ammonium molybdate)": "يذوب دون فوران (فوسفات PO₄³⁻)",
    "Precipitate dissolves in HCl evolving suffocating SO₂ gas": "يذوب مع غاز SO₂ (كبريتيت SO₃²⁻)",
    "No precipitate forms / no change": "لا يتكون راسب / لا تغيير",
    "Formation of a brown ring at the liquid junction (Brown Ring Test, Nitrate)": "تكون حلقة بنية فاصلة (نترات NO₃⁻)",
    "Appearance of characteristic blood-red coloration with neutral FeCl₃": "لون أحمر دامي مع FeCl₃ (أسيتات CH₃COO⁻)",
    "No obvious change / no reaction": "لا تفاعل / عينة غير محددة",
    "Deep royal blue solution (Tetraamminecopper complex)": "أزرق داكن (محلول معقد أزرق ملكي)",
    "No change / remains as precipitate": "لا تغيير / يظل راسباً",
    "Surface gradually turns reddish-brown due to oxidation": "يتحول إلى بني محمر بالأكسدة",
    "Remains green and stable": "يظل أخضر ثابتاً",
    "Effervescence and gas evolution": "فوران وتصاعد غاز",
    "No change / no precipitate or gas formed": "لا تغيير / لا يتكون راسب أو غاز",
    "Solution color changes": "تغير لون المحلول",
    "Other observation": "أخرى",
    "Brick-red flame and white precipitate with ammonium oxalate (Ca²⁺)": "لهب أحمر طوبي (Ca²⁺)",
    "No distinctive flame color (White precipitate giving blue color with Magneson, Mg²⁺)": "لا لون مميز للهب (Mg²⁺)",
    "Dissolves in hot water and recrystallizes on cooling": "يذوب في الماء الساخن (Pb²⁺)",
    "Colorless gas turning clear lime water turbid temporarily (CO₂)": "غاز عديم اللون يعكر ماء الجير (CO₂)",
    "Rapid instantaneous effervescence with CO₂ (No MgSO₄ ppt in the cold, HCO₃⁻)": "فوران سريع ولحظي (HCO₃⁻)",
    "Rotten-egg odor gas turning lead acetate paper black (H₂S)": "رائحة بيض فاسد يسود أسيتات الرصاص (H₂S)",
    "Suffocating pungent gas turning acidified K₂Cr₂O₇ paper green (SO₂)": "رائحة خانقة تخضر ثاني كرومات البوتاسيوم (SO₂)",
    "SO₂ gas evolution with yellow suspended sulfur turbidity (Thiosulfate)": "تعكر كبريتي أصفر مع غاز SO₂ (ثيوكبريتات)",
    "Reddish-brown fumes at the tube mouth (NO₂)": "أبخرة بنية حمراء عند فوهة الأنبوبة (NO₂)",
    "No gas / other": "لا غاز / أخرى",
    "Yes (dissolves in boiling hot water and recrystallizes upon cooling)": "نعم (يذوب بالماء الساخن)",
    "Does not dissolve in hot water, but dissolves in dilute ammonia": "لا (يذوب في النشادر المخفف)",
    "Does not dissolve in hot water, and precipitate blackens with ammonia": "لا (ويسود بمحلول النشادر)",
    "Evolution of ammonia gas (Pungent odor turning moist red litmus blue)": "تصاعد غاز النشادر ذو الرائحة النفاذة (NH₄⁺)",
    "No change / no gas evolved after heating": "لا تغيير / الانتقال لكواشف الترسيب",
    "Blue precipitate": "راسب أزرق",
    "Green precipitate": "راسب أخضر",
    "Reddish-brown gelatinous precipitate": "راسب بني محمر",
    "White precipitate oxidizing and turning brown in air": "راسب أبيض يتحول لبني",
    "No change / no precipitate in the cold": "لا يتكون راسب على البارد",
    "Yes, precipitate dissolves in excess NaOH with shaking": "نعم، يذوب في الزيادة من NaOH",
    "No, precipitate does not dissolve in excess NaOH": "لا، لا يذوب في الزيادة من NaOH",
    "Aqueous Solution": "محلول مائي",
    "Slowly soluble in dilute ammonia, dissolves in concentrated ammonia": "يذوب في النشادر المركز (بروميد Br⁻)",
    "Does not dissolve in dilute or concentrated ammonia": "شحيح الذوبان جداً",
    "White curdy precipitate (AgCl)": "راسب أبيض",
    "Cream / pale-yellow precipitate (AgBr)": "راسب كريمي / أصفر باهت",
    "Bright yellow precipitate (AgI)": "راسب أصفر فاقع",
    "Black precipitate of silver sulfide (Ag₂S)": "راسب أسود (S²⁻)",
    "Brick-red / reddish-brown precipitate of silver chromate": "راسب أحمر طوبي (CrO₄²⁻)",
    "Yes, completely and rapidly dissolves in dilute ammonia": "نعم، يذوب في النشادر المخفف (كلوريد Cl⁻)",
    "Does not dissolve in dilute ammonia": "لا يذوب في المخفف",
    "Completely insoluble in both dilute and concentrated ammonia (Iodide)": "لا يذوب نهائياً في النشادر (يوديد I⁻)",
    "Dissolves in dilute ammonia and dilute nitric acid (Phosphate)": "يذوب في النشادر وحمض النيتريك (فوسفات PO₄³⁻)",
    "White": "أبيض",
    "Colorless": "عديم اللون",
    "Blue": "أزرق",
    "Green": "أخضر",
    "Yellow": "أصفر",
    "Brown": "بني",
    "Pink": "وردي",
    "Black": "أسود",
    "Orange": "برتقالي",
    "Unspecified / Other": "غير محدد",
    "Organic Chemical Analysis (25 Compounds)": "كشف المركبات العضوية (25 مركباً)",
    "Complete Inorganic Salt Diagnosis (30 Salts)": "تشخيص الأملاح غير العضوية الكامل (30 ملحاً)",
    "Single Inorganic Ion Analysis (Cations & Anions)": "كشف الأيونات غير العضوية المنفردة",
    "Unknown Sample (Flame & Charring Test)": "عينة مجهولة: فحص التفحم والتسخين (عضوي / غير عضوي)",
    "Melting, charring, and evolution of fumes or burnt sugar smell (Organic Compound)": "انصهار وتفحم / رائحة سكر محروق (عضوي)",
    "No charring, stable mineral residue with color change on heating or non-charring vapors (Inorganic Compound)": "لا تفحم / بقاء مادة معدنية ثابتة (غير عضوي)"
};
    const QUESTION_TRANSLATIONS_EN = {
    "الخطوة 5 (المجموعة الثالثة): أضف محلول كلوريد الباريوم (BaCl₂) إلى محلول الملح، ثم اختبر ذوبان الراسب الأبيض في حمض HCl المخفف:": "Step 5 (Group 3 Anions): Add barium chloride (BaCl₂) solution to salt solution, then test precipitate solubility in dilute HCl:",
    "تجربة تأكيدية للتفرقة بين الكربونات والبيكربونات: أضف محلول كبريتات المغنيسيوم (MgSO₄) إلى محلول الملح:": "Confirmatory test to distinguish Carbonate from Bicarbonate: Add magnesium sulfate (MgSO₄) solution to salt solution:",
    "الخطوة 4 (المجموعة الثانية): أضف حمض الكبريتيك المركز (Conc. H₂SO₄) إلى عينة جافة من الملح الصلب مع التسخين الهادئ:": "Step 4 (Group 2 Anions): Add concentrated sulfuric acid (Conc. H₂SO₄) to a dry salt sample with gentle heating:",
    "الخطوة 3 (كشف الشق الحامضي - المجموعة الأولى): أضف حمض الهيدروكلوريك المخفف (Dil. HCl) إلى الملح الصلب، ماذا تلاحظ؟": "Step 3 (Acidic Radical - Group 1): Add dilute hydrochloric acid (Dil. HCl) to the solid salt. What do you observe?",
    "افحص محلول الأنبوبة أثناء تصاعد غاز SO₂، هل تلاحظ تكون راسب أصفر معلق من الكبريت؟": "Inspect the solution during SO₂ gas evolution. Do you observe a yellow colloidal sulfur precipitate?",
    "خذ عينة جديدة من محلول الملح وأضف إليها محلول النشادر (NH₄OH) تدريجياً ثم بزيادة:": "Take a fresh sample and add aqueous ammonia (NH₄OH) dropwise then in excess:",
    "أجرِ اختبار اللهب الجاف (Flame Test) والتجارب التأكيدية للكاتيون ذي الراسب الأبيض غير الذائب في الزيادة:": "Perform dry flame test and confirmatory tests for the cation with white precipitate insoluble in excess NaOH:",
    "أضف محلول هيدروكسيد الصوديوم (NaOH) تدريجياً إلى محلول الملح، ما هو لون الراسب المتكون؟": "Add sodium hydroxide (NaOH) solution dropwise to the salt solution. What is the color of the precipitate?",
    "سخّن أنبوبة الاختبار المحتوية على الملح مع هيدروكسيد الصوديوم (NaOH)، أو أجرِ كشف اللهب الجاف:": "Heat the test tube containing the salt with NaOH, or perform dry flame test:",
    "الآن ننتقل لتحديد الشق القاعدي (Cation): أضف قطرات من حمض HCl المخفف إلى محلول الملح المائي، هل تكون راسب؟": "Now proceeding to identify the Basic Radical (Cation): Add drops of dilute HCl to the aqueous salt solution. Does a precipitate form?",
    "أضف الزيادة من محلول هيدروكسيد الصوديوم (Excess NaOH) إلى الراسب الأبيض مع الرج:": "Add excess sodium hydroxide (Excess NaOH) solution to the white precipitate with shaking:",
    "الخطوة 2 (الذوبانية): أضف عينة صغيرة من الملح إلى الماء المقطر البارد مع الرج، ماذا تلاحظ؟": "Step 2 (Solubility): Add a small sample of the salt to cold distilled water with shaking. What do you observe?",
    "الخطوة 1 (الفحص الفيزيائي): ما هو لون الملح الصلب المجهول أمامك؟": "Step 1 (Physical Examination): What is the color of the unknown solid salt?",
    "الأحماض السائلة — تجربة التمييز الفاصلة بين حمض الفورميك وحمض الأسيتيك:": "Test with acidified Potassium Permanganate (KMnO4) or Tollen's reagent, and observe the odor:",
    "الكحولات السائلة — الخطوة 5: فحص اللزوجة وقوام السائل العضوي:": "Observe the physical viscosity of the alcohol, its volatility, and response to the Borax-Phenolphthalein test:",
    "الألدهيدات السائلة — التجربة التأكيدية الفاصلة بين الأسيتالدهيد والفورمالدهيد:": "Perform the Iodoform test (add Iodine solution + NaOH drops with mild warming to 60°C):",
    "مركبات الكربونيل الأروماتية غير الذائبة — التجربة الفاصلة بين البنزالدهيد والأسيتوفينون:": "Perform Tollen's test and the Iodoform test on the insoluble aromatic liquid:",
    "مركبات الكربونيل السائلة — الخطوة 5: اختبار تولن (Tollen's Test) للتمييز بين الألدهيد والكيتون:": "Add Tollen's reagent (ammoniacal silver nitrate) and warm gently in a water bath for 2-3 minutes:",
    "السوائل غير الممتزجة بالماء — الخطوة 3: اختبار الذوبان في حمض الهيدروكلوريك المخفف (HCl):": "Test solubility in dilute Hydrochloric Acid (HCl 10%), and observe color and flame behavior:",
    "السوائل الممتزجة بالماء — الخطوة 3: أضف محلول بيكربونات الصوديوم (NaHCO₃) إلى السائل:": "Add a few drops of 5% Sodium Bicarbonate (NaHCO3) solution to the miscible liquid. What do you observe?",
    "الكحولات الأحادية الخفيفة — التجربة التأكيدية الفاصلة بين الإيثانول والميثانول:": "Perform the Iodoform test (Iodine solution + NaOH with gentle warming), and check oxidation behavior:",
    "السوائل المتعادلة الممتزجة — الخطوة 4: أضف كاشف 2,4-ثنائي نيتروفينيل هيدرازين (2,4-DNP):": "Add 2,4-Dinitrophenylhydrazine (2,4-DNP) reagent to the liquid sample. What do you observe?",
    "السوائل العضوية — الخطوة 2: اختبر قابلية امتزاج السائل بالماء البارد:": "Is the liquid organic sample miscible with cold distilled water?",
    "الكشف العضوي — الخطوة 1: ما هي الحالة الفيزيائية للعينة أمامك؟": "What is the physical state of the organic sample at room temperature?",
    "الأحماض الأليفاتية الذائبة — التجربة الفاصلة بكلوريد الكالسيوم (CaCl₂):": "Neutralize the acid solution with dilute ammonia and add Calcium Chloride (CaCl2) solution. Observe cold and boil:",
    "الأحماض الأروماتية غير الذائبة بالماء البارد — التجربة التأكيدية الفاصلة بين البنزويك والساليسيليك:": "Neutralize the acid solution with dilute ammonia, boil off excess NH3, and add neutral FeCl3 solution:",
    "المواد الصلبة غير الذائبة بالماء — الخطوة 3: اختبار الذوبان في NaHCO₃ وهيدروكسيد الصوديوم NaOH:": "Test solubility of the solid in 5% NaHCO3 solution and in 10% NaOH solution:",
    "النافثولات — التجربة التأكيدية الفاصلة بين ألفا-نافثول وبيتا-نافثول:": "Add filtered Bleaching Powder solution (or NaOCl) / FeCl3 to the naphthol sample in dilute alkali or alcohol:",
    "المواد الذائبة المتعادلة — الخطوة 4: اختبار موليش (Molisch Test) العام للكشف عن السكريات:": "Perform Molisch's test (add alpha-naphthol solution, then pour concentrated H2SO4 down the inner tube wall):",
    "المواد الذائبة غير السكرية — التجربة الفاصلة بين الريسورسينول واليوريا:": "Add neutral Ferric Chloride (FeCl3) solution to the sample, and test behavior upon dry heating:",
    "الفينولات والنافثولات — الخطوة 4: التمييز بين الفينول أحادي الحلقة والنافثولات ثنائية الحلقات:": "Observe sample appearance, carbolic odor, and reaction with Bromine Water and neutral FeCl3:",
    "المواد الصلبة العضوية — الخطوة 2: اختبر قابلية ذوبان المادة الصلبة في الماء البارد:": "Is the solid organic sample soluble in cold distilled water?",
    "السكريات المختزلة — التجربة التأكيدية الفاصلة بين الجلوكوز والفركتوز (اختبار سيلوانوف):": "Perform Seliwanoff's test (add Resorcinol in 6M HCl and boil in a water bath for 1-2 minutes):",
    "المواد الصلبة الذائبة بالماء — الخطوة 3: أضف محلول بيكربونات الصوديوم (NaHCO₃):": "Add Sodium Bicarbonate (NaHCO3) solution to the aqueous solution of the soluble solid. What do you observe?",
    "السكريات الذائبة — الخطوة 5: اختبار فهلنج (Fehling's Test) للتمييز بين السكر المختزل وغير المختزل:": "Add Fehling's reagent (A+B) and heat in a boiling water bath for 3-5 minutes. What do you observe?",
    "المرحلة 3: هل يذوب الراسب في زيادة الأمونيا؟": "Step 3: Does the yellow precipitate dissolve in aqueous ammonia?",
    "المرحلة 3: هل يذوب الراسب في حمض مخفف؟": "Step 3: Does the precipitate dissolve in dilute acid?",
    "المرحلة 3: أضف محلول كلوريد الباريوم (BaCl₂). ماذا تلاحظ؟": "Step 3: Add barium chloride (BaCl₂) solution to a fresh neutral sample. What do you observe?",
    "المرحلة 3: أضف كواشف النترات والأسيتات. ماذا تلاحظ؟": "Step 3: Carefully add concentrated sulfuric acid (H₂SO₄) with fresh FeSO₄, or test with neutral FeCl₃. What do you observe?",
    "المرحلة 3: هل يتغير لون المحلول بعد إضافة زيادة من الأمونيا (NH₃)؟ إلى أي لون؟": "Step 3: Does the solution color change upon adding excess aqueous ammonia (NH₃)? What color?",
    "المرحلة 3: هل يتغير لون الراسب عند تركه معرضاً للهواء؟": "Step 3: Does the precipitate color change upon standing exposed to air?",
    "المرحلة 2: أضف حمض الهيدروكلوريك المخفف (HCl) قطرة قطرة إلى العينة. ماذا تلاحظ؟": "Step 2: Add dilute hydrochloric acid (Dil. HCl) dropwise to the sample. What do you observe?",
    "المرحلة 3: قم بإجراء كشف اللهب الجاف. ما هي الملاحظة؟": "Step 3: Perform dry flame test or solubility test. What is the observed sign?",
    "المرحلة 3: هل يتصاعد غاز؟ وما لونه أو رائحته؟": "Step 3: Is a gas evolved? What is its color or odor?",
    "المرحلة 3: هل يذوب الراسب في الماء الساخن؟": "Step 3: Does the white precipitate dissolve in boiling water?",
    "المرحلة 3: هل تحتاج لتسخين الأنبوب؟ ماذا تلاحظ بعد التسخين؟": "Step 3: Gently heat the test tube. What do you observe upon heating?",
    "المرحلة 3: أضف هيدروكسيد الصوديوم (NaOH) قطرة قطرة. ماذا تلاحظ؟": "Step 3: Add sodium hydroxide (NaOH) solution dropwise with shaking. What do you observe?",
    "المرحلة 3: هل يذوب الراسب عند إضافة زيادة من هيدروكسيد الصوديوم (NaOH)؟": "Step 3: Does the precipitate dissolve upon adding excess sodium hydroxide (NaOH)?",
    "المرحلة 1: هل العينة صلبة أم محلول؟": "Step 1: Is the sample a solid substance or an aqueous solution?",
    "المرحلة 3: أضف محلول نترات الفضة (AgNO₃). ماذا تلاحظ؟": "Step 3: Add silver nitrate (AgNO₃) solution to sample acidified with dilute HNO₃. What do you observe?",
    "المرحلة 1: ما لون المادة أو المحلول أمامك؟": "Step 1: What is the initial color of the sample or solution?",
    "الخطوة 1: حدد مسار الفحص التحليلي للعينة المجهولة (عضوي أم غير عضوي)": "Step 1: Select the analytical pathway for the unknown sample (Organic or Inorganic):",
    "فحص الفصل الأولي: سخّن كمية صغيرة جداً من العينة على لهب مباشر أو في أنبوبة جافة. ماذا تلاحظ؟": "Heat a small quantity of the sample directly in a dry test tube or on a flame. What do you observe?"
};
    const QUESTION_TRANSLATIONS_AR = {
    "Step 5 (Group 3 Anions): Add barium chloride (BaCl₂) solution to salt solution, then test precipitate solubility in dilute HCl:": "الخطوة 5 (المجموعة الثالثة): أضف محلول كلوريد الباريوم (BaCl₂) إلى محلول الملح، ثم اختبر ذوبان الراسب الأبيض في حمض HCl المخفف:",
    "Confirmatory test to distinguish Carbonate from Bicarbonate: Add magnesium sulfate (MgSO₄) solution to salt solution:": "تجربة تأكيدية للتفرقة بين الكربونات والبيكربونات: أضف محلول كبريتات المغنيسيوم (MgSO₄) إلى محلول الملح:",
    "Step 4 (Group 2 Anions): Add concentrated sulfuric acid (Conc. H₂SO₄) to a dry salt sample with gentle heating:": "الخطوة 4 (المجموعة الثانية): أضف حمض الكبريتيك المركز (Conc. H₂SO₄) إلى عينة جافة من الملح الصلب مع التسخين الهادئ:",
    "Step 3 (Acidic Radical - Group 1): Add dilute hydrochloric acid (Dil. HCl) to the solid salt. What do you observe?": "الخطوة 3 (كشف الشق الحامضي - المجموعة الأولى): أضف حمض الهيدروكلوريك المخفف (Dil. HCl) إلى الملح الصلب، ماذا تلاحظ؟",
    "Inspect the solution during SO₂ gas evolution. Do you observe a yellow colloidal sulfur precipitate?": "افحص محلول الأنبوبة أثناء تصاعد غاز SO₂، هل تلاحظ تكون راسب أصفر معلق من الكبريت؟",
    "Take a fresh sample and add aqueous ammonia (NH₄OH) dropwise then in excess:": "خذ عينة جديدة من محلول الملح وأضف إليها محلول النشادر (NH₄OH) تدريجياً ثم بزيادة:",
    "Perform dry flame test and confirmatory tests for the cation with white precipitate insoluble in excess NaOH:": "أجرِ اختبار اللهب الجاف (Flame Test) والتجارب التأكيدية للكاتيون ذي الراسب الأبيض غير الذائب في الزيادة:",
    "Add sodium hydroxide (NaOH) solution dropwise to the salt solution. What is the color of the precipitate?": "أضف محلول هيدروكسيد الصوديوم (NaOH) تدريجياً إلى محلول الملح، ما هو لون الراسب المتكون؟",
    "Heat the test tube containing the salt with NaOH, or perform dry flame test:": "سخّن أنبوبة الاختبار المحتوية على الملح مع هيدروكسيد الصوديوم (NaOH)، أو أجرِ كشف اللهب الجاف:",
    "Now proceeding to identify the Basic Radical (Cation): Add drops of dilute HCl to the aqueous salt solution. Does a precipitate form?": "الآن ننتقل لتحديد الشق القاعدي (Cation): أضف قطرات من حمض HCl المخفف إلى محلول الملح المائي، هل تكون راسب؟",
    "Add excess sodium hydroxide (Excess NaOH) solution to the white precipitate with shaking:": "أضف الزيادة من محلول هيدروكسيد الصوديوم (Excess NaOH) إلى الراسب الأبيض مع الرج:",
    "Step 2 (Solubility): Add a small sample of the salt to cold distilled water with shaking. What do you observe?": "الخطوة 2 (الذوبانية): أضف عينة صغيرة من الملح إلى الماء المقطر البارد مع الرج، ماذا تلاحظ؟",
    "Step 1 (Physical Examination): What is the color of the unknown solid salt?": "الخطوة 1 (الفحص الفيزيائي): ما هو لون الملح الصلب المجهول أمامك؟",
    "Test with acidified Potassium Permanganate (KMnO4) or Tollen's reagent, and observe the odor:": "الأحماض السائلة — تجربة التمييز الفاصلة بين حمض الفورميك وحمض الأسيتيك:",
    "Observe the physical viscosity of the alcohol, its volatility, and response to the Borax-Phenolphthalein test:": "الكحولات السائلة — الخطوة 5: فحص اللزوجة وقوام السائل العضوي:",
    "Perform the Iodoform test (add Iodine solution + NaOH drops with mild warming to 60°C):": "الألدهيدات السائلة — التجربة التأكيدية الفاصلة بين الأسيتالدهيد والفورمالدهيد:",
    "Perform Tollen's test and the Iodoform test on the insoluble aromatic liquid:": "مركبات الكربونيل الأروماتية غير الذائبة — التجربة الفاصلة بين البنزالدهيد والأسيتوفينون:",
    "Add Tollen's reagent (ammoniacal silver nitrate) and warm gently in a water bath for 2-3 minutes:": "مركبات الكربونيل السائلة — الخطوة 5: اختبار تولن (Tollen's Test) للتمييز بين الألدهيد والكيتون:",
    "Test solubility in dilute Hydrochloric Acid (HCl 10%), and observe color and flame behavior:": "السوائل غير الممتزجة بالماء — الخطوة 3: اختبار الذوبان في حمض الهيدروكلوريك المخفف (HCl):",
    "Add a few drops of 5% Sodium Bicarbonate (NaHCO3) solution to the miscible liquid. What do you observe?": "السوائل الممتزجة بالماء — الخطوة 3: أضف محلول بيكربونات الصوديوم (NaHCO₃) إلى السائل:",
    "Perform the Iodoform test (Iodine solution + NaOH with gentle warming), and check oxidation behavior:": "الكحولات الأحادية الخفيفة — التجربة التأكيدية الفاصلة بين الإيثانول والميثانول:",
    "Add 2,4-Dinitrophenylhydrazine (2,4-DNP) reagent to the liquid sample. What do you observe?": "السوائل المتعادلة الممتزجة — الخطوة 4: أضف كاشف 2,4-ثنائي نيتروفينيل هيدرازين (2,4-DNP):",
    "Is the liquid organic sample miscible with cold distilled water?": "السوائل العضوية — الخطوة 2: اختبر قابلية امتزاج السائل بالماء البارد:",
    "What is the physical state of the organic sample at room temperature?": "الكشف العضوي — الخطوة 1: ما هي الحالة الفيزيائية للعينة أمامك؟",
    "Neutralize the acid solution with dilute ammonia and add Calcium Chloride (CaCl2) solution. Observe cold and boil:": "الأحماض الأليفاتية الذائبة — التجربة الفاصلة بكلوريد الكالسيوم (CaCl₂):",
    "Neutralize the acid solution with dilute ammonia, boil off excess NH3, and add neutral FeCl3 solution:": "الأحماض الأروماتية غير الذائبة بالماء البارد — التجربة التأكيدية الفاصلة بين البنزويك والساليسيليك:",
    "Test solubility of the solid in 5% NaHCO3 solution and in 10% NaOH solution:": "المواد الصلبة غير الذائبة بالماء — الخطوة 3: اختبار الذوبان في NaHCO₃ وهيدروكسيد الصوديوم NaOH:",
    "Add filtered Bleaching Powder solution (or NaOCl) / FeCl3 to the naphthol sample in dilute alkali or alcohol:": "النافثولات — التجربة التأكيدية الفاصلة بين ألفا-نافثول وبيتا-نافثول:",
    "Perform Molisch's test (add alpha-naphthol solution, then pour concentrated H2SO4 down the inner tube wall):": "المواد الذائبة المتعادلة — الخطوة 4: اختبار موليش (Molisch Test) العام للكشف عن السكريات:",
    "Add neutral Ferric Chloride (FeCl3) solution to the sample, and test behavior upon dry heating:": "المواد الذائبة غير السكرية — التجربة الفاصلة بين الريسورسينول واليوريا:",
    "Observe sample appearance, carbolic odor, and reaction with Bromine Water and neutral FeCl3:": "الفينولات والنافثولات — الخطوة 4: التمييز بين الفينول أحادي الحلقة والنافثولات ثنائية الحلقات:",
    "Is the solid organic sample soluble in cold distilled water?": "المواد الصلبة العضوية — الخطوة 2: اختبر قابلية ذوبان المادة الصلبة في الماء البارد:",
    "Perform Seliwanoff's test (add Resorcinol in 6M HCl and boil in a water bath for 1-2 minutes):": "السكريات المختزلة — التجربة التأكيدية الفاصلة بين الجلوكوز والفركتوز (اختبار سيلوانوف):",
    "Add Sodium Bicarbonate (NaHCO3) solution to the aqueous solution of the soluble solid. What do you observe?": "المواد الصلبة الذائبة بالماء — الخطوة 3: أضف محلول بيكربونات الصوديوم (NaHCO₃):",
    "Add Fehling's reagent (A+B) and heat in a boiling water bath for 3-5 minutes. What do you observe?": "السكريات الذائبة — الخطوة 5: اختبار فهلنج (Fehling's Test) للتمييز بين السكر المختزل وغير المختزل:",
    "Step 3: Does the precipitate dissolve in excess aqueous ammonia?": "المرحلة 3: هل يذوب الراسب في زيادة الأمونيا؟",
    "Step 3: Does the precipitate dissolve in dilute acid?": "المرحلة 3: هل يذوب الراسب في حمض مخفف؟",
    "Step 3: Add barium chloride (BaCl₂) solution to a fresh neutral sample. What do you observe?": "المرحلة 3: أضف محلول كلوريد الباريوم (BaCl₂). ماذا تلاحظ؟",
    "Step 3: Carefully add concentrated sulfuric acid (H₂SO₄) with fresh FeSO₄, or test with neutral FeCl₃. What do you observe?": "المرحلة 3: أضف كواشف النترات والأسيتات. ماذا تلاحظ؟",
    "Step 3: Does the solution color change upon adding excess aqueous ammonia (NH₃)? What color?": "المرحلة 3: هل يتغير لون المحلول بعد إضافة زيادة من الأمونيا (NH₃)؟ إلى أي لون؟",
    "Step 3: Does the precipitate color change upon standing exposed to air?": "المرحلة 3: هل يتغير لون الراسب عند تركه معرضاً للهواء؟",
    "Step 2: Add dilute hydrochloric acid (Dil. HCl) dropwise to the sample. What do you observe?": "المرحلة 2: أضف حمض الهيدروكلوريك المخفف (HCl) قطرة قطرة إلى العينة. ماذا تلاحظ؟",
    "Step 3: Perform dry flame test or solubility test. What is the observed sign?": "المرحلة 3: قم بإجراء كشف اللهب الجاف. ما هي الملاحظة؟",
    "Step 3: Is a gas evolved? What is its color or odor?": "المرحلة 3: هل يتصاعد غاز؟ وما لونه أو رائحته؟",
    "Step 3: Does the white precipitate dissolve in boiling water?": "المرحلة 3: هل يذوب الراسب في الماء الساخن؟",
    "Step 3: Gently heat the test tube. What do you observe upon heating?": "المرحلة 3: هل تحتاج لتسخين الأنبوب؟ ماذا تلاحظ بعد التسخين؟",
    "Step 3: Add sodium hydroxide (NaOH) solution dropwise with shaking. What do you observe?": "المرحلة 3: أضف هيدروكسيد الصوديوم (NaOH) قطرة قطرة. ماذا تلاحظ؟",
    "Step 3: Does the precipitate dissolve upon adding excess sodium hydroxide (NaOH)?": "المرحلة 3: هل يذوب الراسب عند إضافة زيادة من هيدروكسيد الصوديوم (NaOH)؟",
    "Step 1: Is the sample a solid substance or an aqueous solution?": "المرحلة 1: هل العينة صلبة أم محلول؟",
    "Step 3: Does the pale yellow / cream precipitate dissolve in excess ammonia?": "المرحلة 3: هل يذوب الراسب في زيادة الأمونيا؟",
    "Step 3: Add silver nitrate (AgNO₃) solution to sample acidified with dilute HNO₃. What do you observe?": "المرحلة 3: أضف محلول نترات الفضة (AgNO₃). ماذا تلاحظ؟",
    "Step 3: Does the white precipitate dissolve in excess aqueous ammonia?": "المرحلة 3: هل يذوب الراسب في زيادة الأمونيا؟",
    "Step 3: Does the yellow precipitate dissolve in aqueous ammonia?": "المرحلة 3: هل يذوب الراسب في زيادة الأمونيا؟",
    "Step 1: What is the initial color of the sample or solution?": "المرحلة 1: ما لون المادة أو المحلول أمامك؟",
    "Step 1: Select the analytical pathway for the unknown sample (Organic or Inorganic):": "الخطوة 1: حدد مسار الفحص التحليلي للعينة المجهولة (عضوي أم غير عضوي)",
    "Heat a small quantity of the sample directly in a dry test tube or on a flame. What do you observe?": "فحص الفصل الأولي: سخّن كمية صغيرة جداً من العينة على لهب مباشر أو في أنبوبة جافة. ماذا تلاحظ؟"
};

    function formatStepTitle(step, isEn) {
        if (!step) return "";
        const isArChar = (s) => /[؀-ۿ]/.test(s || "");

        // 1. Checkpoint steps
        if (step.isCheckpoint || step.stepId === "anion_identified" || step.stepId === "cation_identified" || step.stepId === "confirmatory_passed") {
            if (step.phase === "anion" || step.stepId === "anion_identified") {
                return isEn ? "Identified Acidic Radical (Anion)" : "الشق الحامضي المشخص (Anion)";
            }
            if (step.phase === "cation" || step.stepId === "cation_identified") {
                return isEn ? "Identified Basic Radical (Cation)" : "الشق القاعدي المشخص (Cation)";
            }
            if (step.phase === "confirm" || step.stepId === "confirmatory_passed") {
                return isEn ? "Confirmatory Test" : "الاختبار التأكيدي";
            }
        }

        // 2. Question node lookup via stepId
        const tree = knowledgeBase && knowledgeBase.unified && knowledgeBase.unified.tree;
        if (step.stepId && tree && tree[step.stepId]) {
            const q = tree[step.stepId];
            if (isEn) {
                if (q.text_en) return q.text_en;
                if (q.text && !isArChar(q.text)) return q.text;
                if (QUESTION_TRANSLATIONS_EN[q.arabic_text || q.text]) return QUESTION_TRANSLATIONS_EN[q.arabic_text || q.text];
            } else {
                if (q.arabic_text) return q.arabic_text;
                if (q.text && isArChar(q.text)) return q.text;
                if (QUESTION_TRANSLATIONS_AR[q.text_en || q.text]) return QUESTION_TRANSLATIONS_AR[q.text_en || q.text];
            }
        }

        // 3. Fallback using step.test_en / step.test_ar / step.test
        if (isEn) {
            if (step.test_en && !isArChar(step.test_en)) return step.test_en;
            if (step.test && !isArChar(step.test)) return step.test;
            if (QUESTION_TRANSLATIONS_EN[step.test_ar || step.test]) return QUESTION_TRANSLATIONS_EN[step.test_ar || step.test];
            return step.test_en || step.test || "Analytical Step";
        } else {
            if (step.test_ar && isArChar(step.test_ar)) return step.test_ar;
            if (step.test && isArChar(step.test)) return step.test;
            if (QUESTION_TRANSLATIONS_AR[step.test_en || step.test]) return QUESTION_TRANSLATIONS_AR[step.test_en || step.test];
            return step.test_ar || step.test || "خطوة تحليلية";
        }
    }

    function formatStepObservation(step, isEn) {
        if (!step) return "";
        const isArChar = (s) => /[؀-ۿ]/.test(s || "");

        // 1. Checkpoint observations for anion / cation
        if (step.isCheckpoint || step.stepId === "anion_identified" || step.stepId === "cation_identified") {
            if (step.anionKey && knowledgeBase && knowledgeBase.anions_data && knowledgeBase.anions_data[step.anionKey]) {
                const a = knowledgeBase.anions_data[step.anionKey];
                return isEn
                    ? `✓ Successfully identified acidic radical: ${a.name_en} (${a.symbol})`
                    : `✓ تم رصد وتحديد الشق الحامضي بنجاح: ${a.name_ar} (${a.symbol})`;
            }
            if (step.cationKey && knowledgeBase && knowledgeBase.cations_data && knowledgeBase.cations_data[step.cationKey]) {
                const c = knowledgeBase.cations_data[step.cationKey];
                return isEn
                    ? `✓ Successfully identified basic radical: ${c.name_en} (${c.symbol})`
                    : `✓ تم رصد وتحديد الشق القاعدي بنجاح: ${c.name_ar} (${c.symbol})`;
            }
        }

        // 2. Confirmatory test observations
        if (step.phase === "confirm") {
            const raw = step.observation_en || step.observation_ar || step.observation || "";
            if (raw.includes("Skipped") || raw.includes("تخطي")) {
                return isEn
                    ? "Skipped confirmatory test, relying on primary inference observations"
                    : "تم تخطي الاختبار التأكيدي، والاعتماد على ملاحظات الاستدلال الأولية";
            }
            if (raw.startsWith("✓")) {
                const sign = step.expected_sign_en || step.expected_sign || "";
                return isEn
                    ? `✓ Confirmatory sign successfully observed${sign ? ": " + sign : ""}`
                    : `✓ ظهرت العلامة التأكيدية بنجاح${sign ? ": " + sign : ""}`;
            }
            if (raw.startsWith("✗")) {
                const sign = step.expected_sign_en || step.expected_sign || "";
                return isEn
                    ? `✗ Expected sign did not appear${sign ? ": " + sign : ""}`
                    : `✗ لم تظهر العلامة المتوقعة${sign ? ": " + sign : ""}`;
            }
        }

        // 3. Regular observations from chosen options
        if (isEn) {
            if (step.observation_en && !isArChar(step.observation_en)) return step.observation_en;
            if (step.observation && !isArChar(step.observation)) return step.observation;
            const lookup = OPTION_TRANSLATIONS_EN[step.observation_ar] || OPTION_TRANSLATIONS_EN[step.observation] || OPTION_TRANSLATIONS_EN[step.observation_en];
            if (lookup) return lookup;

            let s = step.observation_en || step.observation || "";
            s = s.replace(/^✓ تم رصد وتحديد الشق الحامضي بنجاح:\s*/, "✓ Successfully identified acidic radical: ");
            s = s.replace(/^✓ تم رصد وتحديد الشق القاعدي بنجاح:\s*/, "✓ Successfully identified basic radical: ");
            s = s.replace(/^✓ ظهرت العلامة التأكيدية بنجاح:\s*/, "✓ Confirmatory sign successfully observed: ");
            s = s.replace(/^✗ لم تظهر العلامة المتوقعة:\s*/, "✗ Expected sign did not appear: ");
            return s;
        } else {
            if (step.observation_ar && isArChar(step.observation_ar)) return step.observation_ar;
            if (step.observation && isArChar(step.observation)) return step.observation;
            const lookup = OPTION_TRANSLATIONS_AR[step.observation_en] || OPTION_TRANSLATIONS_AR[step.observation] || OPTION_TRANSLATIONS_AR[step.observation_ar];
            if (lookup) return lookup;

            let s = step.observation_ar || step.observation || "";
            s = s.replace(/^✓ Successfully identified acidic radical:\s*/, "✓ تم رصد وتحديد الشق الحامضي بنجاح: ");
            s = s.replace(/^✓ Successfully identified basic radical:\s*/, "✓ تم رصد وتحديد الشق القاعدي بنجاح: ");
            s = s.replace(/^✓ Confirmatory sign successfully observed:\s*/, "✓ ظهرت العلامة التأكيدية بنجاح: ");
            s = s.replace(/^✗ Expected sign did not appear:\s*/, "✗ لم تظهر العلامة المتوقعة: ");
            return s;
        }
    }

    function renderCurrentQuestion() {
        if (!knowledgeBase || !knowledgeBase.unified) return;
        if (!historyStack || historyStack.length === 0) return;

        const currentStep = historyStack[historyStack.length - 1];
        if (!currentStep) return;
        const tree = knowledgeBase.unified.tree;
        const outcomes = knowledgeBase.unified.outcomes;

        stepBackBtn.style.display = historyStack.length > 1 ? "inline-flex" : "none";

        if (currentStep.type === "question") {
            updateQuestionBackgroundImages();
            const qData = tree[currentStep.id];
            if (!qData) {
                console.error("Question node not found:", currentStep.id);
                return;
            }

            const isEn = currentLang === "en";
            const primaryText = isEn ? (qData.text || qData.arabic_text) : (qData.arabic_text || qData.text);
            const secondaryText = isEn
                ? (qData.arabic_text && qData.arabic_text !== qData.text ? qData.arabic_text : "")
                : (qData.text && qData.text !== qData.arabic_text ? qData.text : "");

            questionTextAr.textContent = primaryText;
            questionText.textContent = secondaryText;

            const hintText = isEn ? (qData.hint || qData.arabic_hint) : (qData.arabic_hint || qData.hint);
            const hintSub = isEn
                ? (qData.arabic_hint && qData.arabic_hint !== qData.hint ? qData.arabic_hint : "")
                : (qData.hint && qData.hint !== qData.arabic_hint ? qData.hint : "");

            if (hintText) {
                questionHintBox.style.display = "flex";
                questionHintAr.textContent = "💡 " + hintText;
                questionHintEn.textContent = hintSub;
            } else {
                questionHintBox.style.display = "none";
            }

            optionsGrid.innerHTML = "";

            if (currentStep.id === "start_mode") {
                optionsGrid.classList.add("start-mode-grid");
            } else {
                optionsGrid.classList.remove("start-mode-grid");
            }

            // Flag if we are in inorganic salt diagnosis mode
            if (currentStep.id.startsWith("SALT_") || currentStep.id.startsWith("ANION_") || currentStep.id.startsWith("CATION_")) {
                sessionData.isSaltDiagnosis = true;
            }

            qData.options.forEach(opt => {
                const btn = document.createElement("button");
                btn.className = "option-button";

                const mainDiv = document.createElement("div");
                mainDiv.className = "option-main";

                const swatchSpan = document.createElement("span");
                swatchSpan.className = "color-swatch";
                if (opt.swatch && opt.swatch !== "none") {
                    swatchSpan.style.background = opt.swatch;
                    swatchSpan.style.borderColor = opt.swatch === "#ffffff" ? "#888" : "rgba(255,255,255,0.4)";
                } else {
                    swatchSpan.classList.add("swatch-none");
                }

                const labelsDiv = document.createElement("div");
                labelsDiv.className = "option-labels";

                const labelSpan = document.createElement("span");
                labelSpan.className = "option-label-en";
                const isArChar = (s) => /[\u0600-\u06FF]/.test(s || "");
                let optText = "";
                if (isEn) {
                    if (opt.label_en) {
                        optText = opt.label_en;
                    } else if (opt.label && !isArChar(opt.label)) {
                        optText = opt.label;
                    } else {
                        optText = OPTION_TRANSLATIONS_EN[opt.label] || OPTION_TRANSLATIONS_EN[opt.arabic_label] || opt.label;
                    }
                } else {
                    optText = opt.arabic_label || opt.label;
                }
                labelSpan.textContent = optText;
                labelsDiv.appendChild(labelSpan);

                mainDiv.appendChild(swatchSpan);
                mainDiv.appendChild(labelsDiv);

                const arrowSpan = document.createElement("span");
                arrowSpan.className = "arrow";
                arrowSpan.textContent = isEn ? "→" : "←";

                // Special start-mode 4-card presentation
                if (currentStep.id === "start_mode") {
                    btn.classList.add("start-mode-btn");
                    swatchSpan.style.display = "none";

                    const iconDiv = document.createElement("div");
                    iconDiv.className = "start-mode-icon";

                    const descDiv = document.createElement("div");
                    descDiv.className = "start-mode-desc";

                    if (opt.next === "SALT_START") {
                        iconDiv.textContent = "🧂";
                        descDiv.textContent = isEn
                            ? "Comprehensive diagnosis of 30 inorganic salts across 3 automated stages (physical, anion, cation)"
                            : "تشخيص شامل لـ 30 ملحاً غير عضوي عبر 3 مراحل (فحص فيزيائي، شق حامضي، شق قاعدي)";
                    } else if (opt.next === "org_q_state") {
                        iconDiv.textContent = "🧪";
                        descDiv.textContent = isEn
                            ? "Identification of 25 organic compounds (liquids & solids)"
                            : "تشخيص 25 مركباً عضوياً (سوائل ومواد صلبة)";
                    } else if (opt.next === "start_color") {
                        iconDiv.textContent = "⚗️";
                        descDiv.textContent = isEn
                            ? "Detection of single inorganic cations and anions"
                            : "الكشف عن الكاتيونات والأنيونات غير العضوية المنفردة";
                    } else {
                        iconDiv.textContent = "🔥";
                        descDiv.textContent = isEn
                            ? "Preliminary flame & dry heating test for automated guidance"
                            : "فحص مبدئي بالتسخين واللهب للتوجيه التلقائي";
                    }

                    mainDiv.prepend(iconDiv);
                    labelsDiv.appendChild(descDiv);
                }

                btn.appendChild(mainDiv);
                btn.appendChild(arrowSpan);

                btn.addEventListener("click", () => {
                    handleOptionClick(currentStep, opt);
                });

                optionsGrid.appendChild(btn);
            });
        }
    }

    function handleOptionClick(parentStep, opt) {
        const tree = knowledgeBase.unified.tree;
        const outcomes = knowledgeBase.unified.outcomes;
        const nextKey = opt.next;

        const isEn = currentLang === "en";
        const isArChar = (s) => /[\u0600-\u06FF]/.test(s || "");

        let obsTextEn = opt.label_en || "";
        if (!obsTextEn) {
            if (opt.label && !isArChar(opt.label)) obsTextEn = opt.label;
            else obsTextEn = OPTION_TRANSLATIONS_EN[opt.label] || OPTION_TRANSLATIONS_EN[opt.arabic_label] || opt.label;
        }
        let obsTextAr = opt.arabic_label || "";
        if (!obsTextAr) {
            if (opt.arabic_label && isArChar(opt.arabic_label)) obsTextAr = opt.arabic_label;
            else if (opt.label && isArChar(opt.label)) obsTextAr = opt.label;
            else obsTextAr = OPTION_TRANSLATIONS_AR[opt.label] || opt.label;
        }
        const obsText = isEn ? obsTextEn : obsTextAr;

        // Save physical observations
        if (parentStep.id === "start_color" || parentStep.id === "SALT_START") {
            sessionData.color = obsText;
            sessionData.color_ar = obsTextAr;
            sessionData.color_en = obsTextEn;
        } else if (parentStep.id === "q_physical_state" || parentStep.id === "org_q_state") {
            sessionData.state = obsText;
            sessionData.state_ar = obsTextAr;
            sessionData.state_en = obsTextEn;
        } else if (parentStep.id === "SALT_SOLUBILITY") {
            sessionData.solubility = obsText;
            sessionData.solubility_ar = obsTextAr;
            sessionData.solubility_en = obsTextEn;
            sessionData.state = isEn ? "Solid salt / Aqueous solution" : "ملح صلب / محلول مائي";
            sessionData.state_ar = "ملح صلب / محلول مائي";
            sessionData.state_en = "Solid salt / Aqueous solution";
        }

        // Determine analytical phase
        let phase = "inorganic";
        if (parentStep.id.startsWith("SALT_")) phase = "physical";
        else if (parentStep.id.startsWith("ANION_")) phase = "anion";
        else if (parentStep.id.startsWith("CATION_")) phase = "cation";
        else if (parentStep.id.startsWith("org_")) phase = "organic";

        // Record in chronological analytical trail
        const parentQ = tree[parentStep.id];
        let testLabelAr = "اختبار كيميائي";
        let testLabelEn = "Chemical Test";
        if (parentQ) {
            testLabelAr = parentQ.arabic_text || (parentQ.text && isArChar(parentQ.text) ? parentQ.text : (QUESTION_TRANSLATIONS_AR[parentQ.text] || "اختبار كيميائي"));
            testLabelEn = parentQ.text_en || (parentQ.text && !isArChar(parentQ.text) ? parentQ.text : (QUESTION_TRANSLATIONS_EN[parentQ.arabic_text] || "Chemical Test"));
        }
        const testLabel = isEn ? testLabelEn : testLabelAr;

        sessionData.stepsTrail.push({
            test: testLabel,
            test_ar: testLabelAr,
            test_en: testLabelEn,
            observation: obsText,
            observation_ar: obsTextAr,
            observation_en: obsTextEn,
            phase: phase,
            stepId: parentStep.id
        });

        if (tree && tree[nextKey]) {
            const nextNode = tree[nextKey];

            // Update active mode tab when navigating from start_mode or charring test
            if (parentStep.id === "start_mode") {
                if (nextKey === "SALT_START") {
                    setActiveModeTab("salt");
                    sessionData.isSaltDiagnosis = true;
                } else if (nextKey === "org_q_state") {
                    setActiveModeTab("organic");
                    sessionData.isSaltDiagnosis = false;
                } else if (nextKey === "start_color") {
                    setActiveModeTab("ions");
                    sessionData.isSaltDiagnosis = false;
                } else if (nextKey === "unified_q_charring_heat") {
                    setActiveModeTab("all");
                    sessionData.isSaltDiagnosis = false;
                }
            } else if (parentStep.id === "unified_q_charring_heat") {
                if (nextKey === "org_q_state") {
                    setActiveModeTab("organic");
                    sessionData.isSaltDiagnosis = false;
                } else if (nextKey === "start_color") {
                    setActiveModeTab("ions");
                    sessionData.isSaltDiagnosis = false;
                }
            }

            // ================== المرحلة 1 -> 2: تسجيل الأنيون والانتقال التلقائي ==================
            if (nextNode.kind === "set_anion") {
                sessionData.isSaltDiagnosis = true;
                sessionData.detected_anion = nextNode.anion;
                const aData = (knowledgeBase.anions_data && knowledgeBase.anions_data[nextNode.anion]) || null;
                const aNameAr = aData ? `${aData.name_ar} (${aData.symbol})` : nextNode.anion;
                const aNameEn = aData ? `${aData.name_en} (${aData.symbol})` : nextNode.anion;
                sessionData.stepsTrail.push({
                    test: isEn ? "Identified Acidic Radical (Anion)" : "الشق الحامضي المشخص (Anion)",
                    test_ar: "الشق الحامضي المشخص (Anion)",
                    test_en: "Identified Acidic Radical (Anion)",
                    observation: isEn ? `✓ Successfully identified acidic radical: ${aNameEn}` : `✓ تم رصد وتحديد الشق الحامضي بنجاح: ${aNameAr}`,
                    observation_ar: `✓ تم رصد وتحديد الشق الحامضي بنجاح: ${aNameAr}`,
                    observation_en: `✓ Successfully identified acidic radical: ${aNameEn}`,
                    phase: "anion",
                    isCheckpoint: true,
                    anionKey: nextNode.anion
                });

                // الانتقال التلقائي فوراً ودون توقف للعقدة المحددة في next (CATION_START)
                historyStack.push({
                    type: "question",
                    id: nextNode.next,
                    label: isEn ? `Transition to basic radical tree (${aNameEn})` : `الانتقال لشجرة الشق القاعدي (${aNameAr})`,
                    label_ar: `الانتقال لشجرة الشق القاعدي (${aNameAr})`,
                    label_en: `Transition to basic radical tree (${aNameEn})`,
                    autoFrom: nextKey
                });
                renderCurrentQuestion();
                return;
            }

            // ================== المرحلة 2 -> 3: تسجيل الكاتيون وإنهاء تشخيص الملح ==================
            if (nextNode.kind === "finalize_salt") {
                sessionData.isSaltDiagnosis = true;
                sessionData.detected_cation = nextNode.cation;
                const cData = (knowledgeBase.cations_data && knowledgeBase.cations_data[nextNode.cation]) || null;
                const cNameAr = cData ? `${cData.name_ar} (${cData.symbol})` : nextNode.cation;
                const cNameEn = cData ? `${cData.name_en} (${cData.symbol})` : nextNode.cation;
                sessionData.stepsTrail.push({
                    test: isEn ? "Identified Basic Radical (Cation)" : "الشق القاعدي المشخص (Cation)",
                    test_ar: "الشق القاعدي المشخص (Cation)",
                    test_en: "Identified Basic Radical (Cation)",
                    observation: isEn ? `✓ Successfully identified basic radical: ${cNameEn}` : `✓ تم رصد وتحديد الشق القاعدي بنجاح: ${cNameAr}`,
                    observation_ar: `✓ تم رصد وتحديد الشق القاعدي بنجاح: ${cNameAr}`,
                    observation_en: `✓ Successfully identified basic radical: ${cNameEn}`,
                    phase: "cation",
                    isCheckpoint: true,
                    cationKey: nextNode.cation
                });

                // استدعاء دالة بناء النتيجة النهائية للملح وعرض التقرير
                finalizeSaltDiagnosis(nextNode.cation, sessionData.detected_anion);
                return;
            }

            historyStack.push({
                type: "question",
                id: nextKey,
                label: obsText
            });
            renderCurrentQuestion();
        } else if (outcomes && outcomes[nextKey]) {
            // Identified a suspected outcome
            sessionData.suspectedKey = nextKey;
            sessionData.suspectedData = outcomes[nextKey];

            // Check if user repeated the same failed result from previous attempt
            if (previousFailedAttempt && previousFailedAttempt.key === nextKey) {
                questionContainer.hidden = true;
                stage4Container.hidden = false;
                stage4PromptBlock.hidden = true;
                stage4ExecutionBlock.hidden = true;
                stage4FailureBlock.hidden = true;
                userErrorWarningBlock.hidden = false;

                repeatedFailedIon.textContent = outcomes[nextKey].subtitle || outcomes[nextKey].title;

                userErrorResumeBtn.onclick = () => {
                    userErrorWarningBlock.hidden = true;
                    stage4Container.hidden = true;
                    questionContainer.hidden = false;
                    if (historyStack.length > 1) {
                        historyStack.pop();
                        sessionData.stepsTrail.pop();
                    }
                    renderCurrentQuestion();
                    window.scrollTo({ top: 0, behavior: "smooth" });
                };

                userErrorRestartBtn.onclick = () => {
                    previousFailedAttempt = null;
                    startConsultation();
                };

                window.scrollTo({ top: stage4Container.offsetTop - 30, behavior: "smooth" });
                return;
            }

            // Normal Confirmatory Test Stage
            triggerStage4Confirmatory(nextKey, outcomes[nextKey]);
        } else {
            console.error("Unknown destination key:", nextKey);
        }
    }

    stepBackBtn.addEventListener("click", () => {
        if (historyStack.length > 1) {
            const popped = historyStack.pop();
            if (popped && popped.autoFrom) {
                sessionData.detected_anion = null;
                if (sessionData.stepsTrail.length > 0 && sessionData.stepsTrail[sessionData.stepsTrail.length - 1].isCheckpoint) {
                    sessionData.stepsTrail.pop();
                }
            }
            if (sessionData.stepsTrail.length > 0) {
                sessionData.stepsTrail.pop();
            }

            const current = historyStack[historyStack.length - 1];
            if (current) {
                if (current.id === "start_mode") {
                    setActiveModeTab("all");
                    sessionData.isSaltDiagnosis = false;
                } else if (current.id.startsWith("SALT_") || current.id.startsWith("ANION_") || current.id.startsWith("CATION_")) {
                    setActiveModeTab("salt");
                    sessionData.isSaltDiagnosis = true;
                } else if (current.id.startsWith("org_")) {
                    setActiveModeTab("organic");
                    sessionData.isSaltDiagnosis = false;
                } else if (current.id.startsWith("start_") || current.id.startsWith("group_")) {
                    setActiveModeTab("ions");
                    sessionData.isSaltDiagnosis = false;
                }
            }

            renderCurrentQuestion();
        }
    });

    // ========================================================
    // STAGE 4: CONFIRMATORY TEST
    // ========================================================

    function updateStage4Language() {
        const outData = sessionData.suspectedData;
        const isEn = currentLang === "en";
        const ionName = outData ? (outData.subtitle || outData.title) : (isEn ? "Unknown Substance" : "المادة المجهولة");
        const formula = outData ? outData.title : "";

        if (stage4PromptText) {
            stage4PromptText.textContent = isEn
                ? `Suspected Outcome: ${formula} (${ionName}). Would you like to run the confirmatory test?`
                : `النتيجة المحتملة: ${formula} (${ionName}). هل تريد إجراء الاختبار التأكيدي؟`;
        }

        const confTest = sessionData.confirmatory;
        if (confTest && stage4ExecutionBlock && !stage4ExecutionBlock.hidden) {
            confirmatoryReagentTitle.textContent = isEn ? `Confirmatory Reagent: ${confTest.reagent}` : `الكاشف التأكيدي: ${confTest.reagent}`;
            confirmatoryProcedure.textContent = isEn ? `Procedure: ${confTest.procedure}` : `طريقة الإجراء: ${confTest.procedure}`;
            confirmatorySignBadge.textContent = isEn ? `Expected Sign: ${confTest.expected_sign}` : `العلامة المتوقعة: ${confTest.expected_sign}`;
            confirmatoryQuestionText.textContent = isEn
                ? `Add ${confTest.reagent}. Did the expected sign (${confTest.expected_sign}) appear?`
                : `أضف ${confTest.reagent}. هل ظهرت العلامة المتوقعة (${confTest.expected_sign})؟`;
        }
    }

    function triggerStage4Confirmatory(outcomeKey, outcomeData) {
        setGlobalBackground(2, 3);
        questionContainer.hidden = true;
        stage4Container.hidden = false;
        stage5Container.hidden = true;

        stage4PromptBlock.hidden = false;
        stage4ExecutionBlock.hidden = true;
        stage4FailureBlock.hidden = true;
        userErrorWarningBlock.hidden = true;

        updateStage4Language();

        // Display chemical structure preview if available
        if (stage4StructurePreview && stage4StructureImg) {
            if (outcomeKey && outcomeKey.startsWith("ORG_")) {
                stage4StructureImg.src = `/static/images/structures/${outcomeKey}.png`;
                stage4StructurePreview.style.display = "flex";
            } else {
                stage4StructurePreview.style.display = "none";
            }
        }

        const confTest = (knowledgeBase.confirmatory_tests && knowledgeBase.confirmatory_tests[outcomeKey])
            ? knowledgeBase.confirmatory_tests[outcomeKey]
            : null;

        sessionData.confirmatory = confTest;

        stage4YesBtn.onclick = () => {
            const isEn = currentLang === "en";
            if (confTest) {
                stage4PromptBlock.hidden = true;
                stage4ExecutionBlock.hidden = false;
                confirmatoryReagentTitle.textContent = isEn ? `Confirmatory Reagent: ${confTest.reagent}` : `الكاشف التأكيدي: ${confTest.reagent}`;
                confirmatoryProcedure.textContent = isEn ? `Procedure: ${confTest.procedure}` : `طريقة الإجراء: ${confTest.procedure}`;
                confirmatorySignBadge.textContent = isEn ? `Expected Sign: ${confTest.expected_sign}` : `العلامة المتوقعة: ${confTest.expected_sign}`;
                confirmatoryQuestionText.textContent = isEn
                    ? `Add ${confTest.reagent}. Did the expected sign (${confTest.expected_sign}) appear?`
                    : `أضف ${confTest.reagent}. هل ظهرت العلامة المتوقعة (${confTest.expected_sign})؟`;
                window.scrollTo({ top: stage4ExecutionBlock.offsetTop - 50, behavior: "smooth" });
            } else {
                sessionData.confirmed = true;
                sessionData.stepsTrail.push({
                    test: isEn ? "Confirmatory Test" : "الاختبار التأكيدي",
                    test_ar: "الاختبار التأكيدي",
                    test_en: "Confirmatory Test",
                    observation: isEn ? "Confirmed based on chemical behavior and precipitation sequence" : "تم التأكيد بناءً على مطابقة السلوك الكيميائي وسلسلة الكواشف الترسيبية",
                    observation_ar: "تم التأكيد بناءً على مطابقة السلوك الكيميائي وسلسلة الكواشف الترسيبية",
                    observation_en: "Confirmed based on chemical behavior and precipitation sequence"
                });
                triggerStage5Report();
            }
        };

        stage4SkipBtn.onclick = () => {
            const isEn = currentLang === "en";
            sessionData.confirmed = false;
            sessionData.stepsTrail.push({
                test: isEn ? "Confirmatory Test" : "الاختبار التأكيدي",
                test_ar: "الاختبار التأكيدي",
                test_en: "Confirmatory Test",
                observation: isEn ? "Skipped confirmatory test, relying on primary inference observations" : "تم تخطي الاختبار التأكيدي والاكتفاء بالمشاهدات الاستدلالية المباشرة",
                observation_ar: "تم تخطي الاختبار التأكيدي والاكتفاء بالمشاهدات الاستدلالية المباشرة",
                observation_en: "Skipped confirmatory test, relying on primary inference observations"
            });
            triggerStage5Report();
        };

        confirmatoryConfirmedBtn.onclick = () => {
            const isEn = currentLang === "en";
            sessionData.confirmed = true;
            sessionData.stepsTrail.push({
                test: isEn ? `Confirmatory Test (${confTest.reagent})` : `الاختبار التأكيدي (${confTest.reagent})`,
                test_ar: `الاختبار التأكيدي (${confTest.reagent})`,
                test_en: `Confirmatory Test (${confTest.reagent})`,
                observation: isEn ? `✓ Confirmatory sign successfully observed: ${confTest.expected_sign}` : `✓ ظهرت العلامة التأكيدية بنجاح: ${confTest.expected_sign}`,
                observation_ar: `✓ ظهرت العلامة التأكيدية بنجاح: ${confTest.expected_sign}`,
                observation_en: `✓ Confirmatory sign successfully observed: ${confTest.expected_sign}`
            });
            triggerStage5Report();
        };

        confirmatoryFailedBtn.onclick = () => {
            const isEn = currentLang === "en";
            sessionData.confirmed = false;
            sessionData.stepsTrail.push({
                test: isEn ? `Confirmatory Test (${confTest.reagent})` : `الاختبار التأكيدي (${confTest.reagent})`,
                test_ar: `الاختبار التأكيدي (${confTest.reagent})`,
                test_en: `Confirmatory Test (${confTest.reagent})`,
                observation: isEn ? `✗ Expected sign did not appear: ${confTest.expected_sign}` : `✗ لم تظهر العلامة المتوقعة: ${confTest.expected_sign}`,
                observation_ar: `✗ لم تظهر العلامة المتوقعة: ${confTest.expected_sign}`,
                observation_en: `✗ Expected sign did not appear: ${confTest.expected_sign}`
            });

            // Show failure resolution block (سؤال المستخدم: نعيد من الأول ولا نكمل من اللي وصلنا له)
            stage4PromptBlock.hidden = true;
            stage4ExecutionBlock.hidden = true;
            userErrorWarningBlock.hidden = true;
            stage4FailureBlock.hidden = false;

            failedReagentName.textContent = confTest ? confTest.reagent : (isEn ? "Confirmatory Reagent" : "الكاشف التأكيدي");
            failedIonName.textContent = outcomeData.subtitle || outcomeData.title;

            // الخيار 1: نعيد من الأول (البدء من السؤال الثالث مع الاحتفاظ باللون والحالة)
            failureRestartBtn.onclick = () => {
                previousFailedAttempt = {
                    key: outcomeKey,
                    name: outcomeData.subtitle || outcomeData.title
                };

                // حفظ اللون والحالة والانتقال مباشرة للسؤال الثالث (الكاشف الأول)
                historyStack = [
                    {
                        type: "question",
                        id: "q_first_reagent",
                        label: isEn ? "Stage 2: First Reagent (HCl)" : "المرحلة 2: الكاشف الأول (HCl)",
                        label_ar: "المرحلة 2: الكاشف الأول (HCl)",
                        label_en: "Stage 2: First Reagent (HCl)"
                    }
                ];

                sessionData.stepsTrail = [
                    {
                        test: isEn ? "Initial Sample Color" : "الملاحظة الأولية للون العينة",
                        test_ar: "الملاحظة الأولية للون العينة",
                        test_en: "Initial Sample Color",
                        observation: sessionData.color,
                        observation_ar: sessionData.color_ar || sessionData.color,
                        observation_en: sessionData.color_en || sessionData.color
                    },
                    {
                        test: isEn ? "Physical State of Sample" : "الحالة الفيزيائية للعينة",
                        test_ar: "الحالة الفيزيائية للعينة",
                        test_en: "Physical State of Sample",
                        observation: sessionData.state,
                        observation_ar: sessionData.state_ar || sessionData.state,
                        observation_en: sessionData.state_en || sessionData.state
                    }
                ];
                sessionData.suspectedKey = null;
                sessionData.suspectedData = null;
                sessionData.confirmatory = null;
                sessionData.confirmed = false;

                stage4Container.hidden = true;
                stage4FailureBlock.hidden = true;
                questionContainer.hidden = false;

                renderCurrentQuestion();
                window.scrollTo({ top: 0, behavior: "smooth" });
            };

            // الخيار 2: نكمل من اللي وصلنا له (الرجوع للخطوة السابقة كمسألة جديدة)
            failureResumeBtn.onclick = () => {
                if (historyStack.length > 1) {
                    historyStack.pop();
                    sessionData.stepsTrail.pop();
                }

                sessionData.suspectedKey = null;
                sessionData.suspectedData = null;
                sessionData.confirmatory = null;
                sessionData.confirmed = false;

                stage4Container.hidden = true;
                stage4FailureBlock.hidden = true;
                questionContainer.hidden = false;

                renderCurrentQuestion();
                window.scrollTo({ top: 0, behavior: "smooth" });
            };

            window.scrollTo({ top: stage4FailureBlock.offsetTop - 30, behavior: "smooth" });
        };

        window.scrollTo({ top: stage4Container.offsetTop - 30, behavior: "smooth" });
    }

    // ========================================================
    // INORGANIC SALT DIAGNOSIS FINALE & INFERENCE REASONING
    // ========================================================

    async function finalizeSaltDiagnosis(cation, anion) {
        let outcomeData = null;
        try {
            const res = await fetch("/api/salt_outcome", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ cation, anion })
            });
            if (res.ok) {
                outcomeData = await res.json();
            }
        } catch (e) {
            console.warn("Server salt outcome failed, falling back to client generation", e);
        }

        if (!outcomeData) {
            outcomeData = buildLocalSaltOutcome(cation, anion);
        }

        sessionData.suspectedKey = `SALT_${cation}_${anion}`;
        sessionData.suspectedData = outcomeData;
        sessionData.saltOutcome = outcomeData;
        sessionData.confirmed = true;

        // Skip stage 4 confirmatory prompt and go directly to stage 5 final report
        triggerStage5Report();
    }

    function buildLocalSaltOutcome(cationKey, anionKey) {
        const aData = (knowledgeBase.anions_data && knowledgeBase.anions_data[anionKey]) || {
            symbol: anionKey, name_ar: anionKey, name_en: anionKey, group: "غير محدد", group_en: "Unspecified", equations: [], summary: "", summary_en: ""
        };
        const cData = (knowledgeBase.cations_data && knowledgeBase.cations_data[cationKey]) || {
            symbol: cationKey, name_ar: cationKey, name_en: cationKey, group: "غير محدد", group_en: "Unspecified", equations: [], summary: "", summary_en: ""
        };

        const pairKey = `${cationKey}_${anionKey}`;

        // 1. Incompatible salts
        if (knowledgeBase.incompatible_salts && knowledgeBase.incompatible_salts[pairKey]) {
            const inc = knowledgeBase.incompatible_salts[pairKey];
            const allEqsAr = [...(inc.equations || []), ...(aData.equations || []), ...(cData.equations || [])];
            const allEqsEn = [...(inc.equations_en || inc.equations || []), ...(aData.equations || []), ...(cData.equations || [])];
            const allNotesAr = [
                `الشق الحامضي الذي تم رصده: ${aData.name_ar} (${aData.symbol})`,
                `الشق القاعدي الذي تم رصده: ${cData.name_ar} (${cData.symbol})`,
                "تحقق من عدم حدوث تلوث في أنابيب الاختبار أو تأكسد العينة."
            ];
            const allNotesEn = [
                `Detected Acidic Radical: ${aData.name_en} (${aData.symbol})`,
                `Detected Basic Radical: ${cData.name_en} (${cData.symbol})`,
                "Verify test tube cleanliness and sample integrity against oxidation or cross-contamination."
            ];
            return {
                kind: "result",
                title: inc.title,
                subtitle: inc.subtitle,
                summary: inc.reason,
                summary_en: inc.reason_en || inc.reason,
                equations: allEqsAr,
                equations_en: allEqsEn,
                notes: allNotesAr,
                notes_en: allNotesEn,
                swatch: "#9a4a25",
                formula: false,
                badge: "تحذير علمي: عدم توافق كيميائي",
                badge_en: "Scientific Warning: Incompatible Salt"
            };
        }

        // 2. Reference 30 salts
        if (knowledgeBase.salts_database && knowledgeBase.salts_database[pairKey]) {
            const salt = knowledgeBase.salts_database[pairKey];
            const allEqsAr = [
                `معادلة الملح: ${salt.ionic_equation}`,
                `--- معادلات الشق الحامضي (${aData.name_ar}) ---`,
                ...(aData.equations || []),
                `--- معادلات الشق القاعدي (${cData.name_ar}) ---`,
                ...(cData.equations || [])
            ];
            const allEqsEn = [
                `Salt Formation Equation: ${salt.ionic_equation}`,
                `--- Acidic Radical Reactions (${aData.name_en}) ---`,
                ...(aData.equations || []),
                `--- Basic Radical Reactions (${cData.name_en}) ---`,
                ...(cData.equations || [])
            ];
            const allNotesAr = [
                `الشق الحامضي (Anion): ${aData.name_ar} (${aData.symbol}) — ${aData.group}`,
                `الشق القاعدي (Cation): ${cData.name_ar} (${cData.symbol}) — ${cData.group}`,
                `المظهر الفيزيائي: ${salt.appearance}`,
                `الذوبانية في الماء: ${salt.solubility}`,
                ...(salt.info || [])
            ];
            const allNotesEn = [
                `Acidic Radical (Anion): ${aData.name_en} (${aData.symbol}) — ${aData.group_en || aData.group}`,
                `Basic Radical (Cation): ${cData.name_en} (${cData.symbol}) — ${cData.group_en || cData.group}`,
                `Physical Appearance: ${salt.appearance_en || salt.appearance}`,
                `Solubility in Water: ${salt.solubility_en || salt.solubility}`,
                ...(salt.info_en || salt.info || [])
            ];
            return {
                kind: "result",
                title: salt.formula,
                subtitle: `${salt.name_ar} — ${salt.name_en}`,
                summary: `${aData.summary} كما أن الكاتيون ${cData.summary}`,
                summary_en: `${aData.summary_en || aData.summary} Furthermore, ${cData.summary_en || cData.summary}`,
                equations: allEqsAr,
                equations_en: allEqsEn,
                notes: allNotesAr,
                notes_en: allNotesEn,
                swatch: salt.swatch || "#ffffff",
                formula: true,
                badge: "تم تشخيص الملح بنجاح",
                badge_en: "Salt Identified Successfully"
            };
        }

        // 3. Dynamic salt
        const allEqsAr = [
            `الصيغة المستنتجة: ${cData.symbol}${aData.symbol}`,
            `--- معادلات الشق الحامضي (${aData.name_ar}) ---`,
            ...(aData.equations || []),
            `--- معادلات الشق القاعدي (${cData.name_ar}) ---`,
            ...(cData.equations || [])
        ];
        const allEqsEn = [
            `Balanced Salt Formula: ${cData.symbol}${aData.symbol}`,
            `--- Acidic Radical Reactions (${aData.name_en}) ---`,
            ...(aData.equations || []),
            `--- Basic Radical Reactions (${cData.name_en}) ---`,
            ...(cData.equations || [])
        ];
        const allNotesAr = [
            `الشق الحامضي (Anion): ${aData.name_ar} (${aData.symbol}) — ${aData.group}`,
            `الشق القاعدي (Cation): ${cData.name_ar} (${cData.symbol}) — ${cData.group}`,
            `تفسير الأنيون: ${aData.summary}`,
            `تفسير الكاتيون: ${cData.summary}`
        ];
        const allNotesEn = [
            `Acidic Radical (Anion): ${aData.name_en} (${aData.symbol}) — ${aData.group_en || aData.group}`,
            `Basic Radical (Cation): ${cData.name_en} (${cData.symbol}) — ${cData.group_en || cData.group}`,
            `Anion Diagnostics: ${aData.summary_en || aData.summary}`,
            `Cation Diagnostics: ${cData.summary_en || cData.summary}`
        ];
        return {
            kind: "result",
            title: `${cData.symbol}${aData.symbol}`,
            subtitle: `${aData.name_ar} ${cData.name_ar} — ${cData.name_en} ${aData.name_en}`,
            summary: `تم استنتاج الملح من دمج الشق الحامضي (${aData.name_ar}) مع الشق القاعدي (${cData.name_ar}).`,
            summary_en: `Salt deduced by combining acidic radical (${aData.name_en}) and basic radical (${cData.name_en}).`,
            equations: allEqsAr,
            equations_en: allEqsEn,
            notes: allNotesAr,
            notes_en: allNotesEn,
            swatch: "#ffffff",
            formula: true,
            badge: "تشخيص قياسي مكتمل",
            badge_en: "Standard Diagnostic Deduction"
        };
    }

    function buildSaltHowBreakdown() {
        if (!saltHowPanel) return;

        const isEn = currentLang === "en";
        const anionSteps = sessionData.stepsTrail.filter(s => s.phase === "anion");
        const cationSteps = sessionData.stepsTrail.filter(s => s.phase === "cation");
        const outData = sessionData.suspectedData;
        const aData = (knowledgeBase.anions_data && knowledgeBase.anions_data[sessionData.detected_anion]) || null;
        const cData = (knowledgeBase.cations_data && knowledgeBase.cations_data[sessionData.detected_cation]) || null;

        const p1Title = isEn ? "🧊 Phase 1: Physical Examination of Salt" : "🧊 المرحلة الأولى: الفحص الفيزيائي للملح (Physical Examination)";
        const p1Badge = isEn ? "Phase 1" : "المرحلة 1";
        const p1ColorLabel = isEn ? "Original Solid Color:" : "لون الملح الصلب الأصلي:";
        const p1ColorVal = isEn ? (sessionData.color_en || sessionData.color || "White / Colorless") : (sessionData.color || "أبيض / عديم اللون");
        const p1SolLabel = isEn ? "Solubility in Cold Water:" : "الذوبانية في الماء البارد:";
        const p1SolVal = isEn ? (sessionData.solubility_en || sessionData.state_en || "Dissolves in cold water to form a clear solution") : (sessionData.solubility || sessionData.state || "يذوب في الماء البارد مكوناً محلولاً رائقاً");

        const p2Title = isEn ? "🧪 Phase 2: Acidic Radical (Anion) Tree" : "🧪 المرحلة الثانية: شجرة الكشف عن الشق الحامضي (Anion Tree)";
        const p2Badge = isEn ? "Phase 2" : "المرحلة 2";

        const p3Title = isEn ? "⚗️ Phase 3: Basic Radical (Cation) Tree" : "⚗️ المرحلة الثالثة: شجرة الكشف عن الشق القاعدي (Cation Tree)";
        const p3Badge = isEn ? "Phase 3" : "المرحلة 3";

        const p4Title = isEn ? "⚛️ Phase 4: Radical Integration & Stability Verification" : "⚛️ المرحلة الرابعة: دمج الشقين والاستقرار الكيميائي (Salt Integration & Verification)";
        const p4Badge = isEn ? "Final Outcome" : "النتيجة النهائية";
        const stabilityLabel = isEn ? "Stability Status:" : "حالة الاستقرار:";

        let html = `
            <!-- Phase 0: Physical Examination -->
            <div class="how-phase-card phase-physical">
                <div class="how-phase-title">
                    <span>${p1Title}</span>
                    <span class="how-phase-badge badge-physical">${p1Badge}</span>
                </div>
                <div class="how-step-item">
                    <span class="how-step-num">1</span>
                    <div class="how-step-content">
                        <div class="how-step-name">${p1ColorLabel}</div>
                        <div class="how-step-obs">${p1ColorVal}</div>
                    </div>
                </div>
                <div class="how-step-item">
                    <span class="how-step-num">2</span>
                    <div class="how-step-content">
                        <div class="how-step-name">${p1SolLabel}</div>
                        <div class="how-step-obs">${p1SolVal}</div>
                    </div>
                </div>
            </div>

            <!-- Phase 1: Anion Diagnostic Tree -->
            <div class="how-phase-card phase-anion">
                <div class="how-phase-title">
                    <span>${p2Title}</span>
                    <span class="how-phase-badge badge-anion">${p2Badge}</span>
                </div>
        `;

        anionSteps.forEach((s, idx) => {
            const stepName = formatStepTitle(s, isEn);
            const stepObs = formatStepObservation(s, isEn);
            html += `
                <div class="how-step-item">
                    <span class="how-step-num">${idx + 1}</span>
                    <div class="how-step-content">
                        <div class="how-step-name">${stepName}:</div>
                        <div class="how-step-obs">${stepObs}</div>
                    </div>
                </div>
            `;
        });

        if (aData) {
            const aName = isEn ? `${aData.name_en} (${aData.symbol})` : `${aData.name_ar} (${aData.symbol})`;
            const aGroup = isEn ? (aData.group_en || aData.group) : aData.group;
            const aSummary = isEn ? (aData.summary_en || aData.summary) : aData.summary;
            const aLabel = isEn ? "Deduced Acidic Radical:" : "الشق الحامضي المستنتج:";
            html += `
                <div class="how-result-box">
                    <span class="how-result-badge">🎯</span>
                    <div class="how-result-text">
                        <strong>${aLabel}</strong> ${aName} — ${aGroup}
                        <div style="font-size: 12px; color: #cbd5e1; margin-top: 4px;">${aSummary}</div>
                    </div>
                </div>
            `;
        }

        html += `
            </div>

            <!-- Phase 2: Cation Diagnostic Tree -->
            <div class="how-phase-card phase-cation">
                <div class="how-phase-title">
                    <span>${p3Title}</span>
                    <span class="how-phase-badge badge-cation">${p3Badge}</span>
                </div>
        `;

        cationSteps.forEach((s, idx) => {
            const stepName = formatStepTitle(s, isEn);
            const stepObs = formatStepObservation(s, isEn);
            html += `
                <div class="how-step-item">
                    <span class="how-step-num">${idx + 1}</span>
                    <div class="how-step-content">
                        <div class="how-step-name">${stepName}:</div>
                        <div class="how-step-obs">${stepObs}</div>
                    </div>
                </div>
            `;
        });

        if (cData) {
            const cName = isEn ? `${cData.name_en} (${cData.symbol})` : `${cData.name_ar} (${cData.symbol})`;
            const cGroup = isEn ? (cData.group_en || cData.group) : cData.group;
            const cSummary = isEn ? (cData.summary_en || cData.summary) : cData.summary;
            const cLabel = isEn ? "Deduced Basic Radical:" : "الشق القاعدي المستنتج:";
            html += `
                <div class="how-result-box">
                    <span class="how-result-badge">🎯</span>
                    <div class="how-result-text">
                        <strong>${cLabel}</strong> ${cName} — ${cGroup}
                        <div style="font-size: 12px; color: #cbd5e1; margin-top: 4px;">${cSummary}</div>
                    </div>
                </div>
            `;
        }

        html += `
            </div>

            <!-- Phase 3: Final Synthesis & Compatibility Check -->
            <div class="how-phase-card phase-salt">
                <div class="how-phase-title">
                    <span>${p4Title}</span>
                    <span class="how-phase-badge badge-salt">${p4Badge}</span>
                </div>
                <div class="how-result-box" style="background: rgba(139, 92, 246, 0.15); border-color: rgba(139, 92, 246, 0.4);">
                    <span class="how-result-badge">🧂</span>
                    <div class="how-result-text">
                        <div style="font-size: 15px; color: #e9d5ff; font-weight: 800; font-family: 'JetBrains Mono', monospace;">
                            ${outData ? outData.title : ''} — ${outData ? (isEn ? (outData.subtitle_en || outData.subtitle) : outData.subtitle) : ''}
                        </div>
                        <div style="margin-top: 6px; font-size: 12px; color: #ddd; line-height: 1.6;">
                            ${outData ? outData.summary : ''}
                        </div>
                        <div style="margin-top: 6px; font-size: 11px; color: #a78bfa;">
                            ${stabilityLabel} ${outData ? (outData.badge || (isEn ? 'Salt Diagnosed Successfully' : 'تم تشخيص الملح بنجاح')) : ''}
                        </div>
                    </div>
                </div>
            </div>
        `;

        saltHowPanel.innerHTML = html;
        if (saltHowModalBody) saltHowModalBody.innerHTML = html;
    }

    function toggleSaltHowPanel() {
        if (!saltHowPanel) return;
        const isHidden = saltHowPanel.style.display === "none" || saltHowPanel.style.display === "";
        saltHowPanel.style.display = isHidden ? "flex" : "none";
        if (saltHowBtn) {
            saltHowBtn.classList.toggle("active", isHidden);
        }
        if (saltHowArrow) {
            saltHowArrow.textContent = isHidden ? "▲" : "▼";
        }
        if (isHidden) {
            saltHowPanel.scrollIntoView({ behavior: "smooth", block: "nearest" });
        }
    }

    function setupSaltDiagnosisListeners() {
        if (saltDirectHeaderBtn) {
            saltDirectHeaderBtn.addEventListener("click", () => {
                startSaltDiagnosis();
            });
        }

        if (saltHowBtn) {
            saltHowBtn.addEventListener("click", () => {
                toggleSaltHowPanel();
            });
        }

        if (saltHowModalClose) {
            saltHowModalClose.addEventListener("click", () => {
                if (saltHowModal) saltHowModal.classList.remove("active");
            });
        }

        if (saltHowModal) {
            saltHowModal.addEventListener("click", (e) => {
                if (e.target === saltHowModal) {
                    saltHowModal.classList.remove("active");
                }
            });
        }
    }

    // ========================================================
    // STAGE 5: FINAL LABORATORY REPORT
    // ========================================================

    function triggerStage5Report() {
        setGlobalBackground(4, 5);
        questionContainer.hidden = true;
        stage4Container.hidden = true;
        stage5Container.hidden = false;

        const isEn = currentLang === "en";
        const outData = sessionData.suspectedData;
        const confTest = sessionData.confirmatory;

        const reportNum = "CHEMLAB-" + Math.floor(100000 + Math.random() * 900000);
        const now = new Date();
        const dateStr = now.toLocaleDateString(isEn ? "en-US" : "ar-EG", {
            year: "numeric", month: "long", day: "numeric",
            hour: "2-digit", minute: "2-digit"
        });

        reportId.textContent = `REPORT ID: ${reportNum}`;
        reportDate.textContent = `DATE: ${dateStr}`;

        if (sessionData.isSaltDiagnosis) {
            reportTypeVal.textContent = isEn ? "Inorganic Salt" : (outData ? (outData.badge || "ملح غير عضوي (Inorganic Salt)") : "ملح غير عضوي");
            reportStateVal.textContent = isEn
                ? (sessionData.solubility_en || sessionData.state_en || "Soluble in cold water")
                : (sessionData.solubility || sessionData.state || "يذوب في الماء البارد");

            if (outData && outData.badge && (outData.badge.includes("عدم توافق") || outData.badge.includes("Incompatibility"))) {
                reportStatus.textContent = isEn ? "STATUS: CHEMICAL INCOMPATIBILITY" : "STATUS: CHEMICAL INCOMPATIBILITY (عدم توافق كيميائي)";
                reportStatus.style.color = "#ef4444";
                reportConfirmVal.textContent = isEn ? "Chemically Unstable / Incompatible ⚠️" : "مركب غير مستقر كيميائياً ⚠️";
                reportConfirmVal.style.color = "#ef4444";
            } else {
                reportStatus.textContent = isEn ? "STATUS: VERIFIED (Salt Diagnosed)" : "STATUS: VERIFIED (تشخيص ملح مكتمل)";
                reportStatus.style.color = "#69bd78";
                reportConfirmVal.textContent = isEn ? "Salt Successfully Diagnosed ✓" : "تم تشخيص الملح بنجاح ✓";
                reportConfirmVal.style.color = "#69bd78";
            }
            if (saltHowContainer) {
                saltHowContainer.style.display = "block";
                buildSaltHowBreakdown();
            }
        } else {
            if (saltHowContainer) {
                saltHowContainer.style.display = "none";
            }
            if (sessionData.confirmed) {
                reportStatus.textContent = isEn ? "STATUS: VERIFIED" : "STATUS: VERIFIED (مؤكد معملياً)";
                reportStatus.style.color = "#69bd78";
                reportConfirmVal.textContent = isEn ? "Verified in Lab ✓" : "مؤكد معملياً بنجاح ✓";
                reportConfirmVal.style.color = "#69bd78";
            } else {
                reportStatus.textContent = isEn ? "STATUS: UNCONFIRMED" : "STATUS: UNCONFIRMED (غير مؤكد)";
                reportStatus.style.color = "#f0cf2e";
                reportConfirmVal.textContent = isEn ? "Unconfirmed (Re-test recommended) ⚠️" : "غير مؤكد (يوصى بإعادة الفحص) ⚠️";
                reportConfirmVal.style.color = "#f0cf2e";
            }
            reportStateVal.textContent = isEn
                ? (sessionData.state_en || "Aqueous Solution")
                : (sessionData.state || "محلول مائي");
        }

        reportColorVal.textContent = isEn
            ? (formatStepObservation({ observation_en: sessionData.color_en, observation: sessionData.color }, true) || "Not specified")
            : (formatStepObservation({ observation_ar: sessionData.color_ar, observation: sessionData.color }, false) || "غير محدد");

        if (outData) {
            reportFormulaVal.textContent = outData.title;
            reportNameVal.textContent = outData.subtitle || outData.title;
            if (!sessionData.isSaltDiagnosis) {
                if (sessionData.suspectedKey && sessionData.suspectedKey.startsWith("ORG_")) {
                    reportTypeVal.textContent = isEn ? "Organic Compound" : (outData.badge ? `مركب عضوي — ${outData.badge}` : "مركب عضوي (Organic Compound)");
                } else {
                    reportTypeVal.textContent = isEn ? "Qualitative Ion / Substance" : (outData.formula ? "أيون كيميائي نوعي" : "مركب غير عضوي");
                }
            }
        } else {
            reportFormulaVal.textContent = "—";
            reportNameVal.textContent = isEn ? "Unidentified" : "غير محدد بدقة";
            reportTypeVal.textContent = isEn ? "Unknown Sample" : "عينة مجهولة";
        }

        // Display Chemical Structure in Stage 5 Report
        if (reportStructureCard && reportStructureImg) {
            if (sessionData.suspectedKey && sessionData.suspectedKey.startsWith("ORG_")) {
                reportStructureImg.src = `/static/images/structures/${sessionData.suspectedKey}.png`;
                reportStructureCard.style.display = "flex";
            } else {
                reportStructureCard.style.display = "none";
            }
        }

        // Timeline of steps (dynamically bilingual)
        reportTimelineList.innerHTML = "";
        sessionData.stepsTrail.forEach((step, idx) => {
            const node = document.createElement("div");
            node.className = "report-step-node";

            const testSpan = document.createElement("span");
            testSpan.className = "node-test";
            const stepTitle = formatStepTitle(step, isEn);
            testSpan.textContent = `${idx + 1}. ${stepTitle}`;

            if (step.phase) {
                const phaseTag = document.createElement("span");
                phaseTag.className = `how-phase-badge badge-${step.phase}`;
                if (step.phase === "physical") phaseTag.textContent = isEn ? "Physical Exam" : "فحص فيزيائي";
                else if (step.phase === "anion") phaseTag.textContent = isEn ? "Acidic Radical" : "الشق الحامضي";
                else if (step.phase === "cation") phaseTag.textContent = isEn ? "Basic Radical" : "الشق القاعدي";
                else if (step.phase === "organic") phaseTag.textContent = isEn ? "Organic Exam" : "فحص عضوي";
                else if (step.phase === "confirm") phaseTag.textContent = isEn ? "Confirmation" : "تأكيد معملي";
                else if (step.phase === "inorganic") phaseTag.textContent = isEn ? "Inorganic Exam" : "فحص غير عضوي";
                else phaseTag.textContent = isEn ? "Analytical Step" : "خطوة تحليلية";
                testSpan.appendChild(phaseTag);
            }

            const obsSpan = document.createElement("span");
            obsSpan.className = "node-obs";
            obsSpan.textContent = formatStepObservation(step, isEn);

            node.appendChild(testSpan);
            node.appendChild(obsSpan);
            reportTimelineList.appendChild(node);
        });

        // Chemical Equations
        reportEquationList.innerHTML = "";
        let rawEquations = [];
        if (isEn && outData && outData.equations_en && outData.equations_en.length > 0) {
            rawEquations = [...outData.equations_en];
        } else if (outData && outData.equations) {
            rawEquations = [...outData.equations];
        }
        if (confTest && confTest.equations && sessionData.confirmed) {
            rawEquations.push(...confTest.equations);
        }

        if (rawEquations.length > 0) {
            rawEquations.forEach(eq => {
                const item = document.createElement("div");
                item.className = "equation-item";
                item.textContent = isEn ? formatEquationEn(eq) : eq;
                reportEquationList.appendChild(item);
            });
        } else {
            const item = document.createElement("div");
            item.className = "equation-item";
            item.textContent = isEn ? "No additional chemical equations recorded for this sample." : "لا توجد معادلات كيميائية إضافية مسجلة لهذه العينة.";
            reportEquationList.appendChild(item);
        }

        // Notes (dynamically bilingual)
        reportNotesList.innerHTML = "";
        let rawNotes = [];
        if (isEn) {
            if (outData && outData.notes_en && outData.notes_en.length > 0) {
                rawNotes = [...outData.notes_en];
            } else if (outData && outData.notes) {
                rawNotes = outData.notes.map(n => formatNoteEn(n));
            }
        } else {
            if (outData && outData.notes_ar && outData.notes_ar.length > 0) {
                rawNotes = [...outData.notes_ar];
            } else if (outData && outData.notes) {
                rawNotes = outData.notes.map(n => formatNoteAr(n));
            }
        }

        if (rawNotes.length > 0) {
            rawNotes.forEach(note => {
                const li = document.createElement("li");
                li.className = "note-item";
                li.textContent = isEn ? formatNoteEn(note) : formatNoteAr(note);
                reportNotesList.appendChild(li);
            });
        } else {
            const li = document.createElement("li");
            li.className = "note-item";
            li.textContent = isEn ? "Analytical procedure completed in accordance with qualitative protocol." : "تم إتمام الفحص التحليلي وفقاً للبروتوكول المعملي الاستدلالي المعتمد.";
            reportNotesList.appendChild(li);
        }

        window.scrollTo({ top: stage5Container.offsetTop - 30, behavior: "smooth" });
    }

    function formatEquationEn(eq) {
        if (!eq) return "";
        let str = eq;
        str = str.replace(/^معادلة الملح:\s*/, "Salt Formation Equation: ");
        str = str.replace(/^الصيغة الموزونة المستنتجة:\s*/, "Balanced Salt Formula: ");
        str = str.replace(/^الصيغة المستنتجة:\s*/, "Deducted Formula: ");
        str = str.replace(/--- معادلات الشق الحامضي \((.*?)\) ---/, (m, p1) => {
            const aNameEn = lookupAnionNameEn(p1) || p1;
            return `--- Acidic Radical Reactions (${aNameEn}) ---`;
        });
        str = str.replace(/--- معادلات الشق القاعدي \((.*?)\) ---/, (m, p1) => {
            const cNameEn = lookupCationNameEn(p1) || p1;
            return `--- Basic Radical Reactions (${cNameEn}) ---`;
        });
        str = str.replace(/\(أخضر\)/g, "(Green)");
        str = str.replace(/\(أبيض\)/g, "(White)");
        str = str.replace(/\(أحمر طوبي\)/g, "(Brick-red)");
        str = str.replace(/\(راسب أصفر\)/g, "(Yellow precipitate)");
        str = str.replace(/\(راسب أسود\)/g, "(Black precipitate)");
        str = str.replace(/\(لون بنفسجي\)/g, "(Violet coloration)");
        str = str.replace(/\(أصفر\)/g, "(Yellow)");
        str = str.replace(/\(أزرق\)/g, "(Blue)");
        str = str.replace(/\(بني\)/g, "(Brown)");
        str = str.replace(/\(يتكون أثناء الغليان فقط\)/g, "(Forms during boiling only)");
        return str;
    }

    function lookupAnionNameEn(arName) {
        if (!knowledgeBase || !knowledgeBase.anions_data) return arName;
        for (const [k, v] of Object.entries(knowledgeBase.anions_data)) {
            if (v.name_ar === arName || v.name_ar.includes(arName) || arName.includes(v.name_ar)) {
                return v.name_en || arName;
            }
        }
        return arName;
    }

    function lookupCationNameEn(arName) {
        if (!knowledgeBase || !knowledgeBase.cations_data) return arName;
        for (const [k, v] of Object.entries(knowledgeBase.cations_data)) {
            if (v.name_ar === arName || v.name_ar.includes(arName) || arName.includes(v.name_ar)) {
                return v.name_en || arName;
            }
        }
        return arName;
    }

    function formatNoteEn(note) {
        if (!note) return "";
        let str = note;
        str = str.replace(/^الشق الحامضي \(Anion\):\s*/, "Acidic Radical (Anion): ");
        str = str.replace(/^الشق القاعدي \(Cation\):\s*/, "Basic Radical (Cation): ");
        str = str.replace(/^المظهر الفيزيائي:\s*/, "Physical Appearance: ");
        str = str.replace(/^الذوبانية في الماء:\s*/, "Solubility in Water: ");
        str = str.replace(/^تفسير الأنيون:\s*/, "Anion Diagnostics: ");
        str = str.replace(/^تفسير الكاتيون:\s*/, "Cation Diagnostics: ");
        str = str.replace(/^الشق الحامضي الذي تم رصده:\s*/, "Detected Acidic Radical: ");
        str = str.replace(/^الشق القاعدي الذي تم رصده:\s*/, "Detected Basic Radical: ");
        str = str.replace(/^تحقق من عدم حدوث تلوث في أنابيب الاختبار أو تأكسد العينة\./, "Verify test tube cleanliness and sample integrity against oxidation or cross-contamination.");
        return str;
    }

    function formatNoteAr(note) {
        if (!note) return "";
        let str = note;
        str = str.replace(/^Acidic Radical \(Anion\):\s*/, "الشق الحامضي (Anion): ");
        str = str.replace(/^Basic Radical \(Cation\):\s*/, "الشق القاعدي (Cation): ");
        str = str.replace(/^Physical Appearance:\s*/, "المظهر الفيزيائي: ");
        str = str.replace(/^Solubility in Water:\s*/, "الذوبانية في الماء: ");
        str = str.replace(/^Anion Diagnostics:\s*/, "تفسير الأنيون: ");
        str = str.replace(/^Cation Diagnostics:\s*/, "تفسير الكاتيون: ");
        str = str.replace(/^Detected Acidic Radical:\s*/, "الشق الحامضي الذي تم رصده: ");
        str = str.replace(/^Detected Basic Radical:\s*/, "الشق القاعدي الذي تم رصده: ");
        str = str.replace(/^Verify test tube cleanliness and sample integrity against oxidation or cross-contamination\./, "تحقق من عدم حدوث تلوث في أنابيب الاختبار أو تأكسد العينة.");
        return str;
    }

    reportPrintBtn.addEventListener("click", () => {
        window.print();
    });

    reportNewSampleBtn.addEventListener("click", () => {
        startConsultation();
    });

    newSampleHeaderBtn.addEventListener("click", () => {
        startConsultation();
    });

    // Reference Modal Handlers
    refModalBtn.addEventListener("click", () => {
        setGlobalBackground(8, 9);
        refModal.hidden = false;
    });
    refModalClose.addEventListener("click", () => {
        refModal.hidden = true;
        updateQuestionBackgroundImages();
    });
    refModal.addEventListener("click", (e) => {
        if (e.target === refModal) {
            refModal.hidden = true;
            updateQuestionBackgroundImages();
        }
    });

    // Toggle Predictor Tool
    togglePredictorBtn.addEventListener("click", () => {
        predictorView.hidden = !predictorView.hidden;
        if (!predictorView.hidden) {
            setGlobalBackground(6, 7);
            predictorView.scrollIntoView({ behavior: "smooth" });
        } else {
            updateQuestionBackgroundImages();
        }
    });

    // ========================================================
    // REACTION PREDICTOR MODULE (50 Reactions)
    // ========================================================

    function setupPredictorControls() {
        if (!knowledgeBase || !knowledgeBase.prediction) return;

        const cations = knowledgeBase.prediction.cations || [
            "Cu²⁺", "Fe²⁺", "Fe³⁺", "Zn²⁺", "Al³⁺", "Ca²⁺", "Mg²⁺", "NH₄⁺", "Pb²⁺", "Mn²⁺", "Ag⁺", "Ni²⁺", "Co²⁺", "Hg₂²⁺"
        ];
        const anions = knowledgeBase.prediction.anions || [
            "CO₃²⁻", "HCO₃⁻", "S²⁻", "SO₃²⁻", "S₂O₃²⁻", "NO₂⁻", "Cl⁻", "Br⁻", "I⁻", "NO₃⁻", "SO₄²⁻", "PO₄³⁻", "CrO₄²⁻", "CH₃COO⁻"
        ];
        const reagents = knowledgeBase.prediction.reagents;

        cationsPills.innerHTML = "";
        cations.forEach(ion => {
            const btn = createPill(ion, "ion");
            cationsPills.appendChild(btn);
        });

        anionsPills.innerHTML = "";
        anions.forEach(ion => {
            const btn = createPill(ion, "ion");
            anionsPills.appendChild(btn);
        });

        reagentsPills.innerHTML = "";
        reagents.forEach(reagent => {
            const btn = createPill(reagent, "reagent");
            reagentsPills.appendChild(btn);
        });

        // Setup Quick Preset buttons dynamically
        document.querySelectorAll(".combo-btn").forEach(btn => {
            btn.addEventListener("click", () => {
                const targetIon = btn.dataset.ion;
                const targetReagent = btn.dataset.reagent;
                selectIon(targetIon);
                selectReagent(targetReagent);
                executePrediction();
            });
        });
    }

    function createPill(text, type) {
        const btn = document.createElement("button");
        btn.className = "pill-btn";
        btn.textContent = text;
        btn.addEventListener("click", () => {
            if (type === "ion") {
                selectIon(text);
            } else {
                selectReagent(text);
            }
        });
        return btn;
    }

    function selectIon(ionStr) {
        selectedIon = ionStr;
        document.querySelectorAll("#cations-pills .pill-btn, #anions-pills .pill-btn").forEach(btn => {
            btn.classList.toggle("active", btn.textContent === ionStr);
        });
    }

    function selectReagent(reagentStr) {
        selectedReagent = reagentStr;
        document.querySelectorAll("#reagents-pills .pill-btn").forEach(btn => {
            btn.classList.toggle("active", btn.textContent === reagentStr);
        });
    }

    predictBtn.addEventListener("click", () => {
        executePrediction();
    });

    async function executePrediction() {
        if (!selectedIon || !selectedReagent) {
            alert(currentLang === "en" ? "Please select both an ion and a reagent to predict the reaction." : "يرجى اختيار الأيون والكاشف معاً للتنبؤ بالتفاعل.");
            return;
        }

        tubeLabel.textContent = currentLang === "en" ? `Analyzing: ${selectedIon} + ${selectedReagent}...` : `تحليل: ${selectedIon} + ${selectedReagent}...`;

        try {
            const response = await fetch("/api/predict", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ ion: selectedIon, reagent: selectedReagent })
            });

            if (!response.ok) throw new Error("Prediction API call failed");
            const data = await response.json();
            renderPredictionResult(data);
        } catch (err) {
            console.error(err);
            renderLocalPrediction(selectedIon, selectedReagent);
        }
    }

    function renderPredictionResult(data) {
        predictResultPlaceholder.hidden = true;
        predictResultCard.hidden = false;

        const isEn = currentLang === "en";
        tubeLabel.textContent = `${data.ion} + ${data.reagent}`;

        if (data.status === "validated") {
            predictStatusBadge.className = "status-badge-validated";
            predictStatusBadge.textContent = isEn ? "VALIDATED REACTION RESULT" : "VALIDATED REACTION RESULT — تفاعل مؤكد معملياً";

            if (isEn) {
                predictResultTitle.textContent = data.result;
                predictResultAr.textContent = data.arabic_result || "";
            } else {
                predictResultTitle.textContent = data.arabic_result || data.result;
                predictResultAr.textContent = data.arabic_result ? data.result : "";
            }

            const swatch = data.swatch || "#ffffff";
            tubePrecipitate.style.background = swatch;
            tubePrecipitate.style.opacity = "1";
            tubePrecipitate.style.boxShadow = `0 0 15px ${swatch}aa`;

            if (data.equations && data.equations.length > 0) {
                predictEquationsContainer.hidden = false;
                predictEquationsList.innerHTML = "";
                data.equations.forEach(eq => {
                    const div = document.createElement("div");
                    div.className = "equation-item";
                    div.textContent = eq;
                    predictEquationsList.appendChild(div);
                });
            } else {
                predictEquationsContainer.hidden = true;
            }

            if (data.notes && data.notes.length > 0) {
                predictNotesContainer.hidden = false;
                predictNotesList.innerHTML = "";
                data.notes.forEach(note => {
                    const li = document.createElement("li");
                    li.className = "note-item";
                    li.textContent = note;
                    predictNotesList.appendChild(li);
                });
            } else {
                predictNotesContainer.hidden = true;
            }
        } else {
            predictStatusBadge.className = "status-badge-unvalidated";
            predictStatusBadge.textContent = isEn ? "UNVALIDATED PAIR — NO VERIFIED DATA" : "UNVALIDATED PAIR — لا تتوفر بيانات مؤكدة";

            if (isEn) {
                predictResultTitle.textContent = data.result;
                predictResultAr.textContent = data.arabic_result || "";
            } else {
                predictResultTitle.textContent = data.arabic_result || data.result;
                predictResultAr.textContent = data.arabic_result ? data.result : "";
            }

            tubePrecipitate.style.background = "transparent";
            tubePrecipitate.style.boxShadow = "none";

            predictEquationsContainer.hidden = true;

            predictNotesContainer.hidden = false;
            predictNotesList.innerHTML = "";
            data.notes.forEach(note => {
                const li = document.createElement("li");
                li.className = "note-item";
                li.textContent = note;
                predictNotesList.appendChild(li);
            });
        }
    }

    function renderLocalPrediction(ion, reagent) {
        if (!knowledgeBase) return;
        const key = `${ion}_${reagent}`;
        const match = knowledgeBase.prediction.reactions[key];

        if (match) {
            renderPredictionResult({
                status: "validated",
                ion: ion,
                reagent: reagent,
                result: match.result,
                arabic_result: match.arabic_result,
                swatch: match.swatch,
                equations: match.equations,
                notes: match.notes
            });
        } else {
            renderPredictionResult({
                status: "unvalidated",
                ion: ion,
                reagent: reagent,
                result: "No validated data available for this ion–reagent combination.",
                arabic_result: "لا تتوفر بيانات مؤكدة معملياً لهذا المزيج من الأيون والكاشف.",
                equations: [],
                notes: [
                    "Do not assume a missing combination means 'no reaction'.",
                    "The scientific outcome for this specific ion–reagent pair has not been documented in the verified knowledge base.",
                    "Testing requires verified scientific literature or lab verification under specified conditions."
                ]
            });
        }
    }
});
