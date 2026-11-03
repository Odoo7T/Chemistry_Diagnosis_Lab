"""
Chemistry Expert System — Complete Knowledge Base
Qualitative Inorganic Analysis and Reaction Prediction
"""

# 1. Color Constants
BLUE = "#3b82d6"           # راسب أزرق / أملاح النحاس المائية
DEEP_BLUE = "#1d4ed8"      # محلول أزرق قاتم (معقد النحاس النشادرى)
BLUE_GREEN = "#0d9488"     # بلورات زرقاء مخضرة (كلوريد النحاس)
GREEN = "#6f9a4f"          # راسب أخضر / أملاح الحديد الثنائي
APPLE_GREEN = "#84cc16"    # لهب أخضر تفاحي (الباريوم)
BROWN = "#9a4a25"          # راسب بني محمر (الحديد الثلاثي / نيسلر / الحلقة البنية)
WHITE = "#ffffff"          # راسب أبيض / ملح أبيض
NONE = "none"              # عديم اللون / لا يوجد راسب
PALE_YELLOW = "#efe6a0"    # راسب أبيض مصفر (كريمي - بروميد الفضة)
YELLOW = "#f0cf2e"         # راسب أصفر (يوديد الفضة / فوسفات الفضة / كرومات الباريوم / كبريت)
GOLDEN_YELLOW = "#fbbf24"  # لهب أصفر ذهبي (الصوديوم)
ORANGE = "#f97316"         # أبخرة برتقالية حمراء (البروم)
BRICK_RED = "#b91c1c"      # لهب أحمر طوبي (الكالسيوم)
BLOOD_RED = "#7f1d1d"      # لون أحمر دامي (ثيوسيانات الحديد الثلاثي)
VIOLET = "#8b5cf6"         # أبخرة اليود البنفسجية / برمنجنات البوتاسيوم
LILAC = "#c084fc"          # لهب بنفسجي فاتح (البوتاسيوم)
BLACK = "#1f2937"          # راسب أسود (الكبريتيدات / أكسيد النحاس)
GRAY_BLACK = "#374151"     # صلب أسود رمادي (كبريتيد الحديد)


# 2. Knowledge Base Helper Functions
def option(label, nxt, swatch=None, arabic_label=None):
    return {
        "label": label,
        "arabic_label": arabic_label,
        "next": nxt,
        "swatch": swatch
    }


def question(id_key, text, options, hint=None, arabic_text=None, arabic_hint=None):
    return {
        "id": id_key,
        "kind": "question",
        "text": text,
        "arabic_text": arabic_text,
        "hint": hint,
        "arabic_hint": arabic_hint,
        "options": options
    }


def outcome(title, subtitle, summary, equations=(), notes=(), swatch=None, formula=False, badge=None, arabic_summary=None, **kwargs):
    res = {
        "kind": "result",
        "title": title,
        "subtitle": subtitle,
        "summary": summary,
        "arabic_summary": arabic_summary,
        "equations": list(equations),
        "notes": list(notes),
        "swatch": swatch,
        "formula": formula,
        "badge": badge
    }
    res.update(kwargs)
    return res


def ion(formula, name, summary, equations, notes=(), swatch=None, arabic_summary=None, badge=None):
    return outcome(
        formula,
        name,
        summary,
        equations,
        notes,
        swatch,
        formula=True,
        badge=badge,
        arabic_summary=arabic_summary
    )


# 3. Cation Analysis Knowledge & Decision Tree
CATION_OUTCOMES = {
    "CU": ion(
        "Cu²⁺",
        "Copper(II) — أيون النحاس الثنائي",
        "Blue precipitate forms upon adding NaOH; precipitate does not dissolve in excess NaOH.",
        [
            "Cu²⁺ + 2OH⁻ → Cu(OH)₂ ↓"
        ],
        notes=[
            "A distinctive pale blue precipitate of copper(II) hydroxide forms.",
            "The precipitate does not dissolve in excess sodium hydroxide under standard conditions.",
            "In excess aqueous ammonia, it dissolves to form a deep royal blue tetraamminecopper(II) complex: [Cu(NH₃)₄]²⁺."
        ],
        swatch=BLUE,
        arabic_summary="يتكون راسب أزرق من هيدروكسيد النحاس الثنائي لا يذوب في الزيادة من هيدروكسيد الصوديوم."
    ),

    "FE2": ion(
        "Fe²⁺",
        "Iron(II) — أيون الحديد الثنائي",
        "Dirty-green precipitate forms upon adding NaOH; oxidizes to reddish-brown at the surface on exposure to air.",
        [
            "Fe²⁺ + 2OH⁻ → Fe(OH)₂ ↓",
            "4Fe(OH)₂ + O₂ + 2H₂O → 4Fe(OH)₃"
        ],
        notes=[
            "Initial precipitate is iron(II) hydroxide Fe(OH)₂, which is dirty-green.",
            "Rapidly oxidizes when exposed to oxygen in the air, turning reddish-brown Fe(OH)₃.",
            "Insoluble in excess NaOH."
        ],
        swatch=GREEN,
        arabic_summary="يتكون راسب أخضر قذر من هيدروكسيد الحديد الثنائي يتحول بالتدريج إلى بني محمر عند تعرضه للهواء."
    ),

    "FE3": ion(
        "Fe³⁺",
        "Iron(III) — أيون الحديد الثلاثي",
        "Reddish-brown gelatinous precipitate forms upon adding NaOH; insoluble in excess.",
        [
            "Fe³⁺ + 3OH⁻ → Fe(OH)₃ ↓"
        ],
        notes=[
            "A reddish-brown precipitate of iron(III) hydroxide forms immediately.",
            "The precipitate does not dissolve in excess sodium hydroxide.",
            "Can also be confirmed using potassium thiocyanate (KSCN), yielding a blood-red solution."
        ],
        swatch=BROWN,
        arabic_summary="يتكون راسب بني محمر جيلاتيني من هيدروكسيد الحديد الثلاثي لا يذوب في الزيادة من NaOH."
    ),

    "ZN": ion(
        "Zn²⁺",
        "Zinc — أيون الزنك",
        "White precipitate forms with NaOH, dissolves in excess NaOH, and also dissolves in excess ammonia solution.",
        [
            "Zn²⁺ + 2OH⁻ → Zn(OH)₂ ↓",
            "Zn(OH)₂ + 2OH⁻ → [Zn(OH)₄]²⁻",
            "Zn(OH)₂ + 4NH₃ ⇌ [Zn(NH₃)₄]²⁺ + 2OH⁻"
        ],
        notes=[
            "Zinc hydroxide Zn(OH)₂ initially forms as a white precipitate.",
            "Due to amphoteric nature, it dissolves in excess NaOH forming the soluble tetrahydroxozincate(II) ion.",
            "Crucial distinction from Al³⁺: Zinc hydroxide dissolves in excess aqueous ammonia solution to form the tetraamminezinc(II) complex."
        ],
        swatch=WHITE,
        arabic_summary="يتكون راسب أبيض يذوب في وفرة من هيدروكسيد الصوديوم، ويذوب أيضاً في وفرة من محلول النشادر."
    ),

    "AL": ion(
        "Al³⁺",
        "Aluminium — أيون الألومنيوم",
        "White gelatinous precipitate with NaOH, dissolves in excess NaOH, but does NOT dissolve in excess ammonia.",
        [
            "Al³⁺ + 3OH⁻ → Al(OH)₃ ↓",
            "Al(OH)₃ + OH⁻ → [Al(OH)₄]⁻"
        ],
        notes=[
            "Forms a white gelatinous precipitate of aluminium hydroxide Al(OH)₃.",
            "Being amphoteric, it readily dissolves in excess NaOH forming soluble tetrahydroxoaluminate [Al(OH)₄]⁻.",
            "Key distinction from Zn²⁺: aluminium hydroxide does NOT dissolve in excess ammonia solution."
        ],
        swatch=WHITE,
        arabic_summary="يتكون راسب أبيض جيلاتيني يذوب في وفرة من NaOH، ولكنه لا يذوب في وفرة من محلول النشادر."
    ),

    "CA": ion(
        "Ca²⁺",
        "Calcium — أيون الكالسيوم",
        "Faint or white precipitate forms with NaOH, does not dissolve in excess NaOH; brick-red flame test.",
        [
            "Ca²⁺ + 2OH⁻ → Ca(OH)₂ ↓"
        ],
        notes=[
            "Calcium hydroxide is sparingly soluble, so precipitation may be light or require sufficient ion concentration.",
            "Does not dissolve in excess sodium hydroxide.",
            "Flame test confirms Ca²⁺ with a characteristic brick-red (orange-red) color.",
            "Ammonium oxalate can be used as a further confirmatory test to produce white calcium oxalate."
        ],
        swatch=BRICK_RED,
        arabic_summary="يتكون راسب أبيض خفيف لا يذوب في وفرة من NaOH؛ ويعطي لهب بنزن لوناً أحمر طوبياً مميزاً."
    ),

    "MG": ion(
        "Mg²⁺",
        "Magnesium — أيون المغنيسيوم",
        "White precipitate with NaOH, does not dissolve in excess NaOH; no distinctive flame test color.",
        [
            "Mg²⁺ + 2OH⁻ → Mg(OH)₂ ↓"
        ],
        notes=[
            "Magnesium hydroxide forms a distinct white precipitate.",
            "It does not dissolve in excess NaOH under standard conditions.",
            "Magnesium produces no characteristic flame color in standard flame tests (distinguishing it from Ca²⁺).",
            "Can be confirmed with Titan Yellow or Magneson reagent forming a characteristic blue precipitate."
        ],
        swatch=WHITE,
        arabic_summary="يتكون راسب أبيض من هيدروكسيد المغنيسيوم لا يذوب في وفرة من NaOH، ولا يعطي لوناً مميزاً للهب."
    ),

    "NH4": ion(
        "NH₄⁺",
        "Ammonium — أيون الأمونيوم",
        "No precipitate with cold NaOH; upon gentle heating under approved procedures, pungent ammonia gas is liberated.",
        [
            "NH₄⁺ + OH⁻ → NH₃ ↑ + H₂O"
        ],
        notes=[
            "No precipitate forms with sodium hydroxide solution.",
            "Upon careful warming with dilute NaOH, ammonia gas (NH₃) is evolved.",
            "Ammonia gas turns damp red litmus paper blue and produces dense white fumes of NH₄Cl with concentrated HCl vapors.",
            "Safety: Never inhale gas directly. Perform test under proper laboratory ventilation."
        ],
        swatch=NONE,
        badge="Gas Evolution",
        arabic_summary="لا يتكون راسب؛ وبالتسخين اللطيف مع NaOH يتصاعد غاز النشادر ذو الرائحة النفاذة الذي يزرق ورقة عباد الشمس الحمراء."
    ),

    "CATION_INCONCLUSIVE": outcome(
        "Inconclusive Result",
        "نتيجة غير محددة",
        "The observed reactions do not match the documented 8 principal cations under this simplified educational scheme.",
        notes=[
            "Check reagents for contamination and confirm appropriate concentrations.",
            "If no precipitate was formed, consider testing for alkali metal cations (Na⁺, K⁺) via flame test:",
            "• Sodium (Na⁺): Characteristic golden-yellow persistent flame.",
            "• Potassium (K⁺): Characteristic lilac / pale violet flame (viewed through cobalt glass).",
            "Consult comprehensive qualitative analysis manuals (e.g. Vogel's Qualitative Inorganic Analysis) for further group separation."
        ],
        swatch=NONE,
        badge="Inconclusive"
    )
}

CATION_DECISION_TREE = {
    "start": question(
        "start",
        "What is the observed color of the precipitate after adding dilute NaOH to the unknown solution?",
        [
            option("Blue precipitate", "CU", swatch=BLUE, arabic_label="راسب أزرق"),
            option("Green precipitate", "FE2", swatch=GREEN, arabic_label="راسب أخضر"),
            option("Reddish-brown precipitate", "FE3", swatch=BROWN, arabic_label="راسب بني محمر"),
            option("White precipitate", "q_white_precipitate", swatch=WHITE, arabic_label="راسب أبيض"),
            option("No precipitate", "q_no_precipitate", swatch=NONE, arabic_label="لا يتكون راسب")
        ],
        hint="Add sodium hydroxide solution dropwise initially, observing any immediate precipitate formation and its color.",
        arabic_text="ما هو لون الراسب المتكون عند إضافة محلول هيدروكسيد الصوديوم (NaOH) قطرة قطرة؟",
        arabic_hint="أضف محلول هيدروكسيد الصوديوم تدريجياً وسجل لون الراسب الأولي المتكون بدقة."
    ),

    "q_white_precipitate": question(
        "q_white_precipitate",
        "Does the white precipitate dissolve when excess NaOH is added?",
        [
            option("Yes, dissolves in excess NaOH", "q_excess_ammonia", arabic_label="نعم، يذوب في وفرة من NaOH"),
            option("No, does not dissolve in excess NaOH", "q_flame_test", arabic_label="لا، لا يذوب في وفرة من NaOH")
        ],
        hint="Shake the tube thoroughly while adding excess concentrated NaOH to check if the hydroxide is amphoteric.",
        arabic_text="هل يذوب الراسب الأبيض عند إضافة وفرة من محلول هيدروكسيد الصوديوم مع الرج؟",
        arabic_hint="رج أنبوبة الاختبار جيداً عند إضافة الزيادة للتحقق من السلوك المتردد (Amphoteric)."
    ),

    "q_excess_ammonia": question(
        "q_excess_ammonia",
        "Test a fresh sample of the unknown solution with aqueous ammonia (NH₃(aq)) dropwise, then in excess. Does the precipitate dissolve in excess ammonia?",
        [
            option("Dissolves in excess ammonia", "ZN", arabic_label="يذوب في وفرة من محلول النشادر"),
            option("Does NOT dissolve in excess ammonia", "AL", arabic_label="لا يذوب في وفرة من محلول النشادر")
        ],
        hint="Zinc hydroxide forms soluble tetraammine complex [Zn(NH₃)₄]²⁺; aluminium hydroxide does not dissolve in aqueous ammonia.",
        arabic_text="اختبر عينة جديدة بإضافة محلول النشادر قطرة قطرة ثم في وفرة. هل يذوب الراسب في وفرة من النشادر؟",
        arabic_hint="هيدروكسيد الزنك يذوب لتكوين معقد النشادر الذائب، بينما هيدروكسيد الألومنيوم يظل راسباً."
    ),

    "q_flame_test": question(
        "q_flame_test",
        "Perform a clean platinum-wire flame test on the solid salt moistened with concentrated HCl. What flame color is observed?",
        [
            option("Brick-red (orange-red) flame", "CA", swatch=BRICK_RED, arabic_label="لهب أحمر طوبي (برتقالي-أحمر)"),
            option("No distinctive flame color", "MG", swatch=WHITE, arabic_label="لا يوجد لون مميز للهب")
        ],
        hint="Clean the platinum wire in conc. HCl until no flame color is imparted before dipping in the sample.",
        arabic_text="قم بإجراء كشف اللهب (كشف الجافة) باستخدام سلك بلاتيني نظيف وحمض HCl المركز. ما هو لون اللهب؟",
        arabic_hint="نظف السلك جيداً بالحمض حتى لا يظهر أي تلوث لوني قبل اختبار العينة."
    ),

    "q_no_precipitate": question(
        "q_no_precipitate",
        "Gently warm the mixture of the sample and NaOH solution in an approved fume hood. Is ammonia gas evolved?",
        [
            option("Ammonia gas liberated (turns damp red litmus paper blue)", "NH4", arabic_label="يتصاعد غاز النشادر (يزرق ورقة عباد الشمس)"),
            option("No gas evolved / No noticeable change", "CATION_INCONCLUSIVE", arabic_label="لا يتصاعد غاز / لا يحدث تغير")
        ],
        hint="Ammonia gas has a characteristic alkaline odor and turns damp red litmus blue. Never smell directly from the tube.",
        arabic_text="سخن الخليط بلطف تحت إشراف معملي في خزانة الغازات. هل يتصاعد غاز قلوي يزرق ورقة عباد الشمس الحمراء المبللة؟",
        arabic_hint="غاز النشادر قلوي التأثير. تجنب استنشاق الغاز مباشرة واعتمد على ورقة عباد الشمس."
    )
}


