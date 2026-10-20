document.addEventListener("DOMContentLoaded", () => {
    // DOM Elements - Shell
    const newSampleHeaderBtn = document.getElementById("new-sample-header-btn");
    const togglePredictorBtn = document.getElementById("toggle-predictor-btn");
    const refModalBtn = document.getElementById("ref-modal-btn");
    const refModal = document.getElementById("ref-modal");
    const refModalClose = document.getElementById("ref-modal-close");

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
        stepsTrail: [],
        suspectedKey: null,
        suspectedData: null,
        confirmatory: null,
        confirmed: false
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
            stepsTrail: [],
            suspectedKey: null,
            suspectedData: null,
            confirmatory: null,
            confirmed: false
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

            questionTextAr.textContent = qData.arabic_text || qData.text;
            questionText.textContent = qData.text !== qData.arabic_text ? qData.text : "";

            if (qData.hint) {
                questionHintBox.style.display = "flex";
                questionHintAr.textContent = "💡 " + (qData.arabic_hint || qData.hint);
                questionHintEn.textContent = qData.hint !== qData.arabic_hint ? qData.hint : "";
            } else {
                questionHintBox.style.display = "none";
            }

            optionsGrid.innerHTML = "";

            if (currentStep.id === "start_mode") {
                optionsGrid.classList.add("grid-cols-3");
            } else {
                optionsGrid.classList.remove("grid-cols-3");
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

                const arLabel = document.createElement("span");
                arLabel.className = "option-label-en";
                arLabel.textContent = opt.arabic_label || opt.label;
                labelsDiv.appendChild(arLabel);

                mainDiv.appendChild(swatchSpan);
                mainDiv.appendChild(labelsDiv);

                const arrowSpan = document.createElement("span");
                arrowSpan.className = "arrow";
                arrowSpan.textContent = "←";

                // Special start-mode 3-choice presentation
                if (currentStep.id === "start_mode") {
                    btn.classList.add("start-mode-btn");
                    swatchSpan.style.display = "none";

                    const iconDiv = document.createElement("div");
                    iconDiv.className = "start-mode-icon";

                    const descDiv = document.createElement("div");
                    descDiv.className = "start-mode-desc";

                    if (opt.next === "org_q_state") {
                        iconDiv.textContent = "🧪";
                        descDiv.textContent = "تشخيص 25 مركباً عضوياً (سوائل ومواد صلبة)";
                    } else if (opt.next === "start_color") {
                        iconDiv.textContent = "⚗️";
                        descDiv.textContent = "الكشف عن الكاتيونات والأنيونات غير العضوية";
                    } else {
                        iconDiv.textContent = "🔥";
                        descDiv.textContent = "فحص مبدئي بالتسخين واللهب للتوجيه التلقائي";
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

        const obsText = opt.arabic_label || opt.label;

        // Save initial physical observations
        if (parentStep.id === "start_color") {
            sessionData.color = obsText;
        } else if (parentStep.id === "q_physical_state" || parentStep.id === "org_q_state") {
            sessionData.state = obsText;
        }

        // Record in chronological analytical trail
        const testLabel = parentStep.label || (tree[parentStep.id] ? tree[parentStep.id].arabic_text : "اختبار كيميائي");
        sessionData.stepsTrail.push({
            test: testLabel,
            observation: obsText
        });

        if (tree && tree[nextKey]) {
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
            historyStack.pop();
            sessionData.stepsTrail.pop();
            renderCurrentQuestion();
        }
    });

    // ========================================================
    // STAGE 4: CONFIRMATORY TEST
    // ========================================================

    function triggerStage4Confirmatory(outcomeKey, outcomeData) {
        setGlobalBackground(2, 3);
        questionContainer.hidden = true;
        stage4Container.hidden = false;
        stage5Container.hidden = true;

        stage4PromptBlock.hidden = false;
        stage4ExecutionBlock.hidden = true;
        stage4FailureBlock.hidden = true;
        userErrorWarningBlock.hidden = true;

        const ionName = outcomeData ? (outcomeData.subtitle || outcomeData.title) : "المادة المجهولة";
        const formula = outcomeData ? outcomeData.title : "";

        stage4PromptText.textContent = `النتيجة المحتملة: ${formula} (${ionName}). هل تريد إجراء الاختبار التأكيدي؟`;

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
            if (confTest) {
                stage4PromptBlock.hidden = true;
                stage4ExecutionBlock.hidden = false;
                confirmatoryReagentTitle.textContent = `الكاشف التأكيدي: ${confTest.reagent}`;
                confirmatoryProcedure.textContent = `طريقة الإجراء: ${confTest.procedure}`;
                confirmatorySignBadge.textContent = `العلامة المتوقعة: ${confTest.expected_sign}`;
                confirmatoryQuestionText.textContent = `أضف ${confTest.reagent}. هل ظهرت العلامة المتوقعة (${confTest.expected_sign})؟`;
                window.scrollTo({ top: stage4ExecutionBlock.offsetTop - 50, behavior: "smooth" });
            } else {
                sessionData.confirmed = true;
                sessionData.stepsTrail.push({
                    test: "الاختبار التأكيدي",
                    observation: "تم التأكيد بناءً على مطابقة السلوك الكيميائي وسلسلة الكواشف الترسيبية"
                });
                triggerStage5Report();
            }
        };

        stage4SkipBtn.onclick = () => {
            sessionData.confirmed = false;
            sessionData.stepsTrail.push({
                test: "الاختبار التأكيدي",
                observation: "تم تخطي الاختبار التأكيدي والاكتفاء بالمشاهدات الاستدلالية المباشرة"
            });
            triggerStage5Report();
        };

        confirmatoryConfirmedBtn.onclick = () => {
            sessionData.confirmed = true;
            sessionData.stepsTrail.push({
                test: `الاختبار التأكيدي (${confTest.reagent})`,
                observation: `✓ ظهرت العلامة التأكيدية بنجاح: ${confTest.expected_sign}`
            });
            triggerStage5Report();
        };

        confirmatoryFailedBtn.onclick = () => {
            sessionData.confirmed = false;
            sessionData.stepsTrail.push({
                test: `الاختبار التأكيدي (${confTest.reagent})`,
                observation: `✗ لم تظهر العلامة المتوقعة: ${confTest.expected_sign}`
            });

            // Show failure resolution block (سؤال المستخدم: نعيد من الأول ولا نكمل من اللي وصلنا له)
            stage4PromptBlock.hidden = true;
            stage4ExecutionBlock.hidden = true;
            userErrorWarningBlock.hidden = true;
            stage4FailureBlock.hidden = false;

            failedReagentName.textContent = confTest ? confTest.reagent : "الكاشف التأكيدي";
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
                        label: "المرحلة 2: الكاشف الأول (HCl)"
                    }
                ];

                sessionData.stepsTrail = [
                    { test: "الملاحظة الأولية للون العينة", observation: sessionData.color },
                    { test: "الحالة الفيزيائية للعينة", observation: sessionData.state }
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
                // العودة للخطوة السابقة مباشرة قبل النتيجة
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
    // STAGE 5: FINAL LABORATORY REPORT
    // ========================================================

    function triggerStage5Report() {
        setGlobalBackground(4, 5);
        questionContainer.hidden = true;
        stage4Container.hidden = true;
        stage5Container.hidden = false;

        const outData = sessionData.suspectedData;
        const confTest = sessionData.confirmatory;

        const reportNum = "CHEMLAB-" + Math.floor(100000 + Math.random() * 900000);
        const now = new Date();
        const dateStr = now.toLocaleDateString("ar-EG", {
            year: "numeric", month: "long", day: "numeric",
            hour: "2-digit", minute: "2-digit"
        });

        reportId.textContent = `REPORT ID: ${reportNum}`;
        reportDate.textContent = `DATE: ${dateStr}`;

        if (sessionData.confirmed) {
            reportStatus.textContent = "STATUS: VERIFIED (مؤكد معملياً)";
            reportStatus.style.color = "#69bd78";
            reportConfirmVal.textContent = "مؤكد معملياً بنجاح ✓";
            reportConfirmVal.style.color = "#69bd78";
        } else {
            reportStatus.textContent = "STATUS: UNCONFIRMED (غير مؤكد)";
            reportStatus.style.color = "#f0cf2e";
            reportConfirmVal.textContent = "غير مؤكد (يوصى بإعادة الفحص) ⚠️";
            reportConfirmVal.style.color = "#f0cf2e";
        }

        reportColorVal.textContent = sessionData.color || "غير محدد";
        reportStateVal.textContent = sessionData.state || "محلول مائي";

        if (outData) {
            reportFormulaVal.textContent = outData.title;
            reportNameVal.textContent = outData.subtitle || outData.title;
            if (sessionData.suspectedKey && sessionData.suspectedKey.startsWith("ORG_")) {
                reportTypeVal.textContent = outData.badge ? `مركب عضوي — ${outData.badge}` : "مركب عضوي (Organic Compound)";
            } else {
                reportTypeVal.textContent = outData.formula ? "أيون كيميائي نوعي" : "مركب غير عضوي";
            }
        } else {
            reportFormulaVal.textContent = "—";
            reportNameVal.textContent = "غير محدد بدقة";
            reportTypeVal.textContent = "عينة مجهولة";
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
            testSpan.textContent = `${idx + 1}. ${step.test}`;

            const obsSpan = document.createElement("span");
            obsSpan.className = "node-obs";
            obsSpan.textContent = step.observation;

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
            item.textContent = "لا توجد معادلات كيميائية إضافية مسجلة لهذه العينة.";
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
            li.textContent = "تم إتمام الفحص التحليلي وفقاً للبروتوكول المعملي الاستدلالي المعتمد.";
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
            alert("يرجى اختيار الأيون والكاشف معاً للتنبؤ بالتفاعل.");
            return;
        }

        tubeLabel.textContent = `تحليل: ${selectedIon} + ${selectedReagent}...`;

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

        tubeLabel.textContent = `${data.ion} + ${data.reagent}`;

        if (data.status === "validated") {
            predictStatusBadge.className = "status-badge-validated";
            predictStatusBadge.textContent = "VALIDATED REACTION RESULT — تفاعل مؤكد معملياً";

            predictResultTitle.textContent = data.result;
            predictResultAr.textContent = data.arabic_result || "";

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
            predictStatusBadge.textContent = "UNVALIDATED PAIR — لا تتوفر بيانات مؤكدة";

            predictResultTitle.textContent = data.result;
            predictResultAr.textContent = data.arabic_result || "";

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
