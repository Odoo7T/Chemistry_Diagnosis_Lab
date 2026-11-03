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
            workspace_title: "فحص وتشخيص العينة المجهولة",
            workspace_desc: "حدد مسار الفحص (عضوي أو غير عضوي أو غير محدد) وأجب عن الأسئلة المعملية وسيقوم محرك الاستدلال بإرشادك خطوة بخطوة حتى الوصول للنتيجة والتجربة التأكيدية.",
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
            workspace_title: "Unknown Sample Analysis & Diagnosis",
            workspace_desc: "Select your diagnostic route and answer the laboratory prompts. The inference engine will guide you step by step to identify the substance and perform confirmatory tests.",
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

        // Re-render question if active
        if (questionContainer && !questionContainer.hidden) {
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
            setupLanguageSwitcher();
            startConsultation();
        } catch (err) {
            console.error("Error loading knowledge base:", err);
        }
    }

    loadData();

    // ========================================================
    // UNIFIED LAB CONSULTATION (Starts directly with Question 1)
    // ========================================================

    function startConsultation() {
        previousFailedAttempt = null;
        sessionData = {
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

        historyStack = [];
        historyStack.push({
            type: "question",
            id: "start_mode",
            label: "تحديد مسار التحليل الكيميائي"
        });

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

    function startSaltDiagnosis() {
        startConsultation();
        sessionData.isSaltDiagnosis = true;
        historyStack = [{
            type: "question",
            id: "SALT_START",
            label: "الخطوة 1: الفحص الفيزيائي للملح"
        }];
        stepBackBtn.style.display = "none";
        renderCurrentQuestion();
        window.scrollTo({ top: 0, behavior: "smooth" });
    }

    function renderCurrentQuestion() {
        if (!knowledgeBase || !knowledgeBase.unified) return;

        const currentStep = historyStack[historyStack.length - 1];
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
                labelSpan.textContent = isEn ? (opt.label || opt.arabic_label) : (opt.arabic_label || opt.label);
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
        const obsTextAr = opt.arabic_label || opt.label;
        const obsTextEn = opt.label || opt.arabic_label;
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
        const testLabelAr = parentStep.label_ar || parentStep.label || (parentQ ? (parentQ.arabic_text || parentQ.text) : "اختبار كيميائي");
        const testLabelEn = parentStep.label_en || (parentQ ? (parentQ.text || parentQ.arabic_text) : "Chemical Test");
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
            symbol: anionKey, name_ar: anionKey, name_en: anionKey, group: "غير محدد", equations: [], summary: ""
        };
        const cData = (knowledgeBase.cations_data && knowledgeBase.cations_data[cationKey]) || {
            symbol: cationKey, name_ar: cationKey, name_en: cationKey, group: "غير محدد", equations: [], summary: ""
        };

        const pairKey = `${cationKey}_${anionKey}`;

        // 1. Incompatible salts
        if (knowledgeBase.incompatible_salts && knowledgeBase.incompatible_salts[pairKey]) {
            const inc = knowledgeBase.incompatible_salts[pairKey];
            return {
                kind: "result",
                title: inc.title,
                subtitle: inc.subtitle,
                summary: inc.reason,
                equations: [...(inc.equations || []), ...(aData.equations || []), ...(cData.equations || [])],
                notes: [
                    `الشق الحامضي الذي تم رصده: ${aData.name_ar} (${aData.symbol})`,
                    `الشق القاعدي الذي تم رصده: ${cData.name_ar} (${cData.symbol})`,
                    "تحقق من عدم حدوث تلوث في أنابيب الاختبار أو تأكسد العينة."
                ],
                swatch: "#9a4a25",
                formula: false,
                badge: "تحذير علمي: عدم توافق كيميائي"
            };
        }

        // 2. Reference 30 salts
        if (knowledgeBase.salts_database && knowledgeBase.salts_database[pairKey]) {
            const salt = knowledgeBase.salts_database[pairKey];
            const allEqs = [
                `معادلة الملح: ${salt.ionic_equation}`,
                `--- معادلات الشق الحامضي (${aData.name_ar}) ---`,
                ...(aData.equations || []),
                `--- معادلات الشق القاعدي (${cData.name_ar}) ---`,
                ...(cData.equations || [])
            ];
            const allNotes = [
                `الشق الحامضي (Anion): ${aData.name_ar} (${aData.symbol}) — ${aData.group}`,
                `الشق القاعدي (Cation): ${cData.name_ar} (${cData.symbol}) — ${cData.group}`,
                `المظهر الفيزيائي: ${salt.appearance}`,
                `الذوبانية في الماء: ${salt.solubility}`,
                ...(salt.info || [])
            ];
            return {
                kind: "result",
                title: salt.formula,
                subtitle: `${salt.name_ar} — ${salt.name_en}`,
                summary: `${aData.summary} كما أن الكاتيون ${cData.summary}`,
                equations: allEqs,
                notes: allNotes,
                swatch: salt.swatch || "#ffffff",
                formula: true,
                badge: "تم تشخيص الملح بنجاح"
            };
        }

        // 3. Dynamic salt
        return {
            kind: "result",
            title: `${cData.symbol}${aData.symbol}`,
            subtitle: `${aData.name_ar} ${cData.name_ar} — ${cData.name_en} ${aData.name_en}`,
            summary: `تم استنتاج الملح من دمج الشق الحامضي (${aData.name_ar}) مع الشق القاعدي (${cData.name_ar}).`,
            equations: [
                `الصيغة المستنتجة: ${cData.symbol}${aData.symbol}`,
                `--- معادلات الشق الحامضي (${aData.name_ar}) ---`,
                ...(aData.equations || []),
                `--- معادلات الشق القاعدي (${cData.name_ar}) ---`,
                ...(cData.equations || [])
            ],
            notes: [
                `الشق الحامضي (Anion): ${aData.name_ar} (${aData.symbol}) — ${aData.group}`,
                `الشق القاعدي (Cation): ${cData.name_ar} (${cData.symbol}) — ${cData.group}`,
                `تفسير الأنيون: ${aData.summary}`,
                `تفسير الكاتيون: ${cData.summary}`
            ],
            swatch: "#ffffff",
            formula: true,
            badge: "تشخيص قياسي مكتمل"
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
            const stepName = isEn ? (s.test_en || s.test) : (s.test_ar || s.test);
            const stepObs = isEn ? (s.observation_en || s.observation) : (s.observation_ar || s.observation);
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
            const aLabel = isEn ? "Deduced Acidic Radical:" : "الشق الحامضي المستنتج:";
            html += `
                <div class="how-result-box">
                    <span class="how-result-badge">🎯</span>
                    <div class="how-result-text">
                        <strong>${aLabel}</strong> ${aName} — ${aData.group}
                        <div style="font-size: 12px; color: #cbd5e1; margin-top: 4px;">${aData.summary}</div>
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
            const stepName = isEn ? (s.test_en || s.test) : (s.test_ar || s.test);
            const stepObs = isEn ? (s.observation_en || s.observation) : (s.observation_ar || s.observation);
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
            const cLabel = isEn ? "Deduced Basic Radical:" : "الشق القاعدي المستنتج:";
            html += `
                <div class="how-result-box">
                    <span class="how-result-badge">🎯</span>
                    <div class="how-result-text">
                        <strong>${cLabel}</strong> ${cName} — ${cData.group}
                        <div style="font-size: 12px; color: #cbd5e1; margin-top: 4px;">${cData.summary}</div>
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
            ? (sessionData.color_en || sessionData.color || "Not specified")
            : (sessionData.color || "غير محدد");

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

        // Timeline of steps
        reportTimelineList.innerHTML = "";
        sessionData.stepsTrail.forEach((step, idx) => {
            const node = document.createElement("div");
            node.className = "report-step-node";

            const testSpan = document.createElement("span");
            testSpan.className = "node-test";
            const stepTitle = isEn ? (step.test_en || step.test) : (step.test_ar || step.test);
            testSpan.textContent = `${idx + 1}. ${stepTitle}`;

            if (step.phase) {
                const phaseTag = document.createElement("span");
                phaseTag.className = `how-phase-badge badge-${step.phase}`;
                if (step.phase === "physical") phaseTag.textContent = isEn ? "Physical Exam" : "فحص فيزيائي";
                else if (step.phase === "anion") phaseTag.textContent = isEn ? "Acidic Radical" : "الشق الحامضي";
                else if (step.phase === "cation") phaseTag.textContent = isEn ? "Basic Radical" : "الشق القاعدي";
                else if (step.phase === "organic") phaseTag.textContent = isEn ? "Organic Exam" : "فحص عضوي";
                testSpan.appendChild(phaseTag);
            }

            const obsSpan = document.createElement("span");
            obsSpan.className = "node-obs";
            obsSpan.textContent = isEn ? (step.observation_en || step.observation) : (step.observation_ar || step.observation);

            node.appendChild(testSpan);
            node.appendChild(obsSpan);
            reportTimelineList.appendChild(node);
        });

        // Chemical Equations
        reportEquationList.innerHTML = "";
        const allEquations = [];
        if (outData && outData.equations) {
            allEquations.push(...outData.equations);
        }
        if (confTest && confTest.equations && sessionData.confirmed) {
            allEquations.push(...confTest.equations);
        }

        if (allEquations.length > 0) {
            allEquations.forEach(eq => {
                const item = document.createElement("div");
                item.className = "equation-item";
                item.textContent = eq;
                reportEquationList.appendChild(item);
            });
        } else {
            const item = document.createElement("div");
            item.className = "equation-item";
            item.textContent = isEn ? "No additional chemical equations recorded for this sample." : "لا توجد معادلات كيميائية إضافية مسجلة لهذه العينة.";
            reportEquationList.appendChild(item);
        }

        // Notes
        reportNotesList.innerHTML = "";
        if (outData && outData.notes && outData.notes.length > 0) {
            outData.notes.forEach(note => {
                const li = document.createElement("li");
                li.className = "note-item";
                li.textContent = note;
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