# 4. Anion Analysis Knowledge & Decision Tree
ANION_OUTCOMES = {
    "CO3": ion(
        "CO₃²⁻",
        "Carbonate — أيون الكربونات",
        "Effervescence with dilute acid; released CO₂ turns limewater cloudy.",
        [
            "CO₃²⁻ + 2H⁺ → CO₂ ↑ + H₂O",
            "CO₂ + Ca(OH)₂ → CaCO₃ ↓ + H₂O"
        ],
        notes=[
            "Addition of dilute HCl or H₂SO₄ causes vigorous effervescence of colorless, odorless carbon dioxide gas.",
            "Bubbling CO₂ through limewater Ca(OH)₂ produces a milky turbidity of insoluble calcium carbonate.",
            "Bicarbonate (HCO₃⁻) also releases CO₂; distinction can be made with MgSO₄ in the cold (forms precipitate immediately with CO₃²⁻, only upon boiling with HCO₃⁻)."
        ],
        swatch=WHITE,
        badge="Effervescence",
        arabic_summary="يحدث فوران مع تصاعد غاز ثاني أكسيد الكربون الذي يعكر ماء الجير الرائق."
    ),

    "S2": ion(
        "S²⁻",
        "Sulfide — أيون الكبريتيد",
        "Releases hydrogen sulfide (H₂S) gas upon acidification; black precipitate forms with lead(II) acetate paper.",
        [
            "S²⁻ + 2H⁺ → H₂S ↑",
            "H₂S + Pb(CH₃COO)₂ → PbS ↓ + 2CH₃COOH"
        ],
        notes=[
            "Acidification liberates hydrogen sulfide gas.",
            "Filter paper moistened with lead(II) acetate turns shiny black due to the formation of lead(II) sulfide (PbS).",
            "Safety Warning: Hydrogen sulfide is toxic and paralyzes the olfactory nerve. Detect only using chemical test paper under an approved fume hood."
        ],
        swatch="#1a1a1a",
        badge="Toxic Gas Hazard",
        arabic_summary="يتصاعد غاز كبريتيد الهيدروجين الذي يسود ورقة مبللة بمحلول أسيتات الرصاص لتكوين PbS الأسود."
    ),

    "SO3": ion(
        "SO₃²⁻",
        "Sulfite — أيون الكبريتيت",
        "Releases sulfur dioxide (SO₂) gas upon acidification; turns acidified potassium dichromate paper green.",
        [
            "SO₃²⁻ + 2H⁺ → SO₂ ↑ + H₂O",
            "3SO₂ + Cr₂O₇²⁻ + 2H⁺ → 2Cr³⁺ (green) + 3SO₄²⁻ + H₂O"
        ],
        notes=[
            "Acidification with dilute acid yields choking sulfur dioxide gas (SO₂).",
            "SO₂ is a strong reducing agent; it reduces orange acidified potassium dichromate (K₂Cr₂O₇) to green chromium(III) sulfate.",
            "Safety Warning: SO₂ gas is an irritating respiratory hazard. Handle exclusively under laboratory fume hoods."
        ],
        swatch=GREEN,
        badge="Reducing Gas",
        arabic_summary="يتصاعد غاز ثاني أكسيد الكبريت الخانق الذي يخضر ورقة مبللة بمحلول ثاني كرومات البوتاسيوم المحمضة."
    ),

    "SO4": ion(
        "SO₄²⁻",
        "Sulfate — أيون الكبريتات",
        "Heavy white precipitate forms with BaCl₂; completely insoluble in dilute hydrochloric acid.",
        [
            "Ba²⁺ + SO₄²⁻ → BaSO₄ ↓"
        ],
        notes=[
            "Barium chloride solution yields a dense white precipitate of barium sulfate (BaSO₄).",
            "Crucial verification: BaSO₄ is completely insoluble in dilute HCl or HNO₃ (distinguishing it from BaCO₃ and BaSO₃).",
            "Barium salts are toxic; handle with appropriate laboratory care."
        ],
        swatch=WHITE,
        arabic_summary="يتكون راسب أبيض كثيف من كبريتات الباريوم لا يذوب في حمض الهيدروكلوريك المخفف."
    ),

    "CL": ion(
        "Cl⁻",
        "Chloride — أيون الكلوريد",
        "White curdy precipitate forms with AgNO₃; dissolves readily in dilute aqueous ammonia.",
        [
            "Ag⁺ + Cl⁻ → AgCl ↓",
            "AgCl + 2NH₃ → [Ag(NH₃)₂]⁺ + Cl⁻"
        ],
        notes=[
            "Silver nitrate solution yields a white curdy precipitate of silver chloride (AgCl).",
            "The precipitate turns grey/purple when exposed to sunlight due to photodecomposition.",
            "Dissolves readily in dilute aqueous ammonia solution forming the diamminesilver(I) complex."
        ],
        swatch=WHITE,
        arabic_summary="يتكون راسب أبيض متجبن من كلوريد الفضة يذوب بسهولة في محلول النشادر المخفف."
    ),

    "BR": ion(
        "Br⁻",
        "Bromide — أيون البروميد",
        "Cream / pale-yellow precipitate forms with AgNO₃; sparingly soluble in dilute ammonia, dissolves in concentrated ammonia.",
        [
            "Ag⁺ + Br⁻ → AgBr ↓",
            "AgBr + 2NH₃ (conc.) → [Ag(NH₃)₂]⁺ + Br⁻"
        ],
        notes=[
            "Silver nitrate solution produces a pale yellow / cream precipitate of silver bromide (AgBr).",
            "It is sparingly soluble in dilute ammonia solution, but dissolves in concentrated ammonia.",
            "Chlorine water test: Adding chlorine water + organic solvent (CCl₄ / CH₂Cl₂) liberates reddish-brown bromine dissolved in the organic layer."
        ],
        swatch=PALE_YELLOW,
        arabic_summary="يتكون راسب أبيض مصفر (كريمي) من بروميد الفضة يذوب بصعوبة في النشادر المخفف ويذوب في المركز."
    ),

    "IODIDE": ion(
        "I⁻",
        "Iodide — أيون اليوديد",
        "Bright yellow precipitate forms with AgNO₃; completely insoluble in aqueous ammonia.",
        [
            "Ag⁺ + I⁻ → AgI ↓"
        ],
        notes=[
            "Silver nitrate solution forms a canary yellow precipitate of silver iodide (AgI).",
            "The precipitate is completely insoluble in both dilute and concentrated aqueous ammonia.",
            "Chlorine water test: Liberates violet iodine, which imparts a deep violet color to an organic extraction layer or turns starch solution intense dark blue."
        ],
        swatch=YELLOW,
        arabic_summary="يتكون راسب أصفر فاقع من يوديد الفضة لا يذوب في محلول النشادر سواء كان مخففاً أو مركزاً."
    ),

    "NO3_CHECK": outcome(
        "Nitrate Identification Protocol",
        "NO₃⁻ — بروتوكول الكشف عن أيون النترات",
        "Nitrate does not precipitate with BaCl₂ or AgNO₃. Identification requires the Brown Ring Test or Devarda's Alloy reduction.",
        equations=[
            "NO₃⁻ + 3Fe²⁺ + 4H⁺ → NO + 3Fe³⁺ + 2H₂O",
            "[Fe(H₂O)₆]²⁺ + NO → [Fe(H₂O)₅(NO)]²⁺ (brown ring) + H₂O"
        ],
        notes=[
            "Brown Ring Test: Mix sample with freshly prepared iron(II) sulfate (FeSO₄). Incline test tube and carefully run concentrated H₂SO₄ down the side.",
            "A characteristic brown ring forms at the junction of the two liquid layers: pentaaquanitrosyliron(II) complex.",
            "Devarda's Alloy Alternative: Heating nitrate solution with Devarda's alloy (Cu/Al/Zn) and NaOH releases ammonia gas.",
            "Safety Warning: Concentrated sulfuric acid is highly corrosive and generates intense heat on contact with aqueous solutions. Must only be executed by trained personnel in an approved lab."
        ],
        swatch=BROWN,
        badge="Specialized Test",
        arabic_summary="أملاح النترات قابلة للذوبان ولا تعطي رواسب مع BaCl₂ أو AgNO₃. يتم التأكيد بواسطة اختبار الحلقة البنية أو سبيكة ديفاردا."
    ),

    "ANION_INCONCLUSIVE": outcome(
        "Inconclusive Anion Result",
        "نتيجة أنيون غير محددة",
        "The observations do not match the documented common anions under this educational diagnostic sequence.",
        notes=[
            "Ensure the initial solution was properly prepared (neutral or weakly acidic) before testing with BaCl₂ and AgNO₃.",
            "If no precipitates or gases were observed, perform the specific Brown Ring Test for Nitrate (NO₃⁻).",
            "Other anions (phosphate PO₄³⁻, nitrite NO₂⁻, thiosulfate S₂O₃²⁻) require further systematic group testing."
        ],
        swatch=NONE,
        badge="Inconclusive"
    )
}

ANION_DECISION_TREE = {
    "start": question(
        "start",
        "What is observed upon adding dilute hydrochloric acid (HCl) or sulfuric acid (H₂SO₄) to the solid salt or test solution?",
        [
            option("Effervescence; gas turns limewater cloudy", "CO3", swatch=WHITE, arabic_label="فوران وغاز يعكر ماء الجير"),
            option("Gas released; turns lead acetate paper black", "S2", swatch="#1a1a1a", arabic_label="غاز يسود ورقة أسيتات الرصاص"),
            option("Pungent gas; turns acidified dichromate green", "SO3", swatch=GREEN, arabic_label="غاز يخضر ورقة ثاني كرومات البوتاسيوم"),
            option("No visible gas evolution / No effervescence", "q_barium_test", swatch=NONE, arabic_label="لا يتصاعد غاز / لا يحدث فوران")
        ],
        hint="Preliminary acid test identifies anions that decompose with acid to liberate volatile gases (CO₃²⁻, S²⁻, SO₃²⁻).",
        arabic_text="ماذا تلاحظ عند إضافة حمض الهيدروكلوريك المخفف (HCl) إلى الملح الصلب أو المحلول؟",
        arabic_hint="اختبار الحمض المخفف يكشف عن الأنيونات التي تتفكك بالحمض متصاعدة كغازات (كربونات، كبريتيد، كبريتيت)."
    ),

    "q_barium_test": question(
        "q_barium_test",
        "To a fresh neutral or slightly acidified solution of the salt, add Barium Chloride solution (BaCl₂). What occurs?",
        [
            option("White precipitate insoluble in dilute HCl", "SO4", swatch=WHITE, arabic_label="راسب أبيض لا يذوب في حمض HCl المخفف"),
            option("No precipitate formed", "q_silver_test", swatch=NONE, arabic_label="لا يتكون راسب")
        ],
        hint="Barium sulfate is an extremely insoluble white precipitate that does not dissolve upon addition of dilute hydrochloric acid.",
        arabic_text="أضف محلول كلوريد الباريوم (BaCl₂) إلى عينة جديدة من محلول الملح. ماذا تلاحظ؟",
        arabic_hint="راسب كبريتات الباريوم أبيض كثيف ومميز بعدم ذوبانه في الأحماض المخففة."
    ),

    "q_silver_test": question(
        "q_silver_test",
        "To a fresh solution acidified with dilute nitric acid (HNO₃), add Silver Nitrate solution (AgNO₃). What precipitate forms?",
        [
            option("White precipitate (soluble in dilute NH₃)", "CL", swatch=WHITE, arabic_label="راسب أبيض (يذوب في النشادر المخفف)"),
            option("Cream / pale-yellow precipitate (sparingly soluble in NH₃)", "BR", swatch=PALE_YELLOW, arabic_label="راسب كريمي/أبيض مصفر (يذوب بصعوبة)"),
            option("Canary yellow precipitate (insoluble in NH₃)", "IODIDE", swatch=YELLOW, arabic_label="راسب أصفر فاقع (لا يذوب في النشادر)"),
            option("No precipitate formed", "q_nitrate_query", swatch=NONE, arabic_label="لا يتكون أي راسب")
        ],
        hint="Silver halides (AgCl, AgBr, AgI) exhibit progressive color gradation and decreasing solubility in aqueous ammonia.",
        arabic_text="حمض عينة جديدة بحمض النيتريك المخفف ثم أضف محلول نترات الفضة (AgNO₃). ما هو لون الراسب؟",
        arabic_hint="هاليدات الفضة تتميز بتدرج لوني واضح وسلوك ذوبانية محدد في محلول هيدروكسيد الأمونيوم."
    ),

    "q_nitrate_query": question(
        "q_nitrate_query",
        "Since neither BaCl₂ nor AgNO₃ yielded a precipitate, would you like to view the validated procedure for testing Nitrate (NO₃⁻)?",
        [
            option("View Nitrate (NO₃⁻) Brown Ring Test protocol", "NO3_CHECK", arabic_label="عرض بروتوكول اختبار حلقة النترات البنية"),
            option("Report sample as Inconclusive", "ANION_INCONCLUSIVE", arabic_label="تسجيل النتيجة كعينة غير محددة")
        ],
        hint="Nitrate salts are water-soluble and require specialized confirmatory reduction or coordination chemistry tests.",
        arabic_text="نظراً لعدم تكون رواسب مع كلوريد الباريوم أو نترات الفضة، هل ترغب في الاطلاع على بروتوكول اختبار النترات؟",
        arabic_hint="أملاح النترات تذوب في الماء ولا تعطي رواسب، وتتطلب اختبار الحلقة البنية للتأكيد."
    )
}

# Extended Outcomes for 50 Reactions System
EXTENDED_OUTCOMES = {
    "PB": ion(
        "Pb²⁺",
        "Lead(II) — أيون الرصاص الثنائي",
        "White precipitate with HCl soluble in hot water, recrystallizes on cooling; white precipitate with NaOH soluble in excess.",
        [
            "Pb²⁺ + 2Cl⁻ → PbCl₂ ↓",
            "Pb²⁺ + 2OH⁻ → Pb(OH)₂ ↓",
            "Pb(OH)₂ + 2OH⁻ → [Pb(OH)₄]²⁻"
        ],
        notes=[
            "PbCl₂ dissolves in boiling water and separates as glistening needles on cooling.",
            "Forms yellow precipitate of PbI₂ with KI."
        ],
        swatch=WHITE,
        arabic_summary="راسب أبيض من كلوريد الرصاص يذوب في الماء الساخن ويعود للترسب بالتبريد، ويذوب هيدروكسيده في الزيادة من NaOH."
    ),

    "MN": ion(
        "Mn²⁺",
        "Manganese(II) — أيون المنجنيز الثنائي",
        "White precipitate with NaOH rapidly turning brown due to oxidation in air.",
        [
            "Mn²⁺ + 2OH⁻ → Mn(OH)₂ ↓",
            "2Mn(OH)₂ + O₂ → 2MnO(OH)₂ ↓ + H₂O"
        ],
        notes=[
            "White manganese(II) hydroxide oxidizes rapidly on exposure to atmospheric oxygen to form brown hydrated manganese dioxide."
        ],
        swatch="#d2b48c",
        arabic_summary="يتكون راسب أبيض يتأكسد بسرعة عند ملامسة الهواء ويتحول إلى اللون البني."
    ),

    "AG": ion(
        "Ag⁺",
        "Silver(I) — أيون الفضة",
        "White curdy precipitate with HCl, soluble in dilute ammonia; darkens in sunlight.",
        [
            "Ag⁺ + Cl⁻ → AgCl ↓",
            "AgCl + 2NH₃ → [Ag(NH₃)₂]⁺ + Cl⁻"
        ],
        notes=[
            "Silver chloride dissolves completely in dilute aqueous ammonia solution."
        ],
        swatch=WHITE,
        arabic_summary="راسب أبيض متجبن من كلوريد الفضة يذوب بسهولة وسرعة في النشادر المخفف."
    ),

    "HG2": ion(
        "Hg₂²⁺",
        "Mercury(I) — أيون الزئبقوز",
        "White precipitate with HCl that turns black upon adding aqueous ammonia.",
        [
            "Hg₂²⁺ + 2Cl⁻ → Hg₂Cl₂ ↓",
            "Hg₂Cl₂ + 2NH₃ → HgNH₂Cl + Hg ↓ + NH₄⁺ + Cl⁻"
        ],
        notes=[
            "The blackening upon adding ammonia is due to disproportionation yielding finely divided black metallic mercury."
        ],
        swatch=WHITE,
        arabic_summary="راسب أبيض يسود فور إضافة محلول النشادر بسبب ترسب الزئبق الفلزي الأسود."
    ),

    "HCO3": ion(
        "HCO₃⁻",
        "Bicarbonate — أيون البيكربونات",
        "Effervescence with dilute HCl releasing CO₂; does NOT precipitate with MgSO₄ in the cold, but forms white precipitate upon boiling.",
        [
            "HCO₃⁻ + H⁺ → CO₂ ↑ + H₂O",
            "Mg(HCO₃)₂ —(Δ)→ MgCO₃ ↓ + CO₂ ↑ + H₂O"
        ],
        notes=[
            "Crucial distinction from CO₃²⁻: Bicarbonates do not form precipitate with MgSO₄ in the cold, only after boiling."
        ],
        swatch=WHITE,
        arabic_summary="فوران سريع بتصاعد غاز CO₂، ويميز عن الكربونات بعدم تكوين راسب مع MgSO₄ على البارد وتكوينه بالغليان فقط."
    ),

    "S2O3": ion(
        "S₂O₃²⁻",
        "Thiosulfate — أيون الثيوكبريتات",
        "Acidification releases pungent SO₂ gas accompanied by a progressive yellow turbidity of sulfur.",
        [
            "S₂O₃²⁻ + 2H⁺ → SO₂ ↑ + S ↓ + H₂O"
        ],
        notes=[
            "Characteristic colloidal yellow sulfur precipitates out over time.",
            "Decolorizes iodine solution immediately."
        ],
        swatch="#fde047",
        arabic_summary="تصاعد غاز SO₂ الخانق مصحوباً بظهور تعكر كبريتي أصفر معلق تدريجياً في الأنبوبة."
    ),

    "NO2": ion(
        "NO₂⁻",
        "Nitrite — أيون النتريت",
        "Acidification yields brown NO₂ fumes at the mouth of the tube; dark brown solution with cold FeSO₄.",
        [
            "NO₂⁻ + H⁺ → HNO₂",
            "3HNO₂ → HNO₃ + 2NO ↑ + H₂O",
            "2NO + O₂ → 2NO₂ ↑"
        ],
        notes=[
            "Colorless NO oxidizes to reddish-brown NO₂ on contact with atmospheric oxygen at the test tube mouth."
        ],
        swatch="#b45309",
        arabic_summary="تصاعد غاز عديم اللون يتحول لأبخرة بنية حمراء عند فوهة الأنبوبة، ويعطي لوناً بنياً مع FeSO₄ على البارد."
    ),

    "PO4": ion(
        "PO₄³⁻",
        "Phosphate — أيون الفوسفات",
        "White precipitate with BaCl₂ soluble in dilute HCl; bright yellow precipitate with ammonium molybdate or AgNO₃.",
        [
            "3Ba²⁺ + 2PO₄³⁻ → Ba₃(PO₄)₂ ↓",
            "3Ag⁺ + PO₄³⁻ → Ag₃PO₄ ↓"
        ],
        notes=[
            "Silver phosphate is yellow, soluble in dilute HNO₃ and aqueous ammonia.",
            "Forms canary-yellow ammonium phosphomolybdate precipitate with molybdate reagent."
        ],
        swatch="#facc15",
        arabic_summary="راسب أصفر مع نترات الفضة يذوب في الأحماض والنشادر، ويعطي راسباً أصفر كنارياً مع موليبدات الأمونيوم."
    ),

    "CRO4": ion(
        "CrO₄²⁻",
        "Chromate — أيون الكرومات",
        "Yellow solution; forms reddish-brown / brick-red precipitate with AgNO₃, yellow precipitate with BaCl₂.",
        [
            "2Ag⁺ + CrO₄²⁻ → Ag₂CrO₄ ↓",
            "Ba²⁺ + CrO₄²⁻ → BaCrO₄ ↓"
        ],
        notes=[
            "Silver chromate is brick-red / reddish-brown.",
            "Yellow color in alkaline solution shifts to orange dichromate upon acidification."
        ],
        swatch="#c84630",
        arabic_summary="محلول أصفر يعطي راسباً أحمر طوبياً / بنياً محمراً مع نترات الفضة، وراسباً أصفر مع كلوريد الباريوم."
    ),

    "CH3COO": ion(
        "CH₃COO⁻",
        "Acetate — أيون الأسيتات",
        "Releases vinegar odor of acetic acid on warming with dilute H₂SO₄; blood-red coloration with neutral FeCl₃.",
        [
            "CH₃COO⁻ + H⁺ → CH₃COOH",
            "3CH₃COO⁻ + Fe³⁺ + 2H₂O → [Fe₃(OH)₂(CH₃COO)₆]⁺ + 2H⁺"
        ],
        notes=[
            "Reaction with neutral iron(III) chloride gives an intense blood-red color which precipitates as basic iron acetate upon boiling."
        ],
        swatch="#991b1b",
        arabic_summary="رائحة الخل المميزة مع الأحماض، ولون أحمر دامي كثيف مع كلوريد الحديد الثلاثي المتعادل."
    ),

    "UNKNOWN_INCONCLUSIVE": outcome(
        "Inconclusive Sample Analysis",
        "عينة غير محددة",
        "The recorded observations do not uniquely correspond to one of the 28 principal ions in this qualitative diagnostic scheme.",
        notes=[
            "Ensure that reagents are freshly prepared and standard lab concentrations are maintained.",
            "Confirm whether sample contains mixed salts or complex interfering ions.",
            "Consider systematic separation groups (Group I to Group VI) following Vogel's Qualitative Inorganic Analysis."
        ],
        swatch=NONE,
        badge="Inconclusive"
    )
}

from organic_kb import (
    ORGANIC_OUTCOMES,
    ORGANIC_CONFIRMATORY_TESTS,
    ORGANIC_DECISION_TREE
)

from salt_kb import (
    ANIONS_DATA,
    CATIONS_DATA,
    SALT_DIAGNOSIS_NODES,
    SALTS_DATABASE,
    INCOMPATIBLE_SALTS,
    ION_VALENCES,
    SUBSCRIPTS,
    format_ion_part,
    auto_balance_formula,
    build_final_salt_outcome,
    check_salt_solubility,
    generate_synthesis_recipe,
    get_direct_salt_dossier
)

ALL_OUTCOMES = {
    **CATION_OUTCOMES,
    **ANION_OUTCOMES,
    **EXTENDED_OUTCOMES,
    **ORGANIC_OUTCOMES
}

# Apply extended notes for complete bilingual support
for _key, _dict in {'PB': {'notes_ar': ['يذوب كلوريد الرصاص الثنائي (PbCl₂) في الماء المغلي وينفصل كإبر لامعة براقة عند التبريد.', 'يعطي راسباً أصفر ساطعاً من يوديد الرصاص (PbI₂) مع يوديد البوتاسيوم (اختبار المطر الذهبي).'], 'notes_en': ['PbCl₂ dissolves in boiling water and separates as glistening needles on cooling.', 'Forms a brilliant yellow precipitate of PbI₂ with KI (Golden Rain test).']}, 'MN': {'notes_ar': ['هيدروكسيد المنغنيز الثنائي الأبيض يتأكسد سريعاً عند تعرضه لأكسجين الهواء الجوي ليتكون ثاني أكسيد المنغنيز المائي البني.', 'يؤكد باختبار فوق البزموتات أو فوق الكبريتات في وسط حمضي ليعطي لون البرمنجنات البنفسجي المميز.'], 'notes_en': ['White manganese(II) hydroxide oxidizes rapidly on exposure to atmospheric oxygen to form brown hydrated manganese dioxide.', 'Confirmed by bismuthate or persulfate oxidation in acidic medium, yielding the characteristic purple permanganate coloration.']}, 'AG': {'notes_ar': ['راسب كلوريد الفضة الأبيض (AgCl) يذوب تماماً وبسهولة في محلول النشادر المائي المخفف بفعل تكوين معقد ثنائي أمين الفضة.', 'يتحول لون راسب AgCl إلى اللون البنفسجي ثم الرمادي القاتم عند تعرضه لضوء الشمس المباشر.'], 'notes_en': ['Silver chloride (AgCl) white precipitate dissolves completely in dilute aqueous ammonia solution forming diamminesilver(I) complex.', 'AgCl precipitate turns violet then grayish-black upon prolonged exposure to sunlight.']}, 'HG2': {'notes_ar': ['اسوداد راسب كلوريد الزئبقوز عند إضافة محلول النشادر يرجع إلى تفاعل التفكك الذاتي (Disproportionation) الذي ينتج الزئبق الفلزي الأسود الدقيق.', 'أملاح الزئبق شديدة السمية معملياً ويجب التخلص منها بحذر فائق.'], 'notes_en': ['The blackening upon adding ammonia is due to disproportionation yielding finely divided black metallic mercury.', 'Mercury compounds are highly toxic and require strict hazardous waste management.']}, 'HCO3': {'notes_ar': ['التمييز الجوهري عن الكربونات: البيكربونات لا تعطي راسباً مع كبريتات المغنيسيوم على البارد، ولكن يتكون راسب أبيض بعد الغليان فقط.', 'محلول البيكربونات المائي متعادل تقريباً أو ضعيف القلوية تجاه الفينولفثالين.'], 'notes_en': ['Crucial distinction from CO₃²⁻: Bicarbonates do not form precipitate with MgSO₄ in the cold, only after boiling.', 'Aqueous bicarbonate solutions are weakly alkaline and do not color phenolphthalein.']}, 'S2O3': {'notes_ar': ['يتصاعد غاز SO₂ مع ترسب كبريت أصفر غروي معلق بمرور الوقت في المحلول الحمضي.', 'يزيل لون محلول اليود البني فورياً مع تكوين رباعي ثيونات الصوديوم عديم اللون.'], 'notes_en': ['Characteristic colloidal yellow sulfur precipitates out over time with SO₂ gas in acidic medium.', 'Decolorizes brown iodine solution immediately via oxidation to tetrathionate.']}, 'NO2': {'notes_ar': ['يتصاعد غاز أكسيد النيتريك (NO) عديم اللون والذي يتأكسد عند فوهة الأنبوبة إلى أبخرة بنية حمراء من NO₂.', 'يزيل لون برمنجنات البوتاسيوم البنفسجية المحمضة، ويعطي راسباً أسود أو حلقة بنية مميزة مع كبريتات الحديد الثنائي.'], 'notes_en': ['Colorless NO oxidizes to reddish-brown NO₂ on contact with atmospheric oxygen at the test tube mouth.', 'Decolorizes acidified potassium permanganate and gives brown ring / black coloration with FeSO₄.']}, 'PO4': {'notes_ar': ['راسب فوسفات الفضة أصفر اللون، يذوب في حمض النيتريك المخفف وفي محلول النشادر المائي.', 'يعطي راسباً أصفر كنارياً بلورياً من فوسفوموليبدات الأمونيوم مع كاشف موليبدات الأمونيوم في وسط حمضي نيتريكي ساخن.'], 'notes_en': ['Silver phosphate is yellow, soluble in dilute HNO₃ and aqueous ammonia.', 'Forms canary-yellow ammonium phosphomolybdate precipitate with molybdate reagent in hot nitric acid medium.']}, 'CRO4': {'notes_ar': ['راسب كرومات الفضة ذو لون أحمر طوبي / بني محمر، بينما كرومات الباريوم راسب أصفر.', 'اللون الأصفر لمحلول الكرومات في الوسط القاعدي يتحول إلى اللون البرتقالي لثنائي الكرومات عند التحميض بحمض مخفف.'], 'notes_en': ['Silver chromate is brick-red / reddish-brown, while barium chromate forms a bright yellow precipitate.', 'Yellow color in alkaline solution shifts to orange dichromate upon acidification with dilute acid.']}, 'CH3COO': {'notes_ar': ['التفاعل مع محلول كلوريد الحديد الثلاثي المتعادل يعطي لوناً أحمر دامياً مكثفاً يرسب كأسيتات الحديد القاعدية بالتسخين للغليان.', 'تفاعل الأسترة بالتسخين مع الكحول الإيثيلي وحمض الكبريتيك المركز يطلق رائحة إستر أسيتات الإيثيل الذكية المميزة.'], 'notes_en': ['Reaction with neutral iron(III) chloride gives an intense blood-red color which precipitates as basic iron acetate upon boiling.', 'Esterification by heating with ethanol and conc. H₂SO₄ yields the pleasant fruity fragrance of ethyl acetate.']}, 'UNKNOWN_INCONCLUSIVE': {'notes_ar': ['تأكد من استخدام كواشف معملية طازجة التحضير ومن ضبط التركيزات القياسية بدقة.', 'تحقق مما إذا كانت العينة تحتوي على خليط أملاح أو أيونات متداخلة تحجب التفاعلات النموذجية.', 'يُنصح بإجراء الفصل المجموعي المنهجي المعتمد (من المجموعة الأولى إلى السادسة) وفقاً لمرجع فوجل للتحليل غير العضوي.'], 'notes_en': ['Ensure that reagents are freshly prepared and standard lab concentrations are maintained.', 'Confirm whether sample contains mixed salts or complex interfering ions.', "Consider systematic separation groups (Group I to Group VI) following Vogel's Qualitative Inorganic Analysis."]}, 'ORG_SUCROSE': {'notes_ar': ['سكر ثنائي صلب بلوري أبيض يذوب في الماء بسهولة، يتفحم برائحة السكر المحروق وتفاعل موليش إيجابي بحلقة بنفسجية.', 'سكر غير مختزل مباشرة (سلبي تماماً مع فهلنج وبارفويد)؛ وعند غليه مع قطرات من HCl المركز ثم معادلته بهيدروكسيد الصوديوم يتحلل مائياً ويختزل فهلنج فورياً.'], 'notes_en': ['White crystalline disaccharide solid readily soluble in water; chars with burnt sugar odor; Molisch test is positive yielding a violet ring.', "Directly non-reducing (strictly negative with Fehling's and Barfoed's); upon boiling with dilute HCl and neutralizing with NaOH, it hydrolyzes and immediately reduces Fehling's reagent."]}}.items():
    if _key in EXTENDED_OUTCOMES:
        EXTENDED_OUTCOMES[_key].update(_dict)
    if _key in ORGANIC_OUTCOMES:
        ORGANIC_OUTCOMES[_key].update(_dict)
    if _key in ALL_OUTCOMES:
        ALL_OUTCOMES[_key].update(_dict)


UNIFIED_DECISION_TREE = {
    "start_mode": question(
        "start_mode",
        "Step 1: Select the analytical pathway for the unknown sample (Organic or Inorganic):",
        [
            option("Complete Inorganic Salt Diagnosis (30 Salts)", "SALT_START", swatch=WHITE, arabic_label="تشخيص ملح غير عضوي كامل"),
            option("Single Inorganic Ion Analysis (Cations & Anions)", "start_color", swatch=BLUE, arabic_label="كشف غير عضوي (أيونات)"),
            option("Organic Chemical Analysis (25 Compounds)", "org_q_state", swatch=GREEN, arabic_label="كشف عضوي"),
            option("Direct Salt Explorer & Synthesis Recipe Planner", "EXPLORER_MODE_DIRECT", swatch=BLUE, arabic_label="مستكشف وتحضير الأملاح")
        ],
        hint="اختر 'تشخيص ملح غير عضوي كامل' للكشف عن الملح بشقيه، أو كشف الأيونات، أو المركبات العضوية، أو مستكشف وتحضير الأملاح لتوليد الوصفة مباشرة، أو فحص اللهب.",
        arabic_text="المرحلة 1: حدد مسار الفحص التحليلي للعينة المجهولة",
        arabic_hint="اختر 'تشخيص ملح غير عضوي كامل' للكشف عن الملح بشقيه الحامضي والقاعدي واكتشاف الـ 30 ملحاً المرجعية، أو اختر كشف الأيونات المنفردة أو المركبات العضوية أو مستكشف وتحضير الأملاح."
    ),

    "unified_q_charring_heat": question(
        "unified_q_charring_heat",
        "Heat a small quantity of the sample directly in a dry test tube or on a flame. What do you observe?",
        [
            option("انصهار وتفحم وتصاعد أدخنة أو رائحة سكر محروق (مركب عضوي)", "org_q_state", arabic_label="انصهار وتفحم / رائحة سكر محروق (عضوي)"),
            option("لا تفحم، بقاء راسب معدني ثابت مع تغير اللون أثناء التسخين أو أبخرة غير متفحمة (مركب غير عضوي)", "start_color", arabic_label="لا تفحم / بقاء مادة معدنية ثابتة (غير عضوي)")
        ],
        hint="المركبات العضوية تحترق أو تتفحم برائحة مميزة (مثل السكر المحروق أو لهب مدخن)، بينما الأملاح غير العضوية لا تتفحم وتبقى كتلة معدنية صلبة ثابتة.",
        arabic_text="فحص الفصل الأولي: سخّن كمية صغيرة جداً من العينة على لهب مباشر أو في أنبوبة جافة. ماذا تلاحظ؟"
    ),

    "start_color": question(
        "start_color",
        "ما لون المادة أو المحلول أمامك؟",
        [
            option("أبيض", "q_physical_state", swatch=WHITE, arabic_label="أبيض"),
            option("عديم اللون", "q_physical_state", swatch=NONE, arabic_label="عديم اللون"),
            option("أزرق", "q_physical_state", swatch=BLUE, arabic_label="أزرق"),
            option("أخضر", "q_physical_state", swatch=GREEN, arabic_label="أخضر"),
            option("أصفر", "q_physical_state", swatch=YELLOW, arabic_label="أصفر"),
            option("بني", "q_physical_state", swatch=BROWN, arabic_label="بني"),
            option("وردي", "q_physical_state", swatch="#ec4899", arabic_label="وردي"),
            option("أسود", "q_physical_state", swatch="#1a1a1a", arabic_label="أسود"),
            option("برتقالي", "q_physical_state", swatch="#f97316", arabic_label="برتقالي"),
            option("غير محدد", "q_physical_state", swatch=NONE, arabic_label="غير محدد")
        ],
        hint="سجل اللون الأولي للعينة الصلبة أو المحلول المائي بدقة، حيث يوفر مؤشراً مبدئياً مهماً.",
        arabic_text="المرحلة 1: ما لون المادة أو المحلول أمامك؟"
    ),

    "q_physical_state": question(
        "q_physical_state",
        "هل العينة صلبة أم محلول؟",
        [
            option("محلول مائي (Solution)", "q_first_reagent", arabic_label="محلول مائي"),
            option("مادة صلبة (Solid)", "q_first_reagent", arabic_label="مادة صلبة")
        ],
        hint="إذا كانت العينة صلبة، ستحتاج إلى إذابة جزء منها في ماء مقطر لتحضير محلول الفحص.",
        arabic_text="المرحلة 1: هل العينة صلبة أم محلول؟"
    ),

    "q_first_reagent": question(
        "q_first_reagent",
        "أضف حمض الهيدروكلوريك المخفف (HCl) قطرة قطرة إلى العينة — [الملاحظة المباشرة]. ماذا تلاحظ؟",
        [
            option("فوران وتصاعد غاز", "q_gas_observation", arabic_label="فوران وتصاعد غاز"),
            option("راسب أبيض", "q_hcl_white_precipitate", swatch=WHITE, arabic_label="راسب أبيض"),
            option("لا تغيير / لا يتكون راسب أو غاز", "q_naoh_addition", swatch=NONE, arabic_label="لا تغيير / لا يتكون راسب أو غاز"),
            option("تغير لون المحلول", "q_naoh_addition", arabic_label="تغير لون المحلول"),
            option("أخرى", "q_naoh_addition", arabic_label="أخرى")
        ],
        hint="حمض الهيدروكلوريك المخفف هو الكاشف الاستدلالي الأول؛ يكشف عن الأنيونات المتطايرة ويرسب كاتيونات المجموعة الأولى (Ag⁺, Pb²⁺, Hg₂²⁺).",
        arabic_text="المرحلة 2: أضف حمض الهيدروكلوريك المخفف (HCl) قطرة قطرة إلى العينة. ماذا تلاحظ؟"
    ),

    "q_gas_observation": question(
        "q_gas_observation",
        "هل يتصاعد غاز؟ وما لونه أو رائحته؟",
        [
            option("غاز عديم اللون يعكر ماء الجير الرائق لفترة وجيزة", "CO3", swatch=WHITE, arabic_label="غاز عديم اللون يعكر ماء الجير (CO₂)"),
            option("فوران سريع ولحظي بتصاعد غاز CO₂ (لا يرسب MgSO₄ على البارد)", "HCO3", swatch=WHITE, arabic_label="فوران سريع ولحظي (HCO₃⁻)"),
            option("رائحة بيض فاسد يسود ورقة مبللة بأسيتات الرصاص", "S2", swatch="#1a1a1a", arabic_label="رائحة بيض فاسد يسود أسيتات الرصاص (H₂S)"),
            option("رائحة نفاذة خانقة تخضر ورقة مبللة بثاني كرومات البوتاسيوم", "SO3", swatch=GREEN, arabic_label="رائحة خانقة تخضر ثاني كرومات البوتاسيوم (SO₂)"),
            option("تصاعد غاز SO₂ مع ظهور تعكر كبريتي أصفر معلق", "S2O3", swatch="#fde047", arabic_label="تعكر كبريتي أصفر مع غاز SO₂ (ثيوكبريتات)"),
            option("أبخرة بنية حمراء عند فوهة الأنبوبة", "NO2", swatch="#b45309", arabic_label="أبخرة بنية حمراء عند فوهة الأنبوبة (NO₂)"),
            option("لا غاز / أخرى", "q_naoh_addition", swatch=NONE, arabic_label="لا غاز / أخرى")
        ],
        hint="غاز CO₂ يعكر ماء الجير، H₂S له رائحة مميزة ويسود أسيتات الرصاص، SO₂ يخضر ثاني كرومات البوتاسيوم.",
        arabic_text="المرحلة 3: هل يتصاعد غاز؟ وما لونه أو رائحته؟"
    ),

    "q_hcl_white_precipitate": question(
        "q_hcl_white_precipitate",
        "هل يذوب الراسب في الماء الساخن؟",
        [
            option("نعم (يذوب بالماء الساخن المغلي ويعود للترسيب بالتبريد)", "PB", swatch=WHITE, arabic_label="نعم (يذوب بالماء الساخن)"),
            option("لا يذوب في الماء الساخن، ولكن يذوب في محلول النشادر المخفف", "AG", swatch=WHITE, arabic_label="لا (يذوب في النشادر المخفف)"),
            option("لا يذوب في الماء الساخن، ويسود الراسب عند إضافة محلول النشادر", "HG2", swatch=WHITE, arabic_label="لا (ويسود بمحلول النشادر)")
        ],
        hint="كلوريد الرصاص PbCl₂ يذوب في الماء الساخن، وكلوريد الفضة AgCl يذوب في النشادر المخفف.",
        arabic_text="المرحلة 3: هل يذوب الراسب في الماء الساخن؟"
    ),

    "q_naoh_addition": question(
        "q_naoh_addition",
        "أضف هيدروكسيد الصوديوم (NaOH) قطرة قطرة إلى عينة جديدة مع الرج. ماذا تلاحظ؟",
        [
            option("راسب أزرق", "q_cu_ammonia", swatch=BLUE, arabic_label="راسب أزرق"),
            option("راسب أخضر", "q_fe2_air", swatch=GREEN, arabic_label="راسب أخضر"),
            option("راسب بني محمر جيلاتيني", "FE3", swatch=BROWN, arabic_label="راسب بني محمر"),
            option("راسب أبيض", "q_naoh_excess", swatch=WHITE, arabic_label="راسب أبيض"),
            option("راسب أبيض يتأكسد ويتحول إلى بني بالهواء", "MN", swatch="#d2b48c", arabic_label="راسب أبيض يتحول لبني"),
            option("لا تغيير / لا يتكون راسب على البارد", "q_heat_tube", swatch=NONE, arabic_label="لا يتكون راسب على البارد")
        ],
        hint="هيدروكسيد الصوديوم يكشف عن هيدروكسيدات الفلزات المميزة بألوانها وسلوكها القلوي.",
        arabic_text="المرحلة 3: أضف هيدروكسيد الصوديوم (NaOH) قطرة قطرة. ماذا تلاحظ؟"
    ),

    "q_cu_ammonia": question(
        "q_cu_ammonia",
        "هل يتغير لون المحلول بعد إضافة زيادة من الأمونيا (NH₃)؟ إلى أي لون؟",
        [
            option("أزرق داكن (محلول معقد أزرق ملكي ساطع)", "CU", swatch="#1d4ed8", arabic_label="أزرق داكن (محلول معقد أزرق ملكي)"),
            option("لا تغيير / يظل راسباً", "CU", swatch=BLUE, arabic_label="لا تغيير / يظل راسباً")
        ],
        hint="النحاس الثنائي يذوب في وفرة الأمونيا لتكوين معقد الأمين الملكي ذي اللون الأزرق الداكن الساطع.",
        arabic_text="المرحلة 3: هل يتغير لون المحلول بعد إضافة زيادة من الأمونيا (NH₃)؟ إلى أي لون؟"
    ),

    "q_fe2_air": question(
        "q_fe2_air",
        "هل يتغير لون الراسب عند تركه معرضاً للهواء؟",
        [
            option("يتحول السطح تدريجياً إلى بني محمر نتيجة التأكسد", "FE2", swatch=GREEN, arabic_label="يتحول إلى بني محمر بالأكسدة"),
            option("يظل لونه أخضر ثابتاً", "FE2", swatch=GREEN, arabic_label="يظل أخضر ثابتاً")
        ],
        hint="هيدروكسيد الحديد الثنائي Fe(OH)₂ يتأكسد بأكسجين الهواء إلى هيدروكسيد الحديد الثلاثي البني المحمر.",
        arabic_text="المرحلة 3: هل يتغير لون الراسب عند تركه معرضاً للهواء؟"
    ),

    "q_naoh_excess": question(
        "q_naoh_excess",
        "هل يذوب الراسب عند إضافة زيادة من هيدروكسيد الصوديوم (NaOH)؟",
        [
            option("نعم، يذوب الراسب في الزيادة من NaOH مع الرج", "q_ammonia_excess_white", arabic_label="نعم، يذوب في الزيادة من NaOH"),
            option("لا، لا يذوب الراسب في الزيادة من NaOH", "q_flame_test_white", arabic_label="لا، لا يذوب في الزيادة من NaOH")
        ],
        hint="الألومنيوم والزنك والرصاص لها هيدروكسيدات مترددة (amphoteric) تذوب في وفرة هيدروكسيد الصوديوم.",
        arabic_text="المرحلة 3: هل يذوب الراسب عند إضافة زيادة من هيدروكسيد الصوديوم (NaOH)؟"
    ),

    "q_ammonia_excess_white": question(
        "q_ammonia_excess_white",
        "هل يذوب الراسب في زيادة الأمونيا؟",
        [
            option("نعم، يذوب الراسب في زيادة الأمونيا", "ZN", swatch=WHITE, arabic_label="نعم، يذوب في زيادة الأمونيا (Zn²⁺)"),
            option("لا، لا يذوب الراسب في زيادة الأمونيا", "AL", swatch=WHITE, arabic_label="لا، لا يذوب في زيادة الأمونيا (Al³⁺)")
        ],
        hint="الزنك يذوب في زيادة النشادر لتكوين معقد رباعي أمين الزنك الذائب، بينما الألومنيوم يظل راسباً جيلاتينياً.",
        arabic_text="المرحلة 3: هل يذوب الراسب في زيادة الأمونيا؟"
    ),

    "q_flame_test_white": question(
        "q_flame_test_white",
        "قم بإجراء كشف اللهب أو اختبار الذوبان. ما هي الملاحظة؟",
        [
            option("لهب أحمر طوبي (brick-red flame) وراسب أبيض مع الأوكسالات", "CA", swatch=BRICK_RED, arabic_label="لهب أحمر طوبي (Ca²⁺)"),
            option("لا يوجد لون مميز للهب (راسب أبيض ثابت يعطي لوناً مع الماغنسون)", "MG", swatch=WHITE, arabic_label="لا لون مميز للهب (Mg²⁺)"),
            option("يذوب في الماء الساخن ويعود بالتبريد", "PB", swatch=WHITE, arabic_label="يذوب في الماء الساخن (Pb²⁺)")
        ],
        hint="الكالسيوم يعطي لهباً أحمر طوبياً مميزاً، بينما الماغنسيوم لا يعطي لوناً مميزاً في كشف اللهب العادي.",
        arabic_text="المرحلة 3: قم بإجراء كشف اللهب الجاف. ما هي الملاحظة؟"
    ),

    "q_heat_tube": question(
        "q_heat_tube",
        "هل تحتاج لتسخين الأنبوب؟ ماذا تلاحظ بعد التسخين؟",
        [
            option("تصاعد غاز النشادر (رائحة نفاذة يزرق ورقة تباع الشمس المبللة)", "NH4", arabic_label="تصاعد غاز النشادر ذو الرائحة النفاذة (NH₄⁺)"),
            option("لا تغيير / لا يتصاعد غاز بعد التسخين", "q_barium_reagent", swatch=NONE, arabic_label="لا تغيير / الانتقال لكواشف الترسيب")
        ],
        hint="أملاح الأمونيوم لا ترسب مع NaOH البارد ولكنها تتفكك بالحرارة متصاعدة كغاز الأمونيا القلوي.",
        arabic_text="المرحلة 3: هل تحتاج لتسخين الأنبوب؟ ماذا تلاحظ بعد التسخين؟"
    ),

    "q_barium_reagent": question(
        "q_barium_reagent",
        "أضف محلول كلوريد الباريوم (BaCl₂) إلى عينة جديدة متعادلة. ماذا تلاحظ؟",
        [
            option("راسب أبيض", "q_barium_acid_solubility", swatch=WHITE, arabic_label="راسب أبيض"),
            option("لا يتكون راسب / لا تغيير", "q_silver_reagent", swatch=NONE, arabic_label="لا يتكون راسب / لا تغيير")
        ],
        hint="كلوريد الباريوم كاشف نوعي لترسيب الكبريتات والفوسفات والكبريتيت والكربونات.",
        arabic_text="المرحلة 3: أضف محلول كلوريد الباريوم (BaCl₂). ماذا تلاحظ؟"
    ),

    "q_barium_acid_solubility": question(
        "q_barium_acid_solubility",
        "هل يذوب الراسب في حمض مخفف؟",
        [
            option("لا يذوب الراسب إطلاقاً في حمض HCl المخفف أو المركز", "SO4", swatch=WHITE, arabic_label="لا يذوب في حمض مخفف (كبريتات SO₄²⁻)"),
            option("يذوب الراسب في حمض HCl مع فوران وتصاعد غاز CO₂", "CO3", swatch=WHITE, arabic_label="يذوب في الحمض مع فوران (كربونات CO₃²⁻)"),
            option("يذوب الراسب في حمض HCl دون فوران (يعطي راسباً أصفر مع الموليبدات)", "PO4", swatch=WHITE, arabic_label="يذوب دون فوران (فوسفات PO₄³⁻)"),
            option("يذوب الراسب في حمض HCl مع تصاعد غاز SO₂ الخانق", "SO3", swatch=WHITE, arabic_label="يذوب مع غاز SO₂ (كبريتيت SO₃²⁻)")
        ],
        hint="كبريتات الباريوم BaSO₄ مميزة جداً بعدم ذوبانها في أي حمض مخفف.",
        arabic_text="المرحلة 3: هل يذوب الراسب في حمض مخفف؟"
    ),

    "q_silver_reagent": question(
        "q_silver_reagent",
        "أضف محلول نترات الفضة (AgNO₃) إلى عينة جديدة محمضة بحمض النيتريك المخفف. ماذا تلاحظ؟",
        [
            option("راسب أبيض متجبن", "q_silver_white_ammonia", swatch=WHITE, arabic_label="راسب أبيض"),
            option("راسب كريمي / أصفر باهت", "q_silver_cream_ammonia", swatch=PALE_YELLOW, arabic_label="راسب كريمي / أصفر باهت"),
            option("راسب أصفر فاقع", "q_silver_yellow_ammonia", swatch=YELLOW, arabic_label="راسب أصفر فاقع"),
            option("راسب أسود من كبريتيد الفضة", "S2", swatch="#1a1a1a", arabic_label="راسب أسود (S²⁻)"),
            option("راسب أحمر طوبي / بني محمر من كرومات الفضة", "CRO4", swatch="#c84630", arabic_label="راسب أحمر طوبي (CrO₄²⁻)"),
            option("لا يتكون أي راسب", "q_conc_h2so4", swatch=NONE, arabic_label="لا يتكون أي راسب")
        ],
        hint="نترات الفضة ترسب الهاليدات (Cl⁻, Br⁻, I⁻) وكذلك الكبريتيد والكرومات بتدرجات لونية واضحة.",
        arabic_text="المرحلة 3: أضف محلول نترات الفضة (AgNO₃). ماذا تلاحظ؟"
    ),

    "q_silver_white_ammonia": question(
        "q_silver_white_ammonia",
        "هل يذوب الراسب في زيادة الأمونيا؟",
        [
            option("نعم، يذوب تماماً وبسرعة في النشادر المخفف", "CL", swatch=WHITE, arabic_label="نعم، يذوب في النشادر المخفف (كلوريد Cl⁻)"),
            option("لا يذوب في المخفف", "CL", swatch=WHITE, arabic_label="لا يذوب في المخفف")
        ],
        hint="كلوريد الفضة AgCl يذوب بسهولة شديدة في محلول النشادر المخفف.",
        arabic_text="المرحلة 3: هل يذوب الراسب في زيادة الأمونيا؟"
    ),

    "q_silver_cream_ammonia": question(
        "q_silver_cream_ammonia",
        "هل يذوب الراسب في زيادة الأمونيا؟",
        [
            option("يذوب بصعوبة في المخفف ويذوب في النشادر المركز", "BR", swatch=PALE_YELLOW, arabic_label="يذوب في النشادر المركز (بروميد Br⁻)"),
            option("لا يذوب في المخفف أو المركز", "BR", swatch=PALE_YELLOW, arabic_label="شحيح الذوبان جداً")
        ],
        hint="بروميد الفضة AgBr يذوب في النشادر المركز فقط.",
        arabic_text="المرحلة 3: هل يذوب الراسب في زيادة الأمونيا؟"
    ),

    "q_silver_yellow_ammonia": question(
        "q_silver_yellow_ammonia",
        "هل يذوب الراسب في زيادة الأمونيا؟",
        [
            option("لا يذوب نهائياً في النشادر سواء مخفف أو مركز", "IODIDE", swatch=YELLOW, arabic_label="لا يذوب نهائياً في النشادر (يوديد I⁻)"),
            option("يذوب في النشادر المخفف وحمض النيتريك", "PO4", swatch=YELLOW, arabic_label="يذوب في النشادر وحمض النيتريك (فوسفات PO₄³⁻)")
        ],
        hint="يوديد الفضة AgI لا يذوب إطلاقاً في محلول الأمونيا، بينما فوسفات الفضة تذوب بسهولة.",
        arabic_text="المرحلة 3: هل يذوب الراسب في زيادة الأمونيا؟"
    ),

    "q_conc_h2so4": question(
        "q_conc_h2so4",
        "أضف حمض الكبريتيك المركز (H₂SO₄) مع كبريتات الحديد الثنائي بحرص، أو اختبر المحلول مع كلوريد الحديد الثلاثي (FeCl₃). ماذا تلاحظ؟",
        [
            option("تكون حلقة بنية فاصلة عند السطح الفاصل بين الطبقتين (الحلقة البنية)", "NO3_CHECK", swatch=BROWN, arabic_label="تكون حلقة بنية فاصلة (نترات NO₃⁻)"),
            option("ظهور لون أحمر دامي مميز عند إضافة كلوريد الحديد الثلاثي المتعادل", "CH3COO", swatch="#991b1b", arabic_label="لون أحمر دامي مع FeCl₃ (أسيتات CH₃COO⁻)"),
            option("لا تغيير واضح / لا تفاعل", "UNKNOWN_INCONCLUSIVE", swatch=NONE, arabic_label="لا تفاعل / عينة غير محددة")
        ],
        hint="النترات تعطي اختبار الحلقة البنية، والأسيتات تعطي لوناً أحمر دامي مع كلوريد الحديد الثلاثي.",
        arabic_text="المرحلة 3: أضف كواشف النترات والأسيتات. ماذا تلاحظ؟"
    )
}

# Integrate Organic & Salt Diagnosis Decision Trees into Unified Diagnostic Tree
UNIFIED_DECISION_TREE.update(ORGANIC_DECISION_TREE)
UNIFIED_DECISION_TREE.update(SALT_DIAGNOSIS_NODES)


# 4.5 Confirmatory Tests & Initial Color Mapping for 5-Stage Protocol

# Apply question node bilingual texts
for _qid, _qvals in {'start_color': {'text': 'Step 1: What is the initial color of the sample or solution?', 'arabic_text': 'المرحلة 1: ما لون المادة أو المحلول أمامك؟', 'text_en': 'Step 1: What is the initial color of the sample or solution?'}, 'q_physical_state': {'text': 'Step 1: Is the sample a solid substance or an aqueous solution?', 'arabic_text': 'المرحلة 1: هل العينة صلبة أم محلول؟', 'text_en': 'Step 1: Is the sample a solid substance or an aqueous solution?'}, 'q_first_reagent': {'text': 'Step 2: Add dilute hydrochloric acid (Dil. HCl) dropwise to the sample. What do you observe?', 'arabic_text': 'المرحلة 2: أضف حمض الهيدروكلوريك المخفف (HCl) قطرة قطرة إلى العينة. ماذا تلاحظ؟', 'text_en': 'Step 2: Add dilute hydrochloric acid (Dil. HCl) dropwise to the sample. What do you observe?'}, 'q_gas_observation': {'text': 'Step 3: Is a gas evolved? What is its color or odor?', 'arabic_text': 'المرحلة 3: هل يتصاعد غاز؟ وما لونه أو رائحته؟', 'text_en': 'Step 3: Is a gas evolved? What is its color or odor?'}, 'q_hcl_white_precipitate': {'text': 'Step 3: Does the white precipitate dissolve in boiling water?', 'arabic_text': 'المرحلة 3: هل يذوب الراسب في الماء الساخن؟', 'text_en': 'Step 3: Does the white precipitate dissolve in boiling water?'}, 'q_naoh_addition': {'text': 'Step 3: Add sodium hydroxide (NaOH) solution dropwise with shaking. What do you observe?', 'arabic_text': 'المرحلة 3: أضف هيدروكسيد الصوديوم (NaOH) قطرة قطرة. ماذا تلاحظ؟', 'text_en': 'Step 3: Add sodium hydroxide (NaOH) solution dropwise with shaking. What do you observe?'}, 'q_cu_ammonia': {'text': 'Step 3: Does the solution color change upon adding excess aqueous ammonia (NH₃)? What color?', 'arabic_text': 'المرحلة 3: هل يتغير لون المحلول بعد إضافة زيادة من الأمونيا (NH₃)؟ إلى أي لون؟', 'text_en': 'Step 3: Does the solution color change upon adding excess aqueous ammonia (NH₃)? What color?'}, 'q_fe2_air': {'text': 'Step 3: Does the precipitate color change upon standing exposed to air?', 'arabic_text': 'المرحلة 3: هل يتغير لون الراسب عند تركه معرضاً للهواء؟', 'text_en': 'Step 3: Does the precipitate color change upon standing exposed to air?'}, 'q_naoh_excess': {'text': 'Step 3: Does the precipitate dissolve upon adding excess sodium hydroxide (NaOH)?', 'arabic_text': 'المرحلة 3: هل يذوب الراسب عند إضافة زيادة من هيدروكسيد الصوديوم (NaOH)؟', 'text_en': 'Step 3: Does the precipitate dissolve upon adding excess sodium hydroxide (NaOH)?'}, 'q_ammonia_excess_white': {'text': 'Step 3: Does the precipitate dissolve in excess aqueous ammonia?', 'arabic_text': 'المرحلة 3: هل يذوب الراسب في زيادة الأمونيا؟', 'text_en': 'Step 3: Does the precipitate dissolve in excess aqueous ammonia?'}, 'q_flame_test_white': {'text': 'Step 3: Perform dry flame test or solubility test. What is the observed sign?', 'arabic_text': 'المرحلة 3: قم بإجراء كشف اللهب الجاف. ما هي الملاحظة؟', 'text_en': 'Step 3: Perform dry flame test or solubility test. What is the observed sign?'}, 'q_heat_tube': {'text': 'Step 3: Gently heat the test tube. What do you observe upon heating?', 'arabic_text': 'المرحلة 3: هل تحتاج لتسخين الأنبوب؟ ماذا تلاحظ بعد التسخين؟', 'text_en': 'Step 3: Gently heat the test tube. What do you observe upon heating?'}, 'q_barium_reagent': {'text': 'Step 3: Add barium chloride (BaCl₂) solution to a fresh neutral sample. What do you observe?', 'arabic_text': 'المرحلة 3: أضف محلول كلوريد الباريوم (BaCl₂). ماذا تلاحظ؟', 'text_en': 'Step 3: Add barium chloride (BaCl₂) solution to a fresh neutral sample. What do you observe?'}, 'q_barium_acid_solubility': {'text': 'Step 3: Does the precipitate dissolve in dilute acid?', 'arabic_text': 'المرحلة 3: هل يذوب الراسب في حمض مخفف؟', 'text_en': 'Step 3: Does the precipitate dissolve in dilute acid?'}, 'q_silver_reagent': {'text': 'Step 3: Add silver nitrate (AgNO₃) solution to sample acidified with dilute HNO₃. What do you observe?', 'arabic_text': 'المرحلة 3: أضف محلول نترات الفضة (AgNO₃). ماذا تلاحظ؟', 'text_en': 'Step 3: Add silver nitrate (AgNO₃) solution to sample acidified with dilute HNO₃. What do you observe?'}, 'q_silver_white_ammonia': {'text': 'Step 3: Does the white precipitate dissolve in excess aqueous ammonia?', 'arabic_text': 'المرحلة 3: هل يذوب الراسب في زيادة الأمونيا؟', 'text_en': 'Step 3: Does the white precipitate dissolve in excess aqueous ammonia?'}, 'q_silver_cream_ammonia': {'text': 'Step 3: Does the pale yellow / cream precipitate dissolve in excess ammonia?', 'arabic_text': 'المرحلة 3: هل يذوب الراسب في زيادة الأمونيا؟', 'text_en': 'Step 3: Does the pale yellow / cream precipitate dissolve in excess ammonia?'}, 'q_silver_yellow_ammonia': {'text': 'Step 3: Does the yellow precipitate dissolve in aqueous ammonia?', 'arabic_text': 'المرحلة 3: هل يذوب الراسب في زيادة الأمونيا؟', 'text_en': 'Step 3: Does the yellow precipitate dissolve in aqueous ammonia?'}, 'q_conc_h2so4': {'text': 'Step 3: Carefully add concentrated sulfuric acid (H₂SO₄) with fresh FeSO₄, or test with neutral FeCl₃. What do you observe?', 'arabic_text': 'المرحلة 3: أضف كواشف النترات والأسيتات. ماذا تلاحظ؟', 'text_en': 'Step 3: Carefully add concentrated sulfuric acid (H₂SO₄) with fresh FeSO₄, or test with neutral FeCl₃. What do you observe?'}}.items():
    if _qid in UNIFIED_DECISION_TREE:
        UNIFIED_DECISION_TREE[_qid].update(_qvals)

CONFIRMATORY_TESTS = {
    "CU": {
        "ion": "Cu²⁺",
        "name": "Copper(II) — أيون النحاس الثنائي",
        "reagent": "محلول النشادر (NH₃) بالزيادة أو فيروسيانيد البوتاسيوم K₄[Fe(CN)₆]",
        "procedure": "أضف بضع قطرات من محلول النشادر المركز حتى تذوب العينة، أو أضف قطرات من K₄[Fe(CN)₆].",
        "expected_sign": "ذوبان الراسب وتكون محلول أزرق ملكي داكن [Cu(NH₃)₄]²⁺ (أو راسب بني شوكولاتة مع الفيروسيانيد)",
        "equations": [
            "Cu(OH)₂ + 4NH₃ → [Cu(NH₃)₄]²⁺ + 2OH⁻",
            "2Cu²⁺ + [Fe(CN)₆]⁴⁻ → Cu₂[Fe(CN)₆] ↓"
        ]
    },
    "FE2": {
        "ion": "Fe²⁺",
        "name": "Iron(II) — أيون الحديد الثنائي",
        "reagent": "فيريسيانيد البوتاسيوم K₃[Fe(CN)₆]",
        "procedure": "أضف قطرات من محلول فيريسيانيد البوتاسيوم إلى عينة طازجة من المحلول.",
        "expected_sign": "تكون راسب أزرق داكن مميز يُعرف بأزرق ترنبول (Turnbull's blue)",
        "equations": ["3Fe²⁺ + 2[Fe(CN)₆]³⁻ → Fe₃[Fe(CN)₆]₂ ↓"]
    },
    "FE3": {
        "ion": "Fe³⁺",
        "name": "Iron(III) — أيون الحديد الثلاثي",
        "reagent": "ثيوثيانات البوتاسيوم (KSCN) أو فيروسيانيد البوتاسيوم K₄[Fe(CN)₆]",
        "procedure": "أضف قطرات من محلول KSCN إلى المحلول المجهول.",
        "expected_sign": "ظهور لون أحمر دامي كثيف مميز لمعقد ثيوثيانات الحديد [Fe(SCN)]²⁺",
        "equations": ["Fe³⁺ + SCN⁻ ⇌ [Fe(SCN)]²⁺"]
    },
    "ZN": {
        "ion": "Zn²⁺",
        "name": "Zinc — أيون الزنك",
        "reagent": "محلول النشادر (NH₃) بالزيادة وكبريتيد الصوديوم Na₂S",
        "procedure": "أضف وفرة من محلول النشادر مع الرج، ثم أضف بضع قطرات من كبريتيد الصوديوم.",
        "expected_sign": "يذوب الراسب الأبيض تماماً في وفرة النشادر، ويعطي راسباً أبيض غير ذائب مع Na₂S",
        "equations": [
            "Zn(OH)₂ + 4NH₃ ⇌ [Zn(NH₃)₄]²⁺ + 2OH⁻",
            "Zn²⁺ + S²⁻ → ZnS ↓"
        ]
    },
    "AL": {
        "ion": "Al³⁺",
        "name": "Aluminium — أيون الألومنيوم",
        "reagent": "هيدروكسيد الأمونيوم (NH₄OH) بالزيادة",
        "procedure": "أضف وفرة من محلول هيدروكسيد الأمونيوم مع الرج المستمر.",
        "expected_sign": "يظل الراسب الأبيض الجيلاتيني غير ذائب في الزيادة من الأمونيا (تمييزاً له عن الزنك)",
        "equations": ["Al³⁺ + 3NH₃ + 3H₂O → Al(OH)₃ ↓ + 3NH₄⁺"]
    },
    "CA": {
        "ion": "Ca²⁺",
        "name": "Calcium — أيون الكالسيوم",
        "reagent": "كشف اللهب الجاف (Platinum wire flame test) ومحلول أوكسالات الأمونيوم",
        "procedure": "اغمس سلك بلاتين مبلل بحمض HCl المركز في الملح الصلب وعرضه لمنطقة اللهب غير المضيئة.",
        "expected_sign": "تلون لهب بنزن بلون أحمر طوبي (brick-red flame) وظهور راسب أبيض مع الأوكسالات",
        "equations": ["Ca²⁺ + C₂O₄²⁻ → CaC₂O₄ ↓"]
    },
    "MG": {
        "ion": "Mg²⁺",
        "name": "Magnesium — أيون المغنيسيوم",
        "reagent": "كاشف الماغنسون (Magneson) في وسط قلوي أو فوسفات الصوديوم الهيدروجينية",
        "procedure": "أضف قطرات من كاشف الماغنسون ثم هيدروكسيد الصوديوم حتى يصبح الوسط قلوياً.",
        "expected_sign": "تكون راسب أزرق مميز ناتج عن ادمصاص الصبغة على هيدروكسيد المغنيسيوم",
        "equations": ["Mg²⁺ + 2OH⁻ → Mg(OH)₂ ↓"]
    },
    "NH4": {
        "ion": "NH₄⁺",
        "name": "Ammonium — أيون الأمونيوم",
        "reagent": "كاشف نيسلر (Nessler's reagent) أو التسخين مع NaOH وساق مبللة بـ HCl",
        "procedure": "أضف بضع قطرات من كاشف نيسلر القلوي K₂[HgI₄] إلى العينة.",
        "expected_sign": "تكون تلون أو راسب بني محمر فوري، وتصاعد غاز النشادر مع سحب بيضاء مع حمض HCl",
        "equations": [
            "NH₄⁺ + 2[HgI₄]²⁻ + 4OH⁻ → HgO·Hg(NH₂)I ↓ + 7I⁻ + 3H₂O",
            "NH₃ + HCl → NH₄Cl ↓"
        ]
    },
    "PB": {
        "ion": "Pb²⁺",
        "name": "Lead(II) — أيون الرصاص الثنائي",
        "reagent": "يوديد البوتاسيوم (KI) واختبار الذوبان بالماء الساخن",
        "procedure": "أضف قطرات من محلول KI إلى عينة المحلول ثم سخن الأنبوبة.",
        "expected_sign": "تكون راسب أصفر ذهبي يذوب بالغليان ويعود للترسب على هيئة بلورات ذهبية لامعة بالتبريد",
        "equations": ["Pb²⁺ + 2I⁻ → PbI₂ ↓"]
    },
    "CO3": {
        "ion": "CO₃²⁻",
        "name": "Carbonate — أيون الكربونات",
        "reagent": "كبريتات المغنيسيوم (MgSO₄) وتمرير الغاز في ماء الجير الرائق Ca(OH)₂",
        "procedure": "أضف محلول MgSO₄ على البارد، ومرر الغاز المتصاعد في ماء الجير الرائق لفترة وجيزة.",
        "expected_sign": "تكون راسب أبيض على البارد مع MgSO₄، وتعكر ماء الجير الرائق لتكون CaCO₃",
        "equations": [
            "Mg²⁺ + CO₃²⁻ → MgCO₃ ↓",
            "CO₂ + Ca(OH)₂ → CaCO₃ ↓ + H₂O"
        ]
    },
    "HCO3": {
        "ion": "HCO₃⁻",
        "name": "Bicarbonate — أيون البيكربونات",
        "reagent": "كبريتات المغنيسيوم (MgSO₄) مع الغليان",
        "procedure": "أضف محلول MgSO₄ إلى عينة من الملح ثم اغلي الأنبوبة جيداً.",
        "expected_sign": "لا يتكون راسب على البارد، ويتكون راسب أبيض فقط بعد التسخين والغليان",
        "equations": ["Mg(HCO₃)₂ —(Δ)→ MgCO₃ ↓ + CO₂ ↑ + H₂O"]
    },
    "S2": {
        "ion": "S²⁻",
        "name": "Sulfide — أيون الكبريتيد",
        "reagent": "نيتروبروسيد الصوديوم Na₂[Fe(CN)₅NO] أو ورقة أسيتات الرصاص",
        "procedure": "أضف بضع قطرات من محلول نيتروبروسيد الصوديوم في وسط قلوي.",
        "expected_sign": "ظهور لون بنفسجي ياقوتي ساطع ومميز جداً، واسوداد ورقة أسيتات الرصاص",
        "equations": [
            "S²⁻ + [Fe(CN)₅NO]²⁻ → [Fe(CN)₅NOS]⁴⁻ (لون بنفسجي)",
            "H₂S + Pb(CH₃COO)₂ → PbS ↓ + 2CH₃COOH"
        ]
    },
    "SO3": {
        "ion": "SO₃²⁻",
        "name": "Sulfite — أيون الكبريتيت",
        "reagent": "محلول برمنجنات البوتاسيوم المحمضة KMnO₄ أو ثاني كرومات البوتاسيوم",
        "procedure": "أضف قطرات من KMnO₄ المحمضة بحمض الكبريتيك المخفف إلى المحلول.",
        "expected_sign": "زوال اللون البنفسجي لبرمنجنات البوتاسيوم تماماً لاختزالها بواسطة الكبريتيت",
        "equations": ["5SO₃²⁻ + 2MnO₄⁻ + 6H⁺ → 5SO₄²⁻ + 2Mn²⁺ + 3H₂O"]
    },
    "S2O3": {
        "ion": "S₂O₃²⁻",
        "name": "Thiosulfate — أيون الثيوكبريتات",
        "reagent": "محلول اليود المائي I₂",
        "procedure": "أضف محلول اليود البني إلى محلول الثيوكبريتات.",
        "expected_sign": "زوال لون اليود البني على الفور نتيجة تأكسده إلى رباعي ثيونات الصوديوم",
        "equations": ["2S₂O₃²⁻ + I₂ → S₄O₆²⁻ + 2I⁻"]
    },
    "NO2": {
        "ion": "NO₂⁻",
        "name": "Nitrite — أيون النتريت",
        "reagent": "محلول كبريتات الحديد الثنائي FeSO₄ مع حمض الخليك",
        "procedure": "أضف محلول FeSO₄ حديث التحضير مع حمض الخليك المخفف.",
        "expected_sign": "تلون المحلول باللون البني الداكن على البارد دون الحاجة لحمض كبريتيك مركز",
        "equations": ["NO₂⁻ + Fe²⁺ + 2H⁺ → Fe³⁺ + NO + H₂O", "Fe²⁺ + NO → [Fe(NO)]²⁺ (بني)"]
    },
    "CL": {
        "ion": "Cl⁻",
        "name": "Chloride — أيون الكلوريد",
        "reagent": "محلول نترات الفضة (AgNO₃) والنشادر المخفف",
        "procedure": "أضف AgNO₃ ثم أضف محلول النشادر المخفف مع الرج.",
        "expected_sign": "تكون راسب أبيض متجبن يتحول إلى بنفسجي بالضوء، ويذوب تماماً وبسرعة في النشادر المخفف",
        "equations": [
            "Ag⁺ + Cl⁻ → AgCl ↓",
            "AgCl + 2NH₃ → [Ag(NH₃)₂]⁺ + Cl⁻"
        ]
    },
    "BR": {
        "ion": "Br⁻",
        "name": "Bromide — أيون البروميد",
        "reagent": "ماء الكلور Cl₂ water مع مذيب عضوي ونترات الفضة",
        "procedure": "أضف ماء الكلور قطرة قطرة مع طبقة رقيقة من المذيب العضوي ورج جيداً.",
        "expected_sign": "تلون الطبقة العضوية باللون البني المحمر (البروم الحر)، وظهور راسب كريمي يذوب في النشادر المركز فقط",
        "equations": [
            "2Br⁻ + Cl₂ → Br₂ + 2Cl⁻",
            "Ag⁺ + Br⁻ → AgBr ↓"
        ]
    },
    "IODIDE": {
        "ion": "I⁻",
        "name": "Iodide — أيون اليوديد",
        "reagent": "ماء الكلور Cl₂ water ومحلول النشا",
        "procedure": "أضف ماء الكلور ثم قطرات من محلول النشا.",
        "expected_sign": "تحرر اليود وتلون النشا فوراً باللون الأزرق الداكن، وعدم ذوبان راسب AgI الأصفر في الأمونيا",
        "equations": [
            "2I⁻ + Cl₂ → I₂ + 2Cl⁻",
            "I₂ + Starch → Blue complex"
        ]
    },
    "SO4": {
        "ion": "SO₄²⁻",
        "name": "Sulfate — أيون الكبريتات",
        "reagent": "محلول أسيتات الرصاص Pb(CH₃COO)₂ واختبار الغليان مع HCl",
        "procedure": "أضف محلول أسيتات الرصاص أو كلوريد الباريوم ثم اغلي مع حمض HCl المركز.",
        "expected_sign": "تكون راسب أبيض كثيف لا يذوب إطلاقاً في حمض HCl المركز أو الساخن",
        "equations": [
            "Pb²⁺ + SO₄²⁻ → PbSO₄ ↓",
            "Ba²⁺ + SO₄²⁻ → BaSO₄ ↓"
        ]
    },
    "PO4": {
        "ion": "PO₄³⁻",
        "name": "Phosphate — أيون الفوسفات",
        "reagent": "موليبدات الأمونيوم مع حمض النيتريك المركز والتسخين",
        "procedure": "أضف وفرة من محلول موليبدات الأمونيوم وحمض HNO₃ المركز ثم سخن بلطف.",
        "expected_sign": "تكون راسب أصفر كناري مميز من فوسفوموليبدات الأمونيوم",
        "equations": ["PO₄³⁻ + 12MoO₄²⁻ + 3NH₄⁺ + 24H⁺ → (NH₄)₃PO₄·12MoO₃ ↓ + 12H₂O"]
    },
    "NO3_CHECK": {
        "ion": "NO₃⁻",
        "name": "Nitrate — أيون النترات",
        "reagent": "اختبار الحلقة البنية (FeSO₄ حديث التحضير + H₂SO₄ مركز بحرص)",
        "procedure": "اخلط المحلول مع FeSO₄ الطازج، ثم صب H₂SO₄ المركز ببطء شديد على جدار الأنبوبة الداخلي.",
        "expected_sign": "تكون حلقة بنية فاصلة مستقرة عند السطح الفاصل بين الطبقتين تزول بالرج أو التسخين",
        "equations": [
            "NO₃⁻ + 3Fe²⁺ + 4H⁺ → NO + 3Fe³⁺ + 2H₂O",
            "[Fe(H₂O)₆]²⁺ + NO → [Fe(H₂O)₅(NO)]²⁺ (حلقة بنية) + H₂O"
        ]
    },
    "CH3COO": {
        "ion": "CH₃COO⁻",
        "name": "Acetate — أيون الأسيتات",
        "reagent": "محلول كلوريد الحديد الثلاثي FeCl₃ المتعادل",
        "procedure": "أضف قطرات من محلول FeCl₃ المتعادل إلى محلول الأسيتات.",
        "expected_sign": "ظهور لون أحمر دامي مميز يتحول إلى راسب بني محمر عند الغليان",
        "equations": ["3CH₃COO⁻ + Fe³⁺ + 2H₂O → [Fe₃(OH)₂(CH₃COO)₆]⁺ + 2H⁺"]
    }
}

# Integrate Organic Confirmatory Protocols
CONFIRMATORY_TESTS.update(ORGANIC_CONFIRMATORY_TESTS)

# Enrich Confirmatory Tests with English Translations and Arabic fallbacks
from confirmatory_data_en import CONFIRMATORY_TESTS_EN

for _key, _en_data in CONFIRMATORY_TESTS_EN.items():
    if _key in CONFIRMATORY_TESTS:
        _entry = CONFIRMATORY_TESTS[_key]
        _entry.setdefault('reagent_ar', _entry.get('reagent', ''))
        _entry.setdefault('procedure_ar', _entry.get('procedure', ''))
        _entry.setdefault('expected_sign_ar', _entry.get('expected_sign', ''))
        _entry.setdefault('name_ar', _entry.get('name', ''))
        _entry.update(_en_data)

INITIAL_COLOR_HINTS = {
    "أزرق": ["Cu²⁺"],
    "أخضر": ["Fe²⁺", "Ni²⁺", "Cr³⁺"],
    "أصفر": ["Fe³⁺", "CrO₄²⁻"],
    "بني": ["Fe³⁺"],
    "وردي": ["Mn²⁺", "Co²⁺"],
    "أسود": ["S²⁻ (في بعض الأملاح)", "MnO₂"],
    "برتقالي": ["Cr₂O₇²⁻"],
    "أبيض": ["Zn²⁺", "Al³⁺", "Ca²⁺", "Mg²⁺", "Pb²⁺", "Ag⁺", "NH₄⁺", "Ba²⁺"],
    "عديم اللون": ["Zn²⁺", "Al³⁺", "Ca²⁺", "Mg²⁺", "Pb²⁺", "Ag⁺", "NH₄⁺", "المركبات المائية لأغلب الأنيونات"],
    "غير محدد": []
}


# 5. Reaction Prediction Database (50 Expert Reactions)
CATIONS_LIST = [
    "Cu²⁺",
    "Fe²⁺",
    "Fe³⁺",
    "Zn²⁺",
    "Al³⁺",
    "Ca²⁺",
    "Mg²⁺",
    "NH₄⁺",
    "Pb²⁺",
    "Mn²⁺",
    "Ag⁺",
    "Ni²⁺",
    "Co²⁺",
    "Hg₂²⁺"
]

ANIONS_LIST = [
    "CO₃²⁻",
    "HCO₃⁻",
    "S²⁻",
    "SO₃²⁻",
    "S₂O₃²⁻",
    "NO₂⁻",
    "Cl⁻",
    "Br⁻",
    "I⁻",
    "NO₃⁻",
    "SO₄²⁻",
    "PO₄³⁻",
    "CrO₄²⁻",
    "CH₃COO⁻"
]

IONS = CATIONS_LIST + ANIONS_LIST

REAGENTS = [
    "NaOH",
    "NH₃",
    "HCl",
    "H₂SO₄",
    "BaCl₂",
    "AgNO₃",
    "FeCl₃",
    "KSCN",
    "K₃[Fe(CN)₆]",
    "K₄[Fe(CN)₆]",
    "Nessler",
    "KMnO₄",
    "Cl₂ water"
]

REACTIONS = {
    # --- 1 إلى 10: الكاتيونات مع هيدروكسيد الصوديوم (NaOH) ---
    ("Cu²⁺", "NaOH"): {
        "result": "Blue precipitate",
        "arabic_result": "راسب أزرق",
        "swatch": BLUE,
        "equations": ["Cu²⁺ + 2OH⁻ → Cu(OH)₂ ↓"],
        "notes": ["راسب أزرق لا يذوب في الزيادة من هيدروكسيد الصوديوم."]
    },
    ("Fe²⁺", "NaOH"): {
        "result": "Green precipitate",
        "arabic_result": "راسب أبيض مخضر يتحول لبني محمر",
        "swatch": GREEN,
        "equations": ["Fe²⁺ + 2OH⁻ → Fe(OH)₂ ↓", "4Fe(OH)₂ + O₂ + 2H₂O → 4Fe(OH)₃"],
        "notes": ["راسب أبيض مخضر يتحول إلى بني محمر عند التعرض للهواء."]
    },
    ("Fe³⁺", "NaOH"): {
        "result": "Reddish-brown precipitate",
        "arabic_result": "راسب بني محمر جيلاتيني",
        "swatch": BROWN,
        "equations": ["Fe³⁺ + 3OH⁻ → Fe(OH)₃ ↓"],
        "notes": ["راسب بني محمر جيلاتيني لا يذوب في الزيادة."]
    },
    ("Zn²⁺", "NaOH"): {
        "result": "White precipitate dissolving in excess",
        "arabic_result": "راسب أبيض يذوب في وفرة من NaOH",
        "swatch": WHITE,
        "equations": ["Zn²⁺ + 2OH⁻ → Zn(OH)₂ ↓", "Zn(OH)₂ + 2OH⁻ → [Zn(OH)₄]²⁻"],
        "notes": ["راسب أبيض يذوب في الزيادة من NaOH لتكوين معقد زنكات ذائب."]
    },
    ("Al³⁺", "NaOH"): {
        "result": "White gelatinous precipitate dissolving in excess",
        "arabic_result": "راسب أبيض جيلاتيني يذوب في وفرة من NaOH",
        "swatch": WHITE,
        "equations": ["Al³⁺ + 3OH⁻ → Al(OH)₃ ↓", "Al(OH)₃ + OH⁻ → [Al(OH)₄]⁻"],
        "notes": ["راسب أبيض جيلاتيني يذوب في الزيادة من NaOH."]
    },
    ("Ca²⁺", "NaOH"): {
        "result": "Sparsely soluble white precipitate",
        "arabic_result": "راسب أبيض خفيف شحيح الذوبان",
        "swatch": WHITE,
        "equations": ["Ca²⁺ + 2OH⁻ → Ca(OH)₂ ↓"],
        "notes": ["هيدروكسيد الكالسيوم شحيح الذوبان في الماء."]
    },
    ("Mg²⁺", "NaOH"): {
        "result": "White precipitate",
        "arabic_result": "راسب أبيض",
        "swatch": WHITE,
        "equations": ["Mg²⁺ + 2OH⁻ → Mg(OH)₂ ↓"],
        "notes": ["راسب أبيض لا يذوب في الزيادة من هيدروكسيد الصوديوم."]
    },
    ("NH₄⁺", "NaOH"): {
        "result": "Ammonia gas evolution upon heating",
        "arabic_result": "تصاعد غاز النشادر عند التسخين",
        "swatch": NONE,
        "equations": ["NH₄⁺ + OH⁻ → NH₃ ↑ + H₂O"],
        "notes": ["تصاعد غاز النشادر ذو الرائحة النفاذة والذي يزرق ورق تباع الشمس المبلل."]
    },
    ("Pb²⁺", "NaOH"): {
        "result": "White precipitate soluble in excess",
        "arabic_result": "راسب أبيض يذوب في وفرة من NaOH",
        "swatch": WHITE,
        "equations": ["Pb²⁺ + 2OH⁻ → Pb(OH)₂ ↓", "Pb(OH)₂ + 2OH⁻ → [Pb(OH)₄]²⁻"],
        "notes": ["راسب أبيض يذوب في الزيادة من NaOH."]
    },
    ("Mn²⁺", "NaOH"): {
        "result": "White precipitate turning brown",
        "arabic_result": "راسب أبيض يتحول إلى بني بالتأكسد",
        "swatch": "#d2b48c",
        "equations": ["Mn²⁺ + 2OH⁻ → Mn(OH)₂ ↓", "2Mn(OH)₂ + O₂ → 2MnO(OH)₂ ↓ + H₂O"],
        "notes": ["راسب أبيض يتاكسد بسرعة في الهواء ويصبح بني اللون."]
    },

    # --- 11 إلى 18: الكاتيونات مع محلول النشادر / هيدروكسيد الأمونيوم (NH₃) ---
    ("Cu²⁺", "NH₃"): {
        "result": "Deep blue complex solution",
        "arabic_result": "محلول معقد أزرق داكن",
        "swatch": "#1d4ed8",
        "equations": ["Cu²⁺ + 2OH⁻ → Cu(OH)₂ ↓", "Cu(OH)₂ + 4NH₃ → [Cu(NH₃)₄]²⁺ + 2OH⁻"],
        "notes": ["يتكون راسب أزرق يذوب في الزيادة من النشادر مكوّناً لون أزرق داكن."]
    },
    ("Fe²⁺", "NH₃"): {
        "result": "Dirty green precipitate",
        "arabic_result": "راسب أخضر متسخ",
        "swatch": "#556b2f",
        "equations": ["Fe²⁺ + 2NH₃ + 2H₂O → Fe(OH)₂ ↓ + 2NH₄⁺"],
        "notes": ["راسب أخضر متسخ لا يذوب في الزيادة."]
    },
    ("Fe³⁺", "NH₃"): {
        "result": "Reddish-brown precipitate",
        "arabic_result": "راسب بني محمر",
        "swatch": BROWN,
        "equations": ["Fe³⁺ + 3NH₃ + 3H₂O → Fe(OH)₃ ↓ + 3NH₄⁺"],
        "notes": ["راسب بني محمر لا يذوب في الزيادة من النشادر."]
    },
    ("Zn²⁺", "NH₃"): {
        "result": "White precipitate dissolving in excess NH₃",
        "arabic_result": "راسب أبيض يذوب في وفرة من النشادر",
        "swatch": WHITE,
        "equations": ["Zn²⁺ + 2OH⁻ → Zn(OH)₂ ↓", "Zn(OH)₂ + 4NH₃ ⇌ [Zn(NH₃)₄]²⁺ + 2OH⁻"],
        "notes": ["راسب أبيض يذوب في الزيادة من محلول النشادر."]
    },
    ("Al³⁺", "NH₃"): {
        "result": "White gelatinous precipitate",
        "arabic_result": "راسب أبيض جيلاتيني لا يذوب في الزيادة",
        "swatch": WHITE,
        "equations": ["Al³⁺ + 3NH₃ + 3H₂O → Al(OH)₃ ↓ + 3NH₄⁺"],
        "notes": ["راسب أبيض جيلاتيني لا يذوب في الزيادة من النشادر."]
    },
    ("Ag⁺", "NH₃"): {
        "result": "Colorless complex solution",
        "arabic_result": "محلول معقد عديم اللون (أمين الفضة)",
        "swatch": "#e0f2fe",
        "equations": ["Ag⁺ + NH₃ + H₂O → AgOH ↓ + NH₄⁺", "AgOH + 2NH₃ → [Ag(NH₃)₂]⁺ + OH⁻"],
        "notes": ["لا يتكون راسب دائم ويذوب في الزيادة لتكوين أيون أمين الفضة."]
    },
    ("Ni²⁺", "NH₃"): {
        "result": "Blue-purple complex solution",
        "arabic_result": "محلول معقد أزرق بنفسجي",
        "swatch": "#6366f1",
        "equations": ["Ni²⁺ + 2OH⁻ → Ni(OH)₂ ↓", "Ni(OH)₂ + 6NH₃ → [Ni(NH₃)₆]²⁺ + 2OH⁻"],
        "notes": ["راسب أخضر يذوب في الزيادة من النشادر معطياً محلولاً أزرق بنفسجي."]
    },
    ("Co²⁺", "NH₃"): {
        "result": "Straw-colored solution turning brown",
        "arabic_result": "محلول بلون قشي يتحول لبني بالتأكسد",
        "swatch": "#d97706",
        "equations": ["Co²⁺ + 2OH⁻ → Co(OH)₂ ↓", "Co(OH)₂ + 6NH₃ → [Co(NH₃)₆]²⁺ + 2OH⁻"],
        "notes": ["يتكون مركب معقد ذو لون قشري يتاكسد بالهواء."]
    },

    # --- 19 إلى 21: الكاتيونات مع حمض الهيدروكلوريك (HCl) ---
    ("Pb²⁺", "HCl"): {
        "result": "White precipitate soluble in hot water",
        "arabic_result": "راسب أبيض يذوب في الماء الساخن",
        "swatch": WHITE,
        "equations": ["Pb²⁺ + 2Cl⁻ → PbCl₂ ↓"],
        "notes": ["راسب أبيض يذوب في الماء الساخن ويعود للترسيب بالتبريد."]
    },
    ("Ag⁺", "HCl"): {
        "result": "White precipitate soluble in dilute ammonia",
        "arabic_result": "راسب أبيض يذوب في النشادر المخفف",
        "swatch": WHITE,
        "equations": ["Ag⁺ + Cl⁻ → AgCl ↓"],
        "notes": ["راسب أبيض من كلوريد الفضة يذوب في النشادر المخفف."]
    },
    ("Hg₂²⁺", "HCl"): {
        "result": "White precipitate turning black with ammonia",
        "arabic_result": "راسب أبيض يسود عند إضافة محلول النشادر",
        "swatch": WHITE,
        "equations": ["Hg₂²⁺ + 2Cl⁻ → Hg₂Cl₂ ↓", "Hg₂Cl₂ + 2NH₃ → HgNH₂Cl + Hg ↓ + NH₄⁺ + Cl⁻"],
        "notes": ["يتكون راسب أبيض يسود عند إضافة محلول النشادر."]
    },

    # --- 22 إلى 27: تفاعلات الأنيونات مع الحمض المخفف (HCl) ---
    ("CO₃²⁻", "HCl"): {
        "result": "Effervescence and CO₂ gas turning limewater milky",
        "arabic_result": "فوران وتصاعد غاز CO₂ يعكر ماء الجير",
        "swatch": WHITE,
        "equations": ["CO₃²⁻ + 2H⁺ → CO₂ ↑ + H₂O", "CO₂ + Ca(OH)₂ → CaCO₃ ↓ + H₂O"],
        "notes": ["تصاعد غاز ثاني أكسيد الكربون الذي يعكر ماء الجير الرائق لفترة قصيرة."]
    },
    ("HCO₃⁻", "HCl"): {
        "result": "Immediate effervescence releasing CO₂",
        "arabic_result": "فوران سريع ولحظي بتصاعد غاز CO₂",
        "swatch": WHITE,
        "equations": ["HCO₃⁻ + H⁺ → CO₂ ↑ + H₂O"],
        "notes": ["تفاعل فوار سريع لتصاعد غاز CO₂."]
    },
    ("S²⁻", "HCl"): {
        "result": "H₂S gas turning lead acetate paper black",
        "arabic_result": "تصاعد غاز H₂S يسود ورقة أسيتات الرصاص",
        "swatch": "#1a1a1a",
        "equations": ["S²⁻ + 2H⁺ → H₂S ↑", "H₂S + Pb(CH₃COO)₂ → PbS ↓ + 2CH₃COOH"],
        "notes": ["تصاعد غاز كبريتيد الهيدروجين ذو رائحة البيض الفاسد."]
    },
    ("SO₃²⁻", "HCl"): {
        "result": "SO₂ gas choking odor turning dichromate green",
        "arabic_result": "تصاعد غاز SO₂ خانق يخضر ورقة ثاني كرومات البوتاسيوم",
        "swatch": GREEN,
        "equations": ["SO₃²⁻ + 2H⁺ → SO₂ ↑ + H₂O", "3SO₂ + Cr₂O₇²⁻ + 2H⁺ → 3SO₄²⁻ + 2Cr³⁺ + H₂O"],
        "notes": ["تصاعد غاز ثاني أكسيد الكبريت الذي يخضر ورقة مبللة بثاني كرومات البوتاسيوم."]
    },
    ("S₂O₃²⁻", "HCl"): {
        "result": "SO₂ release and yellow sulfur turbidity",
        "arabic_result": "تصاعد غاز SO₂ مع تعكر كبريتي أصفر",
        "swatch": "#fde047",
        "equations": ["S₂O₃²⁻ + 2H⁺ → SO₂ ↑ + S ↓ + H₂O"],
        "notes": ["تصاعد غاز SO₂ وترسيب الكبريت الأصفر المعكر للمحلول."]
    },
    ("NO₂⁻", "HCl"): {
        "result": "Reddish-brown NO₂ fumes at tube mouth",
        "arabic_result": "تصاعد أبخرة بنية حمراء من غاز NO₂",
        "swatch": "#b45309",
        "equations": ["NO₂⁻ + H⁺ → HNO₂", "3HNO₂ → HNO₃ + 2NO ↑ + H₂O", "2NO + O₂ → 2NO₂ ↑"],
        "notes": ["تصاعد غاز عديم اللون يتحول لأبخرة بنية حمراء عند فوهة الأنبوبة."]
    },

    # --- 28 إلى 31: تفاعلات الأنيونات مع حمض الكبريتيك المركز (H₂SO₄) ---
    ("Cl⁻", "H₂SO₄"): {
        "result": "HCl gas forming white fumes with ammonia",
        "arabic_result": "تصاعد غاز HCl يعطي سحباً بيضاء مع النشادر",
        "swatch": WHITE,
        "equations": ["NaCl + H₂SO₄ → NaHSO₄ + HCl ↑", "HCl + NH₃ → NH₄Cl ↓"],
        "notes": ["تصاعد غاز عديم اللون يعطي سحب بيضاء مع ساق مبللة بالنشادر."]
    },
    ("Br⁻", "H₂SO₄"): {
        "result": "Reddish-brown bromine vapors turning starch yellow",
        "arabic_result": "تصاعد أبخرة بروم صفراء حمراء تصفر ورقة النشا",
        "swatch": "#ea580c",
        "equations": ["2NaBr + 2H₂SO₄ → Na₂SO₄ + Br₂ ↑ + SO₂ + 2H₂O"],
        "notes": ["تصاعد أبخرة بروم صفراء حمراء تصفر ورقة النشاء."]
    },
    ("I⁻", "H₂SO₄"): {
        "result": "Violet iodine vapors",
        "arabic_result": "تصاعد أبخرة يود بنفسجية",
        "swatch": "#8b5cf6",
        "equations": ["6NaI + 4H₂SO₄ → 3Na₂SO₄ + 4H₂O + 3I₂ ↑ + S ↓"],
        "notes": ["تصاعد أبخرة يود بنفسجية تحدث لوناً أزرق مع النشاء."]
    },
    ("NO₃⁻", "H₂SO₄"): {
        "result": "Brown ring test formation",
        "arabic_result": "تكون حلقة بنية فاصلة (اختبار الحلقة البنية)",
        "swatch": "#78350f",
        "equations": [
            "NaNO₃ + H₂SO₄ → NaHSO₄ + HNO₃",
            "6FeSO₄ + 2HNO₃ + 3H₂SO₄ → 3Fe₂(SO₄)₃ + 4H₂O + 2NO",
            "FeSO₄ + NO → FeSO₄·NO"
        ],
        "notes": ["تكون حلقة بنية فاصلة عند إضافة كبريتات الحديد II وحمض الكبريتيك المركز."]
    },

    # --- 32 إلى 35: تفاعلات الأنيونات مع محلول كلوريد الباريوم (BaCl₂) ---
    ("SO₄²⁻", "BaCl₂"): {
        "result": "White precipitate insoluble in dilute HCl",
        "arabic_result": "راسب أبيض كثيف لا يذوب في حمض HCl",
        "swatch": WHITE,
        "equations": ["Ba²⁺ + SO₄²⁻ → BaSO₄ ↓"],
        "notes": ["راسب أبيض من كبريتات الباريوم لا يذوب في حمض الهيدروكلوريك المخفف."]
    },
    ("CO₃²⁻", "BaCl₂"): {
        "result": "White precipitate soluble in dilute HCl with effervescence",
        "arabic_result": "راسب أبيض يذوب في حمض HCl مع فوران",
        "swatch": WHITE,
        "equations": ["Ba²⁺ + CO₃²⁻ → BaCO₃ ↓", "BaCO₃ + 2HCl → BaCl₂ + CO₂ ↑ + H₂O"],
        "notes": ["راسب أبيض من كربونات الباريوم يذوب في الحمض مع تصاعد CO₂."]
    },
    ("PO₄³⁻", "BaCl₂"): {
        "result": "White precipitate soluble in dilute HCl",
        "arabic_result": "راسب أبيض من فوسفات الباريوم يذوب في حمض HCl",
        "swatch": WHITE,
        "equations": ["3Ba²⁺ + 2PO₄³⁻ → Ba₃(PO₄)₂ ↓"],
        "notes": ["راسب أبيض من فوسفات الباريوم يذوب في حمض الهيدروكلوريك المخفف."]
    },
    ("SO₃²⁻", "BaCl₂"): {
        "result": "White precipitate soluble in dilute HCl",
        "arabic_result": "راسب أبيض من كبريتيت الباريوم يذوب في الأحماض",
        "swatch": WHITE,
        "equations": ["Ba²⁺ + SO₃²⁻ → BaSO₃ ↓", "BaSO₃ + 2HCl → BaCl₂ + SO₂ ↑ + H₂O"],
        "notes": ["راسب أبيض من كبريتيت الباريوم يذوب في الأحماض."]
    },

    # --- 36 إلى 42: تفاعلات الأنيونات مع نترات الفضة (AgNO₃) ---
    ("Cl⁻", "AgNO₃"): {
        "result": "White precipitate soluble in dilute ammonia",
        "arabic_result": "راسب أبيض متجبن يذوب في النشادر المخفف",
        "swatch": WHITE,
        "equations": ["Ag⁺ + Cl⁻ → AgCl ↓", "AgCl + 2NH₃ → [Ag(NH₃)₂]Cl"],
        "notes": ["راسب أبيض يذوب بسهولة في محلول النشادر المخفف."]
    },
    ("Br⁻", "AgNO₃"): {
        "result": "Cream precipitate soluble in concentrated ammonia",
        "arabic_result": "راسب كريمي يذوب في النشادر المركز",
        "swatch": PALE_YELLOW,
        "equations": ["Ag⁺ + Br⁻ → AgBr ↓", "AgBr + 2NH₃ → [Ag(NH₃)₂]Br"],
        "notes": ["راسب أصفر باهت (كريمي) يذوب ببطء في النشادر المركز."]
    },
    ("I⁻", "AgNO₃"): {
        "result": "Yellow precipitate insoluble in ammonia",
        "arabic_result": "راسب أصفر فاقع لا يذوب في النشادر",
        "swatch": YELLOW,
        "equations": ["Ag⁺ + I⁻ → AgI ↓"],
        "notes": ["راسب أصفر لا يذوب نهائياً في محلول النشادر."]
    },
    ("CO₃²⁻", "AgNO₃"): {
        "result": "White precipitate",
        "arabic_result": "راسب أبيض من كربونات الفضة",
        "swatch": WHITE,
        "equations": ["2Ag⁺ + CO₃²⁻ → Ag₂CO₃ ↓"],
        "notes": ["راسب أبيض من كربونات الفضة."]
    },
    ("S²⁻", "AgNO₃"): {
        "result": "Black precipitate",
        "arabic_result": "راسب أسود من كبريتيد الفضة",
        "swatch": "#1a1a1a",
        "equations": ["2Ag⁺ + S²⁻ → Ag₂S ↓"],
        "notes": ["راسب أسود من كبريتيد الفضة."]
    },
    ("CrO₄²⁻", "AgNO₃"): {
        "result": "Reddish-brown precipitate",
        "arabic_result": "راسب أحمر طوبي / بني محمر من كرومات الفضة",
        "swatch": "#c84630",
        "equations": ["2Ag⁺ + CrO₄²⁻ → Ag₂CrO₄ ↓"],
        "notes": ["راسب أحمر طوبي / بني محمر من كرومات الفضة."]
    },
    ("PO₄³⁻", "AgNO₃"): {
        "result": "Yellow precipitate soluble in dilute HNO₃ and NH₃",
        "arabic_result": "راسب أصفر من فوسفات الفضة",
        "swatch": "#facc15",
        "equations": ["3Ag⁺ + PO₄³⁻ → Ag₃PO₄ ↓"],
        "notes": ["راسب أصفر من فوسفات الفضة يذوب في حمض النيتريك والنشادر."]
    },

    # --- 43 إلى 50: تفاعلات كاشفة وتأكيدية متقدمة لنظم الخبراء ---
    ("CH₃COO⁻", "FeCl₃"): {
        "result": "Blood-red coloration",
        "arabic_result": "تكون لون أحمر دامي مميز لأيون الأسيتات",
        "swatch": "#991b1b",
        "equations": ["3CH₃COO⁻ + Fe³⁺ + 2H₂O → [Fe₃(OH)₂(CH₃COO)₆]⁺ + 2H⁺"],
        "notes": ["يتكون محلول ذو لون أحمر دامي مميز لأيون الأسيتات."]
    },
    ("Fe³⁺", "KSCN"): {
        "result": "Deep red blood-like complex",
        "arabic_result": "معقد أحمر دامي عند الكشف عن الحديد الثلاثي",
        "swatch": "#b91c1c",
        "equations": ["Fe³⁺ + SCN⁻ ⇌ [Fe(SCN)]²⁺"],
        "notes": ["تكون معقد أحمر دامي عند إضافة ثيووسيانات البوتاسيوم للحديد الثلاثي."]
    },
    ("Fe²⁺", "K₃[Fe(CN)₆]"): {
        "result": "Turnbull's blue precipitate",
        "arabic_result": "راسب أزرق ترنبول",
        "swatch": "#1e3a8a",
        "equations": ["3Fe²⁺ + 2[Fe(CN)₆]³⁻ → Fe₃[Fe(CN)₆]₂ ↓"],
        "notes": ["راسب أزرق ترنبول عند الكشف عن الحديد الثنائي."]
    },
    ("Fe³⁺", "K₄[Fe(CN)₆]"): {
        "result": "Prussian blue precipitate",
        "arabic_result": "راسب أزرق بروسي داكن",
        "swatch": "#172554",
        "equations": ["4Fe³⁺ + 3[Fe(CN)₆]⁴⁻ → Fe₄[Fe(CN)₆]₃ ↓"],
        "notes": ["راسب أزرق بروسي داكن عند الكشف عن الحديد الثلاثي."]
    },
    ("Cu²⁺", "K₄[Fe(CN)₆]"): {
        "result": "Chocolate-brown precipitate",
        "arabic_result": "راسب بني شوكولاتة",
        "swatch": "#713f12",
        "equations": ["2Cu²⁺ + [Fe(CN)₆]⁴⁻ → Cu₂[Fe(CN)₆] ↓"],
        "notes": ["راسب بني شوكولاتة مميز للنحاس مع فيروسيانيد البوتاسيوم."]
    },
    ("NH₄⁺", "Nessler"): {
        "result": "Brown precipitate or coloration",
        "arabic_result": "راسب أو تلون بني محمر مع كاشف نيسلر",
        "swatch": "#854d0e",
        "equations": ["NH₄⁺ + 2[HgI₄]²⁻ + 4OH⁻ → HgO·Hg(NH₂)I ↓ + 7I⁻ + 3H₂O"],
        "notes": ["تكون لون أو راسب بني محمر مع كاشف نيسلر للكشف عن الأمونيوم."]
    },
    ("SO₃²⁻", "KMnO₄"): {
        "result": "Decolorization of purple permanganate solution",
        "arabic_result": "زوال اللون البنفسجي لبرمنجنات البوتاسيوم",
        "swatch": "#f8fafc",
        "equations": ["5SO₃²⁻ + 2MnO₄⁻ + 6H⁺ → 5SO₄²⁻ + 2Mn²⁺ + 3H₂O"],
        "notes": ["يزول اللون البنفسجي لبرمنجنات البوتاسيوم المحمضة بواسطة الكبريتيت."]
    },
    ("I⁻", "Cl₂ water"): {
        "result": "Iodine liberation turning starch blue",
        "arabic_result": "تحرر اليود وتلون النشا بالأزرق الداكن",
        "swatch": "#1d4ed8",
        "equations": ["2I⁻ + Cl₂ → I₂ + 2Cl⁻", "I₂ + Starch → Blue complex"],
        "notes": ["تصاعد اليود البنفسجي وتحول لون النشاء إلى الأزرق الداكن."]
    }
}

# Alias for backward compatibility if needed
EXPERT_REACTIONS_50 = REACTIONS


def predict_reaction(ion_str, reagent_str):
    """
    Predict reaction outcome between an ion and a reagent.
    Adheres strictly to the requirement:
    'Do not assume a missing combination means "no reaction".
     The system should display: No validated data available for this ion–reagent combination.'
    """
    key = (ion_str.strip(), reagent_str.strip())
    if key in REACTIONS:
        data = REACTIONS[key]
        return {
            "status": "validated",
            "ion": ion_str,
            "reagent": reagent_str,
            "result": data["result"],
            "arabic_result": data.get("arabic_result", ""),
            "swatch": data.get("swatch", WHITE),
            "equations": data["equations"],
            "notes": data["notes"]
        }
    else:
        return {
            "status": "unvalidated",
            "ion": ion_str,
            "reagent": reagent_str,
            "result": "No validated data available for this ion–reagent combination.",
            "arabic_result": "لا تتوفر بيانات مؤكدة معملياً لهذا المزيج من الأيون والكاشف.",
            "swatch": NONE,
            "equations": [],
            "notes": [
                "Do not assume a missing combination means 'no reaction'.",
                "The scientific outcome for this specific ion–reagent pair has not been documented in the verified knowledge base.",
                "Consult reference laboratory manuals (e.g. Vogel's Inorganic Chemistry) or perform controlled tests under appropriate laboratory supervision."
            ]
        }



# ==== ELEMENT PROPERTIES (for final report) ====
# Detailed physical/chemical data for cations and anions.
ELEMENTS = {
    "Pb": {
        "name": "رصاص",
        "symbol": "Pb",
        "atomic_number": 82,
        "atomic_mass": "207.2",
        "group": "المجموعة 14",
        "period": 6,
        "oxidation_states": ["II", "IV"],
        "metal": True,
        "radius_pm": "~180",
        "thermal_conductivity": "ضعيف نسبيًا (~35 واط/م.ك)",
        "electrical_conductivity": "جيد لكن أقل من Cu",
        "magnetic": "ضد مغناطيسي"
    },
    "Ag": {
        "name": "فضة",
        "symbol": "Ag",
        "atomic_number": 47,
        "atomic_mass": "107.87",
        "group": "المجموعة 11",
        "period": 5,
        "oxidation_states": ["I"],
        "metal": True,
        "radius_pm": "~165",
        "thermal_conductivity": "الأعلى على الإطلاق (~429 واط/م.ك)",
        "electrical_conductivity": "الأعلى على الإطلاق",
        "magnetic": "ضد مغناطيسي"
    },
    "Hg": {
        "name": "زئبق",
        "symbol": "Hg",
        "atomic_number": 80,
        "atomic_mass": "200.59",
        "group": "المجموعة 12",
        "period": 6,
        "oxidation_states": ["I", "II"],
        "metal": True,
        "radius_pm": "~151",
        "thermal_conductivity": "ضعيف (~8 واط/م.ك)",
        "electrical_conductivity": "ضعيف (سائل)",
        "magnetic": "ضد مغناطيسي"
    },
    "Fe": {
        "name": "حديد",
        "symbol": "Fe",
        "atomic_number": 26,
        "atomic_mass": "55.85",
        "group": "المجموعة 8",
        "period": 4,
        "oxidation_states": ["II", "III"],
        "metal": True,
        "radius_pm": "~156",
        "thermal_conductivity": "جيد (~80 واط/م.ك)",
        "electrical_conductivity": "جيد",
        "magnetic": "مغناطيسي (Ferromagnetic)"
    },
    "Mn": {
        "name": "منجنيز",
        "symbol": "Mn",
        "atomic_number": 25,
        "atomic_mass": "54.94",
        "group": "المجموعة 7",
        "period": 4,
        "oxidation_states": ["II", "III", "IV", "VI", "VII"],
        "metal": True,
        "radius_pm": "~161",
        "thermal_conductivity": "ضعيف نسبيًا (~8 واط/م.ك)",
        "electrical_conductivity": "متوسط",
        "magnetic": "بارامغناطيسي"
    },
    "Cu": {
        "name": "نحاس",
        "symbol": "Cu",
        "atomic_number": 29,
        "atomic_mass": "63.55",
        "group": "المجموعة 11",
        "period": 4,
        "oxidation_states": ["I", "II"],
        "metal": True,
        "radius_pm": "~145",
        "thermal_conductivity": "ممتاز (~401 واط/م.ك)",
        "electrical_conductivity": "ممتاز (يتفوق فيه Ag فقط)",
        "magnetic": "ضد مغناطيسي"
    },
    "Zn": {
        "name": "زنك",
        "symbol": "Zn",
        "atomic_number": 30,
        "atomic_mass": "65.38",
        "group": "المجموعة 12",
        "period": 4,
        "oxidation_states": ["II"],
        "metal": True,
        "radius_pm": "~142",
        "thermal_conductivity": "جيد (~116 واط/م.ك)",
        "electrical_conductivity": "جيد",
        "magnetic": "ضد مغناطيسي"
    },
    "Al": {
        "name": "ألومنيوم",
        "symbol": "Al",
        "atomic_number": 13,
        "atomic_mass": "26.98",
        "group": "المجموعة 13",
        "period": 3,
        "oxidation_states": ["III"],
        "metal": True,
        "radius_pm": "~143",
        "thermal_conductivity": "ممتاز (~237 واط/م.ك)",
        "electrical_conductivity": "ممتاز",
        "magnetic": "بارامغناطيسي"
    },
    "Ca": {
        "name": "كالسيوم",
        "symbol": "Ca",
        "atomic_number": 20,
        "atomic_mass": "40.08",
        "group": "المجموعة 2",
        "period": 4,
        "oxidation_states": ["II"],
        "metal": True,
        "radius_pm": "~197",
        "thermal_conductivity": "جيد",
        "electrical_conductivity": "جيد",
        "magnetic": "بارامغناطيسي"
    },
    "Mg": {
        "name": "مغنيسيوم",
        "symbol": "Mg",
        "atomic_number": 12,
        "atomic_mass": "24.31",
        "group": "المجموعة 2",
        "period": 3,
        "oxidation_states": ["II"],
        "metal": True,
        "radius_pm": "~160",
        "thermal_conductivity": "جيد (~156 واط/م.ك)",
        "electrical_conductivity": "جيد",
        "magnetic": "بارامغناطيسي"
    },
    "NH4": {
        "name": "أمونيا",
        "symbol": "NH₄⁺",
        "atomic_number": None,
        "atomic_mass": "18",
        "group": "أيون مركب",
        "oxidation_states": ["+1"],
        "metal": False,
        "radius_pm": "~143 (anyonic)",
        "thermal_conductivity": "—",
        "electrical_conductivity": "موصل جيد في المحاليل",
        "magnetic": "تقريبًا ضد مغناطيسي"
    },
    "C": {
        "name": "كربون",
        "symbol": "C",
        "derived_anions": ["CO₃²⁻", "HCO₃⁻", "CH₃COO⁻"],
        "atomic_number": 6,
        "atomic_mass": "12.01",
        "group": "المجموعة 14",
        "period": 2,
        "oxidation_states": ["±IV"],
        "metal": False,
        "electrical_conductivity": "الجرافيت موصل، الألماس عازل",
        "magnetic": "ضد مغناطيسي"
    },
    "S": {
        "name": "كبريت",
        "symbol": "S",
        "derived_anions": ["S²⁻", "SO₃²⁻", "SO₄²⁻", "S₂O₃²⁻"],
        "atomic_number": 16,
        "atomic_mass": "32.06",
        "group": "المجموعة 16",
        "period": 3,
        "oxidation_states": ["II", "IV", "VI"],
        "metal": False,
        "electrical_conductivity": "عازل (أصفر)",
        "magnetic": "ضد مغناطيسي"
    },
    "N": {
        "name": "نيتروجين",
        "symbol": "N",
        "derived_anions": ["NO₂⁻", "NO₃⁻", "NH₄⁺"],
        "atomic_number": 7,
        "atomic_mass": "14.01",
        "group": "المجموعة 15",
        "period": 2,
        "oxidation_states": ["III", "V (−III)"],
        "metal": False,
        "electrical_conductivity": "عازل",
        "magnetic": "ضد مغناطيسي"
    },
    "P": {
        "name": "فوسفور",
        "symbol": "P",
        "derived_anions": ["PO₄³⁻"],
        "atomic_number": 15,
        "atomic_mass": "30.97",
        "group": "المجموعة 15",
        "period": 3,
        "oxidation_states": ["III", "V"],
        "metal": False,
        "electrical_conductivity": "عازل (لها شكل شبه فلزي)",
        "magnetic": "ضد مغناطيسي"
    },
    "Cr": {
        "name": "كروم",
        "symbol": "Cr",
        "derived_anions": ["CrO₄²⁻"],
        "atomic_number": 24,
        "atomic_mass": "52.00",
        "group": "المجموعة 6",
        "period": 4,
        "oxidation_states": ["II", "III", "VI"],
        "metal": True,
        "electrical_conductivity": "موصل جيد",
        "magnetic": "بارامغناطيسي"
    },
    "Cl": {
        "name": "كلور",
        "symbol": "Cl",
        "derived_anions": ["Cl⁻"],
        "atomic_number": 17,
        "atomic_mass": "35.45",
        "group": "المجموعة 17",
        "period": 3,
        "oxidation_states": ["I", "III", "V", "VII"],
        "metal": False,
        "electrical_conductivity": "عازل",
        "magnetic": "ضد مغناطيسي"
    },
    "Br": {
        "name": "بروم",
        "symbol": "Br",
        "derived_anions": ["Br⁻"],
        "atomic_number": 35,
        "atomic_mass": "79.90",
        "group": "المجموعة 17",
        "period": 4,
        "oxidation_states": ["I", "III", "V", "VII"],
        "metal": False,
        "electrical_conductivity": "عازل (سائل)",
        "magnetic": "ضد مغناطيسي"
    },
    "I": {
        "name": "يود",
        "symbol": "I",
        "derived_anions": ["I⁻"],
        "atomic_number": 53,
        "atomic_mass": "126.90",
        "group": "المجموعة 17",
        "period": 5,
        "oxidation_states": ["I", "V", "VII"],
        "metal": False,
        "electrical_conductivity": "عازل (لبريق فلزي)",
        "magnetic": "ضد مغناطيسي"
    }
}

# The dictionary will be used when generating the final report to display detailed element info.


# ========================================================
# COMPREHENSIVE BILINGUAL DATA ENRICHMENT (Arabic & English)
# ========================================================
# -*- coding: utf-8 -*-
"""
Bilingual notes and options definitions
"""

CATION_NOTES_AR = {
    "CU": [
        "يتكون راسب أزرق باهت مميز من هيدروكسيد النحاس الثنائي Cu(OH)₂.",
        "الراسب لا يذوب في الزيادة من محلول هيدروكسيد الصوديوم في الظروف العادية.",
        "يذوب الراسب في الزيادة من محلول النشادر المائي ليعطي محلولاً أزرق ملكياً داكناً لمعقد النحاس النشادرى: [Cu(NH₃)₄]²⁺."
    ],
    "FE2": [
        "الراسب الابتدائي هو هيدروكسيد الحديد الثنائي Fe(OH)₂ ذو اللون الأبيض المخضر.",
        "يتأكسد سريعاً عند تعرضه لأكسجين الهواء الجوي ليتحول لونه إلى البني المحمر Fe(OH)₃.",
        "لا يذوب في الزيادة من محلول هيدروكسيد الصوديوم NaOH."
    ],
    "FE3": [
        "يتكون راسب جيلاتيني بني محمر فوراً من هيدروكسيد الحديد الثلاثي Fe(OH)₃.",
        "لا يذوب الراسب في الزيادة من هيدروكسيد الصوديوم.",
        "يمكن تأكيد الأيون بإضافة ثيوسيانات البوتاسيوم (KSCN) ليعطي محلولاً أحمر دامي مميز."
    ],
    "ZN": [
        "يتكون راسب أبيض من هيدروكسيد الزنك Zn(OH)₂.",
        "نظراً لطبيعته المترددة (Amphoteric)، فإنه يذوب في الزيادة من NaOH مكوناً أيون الخارصينات الذائب [Zn(OH)₄]²⁻.",
        "فارق جوهري عن الألومنيوم: يذوب راسب هيدروكسيد الزنك في الزيادة من محلول النشادر مكوناً معقد الزنك النشادرى."
    ],
    "AL": [
        "يتكون راسب أبيض جيلاتيني من هيدروكسيد الألومنيوم Al(OH)₃.",
        "نظراً لطبيعته المترددة، فإنه يذوب بسهولة في الزيادة من NaOH مكوناً ألومينات الصوديوم الذائبة [Al(OH)₄]⁻.",
        "فارق جوهري عن الزنك: راسب هيدروكسيد الألومنيوم لا يذوب إطلاقاً في الزيادة من محلول النشادر."
    ],
    "CA": [
        "هيدروكسيد الكالسيوم شحيح الذوبان، لذا قد يكون الترسيب خفيفاً أو يتطلب تركيزاً كافياً للأيون.",
        "لا يذوب في الزيادة من هيدروكسيد الصوديوم.",
        "كشف اللهب يؤكد وجود الكالسيوم بإعطاء لهب أحمر طوبي (برتقالي محمر) مميز.",
        "يمكن استخدام أوكسالات الأمونيوم كاختبار تأكيدي إضافي لترسيب أوكسالات الكالسيوم البيضاء."
    ],
    "MG": [
        "يتكون راسب أبيض ناصع ومميز من هيدروكسيد المغنيسيوم Mg(OH)₂.",
        "لا يذوب الراسب في الزيادة من NaOH في الظروف المعملية القياسية.",
        "المغنيسيوم لا يعطي لوناً مميزاً للهب في كشف اللهب العادي (وهذا يميزه عن الكالسيوم).",
        "يمكن تأكيده باستخدام كاشف الماغنسون حيث يعطي راسباً أزرق مميزاً."
    ],
    "NH4": [
        "لا يتكون أي راسب مع محلول هيدروكسيد الصوديوم على البارد.",
        "عند التسخين اللطيف مع هيدروكسيد الصوديوم، يتصاعد غاز النشادر (NH₃) ذو الرائحة النفاذة.",
        "غاز النشادر يزرق ورقة تباع الشمس الحمراء المبللة ويكون سحباً بيضاء كثيفة من NH₄Cl مع ساق مبللة بـ HCl.",
        "تنبيه سلامة: لا تستنشق الغاز بشكل مباشر وأجرِ التجربة في بيئة جيدة التهوية."
    ],
    "CATION_INCONCLUSIVE": [
        "تحقق من نقاء الكواشف وعدم تلوثها وتأكد من التركيزات المعملية المناسبة.",
        "إذا لم يتكون أي راسب، يوصى باختبار كاتيونات الفلزات القلوية (Na⁺, K⁺) عبر كشف اللهب الجاف:",
        "• الصوديوم (Na⁺): لهب أصفر ذهبي ساطع ومستمر.",
        "• البوتاسيوم (K⁺): لهب بنفسجي فاتح / ليلكي (يُرى عبر زجاج الكوبالت).",
        "راجع المراجع المعملية المعتمدة لتحليلات الفصل المجموعي الموسعة."
    ]
}

ANION_NOTES_AR = {
    "CO3": [
        "إضافة حمض الهيدروكلوريك أو الكبريتيك المخفف تؤدي إلى فوران وتصاعد غاز ثاني أكسيد الكربون عديم اللون والرائحة.",
        "إمرار غاز CO₂ في ماء الجير الرائق Ca(OH)₂ يعكره بتكوين كربونات الكالسيوم غير الذائبة.",
        "البيكربونات (HCO₃⁻) تطلق غاز CO₂ أيضاً؛ والتفرقة تتم باستخدام كبريتات المغنيسيوم MgSO₄ على البارد (راسب فوري مع الكربونات، وبعد الغليان فقط مع البيكربونات)."
    ],
    "S2": [
        "إضافة الحمض المخفف تؤدي لتصاعد غاز كبريتيد الهيدروجين (H₂S) ذو رائحة البيض الفاسد المميزة.",
        "ورقة الترشيح المبللة بمحلول أسيتات الرصاص تسود فوراً بسبب تكون كبريتيد الرصاص الأسود (PbS).",
        "تحذير سلامة: غاز كبريتيد الهيدروجين غاز سام جداً ويشل العصب الشمي، يُكتشف فقط بأوراق الاختبار تحت شفاط المعمل المعتمد."
    ],
    "SO3": [
        "إضافة الحمض المخفف تؤدي لتصاعد غاز ثاني أكسيد الكبريت (SO₂) الخانق ذو الرائحة النفاذة.",
        "غاز SO₂ عامل مختزل قوي يحول لون ورقة مبللة بثاني كرومات البوتاسيوم المحمضة من البرتقالي إلى الأخضر.",
        "تحذير سلامة: غاز SO₂ مخرش للجهاز التنفسي، يجب التعامل معه داخل شفاط المعمل فقط."
    ],
    "SO4": [
        "محلول كلوريد الباريوم يعطي راسباً أبيض كثيفاً من كبريتات الباريوم (BaSO₄).",
        "تحقق جوهري: راسب BaSO₄ لا يذوب إطلاقاً في حمض HCl أو HNO₃ المخفف (مما يميزه عن كربونات وكبريتيت الباريوم).",
        "أملاح الباريوم سامة؛ يجب التعامل معها بحذر معملي ملائم."
    ],
    "CL": [
        "محلول نترات الفضة يعطي راسباً أبيض متجبناً من كلوريد الفضة (AgCl).",
        "الراسب يتحول للون البنفسجي الرمادي عند تعرضه لضوء الشمس بسبب التفكك الضوئي.",
        "يذوب الراسب بسهولة وبسرعة في محلول النشادر المائي المخفف مكوناً معقد الفضة النشادرى."
    ],
    "BR": [
        "محلول نترات الفضة يعطي راسباً أبيض مصفراً (كريمي) من بروميد الفضة (AgBr).",
        "الراسب شحيح الذوبان في النشادر المخفف، ولكنه يذوب في محلول النشادر المركز.",
        "اختبار ماء الكلور: إضافة ماء الكلور ومذيب عضوي تحرر البروم البرتقالي المحمر الذائب في الطبقة العضوية."
    ],
    "IODIDE": [
        "محلول نترات الفضة يعطي راسباً أصفر فاقعاً من يوديد الفضة (AgI).",
        "الراسب لا يذوب نهائياً في محلول النشادر سواء كان مخففاً أو مركزاً.",
        "اختبار ماء الكلور: يحرر اليود البنفسجي الذي يلون الطبقة العضوية باللون البنفسجي أو يزرق محلول النشا بشدة."
    ],
    "NO3_CHECK": [
        "تجربة الحلقة البنية: اخلط العينة بمحلول كبريتات الحديد الثنائي FeSO₄ حديث التحضير، وأمل الأنبوبة وأضف بحرص حمض H₂SO₄ المركز على الجدار الداخلي.",
        "تتكون حلقة بنية مميزة عند السطح الفاصل بين الطبقتين: معقد النتروزوفيروز.",
        "بديل سبيكة ديفاردا: تسخين محلول النترات مع سبيكة ديفاردا و NaOH يطلق غاز النشادر.",
        "تحذير سلامة: حمض الكبريتيك المركز كاوٍ جداً ويولد حرارة هائلة عند تلامسه مع المحاليل، يجب سكبه بحذر شديد."
    ],
    "ANION_INCONCLUSIVE": [
        "تأكد من أن المحلول الأصلي تم تحضيره بصورة صحيحة (متعادل أو حمضي خفيف) قبل الاختبار بكواشف الترسيب.",
        "إذا لم تتكون رواسب أو تتصاعد غازات، أجرِ تجربة الحلقة البنية الخاصة بالنترات (NO₃⁻).",
        "الأنيونات الأخرى (كالفوسفات PO₄³⁻، والنيتريت NO₂⁻، والFileكبريتات S₂O₃²⁻) تتطلب اختبارات مجموعية نوعية إضافية."
    ]
}

ORGANIC_NOTES_EN = {
    "ORG_FORMIC": [
        "Contains a carboxylic group directly attached to hydrogen, giving it unique aldehyde-like reducing properties.",
        "Effervesces vigorously with NaHCO₃, decolorizes acidified KMnO₄, and forms a shining silver mirror with Tollens' reagent."
    ],
    "ORG_ACETIC": [
        "Characteristic pungent vinegar odor; resists oxidation by acidified potassium permanganate.",
        "Gives an intense blood-red color with neutral FeCl₃ that converts to a reddish-brown precipitate upon boiling."
    ],
    "ORG_FORMALDEHYDE": [
        "Gas dissolved in water at 40% concentration (formalin), with a pungent, suffocating, and lacrimatory odor.",
        "Yields a brick-red precipitate with Fehling's reagent and a silver mirror with Tollens'; completely negative in the iodoform test."
    ],
    "ORG_ACETALDEHYDE": [
        "Volatile liquid completely miscible with water in all proportions; gives a shining silver mirror with Tollens' reagent.",
        "Positive in the iodoform test (forms yellow crystalline CHI₃) due to the presence of the CH₃-C=O methyl carbonyl group."
    ],
    "ORG_BENZALDEHYDE": [
        "Oily liquid sparingly soluble in water, characteristic aromatic bitter almond odor; burns with a smoky sooty black flame.",
        "Forms a silver mirror with Tollens' but is negative with Fehling's solution due to being an aromatic aldehyde."
    ],
    "ORG_ACETONE": [
        "Highly volatile, flammable, pleasantly smelling liquid; miscible with water in all proportions.",
        "Gives a prompt orange precipitate with 2,4-DNP; strongly positive in the iodoform test (yellow crystals); negative with Tollens' and Fehling's."
    ],
    "ORG_ETHYL_METHYL_KETONE": [
        "Volatile liquid with an acetone-like odor; positive with 2,4-DNP and gives a prompt yellow iodoform precipitate.",
        "Resists mild oxidation (Tollens' and Fehling's negative), confirming it as an aliphatic methyl ketone."
    ],
    "ORG_ACETOPHENONE": [
        "High-boiling liquid with a sweet, persistent floral odor; insoluble in water; burns with a dense sooty flame.",
        "Gives a prompt crystalline precipitate with 2,4-DNP and a positive iodoform test; negative with Tollens' and Fehling's."
    ],
    "ORG_ETHANOL": [
        "Volatile liquid completely miscible with water; neutral to litmus and bicarbonate; negative with 2,4-DNP.",
        "Distinctly positive in the iodoform test (yellow crystals with antiseptic odor); turns orange potassium dichromate to emerald green."
    ],
    "ORG_METHANOL": [
        "Light volatile liquid completely miscible with water; completely negative in the iodoform test (distinguishing it from ethanol).",
        "Oxidizes to formaldehyde upon testing with a glowing hot copper spiral, evolving pungent formalin vapors."
    ],
    "ORG_GLYCEROL": [
        "Viscous, heavy, sweet-tasting, non-volatile syrupy liquid; completely miscible with water.",
        "Decolorizes the pink color of borax-phenolphthalein in the cold; evolves pungent, lacrimatory acrolein fumes upon heating with KHSO₄."
    ],
    "ORG_ETHYL_ACETATE": [
        "Immiscible neutral organic liquid with a pleasant fruity odor; neutral to litmus and bicarbonate.",
        "Hydrolyzes with hot dilute NaOH to yield ethanol (iodoform positive) and acetate (blood-red with neutral FeCl₃)."
    ],
    "ORG_ANILINE": [
        "Oily liquid turning yellow to brown on air exposure; insoluble in water but completely dissolves in dilute HCl (basic amine).",
        "Reacts in diazotization at 0-5°C with NaNO₂/HCl, coupling with 2-naphthol to form a brilliant orange-red azo dye."
    ],
    "ORG_OXALIC": [
        "White crystalline solid soluble in water; strongly acidic, effervescing vigorously with NaHCO₃.",
        "Forms an immediate white precipitate with CaCl₂ in the cold, insoluble in acetic acid; rapidly decolorizes warm acidified KMnO₄."
    ],
    "ORG_TARTARIC": [
        "White acidic crystalline solid completely soluble in water; effervesces with NaHCO₃.",
        "Forms a white precipitate with CaCl₂ that dissolves in cold NaOH; positive in Fenton's test (deep violet color); chars with a burnt sugar smell."
    ],
    "ORG_CITRIC": [
        "White acidic solid completely soluble in water; effervesces with sodium bicarbonate.",
        "Forms a white calcium citrate precipitate with CaCl₂ only upon boiling (distinguishing it from oxalic and tartaric acids)."
    ],
    "ORG_BENZOIC": [
        "White crystalline solid insoluble in cold water; dissolves in NaHCO₃ with effervescence; burns with a dense sooty flame.",
        "Neutral solution gives a characteristic flesh-colored buff precipitate of ferric benzoate with neutral FeCl₃."
    ],
    "ORG_SALICYLIC": [
        "White needle-like crystals sparingly soluble in cold water; dissolves in NaHCO₃ with effervescence; phenolic carboxylic acid.",
        "Gives an intense, persistent, deep violet coloration with FeCl₃ that does not disappear with excess reagent."
    ],
    "ORG_PHENOL": [
        "Pinkish crystalline masses with a characteristic carbolic odor; partially soluble in cold water; turns blue litmus faint red.",
        "Forms a white precipitate of 2,4,6-tribromophenol with bromine water, and gives a deep violet color with neutral FeCl₃."
    ],
    "ORG_RESORCINOL": [
        "White to light pink crystalline solid soluble in water; dihydric phenol.",
        "Gives a prompt dark violet color with FeCl₃; phthalein reaction with phthalic anhydride produces intensely green fluorescent fluorescein."
    ],
    "ORG_ALPHA_NAPHTHOL": [
        "Solid insoluble in cold water; burns with a heavy smoky flame; mono-hydroxy naphthalene.",
        "Gives a transient deep violet coloration with bleaching powder solution that immediately converts into a dense reddish-brown precipitate."
    ],
    "ORG_BETA_NAPHTHOL": [
        "Crystalline solid insoluble in cold water; burns with a heavy smoky flame; position isomer of alpha-naphthol.",
        "Gives no violet color with bleaching powder; couples with diazotized aniline to form an intense scarlet-red azo dye."
    ],
    "ORG_GLUCOSE": [
        "White crystalline solid soluble in water; reducing aldohexose; positive in Molisch's test (purple ring at interface).",
        "Promptly reduces Fehling's solution to red Cu₂O; forms yellow needle-like phenylglucosazone crystals in 4-5 minutes; negative in Seliwanoff's test within 2 minutes."
    ],
    "ORG_FRUCTOSE": [
        "White crystalline solid soluble in water; reducing ketohexose; positive in Molisch's test.",
        "Strongly positive in Seliwanoff's test (develops a deep red color within 1-2 minutes); reduces Fehling's solution; forms identical glucosazone crystals."
    ],
    "ORG_STARCH": [
        "White non-crystalline powder insoluble in cold water, forming a colloidal opalescent solution on boiling; non-reducing polysaccharide.",
        "Gives an intense deep blue complex with iodine solution (Lugol's) that vanishes upon heating and reappears on cooling."
    ],
    "ORG_UREA": [
        "White crystalline neutral solid soluble in water; non-reducing, negative with Molisch and FeCl₃.",
        "Melts upon dry heating evolving ammonia gas; residue gives a positive biuret test (violet-pink color with alkaline CuSO₄)."
    ]
}


# -*- coding: utf-8 -*-
"""
Option translations for all Arabic options in the decision trees
"""

OPTION_TRANSLATIONS_EN = {
    'لا تغيير / لا يتكون راسب على البارد': 'No change / no precipitate in the cold',
    'لا تغيير / يظل راسباً': 'No change / remains as precipitate',
    'لا تغيير / لا يتصاعد غاز بعد التسخين': 'No change / no gas evolved after heating',
    'لا يتكون راسب / لا تغيير': 'No precipitate forms / no change',
    'لا يذوب الراسب إطلاقاً في حمض HCl المخفف أو المركز': 'Precipitate is completely insoluble in dilute or concentrated HCl',
    'لا يتكون أي راسب': 'No precipitate formed',
    'ظهور لون أحمر دامي مميز عند إضافة كلوريد الحديد الثلاثي المتعادل': 'Appearance of characteristic blood-red coloration with neutral FeCl₃',
    'لا تغيير واضح / لا تفاعل': 'No obvious change / no reaction',
    'فوران وتصاعد فقاعات غاز ثاني أكسيد الكربون CO2 (حمض كربوكسيلي سائل)': 'Effervescence with CO₂ bubbles (Liquid carboxylic acid)',
    'لا يحدث فوران (المركب متعادل — ألدهيد، كيتون، أو كحول)': 'No effervescence (Neutral compound: Aldehyde, Ketone, or Alcohol)',
    'لا يتكون أي راسب ويظل المحلول رائقاً أصفر شفافاً (كحول أليفاتي)': 'No precipitate; solution remains clear transparent yellow (Aliphatic alcohol)',
    'لا تتكون مرآة فضية ويظل المحلول صافياً بدون اختزال (كيتون — أسيتون)': 'No silver mirror forms; solution remains clear (Ketone — Acetone)',
    'سلبي تماماً مع اليودوفورم، وله رائحة نفاذة خانقة مدمعة ويعطي راسباً أحمر مع فهلنج (فورمالدهيد)': 'Negative with iodoform; pungent lacrimatory odor, red ppt with Fehling (Formaldehyde)',
    'سلبي تماماً مع اليودوفورم؛ وعند تسخينه مع حمض الساليسيليك وH2SO4 يعطي رائحة إستر الكافور (ميثانول)': 'Negative with iodoform; heating with salicylic acid yields wintergreen ester odor (Methanol)',
    'سلبي مع كاشف تولن؛ يعطي راسباً أصفر متبلوراً في اختبار اليودوفورم (قد يتجمد في الشتاء < 20°م) (أسيتوفينون)': 'Negative with Tollens; yellow iodoform ppt, freezes below 20°C (Acetophenone)',
    'شحيحة الذوبان أو عديمة الذوبان في الماء البارد (Insoluble / Sparingly Soluble Solids)': 'Sparingly or insoluble in cold water (Insoluble / Sparingly soluble solids)',
    'فوران شديد وتصاعد فقاعات غاز CO2 (حمض كربوكسيلي أليفاتي صلب ذائب بالماء)': 'Vigorous effervescence with CO₂ bubbles (Water-soluble solid aliphatic carboxylic acid)',
    'لا يحدث أي فوران مع بيكربونات الصوديوم (مركب متعادل، سكر، أو فينول ذائب)': 'No effervescence with NaHCO₃ (Neutral compound, sugar, or soluble phenol)',
    'لا يتكون أي راسب على البارد، ولكن يتكون راسب أبيض فقط بعد الغليان الشديد لعدة دقائق (حمض الستريك)': 'No precipitate in the cold; white ppt forms only after boiling for several minutes (Citric acid)',
    'لا تتكون حلقة بنفسجية (سلبي مع موليش — ليس كربوهيدرات: ريسورسينول أو يوريا)': 'No purple ring (Negative with Molisch: Resorcinol or Urea)',
    'لا يتكون أي راسب أحمر ويظل المحلول أزرق صافياً (سكر غير مختزل مباشرة — سكروز)': 'No red precipitate; solution remains clear blue (Non-reducing sugar — Sucrose)',
    'ظهور لون أحمر كرزي / قرمزي داكن فوري وسريع جداً خلال أقل من دقيقتين (سكر كيتوزي — فركتوز)': 'Rapid intense cherry-red color within 1-2 minutes (Ketose sugar — Fructose)',
    'لا تفور مع بيكربونات الصوديوم ولكنها تذوب تماماً في هيدروكسيد الصوديوم NaOH (فينولات ونافثولات)': 'Does not effervesce with NaHCO₃ but completely dissolves in NaOH (Phenols and Naphthols)',
    'لا تفور مع البيكربونات ولا تذوب في NaOH على البارد، وتكوّن معلقاً غروياً عند الغليان بالماء (نشا)': 'Does not effervesce or dissolve in cold NaOH; forms colloidal solution on boiling (Starch)',

    # Colors
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

    # Physical State & Solubility
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

    # Heating & Flame Charring Test
    "انصهار وتفحم وتصاعد أدخنة أو رائحة سكر محروق (مركب عضوي)": "Melting, charring, and evolution of fumes or burnt sugar smell (Organic Compound)",
    "انصهار وتفحم / رائحة سكر محروق (عضوي)": "Melting and charring / burnt sugar smell (Organic)",
    "لا تفحم، بقاء راسب معدني ثابت مع تغير اللون أثناء التسخين أو أبخرة غير متفحمة (مركب غير عضوي)": "No charring, stable mineral residue with color change on heating or non-charring vapors (Inorganic Compound)",
    "لا تفحم / بقاء مادة معدنية ثابتة (غير عضوي)": "No charring / stable mineral residue (Inorganic)",

    # First Reagent Reactions
    "فوران وتصاعد غاز": "Effervescence and gas evolution",
    "راسب أبيض": "White precipitate",
    "لا تغيير / لا يتكون راسب أو غاز": "No change / no precipitate or gas formed",
    "تغير لون المحلول": "Solution color changes",
    "أخرى": "Other observation",

    # Gas Observations
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

    # Dilute HCl / Group I Reactions
    "نعم (يذوب بالماء الساخن المغلي ويعود للترسيب بالتبريد)": "Yes (dissolves in boiling hot water and recrystallizes upon cooling)",
    "نعم (يذوب بالماء الساخن)": "Yes (dissolves in hot water)",
    "لا يذوب في الماء الساخن، ولكن يذوب في محلول النشادر المخفف": "Does not dissolve in hot water, but dissolves in dilute ammonia",
    "لا (يذوب في النشادر المخفف)": "No (dissolves in dilute ammonia)",
    "لا يذوب في الماء الساخن، ويسود الراسب عند إضافة محلول النشادر": "Does not dissolve in hot water, and precipitate blackens with ammonia",
    "لا (ويسود بمحلول النشادر)": "No (blackens with ammonia)",

    # NaOH Addition Reactions
    "راسب أزرق": "Blue precipitate",
    "راسب أخضر": "Green precipitate",
    "راسب بني محمر جيلاتيني": "Reddish-brown gelatinous precipitate",
    "راسب أبيض يتأكسد ويتحول إلى بني بالهواء": "White precipitate oxidizing and turning brown in air",
    "راسب أبيض": "White precipitate",
    "يظل لونه أخضر ثابتاً": "Remains green and stable",
    "يتحول السطح تدريجياً إلى بني محمر نتيجة التأكسد": "Surface gradually turns reddish-brown due to oxidation",
    "أزرق داكن (محلول معقد أزرق ملكي ساطع)": "Deep royal blue solution (Tetraamminecopper complex)",
    "نعم، يذوب الراسب في الزيادة من NaOH مع الرج": "Yes, precipitate dissolves in excess NaOH with shaking",
    "لا، لا يذوب الراسب في الزيادة من NaOH": "No, precipitate does not dissolve in excess NaOH",
    "نعم، يذوب الراسب في زيادة الأمونيا": "Yes, precipitate dissolves in excess ammonia",
    "لا، لا يذوب الراسب في زيادة الأمونيا": "No, precipitate does not dissolve in excess ammonia",

    # Flame Tests
    "لهب أحمر طوبي (brick-red flame) وراسب أبيض مع الأوكسالات": "Brick-red flame and white precipitate with ammonium oxalate (Ca²⁺)",
    "لا يوجد لون مميز للهب (راسب أبيض ثابت يعطي لوناً مع الماغنسون)": "No distinctive flame color (White precipitate giving blue color with Magneson, Mg²⁺)",
    "يذوب في الماء الساخن ويعود بالتبريد": "Dissolves in hot water and recrystallizes on cooling",

    # Heating Test (Dry Tube)
    "تصاعد غاز النشادر (رائحة نفاذة يزرق ورقة تباع الشمس المبللة)": "Evolution of ammonia gas (Pungent odor turning moist red litmus blue)",

    # BaCl₂ Reactions
    "يذوب الراسب في حمض HCl مع فوران وتصاعد غاز CO₂": "Precipitate dissolves in HCl with effervescence evolving CO₂ gas",
    "يذوب الراسب في حمض HCl مع تصاعد غاز SO₂ الخانق": "Precipitate dissolves in HCl evolving suffocating SO₂ gas",
    "يذوب الراسب في حمض HCl دون فوران (يعطي راسباً أصفر مع الموليبدات)": "Precipitate dissolves in HCl without gas (Forms yellow precipitate with ammonium molybdate)",
    "لا يذوب الراسب إطلاقاً في حمض HCl المخفف الساخن": "Precipitate is completely insoluble in hot dilute HCl (BaSO₄)",

    # Silver Nitrate Reactions
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

    # Conc. H₂SO₄ Reaction
    "تكون حلقة بنية فاصلة عند السطح الفاصل بين الطبقتين (الحلقة البنية)": "Formation of a brown ring at the liquid junction (Brown Ring Test, Nitrate)",

    # Organic Liquid Diagnosis Questions
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

    # Organic Solid Diagnosis Questions
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
}


# Enrich CATION_OUTCOMES with Arabic and English notes
for _k, _notes in CATION_NOTES_AR.items():
    if _k in CATION_OUTCOMES:
        CATION_OUTCOMES[_k]["notes_ar"] = _notes
        if "notes_en" not in CATION_OUTCOMES[_k]:
            CATION_OUTCOMES[_k]["notes_en"] = list(CATION_OUTCOMES[_k]["notes"])

# Enrich ANION_OUTCOMES with Arabic and English notes
for _k, _notes in ANION_NOTES_AR.items():
    if _k in ANION_OUTCOMES:
        ANION_OUTCOMES[_k]["notes_ar"] = _notes
        if "notes_en" not in ANION_OUTCOMES[_k]:
            ANION_OUTCOMES[_k]["notes_en"] = list(ANION_OUTCOMES[_k]["notes"])

# Enrich ORGANIC_OUTCOMES with Arabic and English notes
for _k, _notes in ORGANIC_NOTES_EN.items():
    if _k in ORGANIC_OUTCOMES:
        ORGANIC_OUTCOMES[_k]["notes_en"] = _notes
        if "notes_ar" not in ORGANIC_OUTCOMES[_k]:
            ORGANIC_OUTCOMES[_k]["notes_ar"] = list(ORGANIC_OUTCOMES[_k]["notes"])

import re
# Enrich all options in UNIFIED_DECISION_TREE with label_en and English labels
for _qid, _q in UNIFIED_DECISION_TREE.items():
    if _q.get("kind") == "question":
        for _opt in _q.get("options", []):
            _lbl = _opt.get("label", "")
            _ar_lbl = _opt.get("arabic_label", "")
            if _lbl in OPTION_TRANSLATIONS_EN:
                _opt["label_en"] = OPTION_TRANSLATIONS_EN[_lbl]
                if re.search(r'[\u0600-\u06FF]', _lbl):
                    if not _ar_lbl:
                        _opt["arabic_label"] = _lbl
                    _opt["label"] = OPTION_TRANSLATIONS_EN[_lbl]
            elif _ar_lbl in OPTION_TRANSLATIONS_EN:
                _opt["label_en"] = OPTION_TRANSLATIONS_EN[_ar_lbl]
                if re.search(r'[\u0600-\u06FF]', _lbl):
                    _opt["label"] = OPTION_TRANSLATIONS_EN[_ar_lbl]

