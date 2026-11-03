"""
Inorganic Salt Diagnosis Module — 30 Complete Salts
Qualitative Analysis of Unknown Inorganic Salts (Anion & Cation Diagnostic Trees)
"""

import math

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


# 2. بيانات الأنيونات والكاتيونات ومعادلاتها (ANIONS_DATA & CATIONS_DATA)
ANIONS_DATA = {
    "CO3": {
        "symbol": "CO₃²⁻",
        "name_ar": "كربونات",
        "name_en": "Carbonate",
        "group": "مجموعة حمض الهيدروكلوريك المخفف (Dil. HCl)",
        "equations": [
            "CO₃²⁻ + 2H⁺ → CO₂ ↑ + H₂O",
            "CO₂ + Ca(OH)₂ → CaCO₃ ↓ (White) + H₂O",
            "CO₃²⁻ + Mg²⁺ → MgCO₃ ↓ (White on cold)"
        ],
        "summary": "يتصاعد غاز ثاني أكسيد الكربون بفوران ويعكر ماء الجير الرائق، ويعطي راسباً أبيض على البارد مع كبريتات المغنيسيوم."
    },
    "HCO3": {
        "symbol": "HCO₃⁻",
        "name_ar": "بيكربونات",
        "name_en": "Bicarbonate",
        "group": "مجموعة حمض الهيدروكلوريك المخفف (Dil. HCl)",
        "equations": [
            "HCO₃⁻ + H⁺ → CO₂ ↑ + H₂O",
            "2HCO₃⁻ + Mg²⁺ → Mg(HCO₃)₂ (Soluble on cold)",
            "Mg(HCO₃)₂ ──Δ──> MgCO₃ ↓ (White after boiling) + H₂O + CO₂ ↑"
        ],
        "summary": "يتصاعد غاز ثاني أكسيد الكربون بفوران ويعكر ماء الجير، ويعطي راسباً أبيض مع كبريتات المغنيسيوم بعد الغليان فقط."
    },
    "SO3": {
        "symbol": "SO₃²⁻",
        "name_ar": "كبريتيت",
        "name_en": "Sulfite",
        "group": "مجموعة حمض الهيدروكلوريك المخفف (Dil. HCl)",
        "equations": [
            "SO₃²⁻ + 2H⁺ → SO₂ ↑ + H₂O",
            "3SO₂ + Cr₂O₇²⁻ + 2H⁺ → 3SO₄²⁻ + 2Cr³⁺ (Green) + H₂O",
            "SO₃²⁻ + 2Ag⁺ → Ag₂SO₃ ↓ (White turns black on heating)"
        ],
        "summary": "يتصاعد غاز ثاني أكسيد الكبريت ذو الرائحة النفاذة الذي يخضر ورقة مبللة بثاني كرومات البوتاسيوم المحمضة، ويكون راسباً أبيض مع نترات الفضة يسود بالتسخين."
    },
    "S2O3": {
        "symbol": "S₂O₃²⁻",
        "name_ar": "ثيوكبريتات",
        "name_en": "Thiosulfate",
        "group": "مجموعة حمض الهيدروكلوريك المخفف (Dil. HCl)",
        "equations": [
            "S₂O₃²⁻ + 2H⁺ → SO₂ ↑ + S ↓ (Yellow) + H₂O",
            "2S₂O₃²⁻ + I₂ (Brown) → S₄O₆²⁻ (Colorless) + 2I⁻"
        ],
        "summary": "يتصاعد غاز ثاني أكسيد الكبريت مع ظهور راسب أصفر معلق من الكبريت، ويزيل محلولُه لونَ اليود البني."
    },
    "S": {
        "symbol": "S²⁻",
        "name_ar": "كبريتيد",
        "name_en": "Sulfide",
        "group": "مجموعة حمض الهيدروكلوريك المخفف (Dil. HCl)",
        "equations": [
            "S²⁻ + 2H⁺ → H₂S ↑",
            "H₂S + Pb(CH₃COO)₂ → PbS ↓ (Black) + 2CH₃COOH",
            "S²⁻ + 2Ag⁺ → Ag₂S ↓ (Black)"
        ],
        "summary": "يتصاعد غاز كبريتيد الهيدروجين ذو الرائحة الكريهة الذي يسود ورقة مبللة بأسيتات الرصاص، ويعطي راسباً أسود مع نترات الفضة."
    },
    "NO2": {
        "symbol": "NO₂⁻",
        "name_ar": "نيتريت",
        "name_en": "Nitrite",
        "group": "مجموعة حمض الهيدروكلوريك المخفف (Dil. HCl)",
        "equations": [
            "NO₂⁻ + H⁺ → HNO₂",
            "3HNO₂ → HNO₃ + 2NO ↑ + H₂O",
            "2NO + O₂ → 2NO₂ ↑ (Reddish-Brown at tube mouth)",
            "5NO₂⁻ + 2MnO₄⁻ + 6H⁺ → 5NO₃⁻ + 2Mn²⁺ (Colorless) + 3H₂O"
        ],
        "summary": "يتصاعد غاز أكسيد النيتريك عديم اللون الذي يتحول عند فوهة الأنبوبة إلى أبخرة بنية حمراء، ويزيل لون برمنجنات البوتاسيوم المحمضة."
    },
    "CL": {
        "symbol": "Cl⁻",
        "name_ar": "كلوريد",
        "name_en": "Chloride",
        "group": "مجموعة حمض الكبريتيك المركز (Conc. H₂SO₄)",
        "equations": [
            "2Cl⁻ + H₂SO₄ ──Δ──> SO₄²⁻ + 2HCl ↑",
            "HCl + NH₃ → NH₄Cl (Dense white fumes)",
            "Ag⁺ + Cl⁻ → AgCl ↓ (White, soluble in dilute NH₃)"
        ],
        "summary": "يتصاعد غاز كلوريد الهيدروجين الذي يكون سحباً بيضاء مع النشادر، ويعطي راسباً أبيض مع نترات الفضة يذوب بسهولة في النشادر المخفف."
    },
    "BR": {
        "symbol": "Br⁻",
        "name_ar": "بروميد",
        "name_en": "Bromide",
        "group": "مجموعة حمض الكبريتيك المركز (Conc. H₂SO₄)",
        "equations": [
            "2Br⁻ + 2H₂SO₄ ──Δ──> SO₄²⁻ + Br₂ ↑ (Orange-Red) + SO₂ ↑ + 2H₂O",
            "Ag⁺ + Br⁻ → AgBr ↓ (Cream/Pale-yellow, slowly soluble in conc. NH₃)"
        ],
        "summary": "تتصاعد أبخرة البروم البرتقالية الحمراء التي تصفر ورقة النشا، ويعطي راسباً أبيض مصفراً (كريمياً) مع نترات الفضة يذوب ببطء في النشادر المركز."
    },
    "I": {
        "symbol": "I⁻",
        "name_ar": "يوديد",
        "name_en": "Iodide",
        "group": "مجموعة حمض الكبريتيك المركز (Conc. H₂SO₄)",
        "equations": [
            "2I⁻ + 2H₂SO₄ ──Δ──> SO₄²⁻ + I₂ ↑ (Violet) + SO₂ ↑ + 2H₂O",
            "Ag⁺ + I⁻ → AgI ↓ (Yellow, insoluble in NH₃)"
        ],
        "summary": "تتصاعد أبخرة اليود البنفسجية التي تزرق ورقة النشا، ويعطي راسباً أصفر مع نترات الفضة لا يذوب في محلول النشادر."
    },
    "NO3": {
        "symbol": "NO₃⁻",
        "name_ar": "نترات",
        "name_en": "Nitrate",
        "group": "مجموعة حمض الكبريتيك المركز (Conc. H₂SO₄)",
        "equations": [
            "NO₃⁻ + H₂SO₄ ──Δ──> HSO₄⁻ + HNO₃",
            "4HNO₃ + Cu ──Δ──> Cu(NO₃)₂ + 2NO₂ ↑ (Reddish-Brown) + 2H₂O",
            "6FeSO₄ + 2NaNO₃ + 4H₂SO₄ → 3Fe₂(SO₄)₃ + Na₂SO₄ + 4H₂O + 2NO",
            "FeSO₄ + NO → [Fe(H₂O)₅(NO)]SO₄ (Brown Ring)"
        ],
        "summary": "تتصاعد أبخرة بنية حمراء كثيفة بالتسخين مع حمض الكبريتيك المركز وخراطة النحاس، ويعطي حلقة بنية في تجربة الحلقة البنية."
    },
    "SO4": {
        "symbol": "SO₄²⁻",
        "name_ar": "كبريتات",
        "name_en": "Sulfate",
        "group": "مجموعة محلول كلوريد الباريوم (BaCl₂)",
        "equations": [
            "Ba²⁺ + SO₄²⁻ → BaSO₄ ↓ (White, insoluble in dil. HCl)",
            "Pb²⁺ + SO₄²⁻ → PbSO₄ ↓ (White)"
        ],
        "summary": "يعطي راسباً أبيض مع كلوريد الباريوم لا يذوب في حمض الهيدروكلوريك المخفف، وراسباً أبيض مع أسيتات الرصاص."
    },
    "PO4": {
        "symbol": "PO₄³⁻",
        "name_ar": "فوسفات",
        "name_en": "Phosphate",
        "group": "مجموعة محلول كلوريد الباريوم (BaCl₂)",
        "equations": [
            "3Ba²⁺ + 2PO₄³⁻ → Ba₃(PO₄)₂ ↓ (White, soluble in dil. HCl)",
            "3Ag⁺ + PO₄³⁻ → Ag₃PO₄ ↓ (Yellow, soluble in NH₃ and HNO₃)"
        ],
        "summary": "يعطي راسباً أبيض مع كلوريد الباريوم يذوب في حمض الهيدروكلوريك المخفف، وراسباً أصفر مع نترات الفضة."
    }
}

CATIONS_DATA = {
    "PB": {
        "symbol": "Pb²⁺",
        "name_ar": "الرصاص الثنائي",
        "name_en": "Lead(II)",
        "group": "المجموعة التحليلية الأولى (كاشفها Dil. HCl)",
        "equations": [
            "Pb²⁺ + 2Cl⁻ → PbCl₂ ↓ (White, soluble in hot water)",
            "Pb²⁺ + 2I⁻ → PbI₂ ↓ (Bright Yellow)"
        ],
        "summary": "يترسب على هيئة كلوريد رصاص أبيض يذوب في الماء الساخن، ويعطي راسباً أصفر فاقعاً مع يوديد البوتاسيوم."
    },
    "CU": {
        "symbol": "Cu²⁺",
        "name_ar": "النحاس الثنائي",
        "name_en": "Copper(II)",
        "group": "المجموعة التحليلية الثانية / كواشف الهيدروكسيد",
        "equations": [
            "Cu²⁺ + 2OH⁻ → Cu(OH)₂ ↓ (Blue)",
            "Cu(OH)₂ ──Δ──> CuO ↓ (Black) + H₂O",
            "Cu(OH)₂ + 4NH₃ → [Cu(NH₃)₄]²⁺ (Deep Blue Solution) + 2OH⁻"
        ],
        "summary": "يعطي راسباً أزرق مع هيدروكسيد الصوديوم يسود بالتسخين، ويذوب في الزيادة من النشادر مكوناً محلولاً أزرق قاتماً."
    },
    "FE2": {
        "symbol": "Fe²⁺",
        "name_ar": "الحديد الثنائي",
        "name_en": "Iron(II)",
        "group": "المجموعة التحليلية الثالثة",
        "equations": [
            "Fe²⁺ + 2OH⁻ → Fe(OH)₂ ↓ (White-Green)",
            "4Fe(OH)₂ + O₂ + 2H₂O → 4Fe(OH)₃ (Reddish-Brown in air)",
            "3Fe²⁺ + 2[Fe(CN)₆]³⁻ → Fe₃[Fe(CN)₆]₂ ↓ (Turnbull's Blue)"
        ],
        "summary": "يعطي راسباً أبيض مخضراً مع هيدروكسيد الصوديوم أو الأمونيوم لا يذوب في الزيادة، وراسباً أزرق قاتماً مع حديديسيانيد البوتاسيوم."
    },
    "FE3": {
        "symbol": "Fe³⁺",
        "name_ar": "الحديد الثلاثي",
        "name_en": "Iron(III)",
        "group": "المجموعة التحليلية الثالثة",
        "equations": [
            "Fe³⁺ + 3OH⁻ → Fe(OH)₃ ↓ (Reddish-Brown gelatinous)",
            "Fe³⁺ + 3SCN⁻ → Fe(SCN)₃ (Blood-Red coloration)"
        ],
        "summary": "يعطي راسباً جيلاتينياً بنياً محمراً مع هيدروكسيد الصوديوم أو الأمونيوم، ولوناً أحمر دامياً مع ثيوسيانات البوتاسيوم."
    },
    "AL": {
        "symbol": "Al³⁺",
        "name_ar": "الألومنيوم",
        "name_en": "Aluminium",
        "group": "المجموعة التحليلية الثالثة",
        "equations": [
            "Al³⁺ + 3OH⁻ → Al(OH)₃ ↓ (White gelatinous)",
            "Al(OH)₃ + OH⁻ → [Al(OH)₄]⁻ (Soluble in excess NaOH)",
            "Al³⁺ + 3NH₃ + 3H₂O → Al(OH)₃ ↓ + 3NH₄⁺ (Insoluble in excess NH₃)"
        ],
        "summary": "يعطي راسباً أبيض جيلاتينياً يذوب في الزيادة من هيدروكسيد الصوديوم، ولكنه لا يذوب في الزيادة من محلول النشادر."
    },
    "ZN": {
        "symbol": "Zn²⁺",
        "name_ar": "الزنك (الخارصين)",
        "name_en": "Zinc",
        "group": "المجموعة التحليلية الرابعة",
        "equations": [
            "Zn²⁺ + 2OH⁻ → Zn(OH)₂ ↓ (White)",
            "Zn(OH)₂ + 2OH⁻ → [Zn(OH)₄]²⁻ (Soluble in excess NaOH)",
            "Zn(OH)₂ + 4NH₃ ⇌ [Zn(NH₃)₄]²⁺ + 2OH⁻ (Soluble in excess NH₃)"
        ],
        "summary": "يعطي راسباً أبيض يذوب في كل من الزيادة من هيدروكسيد الصوديوم والزيادة من محلول النشادر."
    },
    "CA": {
        "symbol": "Ca²⁺",
        "name_ar": "الكالسيوم",
        "name_en": "Calcium",
        "group": "المجموعة التحليلية الخامسة",
        "equations": [
            "Ca²⁺ + CO₃²⁻ → CaCO₃ ↓ (White)",
            "Ca²⁺ + SO₄²⁻ → CaSO₄ ↓ (White)",
            "Ca²⁺ (Flame Test) → Brick-Red Flame"
        ],
        "summary": "يعطي راسباً أبيض مع كربونات الأمونيوم وحمض الكبريتيك المخفف، ويلون لهب بنزن باللون الأحمر الطوبي."
    },
    "BA": {
        "symbol": "Ba²⁺",
        "name_ar": "الباريوم",
        "name_en": "Barium",
        "group": "المجموعة التحليلية الخامسة",
        "equations": [
            "Ba²⁺ + CO₃²⁻ → BaCO₃ ↓ (White)",
            "Ba²⁺ + CrO₄²⁻ → BaCrO₄ ↓ (Yellow)",
            "Ba²⁺ (Flame Test) → Apple-Green Flame"
        ],
        "summary": "يعطي راسباً أصفر مع كرومات البوتاسيوم، ويلون لهب بنزن باللون الأخضر التفاحي."
    },
    "MG": {
        "symbol": "Mg²⁺",
        "name_ar": "المغنيسيوم",
        "name_en": "Magnesium",
        "group": "المجموعة التحليلية السادسة",
        "equations": [
            "Mg²⁺ + 2OH⁻ → Mg(OH)₂ ↓ (White, insoluble in excess NaOH)",
            "Mg²⁺ + NH₄⁺ + PO₄³⁻ → Mg(NH₄)PO₄ ↓ (White crystalline)"
        ],
        "summary": "يعطي راسباً أبيض مع هيدروكسيد الصوديوم لا يذوب في الزيادة، وراسباً أبيض بلورياً مع فوسفات الصوديوم النشادرية، ولا يلون اللهب."
    },
    "NH4": {
        "symbol": "NH₄⁺",
        "name_ar": "الأمونيوم",
        "name_en": "Ammonium",
        "group": "المجموعة التحليلية السادسة",
        "equations": [
            "NH₄⁺ + OH⁻ ──Δ──> NH₃ ↑ + H₂O",
            "NH₃ + HCl → NH₄Cl (White fumes)",
            "NH₄⁺ + 2[HgI₄]²⁻ + 4OH⁻ → HgO·Hg(NH₂)I ↓ (Reddish-Brown) + 7I⁻ + 3H₂O"
        ],
        "summary": "لا يعطي راسباً مع هيدروكسيد الصوديوم، ويتصاعد بالتسخين غاز النشادر الذي يزرق عباد الشمس ويعطي راسباً بنياً محمراً مع كاشف نيسلر."
    },
    "NA": {
        "symbol": "Na⁺",
        "name_ar": "الصوديوم",
        "name_en": "Sodium",
        "group": "المجموعة التحليلية السادسة (الفلزات القلوية)",
        "equations": [
            "Na⁺ (No precipitate with standard group reagents)",
            "Na⁺ (Dry Flame Test) → Golden-Yellow Flame"
        ],
        "summary": "جميع أملاحه الشائعة تذوب في الماء ولا يترسب بالكواشف العادية، ويكشف عنه بتلوين لهب بنزن باللون الأصفر الذهبي."
    },
    "K": {
        "symbol": "K⁺",
        "name_ar": "البوتاسيوم",
        "name_en": "Potassium",
        "group": "المجموعة التحليلية السادسة (الفلزات القلوية)",
        "equations": [
            "K⁺ (No precipitate with standard group reagents)",
            "K⁺ (Dry Flame Test) → Pale Violet / Lilac Flame"
        ],
        "summary": "جميع أملاحه الشائعة تذوب في الماء، ويكشف عنه بتلوين لهب بنزن باللون البنفسجي الفاتح (الليلكي)."
    }
}

# 3. شجرة أسئلة الكشف الكاملة (SALT_DIAGNOSIS_NODES)
SALT_DIAGNOSIS_NODES = {
    # ================== المرحلة 0: الفحص الفيزيائي للملح ==================
    "SALT_START": {
        "kind": "question",
        "phase": "physical",
        "text": "Step 1 (Physical Examination): What is the color of the unknown solid salt?",
        "arabic_text": "الخطوة 1 (الفحص الفيزيائي): ما هو لون الملح الصلب المجهول أمامك؟",
        "hint": "Solid salt color provides a strong preliminary indication of transition metal cations (e.g., copper and iron).",
        "arabic_hint": "لون الملح الصلب يعطي مؤشراً استباقياً قوياً حول الكاتيونات الانتقالية (مثل النحاس والحديد).",
        "options": [
            {"label": "White or colorless crystals", "arabic_label": "أبيض أو بلورات عديمة اللون", "next": "SALT_SOLUBILITY", "swatch": WHITE},
            {"label": "Blue or blue-green", "arabic_label": "أزرق أو أزرق مخضر", "next": "SALT_SOLUBILITY", "swatch": BLUE},
            {"label": "Pale green", "arabic_label": "أخضر باهت", "next": "SALT_SOLUBILITY", "swatch": GREEN},
            {"label": "Yellow, reddish-brown, or grayish-black", "arabic_label": "أصفر أو بني محمر / أسود رمادي", "next": "SALT_SOLUBILITY", "swatch": BROWN}
        ]
    },
    "SALT_SOLUBILITY": {
        "kind": "question",
        "phase": "physical",
        "text": "Step 2 (Solubility): Add a small sample of the salt to cold distilled water with shaking. What do you observe?",
        "arabic_text": "الخطوة 2 (الذوبانية): أضف عينة صغيرة من الملح إلى الماء المقطر البارد مع الرج، ماذا تلاحظ؟",
        "hint": "Water solubility determines how the stock solution is prepared and narrows anion possibilities.",
        "arabic_hint": "الذوبان في الماء يحدد طريقة تحضير المحلول الأصلي ويحصر احتمالات الأنيونات.",
        "options": [
            {"label": "Dissolves in cold water forming a clear solution", "arabic_label": "يذوب في الماء البارد مكوناً محلولاً رائقاً", "next": "ANION_HCL_TEST", "swatch": NONE},
            {"label": "Insoluble or sparingly soluble in cold water", "arabic_label": "لا يذوب أو شحيح الذوبان جداً في الماء البارد", "next": "ANION_HCL_TEST", "swatch": WHITE}
        ]
    },

    # ================== المرحلة 1: شجرة الكشف عن الأنيون (Anion Tree) ==================
    "ANION_HCL_TEST": {
        "kind": "question",
        "phase": "anion",
        "text": "Step 3 (Acidic Radical - Group 1): Add dilute hydrochloric acid (Dil. HCl) to the solid salt. What do you observe?",
        "arabic_text": "الخطوة 3 (كشف الشق الحامضي - المجموعة الأولى): أضف حمض الهيدروكلوريك المخفف (Dil. HCl) إلى الملح الصلب، ماذا تلاحظ؟",
        "hint": "Dilute HCl displaces weaker, volatile acids as characteristic gases.",
        "arabic_hint": "حمض HCl المخفف يطرد الأحماض الأضعف والأقل ثباتاً على هيئة غازات مميزة.",
        "options": [
            {"label": "Effervescence with colorless, odorless gas that turns clear lime water milky (CO₂)", "arabic_label": "حدوث فوران وتصاعد غاز عديم اللون والرائحة يعكر ماء الجير الرائق (CO₂)", "next": "ANION_CO3_CONFIRM", "swatch": WHITE},
            {"label": "Choking pungent gas (SO₂) that turns acidified potassium dichromate paper green", "arabic_label": "تصاعد غاز ذي رائحة نفاذة خانقة (SO₂) يخضر ورقة مبللة بثاني كرومات البوتاسيوم المحمضة", "next": "ANION_SO2_CHECK", "swatch": GREEN},
            {"label": "Foul rotten-egg odor gas (H₂S) that turns lead acetate paper black", "arabic_label": "تصاعد غاز كريه الرائحة (رائحة البيض الفاسد H₂S) يسود ورقة مبللة بأسيتات الرصاص", "next": "SET_ANION_S", "swatch": BLACK},
            {"label": "Colorless gas turning into reddish-brown fumes (NO₂) at the mouth of the tube", "arabic_label": "تصاعد غاز عديم اللون يتحول عند فوهة الأنبوبة إلى أبخرة بنية حمراء (NO₂)", "next": "SET_ANION_NO2", "swatch": BROWN},
            {"label": "No effervescence and no gas evolved", "arabic_label": "لم يحدث فوران ولم يتصاعد أي غاز", "next": "ANION_H2SO4_TEST", "swatch": NONE}
        ]
    },
    "ANION_CO3_CONFIRM": {
        "kind": "question",
        "phase": "anion",
        "text": "Confirmatory test to distinguish Carbonate from Bicarbonate: Add magnesium sulfate (MgSO₄) solution to salt solution:",
        "arabic_text": "تجربة تأكيدية للتفرقة بين الكربونات والبيكربونات: أضف محلول كبريتات المغنيسيوم (MgSO₄) إلى محلول الملح:",
        "hint": "Magnesium carbonate precipitates in the cold; magnesium bicarbonate is water-soluble and precipitates only after boiling.",
        "arabic_hint": "كربونات المغنيسيوم شحيحة الذوبان تترسب على البارد، بينما بيكربونات المغنيسيوم تذوب في الماء ولا تترسب إلا بعد الغليان.",
        "options": [
            {"label": "White precipitate forms immediately in the cold", "arabic_label": "يتكون راسب أبيض فوراً على البارد", "next": "SET_ANION_CO3", "swatch": WHITE},
            {"label": "No precipitate in the cold; white precipitate forms only after boiling and heating", "arabic_label": "لا يتكون راسب على البارد، ويتكون الراسب الأبيض بعد الغليان والتسخين", "next": "SET_ANION_HCO3", "swatch": WHITE}
        ]
    },
    "ANION_SO2_CHECK": {
        "kind": "question",
        "phase": "anion",
        "text": "Inspect the solution during SO₂ gas evolution. Do you observe a yellow colloidal sulfur precipitate?",
        "arabic_text": "افحص محلول الأنبوبة أثناء تصاعد غاز SO₂، هل تلاحظ تكون راسب أصفر معلق من الكبريت؟",
        "hint": "Distinguishing sulfite from thiosulfate relies on the precipitation of colloidal yellow sulfur in thiosulfate only.",
        "arabic_hint": "التمييز بين الكبريتيت والثيوكبريتات يعتمد على ترسب الكبريت الأصفر الغروي في حالة الثيوكبريتات فقط.",
        "options": [
            {"label": "No yellow precipitate (solution gives white ppt with AgNO₃ turning black upon heating)", "arabic_label": "لا يوجد راسب أصفر (والمحلول يعطي راسباً أبيض يسود بالتسخين مع AgNO₃)", "next": "SET_ANION_SO3", "swatch": NONE},
            {"label": "Yes, yellow suspended sulfur precipitate appears (solution decolorizes brown iodine)", "arabic_label": "نعم، ظهر راسب أصفر معلق من الكبريت (والمحلول يزيل لون اليود البني)", "next": "SET_ANION_S2O3", "swatch": YELLOW}
        ]
    },
    "ANION_H2SO4_TEST": {
        "kind": "question",
        "phase": "anion",
        "text": "Step 4 (Group 2 Anions): Add concentrated sulfuric acid (Conc. H₂SO₄) to a dry salt sample with gentle heating:",
        "arabic_text": "الخطوة 4 (المجموعة الثانية): أضف حمض الكبريتيك المركز (Conc. H₂SO₄) إلى عينة جافة من الملح الصلب مع التسخين الهادئ:",
        "hint": "Concentrated H₂SO₄ is more stable and displaces halide and nitric acids as characteristic colored gases and fumes.",
        "arabic_hint": "حمض الكبريتيك المركز أكثر ثباتاً من أحماض الهاليدات والنيتريك فيطردها على هيئة غازات وأبخرة ملونة.",
        "options": [
            {"label": "Colorless gas (HCl) forming dense white fumes with ammonia-dipped rod (+ white ppt with AgNO₃)", "arabic_label": "تصاعد غاز عديم اللون (HCl) يكون سحباً بيضاء كثيفة مع ساق مبللة بالنشادر (+ راسب أبيض مع AgNO₃)", "next": "SET_ANION_CL", "swatch": WHITE},
            {"label": "Orange-red vapors (Br₂) that turn starch-moistened paper yellow (+ cream ppt with AgNO₃)", "arabic_label": "تصاعد أبخرة برتقالية حمراء (Br₂) تصفر ورقة مبللة بالنشا (+ راسب كريمي مع AgNO₃)", "next": "SET_ANION_BR", "swatch": ORANGE},
            {"label": "Dense violet vapors (I₂) that turn starch-moistened paper blue (+ yellow ppt with AgNO₃)", "arabic_label": "تصاعد أبخرة بنفسجية كثيفة (I₂) تزرق ورقة مبللة بالنشا (+ راسب أصفر مع AgNO₃)", "next": "SET_ANION_I", "swatch": VIOLET},
            {"label": "Reddish-brown fumes (NO₂) increasing upon adding copper turnings (+ brown ring test with FeSO₄)", "arabic_label": "تصاعد أبخرة بنية حمراء (NO₂) تزداد كثافتها بإضافة خراطة نحاس (+ حلقة بنية مع FeSO₄)", "next": "SET_ANION_NO3", "swatch": BROWN},
            {"label": "No gases or vapors evolved with concentrated sulfuric acid", "arabic_label": "لم تتصاعد أي غازات أو أبخرة مع حمض الكبريتيك المركز", "next": "ANION_BACL2_TEST", "swatch": NONE}
        ]
    },
    "ANION_BACL2_TEST": {
        "kind": "question",
        "phase": "anion",
        "text": "Step 5 (Group 3 Anions): Add barium chloride (BaCl₂) solution to salt solution, then test precipitate solubility in dilute HCl:",
        "arabic_text": "الخطوة 5 (المجموعة الثالثة): أضف محلول كلوريد الباريوم (BaCl₂) إلى محلول الملح، ثم اختبر ذوبان الراسب الأبيض في حمض HCl المخفف:",
        "hint": "BaCl₂ reagent group detects thermally stable anions such as sulfate and phosphate.",
        "arabic_hint": "تستخدم مجموعة كلوريد الباريوم للكشف عن الأنيونات الثابتة حرارياً مثل الكبريتات والفوسفات.",
        "options": [
            {"label": "White precipitate insoluble in dilute HCl (+ white ppt with lead acetate)", "arabic_label": "يتكون راسب أبيض لا يذوب في حمض الهيدروكلوريك المخفف (+ راسب أبيض مع أسيتات الرصاص)", "next": "SET_ANION_SO4", "swatch": WHITE},
            {"label": "White precipitate soluble in dilute HCl (+ yellow ppt with silver nitrate AgNO₃)", "arabic_label": "يتكون راسب أبيض يذوب في حمض الهيدروكلوريك المخفف (+ راسب أصفر مع نترات الفضة AgNO₃)", "next": "SET_ANION_PO4", "swatch": YELLOW}
        ]
    },

    # عقد تسجيل الأنيون والانتقال التلقائي للكاتيون
    "SET_ANION_CO3":  {"kind": "set_anion", "anion": "CO3",  "next": "CATION_START"},
    "SET_ANION_HCO3": {"kind": "set_anion", "anion": "HCO3", "next": "CATION_START"},
    "SET_ANION_SO3":  {"kind": "set_anion", "anion": "SO3",  "next": "CATION_START"},
    "SET_ANION_S2O3": {"kind": "set_anion", "anion": "S2O3", "next": "CATION_START"},
    "SET_ANION_S":    {"kind": "set_anion", "anion": "S",    "next": "CATION_START"},
    "SET_ANION_NO2":  {"kind": "set_anion", "anion": "NO2",  "next": "CATION_START"},
    "SET_ANION_CL":   {"kind": "set_anion", "anion": "CL",   "next": "CATION_START"},
    "SET_ANION_BR":   {"kind": "set_anion", "anion": "BR",   "next": "CATION_START"},
    "SET_ANION_I":    {"kind": "set_anion", "anion": "I",    "next": "CATION_START"},
    "SET_ANION_NO3":  {"kind": "set_anion", "anion": "NO3",  "next": "CATION_START"},
    "SET_ANION_SO4":  {"kind": "set_anion", "anion": "SO4",  "next": "CATION_START"},
    "SET_ANION_PO4":  {"kind": "set_anion", "anion": "PO4",  "next": "CATION_START"},

    # ================== المرحلة 2: شجرة الكشف عن الكاتيون (Cation Tree) ==================
    "CATION_START": {
        "kind": "question",
        "phase": "cation",
        "text": "Now proceeding to identify the Basic Radical (Cation): Add drops of dilute HCl to the aqueous salt solution. Does a precipitate form?",
        "arabic_text": "الآن ننتقل لتحديد الشق القاعدي (Cation): أضف قطرات من حمض HCl المخفف إلى محلول الملح المائي، هل تكون راسب؟",
        "hint": "Group I analytical cations (e.g. Lead(II) Pb²⁺) precipitate as sparingly soluble chlorides.",
        "arabic_hint": "تترسب كاتيونات المجموعة التحليلية الأولى (مثل الرصاص الثنائي Pb²⁺) على هيئة كلوريدات شحيحة الذوبان.",
        "options": [
            {"label": "Yes, white precipitate soluble in hot water, giving bright yellow ppt with KI", "arabic_label": "نعم، تكون راسب أبيض يذوب في الماء الساخن، ويعطي راسباً أصفر فاقعاً مع يوديد البوتاسيوم (KI)", "next": "FINISH_PB", "swatch": YELLOW},
            {"label": "No, no precipitate formed with dilute HCl", "arabic_label": "لا، لم يتكون أي راسب مع حمض HCl المخفف", "next": "CATION_NAOH_TEST", "swatch": NONE}
        ]
    },
    "CATION_NAOH_TEST": {
        "kind": "question",
        "phase": "cation",
        "text": "Add sodium hydroxide (NaOH) solution dropwise to the salt solution. What is the color of the precipitate?",
        "arabic_text": "أضف محلول هيدروكسيد الصوديوم (NaOH) تدريجياً إلى محلول الملح، ما هو لون الراسب المتكون؟",
        "hint": "NaOH precipitates most transition and base metals as hydroxides with distinct colors.",
        "arabic_hint": "محلول NaOH يرسب معظم الفلزات الانتقالية والقاعدية على هيئة هيدروكسيدات ذات ألوان مميزة.",
        "options": [
            {"label": "Blue precipitate turning black on heating; dissolves in excess ammonia to royal deep blue solution", "arabic_label": "راسب أزرق يسود بالتسخين، ويذوب في الزيادة من النشادر مكوناً محلولاً أزرق قاتماً", "next": "FINISH_CU", "swatch": BLUE},
            {"label": "Dirty white-green precipitate insoluble in excess; blue ppt with potassium ferricyanide", "arabic_label": "راسب أبيض مخضر لا يذوب في الزيادة، ويعطي راسباً أزرق مع حديديسيانيد البوتاسيوم", "next": "FINISH_FE2", "swatch": GREEN},
            {"label": "Reddish-brown gelatinous precipitate insoluble in excess; blood-red color with KSCN", "arabic_label": "راسب جيلاتيني بني محمر لا يذوب في الزيادة، ويعطي لوناً أحمر دامياً مع ثيوسيانات البوتاسيوم (KSCN)", "next": "FINISH_FE3", "swatch": BROWN},
            {"label": "White precipitate", "arabic_label": "راسب أبيض", "next": "CATION_WHITE_PPT_EXCESS", "swatch": WHITE},
            {"label": "No precipitate formed", "arabic_label": "لم يتكون أي راسب", "next": "CATION_NO_PPT", "swatch": NONE}
        ]
    },
    "CATION_WHITE_PPT_EXCESS": {
        "kind": "question",
        "phase": "cation",
        "text": "Add excess sodium hydroxide (Excess NaOH) solution to the white precipitate with shaking:",
        "arabic_text": "أضف الزيادة من محلول هيدروكسيد الصوديوم (Excess NaOH) إلى الراسب الأبيض مع الرج:",
        "hint": "Amphoteric hydroxides (Al, Zn) dissolve in excess NaOH; Ca, Mg, Ba hydroxides do not.",
        "arabic_hint": "الهيدروكسيدات المترددة (Amphoteric) مثل الألومنيوم والزنك تذوب في الزيادة من NaOH، بينما هيدروكسيدات الكالسيوم والمغنيسيوم والباريوم لا تذوب.",
        "options": [
            {"label": "White precipitate dissolves in excess NaOH forming clear solution", "arabic_label": "يذوب الراسب الأبيض في الزيادة من NaOH مكوناً محلولاً رائقاً", "next": "CATION_AMMONIA_TEST", "swatch": NONE},
            {"label": "White precipitate does not dissolve in excess NaOH", "arabic_label": "لا يذوب الراسب الأبيض في الزيادة من NaOH", "next": "CATION_INSOLUBLE_WHITE_FLAME", "swatch": WHITE}
        ]
    },
    "CATION_AMMONIA_TEST": {
        "kind": "question",
        "phase": "cation",
        "text": "Take a fresh sample and add aqueous ammonia (NH₄OH) dropwise then in excess:",
        "arabic_text": "خذ عينة جديدة من محلول الملح وأضف إليها محلول النشادر (NH₄OH) تدريجياً ثم بزيادة:",
        "hint": "Zinc hydroxide dissolves in excess ammonia forming tetraammine complex; aluminium hydroxide is insoluble in excess ammonia.",
        "arabic_hint": "هيدروكسيد الزنك يذوب في الزيادة من النشادر لتكوين معقد رباعي أمين الزنك، بينما هيدروكسيد الألومنيوم لا يذوب في النشادر.",
        "options": [
            {"label": "White gelatinous precipitate insoluble in excess ammonia", "arabic_label": "يتكون راسب أبيض جيلاتيني لا يذوب في الزيادة من محلول النشادر", "next": "FINISH_AL", "swatch": WHITE},
            {"label": "White precipitate dissolves completely in excess ammonia", "arabic_label": "يتكون راسب أبيض يذوب تماماً في الزيادة من محلول النشادر", "next": "FINISH_ZN", "swatch": NONE}
        ]
    },
    "CATION_INSOLUBLE_WHITE_FLAME": {
        "kind": "question",
        "phase": "cation",
        "text": "Perform dry flame test and confirmatory tests for the cation with white precipitate insoluble in excess NaOH:",
        "arabic_text": "أجرِ اختبار اللهب الجاف (Flame Test) والتجارب التأكيدية للكاتيون ذي الراسب الأبيض غير الذائب في الزيادة:",
        "hint": "Calcium and Barium impart distinct colors to Bunsen flame; Magnesium does not.",
        "arabic_hint": "الكالسيوم والباريوم يلونان لهب بنزن بألوان مميزة، بينما المغنيسيوم لا يلون اللهب.",
        "options": [
            {"label": "Brick-red flame; gives white precipitate with dilute H₂SO₄", "arabic_label": "يلون اللهب باللون الأحمر الطوبي، ويعطي راسباً أبيض مع حمض الكبريتيك المخفف", "next": "FINISH_CA", "swatch": BRICK_RED},
            {"label": "Apple-green flame; gives yellow precipitate with K₂CrO₄", "arabic_label": "يلون اللهب باللون الأخضر التفاحي، ويعطي راسباً أصفر مع كرومات البوتاسيوم (K₂CrO₄)", "next": "FINISH_BA", "swatch": APPLE_GREEN},
            {"label": "No distinctive flame coloration; gives white crystalline ppt with ammoniacal sodium phosphate", "arabic_label": "لا يلون اللهب بأي لون مميز، ويعطي راسباً أبيض بلورياً مع فوسفات الصوديوم النشادرية", "next": "FINISH_MG", "swatch": WHITE}
        ]
    },
    "CATION_NO_PPT": {
        "kind": "question",
        "phase": "cation",
        "text": "Heat the test tube containing the salt with NaOH, or perform dry flame test:",
        "arabic_text": "سخّن أنبوبة الاختبار المحتوية على الملح مع هيدروكسيد الصوديوم (NaOH)، أو أجرِ كشف اللهب الجاف:",
        "hint": "Ammonium salts evolve ammonia gas upon heating with alkali; Sodium and Potassium are detected by flame color.",
        "arabic_hint": "أملاح الأمونيوم تطلق غاز النشادر بالتسخين مع القلويات، بينما الصوديوم والبوتاسيوم يكشف عنهما بلون اللهب.",
        "options": [
            {"label": "Ammonia gas (NH₃) evolved, turning litmus blue and giving reddish-brown ppt with Nessler's reagent", "arabic_label": "يتصاعد غاز النشادر (NH₃) الذي يزرق ورقة عباد الشمس ويعطي راسباً بنياً محمراً مع كاشف نيسلر", "next": "FINISH_NH4", "swatch": BROWN},
            {"label": "No gas evolved; dry salt colors Bunsen flame persistent golden-yellow", "arabic_label": "لا يتصاعد غاز، والملح الجاف يلون لهب بنزن باللون الأصفر الذهبي الساطع", "next": "FINISH_NA", "swatch": GOLDEN_YELLOW},
            {"label": "No gas evolved; dry salt colors Bunsen flame pale violet / lilac", "arabic_label": "لا يتصاعد غاز، والملح الجاف يلون لهب بنزن باللون البنفسجي الفاتح (الليلكي)", "next": "FINISH_K", "swatch": LILAC}
        ]
    },

    # عقد الإنهاء وتوليد الملح النهائي
    "FINISH_PB":  {"kind": "finalize_salt", "cation": "PB"},
    "FINISH_CU":  {"kind": "finalize_salt", "cation": "CU"},
    "FINISH_FE2": {"kind": "finalize_salt", "cation": "FE2"},
    "FINISH_FE3": {"kind": "finalize_salt", "cation": "FE3"},
    "FINISH_AL":  {"kind": "finalize_salt", "cation": "AL"},
    "FINISH_ZN":  {"kind": "finalize_salt", "cation": "ZN"},
    "FINISH_CA":  {"kind": "finalize_salt", "cation": "CA"},
    "FINISH_BA":  {"kind": "finalize_salt", "cation": "BA"},
    "FINISH_MG":  {"kind": "finalize_salt", "cation": "MG"},
    "FINISH_NH4": {"kind": "finalize_salt", "cation": "NH4"},
    "FINISH_NA":  {"kind": "finalize_salt", "cation": "NA"},
    "FINISH_K":   {"kind": "finalize_salt", "cation": "K"}
}

# 4. قاعدة بيانات الـ 30 ملحاً الكاملة (SALTS_DATABASE)
SALTS_DATABASE = {
    # --- أ. الأملاح الملونة الذائبة في الماء (1 إلى 5) ---
    ("CU", "SO4"): {
        "formula": "CuSO₄·5H₂O",
        "name_ar": "كبريتات النحاس الثنائية المائية (التوتيا الزرقاء)",
        "name_en": "Copper(II) Sulfate Pentahydrate",
        "swatch": BLUE,
        "appearance": "بلورات زرقاء زاهية (تصبح بيضاء عند التسخين الشديد وفقد ماء التبلور).",
        "solubility": "يذوب بسهولة في الماء البارد ومحلوله حمضي التأثير ضعيف.",
        "ionic_equation": "Cu²⁺(aq) + SO₄²⁻(aq) + 5H₂O(l) → CuSO₄·5H₂O(s)",
        "info": [
            "يُعرف تجارياً باسم التوتيا الزرقاء (Blue Vitriol).",
            "يُستخدم في تحضير محلول فهلنج، وكمبيد للفطريات، وفي طلاء المعادن بالكهرباء."
        ]
    },
    ("CU", "CL"): {
        "formula": "CuCl₂·2H₂O",
        "name_ar": "كلوريد النحاس الثنائي المائي",
        "name_en": "Copper(II) Chloride Dihydrate",
        "swatch": BLUE_GREEN,
        "appearance": "بلورات زرقاء مخضرة متميعة.",
        "solubility": "شديد الذوبان في الماء والكحول.",
        "ionic_equation": "Cu²⁺(aq) + 2Cl⁻(aq) → CuCl₂(aq)",
        "info": [
            "محلوله المركز لونه أخضر مصفر بسبب تكون معقدات الكلورو [CuCl₄]²⁻، وعند تخفيفه بالماء يتحول للون الأزرق السماوي.",
            "يلون اللهب بلون أخضر مزرق مميز."
        ]
    },
    ("CU", "NO3"): {
        "formula": "Cu(NO₃)₂·3H₂O",
        "name_ar": "نترات النحاس الثنائية",
        "name_en": "Copper(II) Nitrate Trihydrate",
        "swatch": BLUE,
        "appearance": "بلورات زرقاء داكنة شديدة التميع.",
        "solubility": "يذوب بشراهة في الماء.",
        "ionic_equation": "Cu²⁺(aq) + 2NO₃⁻(aq) → Cu(NO₃)₂(aq)",
        "info": [
            "ينحل بالحرارة الشديدة معطياً أكسيد النحاس الأسود (CuO) وأبخرة بنية من ثاني أكسيد النيتروجين (NO₂) وغاز الأكسجين.",
            "مادة مؤكسدة قوية."
        ]
    },
    ("FE2", "SO4"): {
        "formula": "FeSO₄·7H₂O",
        "name_ar": "كبريتات الحديد الثنائي المائية (الزاج الأخضر)",
        "name_en": "Iron(II) Sulfate Heptahydrate",
        "swatch": GREEN,
        "appearance": "بلورات خضراء باهتة.",
        "solubility": "يذوب في الماء البارد.",
        "ionic_equation": "Fe²⁺(aq) + SO₄²⁻(aq) + 7H₂O(l) → FeSO₄·7H₂O(s)",
        "info": [
            "يُعرف تقليدياً بالزاج الأخضر (Green Vitriol).",
            "عامل مختزل قوي يُستخدم أساسياً في تجربة الحلقة البنية للكشف عن النترات.",
            "يتأكسد ببطء عند تعرضه للهواء الجوي ليتحول سطحه إلى اللون الأصفر البني."
        ]
    },
    ("FE3", "CL"): {
        "formula": "FeCl₃·6H₂O",
        "name_ar": "كلوريد الحديد الثلاثي",
        "name_en": "Iron(III) Chloride Hexahydrate",
        "swatch": BROWN,
        "appearance": "كتل بلورية صفراء بنية شديدة التميع.",
        "solubility": "يذوب بسهولة في الماء مع انطلاق حرارة.",
        "ionic_equation": "Fe³⁺(aq) + 3Cl⁻(aq) → FeCl₃(aq)",
        "info": [
            "محلوله المائي حمضي التأثير بشدة على عباد الشمس بسبب التميؤ.",
            "يُستخدم ككاشف أساسي للفينولات وأيون الأسيتات والثيوسيانات."
        ]
    },

    # --- ب. أملاح بيضاء تذوب في الماء وتتفاعل مع Dil. HCl (6 إلى 11) ---
    ("NA", "CO3"): {
        "formula": "Na₂CO₃",
        "name_ar": "كربونات الصوديوم (صودا الغسيل)",
        "name_en": "Sodium Carbonate",
        "swatch": WHITE,
        "appearance": "مسحوق أبيض أو بلورات شفافة متزهرة.",
        "solubility": "يذوب بسهولة في الماء البارد ومحلوله قلوي التأثير.",
        "ionic_equation": "2Na⁺(aq) + CO₃²⁻(aq) → Na₂CO₃(aq)",
        "info": [
            "ثابت حرارياً لا ينحل بالتسخين العادي.",
            "يُستخدم في صناعة الزجاج والورق وإزالة عسر الماء الدائم."
        ]
    },
    ("NA", "HCO3"): {
        "formula": "NaHCO₃",
        "name_ar": "بيكربونات الصوديوم (صودا الخبيز)",
        "name_en": "Sodium Bicarbonate",
        "swatch": WHITE,
        "appearance": "مسحوق بلوري أبيض ناعم.",
        "solubility": "يذوب في الماء البارد بدرجة متوسطة ومحلوله قلوي ضعيف.",
        "ionic_equation": "Na⁺(aq) + HCO₃⁻(aq) → NaHCO₃(aq)",
        "info": [
            "ينحل بالتسخين إلى كربونات صوديوم وماء وغاز ثاني أكسيد الكربون.",
            "يُستخدم في المعمل ككاشف أساسي للأحماض الكربوكسيلية."
        ]
    },
    ("NH4", "CO3"): {
        "formula": "(NH₄)₂CO₃",
        "name_ar": "كربونات الأمونيوم",
        "name_en": "Ammonium Carbonate",
        "swatch": WHITE,
        "appearance": "بلورات بيضاء صلبة تفوح منها رائحة النشادر في الهواء.",
        "solubility": "يذوب بالكامل في الماء البارد.",
        "ionic_equation": "2NH₄⁺(aq) + CO₃²⁻(aq) → (NH₄)₂CO₃(aq)",
        "info": [
            "يُعد الكاشف الأساسي لترسيب كاتيونات المجموعة التحليلية الخامسة (الكالسيوم، الباريوم، الاسترنشيوم).",
            "يتفكك بالتسخين الكامل إلى غاز النشادر وثاني أكسيد الكربون وبخار الماء دون ترك بقايا صلبة."
        ]
    },
    ("NA", "SO3"): {
        "formula": "Na₂SO₃",
        "name_ar": "كبريتيت الصوديوم",
        "name_en": "Sodium Sulfite",
        "swatch": WHITE,
        "appearance": "مسحوق أو بلورات بيضاء.",
        "solubility": "يذوب بسهولة في الماء البارد.",
        "ionic_equation": "2Na⁺(aq) + SO₃²⁻(aq) → Na₂SO₃(aq)",
        "info": [
            "عامل مختزل قوي يزيل لون برمنجنات البوتاسيوم ويخضر ثاني كرومات البوتاسيوم.",
            "يتأكسد تدريجياً بالهواء الجوي ليتحول إلى كبريتات الصوديوم (Na₂SO₄)."
        ]
    },
    ("NA", "S2O3"): {
        "formula": "Na₂S₂O₃·5H₂O",
        "name_ar": "ثيوكبريتات الصوديوم (الهايبو)",
        "name_en": "Sodium Thiosulfate Pentahydrate",
        "swatch": WHITE,
        "appearance": "بلورات منشورية شفافة عديمة اللون أو بيضاء.",
        "solubility": "شديد الذوبان في الماء البارد.",
        "ionic_equation": "2Na⁺(aq) + S₂O₃²⁻(aq) → Na₂S₂O₃(aq)",
        "info": [
            "المادة القياسية الأساسية في معايرات اليود (Iodometry) لقدرته الفورية على اختزال اليود.",
            "يُستخدم في تثبيت أفلام التصوير الفوتوغرافي لإذابة هاليدات الفضة غير المتفاعلة."
        ]
    },
    ("NA", "NO2"): {
        "formula": "NaNO₂",
        "name_ar": "نيتريت الصوديوم",
        "name_en": "Sodium Nitrite",
        "swatch": PALE_YELLOW,
        "appearance": "حبيبات بلورية بيضاء تميل للاصفرار الخفيف.",
        "solubility": "شديد الذوبان في الماء البارد.",
        "ionic_equation": "Na⁺(aq) + NO₂⁻(aq) → NaNO₂(aq)",
        "info": [
            "يُستخدم في تفاعلات الديأزة (Diazotization) للكشف عن الأمينات الأروماتية وتكوين صبغات الآزو.",
            "يسلك سلوك العوامل المؤكسدة والمختزلة معاً حسب الوسط."
        ]
    },

    # --- ج. أملاح بيضاء تذوب في الماء وتتفاعل مع Conc. H₂SO₄ (12 إلى 21) ---
    ("NA", "CL"): {
        "formula": "NaCl",
        "name_ar": "كلوريد الصوديوم (ملح الطعام)",
        "name_en": "Sodium Chloride",
        "swatch": WHITE,
        "appearance": "بلورات مكعبة بيضاء أو شفافة.",
        "solubility": "يذوب في الماء البارد ومحلوله متعادل تماماً (pH = 7).",
        "ionic_equation": "Na⁺(aq) + Cl⁻(aq) → NaCl(aq)",
        "info": [
            "الملح المرجعي الأكثر استقراراً في الطبيعة.",
            "لا يتأثر بحمض HCl المخفف، ويتفاعل مع حمض الكبريتيك المركز مطلقاً غاز HCl."
        ]
    },
    ("NH4", "CL"): {
        "formula": "NH₄Cl",
        "name_ar": "كلوريد الأمونيوم (ملح النشادر)",
        "name_en": "Ammonium Chloride",
        "swatch": WHITE,
        "appearance": "مسحوق بلوري أبيض.",
        "solubility": "يذوب بسهولة في الماء البارد بامتصاص حرارة.",
        "ionic_equation": "NH₄⁺(aq) + Cl⁻(aq) → NH₄Cl(aq)",
        "info": [
            "يتسامى بالتسخين المباشر (يتفكك حرارياً إلى NH₃ و HCl ثم يتحدان مجدداً على السطح البارد).",
            "يُستخدم مع محلول النشادر كمحلول منظم (Buffer) في ترسيب كاتيونات المجموعة الثالثة."
        ]
    },
    ("ZN", "CL"): {
        "formula": "ZnCl₂",
        "name_ar": "كلوريد الزنك (كلوريد الخارصين)",
        "name_en": "Zinc Chloride",
        "swatch": WHITE,
        "appearance": "حبيبات بيضاء شديدة التميع.",
        "solubility": "شديد الذوبان في الماء.",
        "ionic_equation": "Zn²⁺(aq) + 2Cl⁻(aq) → ZnCl₂(aq)",
        "info": [
            "يُستخدم مع حمض الهيدروكلوريك المركز لتحضير كاشف لوكاس (Lucas Reagent) للتمييز بين الكحولات.",
            "محلوله المائي حمضي التأثير."
        ]
    },
    ("AL", "CL"): {
        "formula": "AlCl₃·6H₂O",
        "name_ar": "كلوريد الألومنيوم المائي",
        "name_en": "Aluminium Chloride Hexahydrate",
        "swatch": WHITE,
        "appearance": "بلورات بيضاء أو بيضاء مصفرة متميعة.",
        "solubility": "يذوب في الماء بشدة مع تميؤ جزئي.",
        "ionic_equation": "Al³⁺(aq) + 3Cl⁻(aq) → AlCl₃(aq)",
        "info": [
            "محلوله المائي حمضي التأثير بوضوح.",
            "الصورة اللامائية منه تعمل كحمض لويس وحفاز في تفاعلات فريدل-كرافتس العضوية."
        ]
    },
    ("CA", "CL"): {
        "formula": "CaCl₂",
        "name_ar": "كلوريد الكالسيوم",
        "name_en": "Calcium Chloride",
        "swatch": WHITE,
        "appearance": "قشور أو حبيبات بيضاء مسامية شديدة الامتصاص للرطوبة.",
        "solubility": "شديد الذوبان في الماء مع انطلاق حرارة (طارد للحرارة).",
        "ionic_equation": "Ca²⁺(aq) + 2Cl⁻(aq) → CaCl₂(aq)",
        "info": [
            "يُستخدم كمادة مجففة للغازات والمذيبات العضوية في المعمل.",
            "يُستخدم ككاشف للتفرقة بين أحماض الأوكساليك والطرطريك والستريك."
        ]
    },
    ("BA", "CL"): {
        "formula": "BaCl₂·2H₂O",
        "name_ar": "كلوريد الباريوم المائي",
        "name_en": "Barium Chloride Dihydrate",
        "swatch": WHITE,
        "appearance": "بلورات بيضاء ثقيلة.",
        "solubility": "يذوب بسهولة في الماء البارد.",
        "ionic_equation": "Ba²⁺(aq) + 2Cl⁻(aq) → BaCl₂(aq)",
        "info": [
            "الكاشف الرئيسي للمجموعة الثالثة من الشقوق الحامضية (الكبريتات والفوسفات).",
            "مركب سام يجب التعامل معه بحذر في المعمل."
        ]
    },
    ("K", "BR"): {
        "formula": "KBr",
        "name_ar": "بروميد البوتاسيوم",
        "name_en": "Potassium Bromide",
        "swatch": WHITE,
        "appearance": "بلورات مكعبة بيضاء.",
        "solubility": "يذوب بسهولة في الماء ومحلوله متعادل.",
        "ionic_equation": "K⁺(aq) + Br⁻(aq) → KBr(aq)",
        "info": [
            "مصدر أيون البروميد القياسي في المعامل، ويُستخدم في تحضير أقراص مطيافية الأشعة تحت الحمراء (IR Spectroscopy)."
        ]
    },
    ("K", "I"): {
        "formula": "KI",
        "name_ar": "يوديد البوتاسيوم",
        "name_en": "Potassium Iodide",
        "swatch": WHITE,
        "appearance": "بلورات بيضاء قد تصفر قليلاً عند التخزين الطويل.",
        "solubility": "شديد الذوبان في الماء البارد.",
        "ionic_equation": "K⁺(aq) + I⁻(aq) → KI(aq)",
        "info": [
            "يُستخدم لإذابة اليود في الماء لتحضير محلول اليود القياسي (Lugol's Iodine) لتكون أيون ثلاثي اليوديد I₃⁻.",
            "كاشف تأكيدي ممتاز للرصاص والنحاس."
        ]
    },
    ("PB", "NO3"): {
        "formula": "Pb(NO₃)₂",
        "name_ar": "نترات الرصاص الثنائي",
        "name_en": "Lead(II) Nitrate",
        "swatch": WHITE,
        "appearance": "بلورات بيضاء ثقيلة الوزن غير متميعة.",
        "solubility": "الملح الشائع الوحيد للرصاص (بجانب الأسيتات) الذي يذوب بسهولة في الماء البارد.",
        "ionic_equation": "Pb²⁺(aq) + 2NO₃⁻(aq) → Pb(NO₃)₂(aq)",
        "info": [
            "يتفكك بالتسخين مع صوت طقطقة (Decrepitation) مطلقاً أبخرة بنية من NO₂ وراسب أصفر من أكسيد الرصاص PbO."
        ]
    },
    ("NH4", "NO3"): {
        "formula": "NH₄NO₃",
        "name_ar": "نترات الأمونيوم",
        "name_en": "Ammonium Nitrate",
        "swatch": WHITE,
        "appearance": "بلورات أو حبيبات بيضاء متميعة.",
        "solubility": "يذوب بشراهة في الماء مع امتصاص كبير للحرارة (تبرد الأنبوبة بشدة عند ذوبانه).",
        "ionic_equation": "NH₄⁺(aq) + NO₃⁻(aq) → NH₄NO₃(aq)",
        "info": [
            "يحتوي على النيتروجين في صورتين: كاتيون أمونيوم مختزل وأنيون نترات مؤكسد."
        ]
    },

    # --- د. أملاح بيضاء تذوب في الماء وتتبع مجموعة BaCl₂ (22 إلى 26) ---
    ("MG", "SO4"): {
        "formula": "MgSO₄·7H₂O",
        "name_ar": "كبريتات المغنيسيوم المائية (الملح الإنجليزي)",
        "name_en": "Magnesium Sulfate Heptahydrate",
        "swatch": WHITE,
        "appearance": "بلورات إبرية شفافة أو بيضاء.",
        "solubility": "شديد الذوبان في الماء البارد.",
        "ionic_equation": "Mg²⁺(aq) + SO₄²⁻(aq) + 7H₂O(l) → MgSO₄·7H₂O(s)",
        "info": [
            "يُعرف طبياً وتجارياً بالملح الإنجليزي (Epsom Salt).",
            "يُستخدم في المعمل ككاشف أساسي للتفرقة بين الكربونات والبيكربونات."
        ]
    },
    ("ZN", "SO4"): {
        "formula": "ZnSO₄·7H₂O",
        "name_ar": "كبريتات الزنك المائية (الزاج الأبيض)",
        "name_en": "Zinc Sulfate Heptahydrate",
        "swatch": WHITE,
        "appearance": "بلورات عديمة اللون أو بيضاء متزهرة.",
        "solubility": "يذوب بسهولة في الماء البارد.",
        "ionic_equation": "Zn²⁺(aq) + SO₄²⁻(aq) + 7H₂O(l) → ZnSO₄·7H₂O(s)",
        "info": [
            "يُعرف تاريخياً بالزاج الأبيض (White Vitriol)."
        ]
    },
    ("AL", "SO4"): {
        "formula": "Al₂(SO₄)₃·18H₂O",
        "name_ar": "كبريتات الألومنيوم",
        "name_en": "Aluminium Sulfate",
        "swatch": WHITE,
        "appearance": "مسحوق أو بلورات بيضاء.",
        "solubility": "يذوب في الماء ومحلوله حمضي التأثير.",
        "ionic_equation": "2Al³⁺(aq) + 3SO₄²⁻(aq) → Al₂(SO₄)₃(aq)",
        "info": [
            "يدخل في تركيب شب البوتاسيوم (Alum) المستخدم في تنقية وترويق مياه الشرب."
        ]
    },
    ("NH4", "SO4"): {
        "formula": "(NH₄)₂SO₄",
        "name_ar": "كبريتات الأمونيوم",
        "name_en": "Ammonium Sulfate",
        "swatch": WHITE,
        "appearance": "بلورات بيضاء أو شفافة.",
        "solubility": "شديد الذوبان في الماء البارد.",
        "ionic_equation": "2NH₄⁺(aq) + SO₄²⁻(aq) → (NH₄)₂SO₄(aq)",
        "info": [
            "يُستخدم في ترسيب البروتينات في الكيمياء الحيوية وفي تحضير أملاح الحديد المزدوجة (ملح مور)."
        ]
    },
    ("NA", "PO4"): {
        "formula": "Na₃PO₄",
        "name_ar": "فوسفات الصوديوم",
        "name_en": "Sodium Phosphate",
        "swatch": WHITE,
        "appearance": "مسحوق بلوري أبيض.",
        "solubility": "يذوب بسهولة في الماء البارد ومحلوله قلوي التأثير.",
        "ionic_equation": "3Na⁺(aq) + PO₄³⁻(aq) → Na₃PO₄(aq)",
        "info": [
            "يُستخدم ككاشف تأكيدي لكاتيون المغنيسيوم في وسط نشادري."
        ]
    },

    # --- هـ. أملاح شحيحة أو عديمة الذوبان في الماء وتذوب في الأحماض (27 إلى 30) ---
    ("CA", "CO3"): {
        "formula": "CaCO₃",
        "name_ar": "كربونات الكالسيوم (الحجر الجيري / الرخام)",
        "name_en": "Calcium Carbonate",
        "swatch": WHITE,
        "appearance": "مسحوق أبيض غير بلوري أو بلورات بيضاء.",
        "solubility": "عديم الذوبان في الماء النقي، ولكنه يذوب فوراً في حمض HCl المخفف مع فوران.",
        "ionic_equation": "CaCO₃(s) + 2HCl(aq) → CaCl₂(aq) + H₂O(l) + CO₂ ↑",
        "info": [
            "يتكون كراسب أبيض عند إمرار غاز CO₂ في ماء الجير الرائق لفترة قصيرة."
        ]
    },
    ("MG", "CO3"): {
        "formula": "MgCO₃",
        "name_ar": "كربونات المغنيسيوم",
        "name_en": "Magnesium Carbonate",
        "swatch": WHITE,
        "appearance": "مسحوق أبيض خفيف وهش.",
        "solubility": "لا يذوب في الماء، ويذوب في الأحماض المخففة بفوران.",
        "ionic_equation": "MgCO₃(s) + 2HCl(aq) → MgCl₂(aq) + H₂O(l) + CO₂ ↑",
        "info": [
            "يتكون كراسب أبيض عند إضافة كبريتات المغنيسيوم إلى محلول كربونات على البارد."
        ]
    },
    ("CA", "SO4"): {
        "formula": "CaSO₄·2H₂O",
        "name_ar": "كبريتات الكالسيوم المائية (الجبس)",
        "name_en": "Calcium Sulfate Dihydrate (Gypsum)",
        "swatch": WHITE,
        "appearance": "مسحوق أبيض.",
        "solubility": "شحيح الذوبان جداً في الماء.",
        "ionic_equation": "Ca²⁺(aq) + SO₄²⁻(aq) + 2H₂O(l) → CaSO₄·2H₂O ↓",
        "info": [
            "عند تسخينه جزئياً يفقد ثلاثة أرباع ماء التبلور ويتحول إلى جبس باريس (CaSO₄)₂·H₂O."
        ]
    },
    ("FE2", "S"): {
        "formula": "FeS",
        "name_ar": "كبريتيد الحديد الثنائي",
        "name_en": "Iron(II) Sulfide",
        "swatch": GRAY_BLACK,
        "appearance": "كتل أو مسحوق صلب أسود رمادي داكن.",
        "solubility": "لا يذوب في الماء، ويذوب في حمض HCl المخفف مطلقاً غاز H₂S.",
        "ionic_equation": "FeS(s) + 2HCl(aq) → FeCl₂(aq) + H₂S ↑",
        "info": [
            "يُستخدم في جهاز كيب بالمعامل لتحضير غاز كبريتيد الهيدروجين (H₂S) اللازم لترسيب كاتيونات المجموعة الثانية والرابعة."
        ]
    }
}

# 5. قواعد الاستبعاد الكيميائي ودالة بناء النتيجة النهائية (build_final_salt_outcome)
INCOMPATIBLE_SALTS = {
    ("FE3", "CO3"): {
        "title": "مركب غير مستقر كيميائياً (تميؤ كامل)",
        "subtitle": "كربونات الحديد الثلاثي Fe₂(CO₃)₃ لا تتكون في المحاليل المائية",
        "reason": "نظراً لأن كاتيون الحديد الثلاثي (Fe³⁺) ذو حامضية لويس عالية جداً وأنيون الكربونات (CO₃²⁻) قاعدة، يحدث تميؤ مائي كامل (Complete Hydrolysis) فور تلامسهما في الماء، فيتصاعد غاز ثاني أكسيد الكربون ويترسب هيدروكسيد الحديد الثلاثي البني المحمر.",
        "equations": ["2Fe³⁺ + 3CO₃²⁻ + 3H₂O → 2Fe(OH)₃ ↓ (Reddish-Brown) + 3CO₂ ↑"]
    },
    ("AL", "CO3"): {
        "title": "مركب غير مستقر كيميائياً (تميؤ كامل)",
        "subtitle": "كربونات الألومنيوم Al₂(CO₃)₃ لا تتكون في المحاليل المائية",
        "reason": "يحدث تميؤ مائي كامل في الماء ويتحول فوراً إلى راسب أبيض جيلاتيني من هيدروكسيد الألومنيوم مع تصاعد غاز CO₂.",
        "equations": ["2Al³⁺ + 3CO₃²⁻ + 3H₂O → 2Al(OH)₃ ↓ (White) + 3CO₂ ↑"]
    },
    ("CU", "I"): {
        "title": "تفاعل أكسدة واختزال ذاتي (Redox Incompatibility)",
        "subtitle": "يوديد النحاس الثنائي (CuI₂) غير مستقر ويتفكك فوراً",
        "reason": "يقوم كاتيون النحاس الثنائي (Cu²⁺) بأكسدة أنيون اليوديد (I⁻) إلى يود حر (I₂) بني اللون، بينما يختزل النحاس الثنائي إلى راسب أبيض من يوديد النحاس الأحادي (CuI).",
        "equations": ["2Cu²⁺ + 4I⁻ → 2CuI ↓ (White) + I₂ (Brown solution / Violet vapor)"]
    },
    ("FE3", "I"): {
        "title": "تفاعل أكسدة واختزال ذاتي (Redox Incompatibility)",
        "subtitle": "يوديد الحديد الثلاثي (FeI₃) لا يوجد في المحاليل المائية",
        "reason": "جهد اختزال الحديد الثلاثي أعلى من اليود، فيقوم Fe³⁺ بأكسدة أيون اليوديد I⁻ إلى يود حر I₂ ويتحول هو إلى حديد ثنائي Fe²⁺.",
        "equations": ["2Fe³⁺ + 2I⁻ → 2Fe²⁺ + I₂"]
    },
    ("AL", "S"): {
        "title": "تحلل مائي كامل (Complete Hydrolysis)",
        "subtitle": "كبريتيد الألومنيوم (Al₂S₃) يتحلل فور ملامسته للماء",
        "reason": "يتفاعل كبريتيد الألومنيوم مع الماء بشدة معطياً راسباً أبيض جيلاتينياً من هيدروكسيد الألومنيوم وغاز كبريتيد الهيدروجين.",
        "equations": ["Al₂S₃ + 6H₂O → 2Al(OH)₃ ↓ + 3H₂S ↑"]
    },
    ("FE3", "S"): {
        "title": "أكسدة واختزال وتحلل مائي",
        "subtitle": "كبريتيد الحديد الثلاثي (Fe₂S₃) غير مستقر في الأوساط المائية والحمضية",
        "reason": "يختزل الحديد الثلاثي بواسطة أيون الكبريتيد إلى حديد ثنائي مع ترسب الكبريت الأصفر.",
        "equations": ["2Fe³⁺ + S²⁻ → 2Fe²⁺ + S ↓"]
    }
}

# أعداد التأكسد والتكافؤات لبناء الصيغ الكيميائية ديناميكياً لأي ملح إضافي
ION_VALENCES = {
    "PB": ("Pb", 2), "CU": ("Cu", 2), "FE2": ("Fe", 2), "FE3": ("Fe", 3),
    "AL": ("Al", 3), "ZN": ("Zn", 2), "CA": ("Ca", 2), "BA": ("Ba", 2),
    "MG": ("Mg", 2), "NH4": ("NH₄", 1), "NA": ("Na", 1), "K": ("K", 1),
    "CO3": ("CO₃", 2), "HCO3": ("HCO₃", 1), "SO3": ("SO₃", 2), "S2O3": ("S₂O₃", 2),
    "S": ("S", 2), "NO2": ("NO₂", 1), "CL": ("Cl", 1), "BR": ("Br", 1),
    "I": ("I", 1), "NO3": ("NO₃", 1), "SO4": ("SO₄", 2), "PO4": ("PO₄", 3)
}

SUBSCRIPTS = {1: "", 2: "₂", 3: "₃", 4: "₄"}


def format_ion_part(symbol, count, is_polyatomic):
    if count == 1:
        return symbol
    if is_polyatomic:
        return f"({symbol}){SUBSCRIPTS[count]}"
    return f"{symbol}{SUBSCRIPTS[count]}"


def auto_balance_formula(cation_key, anion_key):
    import math
    c_sym, c_val = ION_VALENCES[cation_key]
    a_sym, a_val = ION_VALENCES[anion_key]
    gcd = math.gcd(c_val, a_val)
    c_count = a_val // gcd
    a_count = c_val // gcd
    c_poly = cation_key == "NH4"
    a_poly = anion_key not in ("S", "CL", "BR", "I")
    return f"{format_ion_part(c_sym, c_count, c_poly)}{format_ion_part(a_sym, a_count, a_poly)}"


# -*- coding: utf-8 -*-
"""
Enrich salt_kb.py with bilingual English data for:
- 12 anions (group_en, summary_en)
- 12 cations (group_en, summary_en)
- 30 salts (appearance_en, solubility_en, info_en)
- build_final_salt_outcome (equations_en, notes_en, summary_en)
"""

ANION_EN = {
    "CO3": {
        "group_en": "Dilute Hydrochloric Acid (Dil. HCl) Group",
        "summary_en": "Evolves carbon dioxide gas with effervescence, turning clear lime water turbid. Forms a white precipitate with magnesium sulfate in the cold."
    },
    "HCO3": {
        "group_en": "Dilute Hydrochloric Acid (Dil. HCl) Group",
        "summary_en": "Evolves carbon dioxide gas with effervescence, turning clear lime water turbid. Forms a white precipitate with magnesium sulfate only upon boiling."
    },
    "SO3": {
        "group_en": "Dilute Hydrochloric Acid (Dil. HCl) Group",
        "summary_en": "Evolves pungent sulfur dioxide gas turning acidified potassium dichromate paper green. Forms a white precipitate with silver nitrate that blackens on heating."
    },
    "S2O3": {
        "group_en": "Dilute Hydrochloric Acid (Dil. HCl) Group",
        "summary_en": "Evolves sulfur dioxide gas with a yellow precipitate of colloidal sulfur. Instantly decolorizes brown iodine solution."
    },
    "S": {
        "group_en": "Dilute Hydrochloric Acid (Dil. HCl) Group",
        "summary_en": "Evolves foul-smelling hydrogen sulfide gas that blackens lead acetate paper. Forms a black precipitate with silver nitrate."
    },
    "NO2": {
        "group_en": "Dilute Hydrochloric Acid (Dil. HCl) Group",
        "summary_en": "Evolves colorless nitric oxide gas turning into reddish-brown NO₂ at the tube mouth. Decolorizes acidified potassium permanganate."
    },
    "CL": {
        "group_en": "Concentrated Sulfuric Acid (Conc. H₂SO₄) Group",
        "summary_en": "Evolves hydrogen chloride gas forming dense white fumes with ammonia. Forms a white precipitate with silver nitrate, readily soluble in dilute ammonia."
    },
    "BR": {
        "group_en": "Concentrated Sulfuric Acid (Conc. H₂SO₄) Group",
        "summary_en": "Evolves orange-red bromine vapors turning starch paper yellow. Forms a pale-yellow precipitate with silver nitrate, slowly soluble in conc. ammonia."
    },
    "I": {
        "group_en": "Concentrated Sulfuric Acid (Conc. H₂SO₄) Group",
        "summary_en": "Evolves violet iodine vapors turning starch paper blue. Forms a yellow precipitate with silver nitrate, insoluble in ammonia."
    },
    "NO3": {
        "group_en": "Concentrated Sulfuric Acid (Conc. H₂SO₄) Group",
        "summary_en": "Evolves dense reddish-brown nitrogen dioxide fumes upon heating with copper turnings. Gives a characteristic brown ring with iron(II) sulfate."
    },
    "SO4": {
        "group_en": "Barium Chloride (BaCl₂) Solution Group",
        "summary_en": "Forms a white precipitate with barium chloride, insoluble in dilute mineral acids. Forms a white precipitate with lead acetate."
    },
    "PO4": {
        "group_en": "Barium Chloride (BaCl₂) Solution Group",
        "summary_en": "Forms a white precipitate with barium chloride, soluble in dilute HCl. Forms a canary-yellow precipitate with silver nitrate, soluble in ammonia and nitric acid."
    }
}

CATION_EN = {
    "PB": {
        "group_en": "Analytical Group I (Insoluble Chlorides / Dil. HCl Group)",
        "summary_en": "Precipitates as white lead(II) chloride soluble in hot water. Forms a bright yellow precipitate with potassium iodide."
    },
    "CU": {
        "group_en": "Analytical Group II (Acidic H₂S Group)",
        "summary_en": "Precipitates as black copper(II) sulfide in acidic medium. Forms a deep royal blue tetraammine complex [Cu(NH₃)₄]²⁺ in excess aqueous ammonia."
    },
    "FE2": {
        "group_en": "Analytical Group III (Ammonium Hydroxide Group)",
        "summary_en": "Forms a dirty-green precipitate of iron(II) hydroxide with alkali, rapidly oxidizing to reddish-brown in air."
    },
    "FE3": {
        "group_en": "Analytical Group III (Ammonium Hydroxide Group)",
        "summary_en": "Forms a reddish-brown precipitate of iron(III) hydroxide with alkali. Imparts a characteristic blood-red coloration with potassium thiocyanate."
    },
    "AL": {
        "group_en": "Analytical Group III (Ammonium Hydroxide Group)",
        "summary_en": "Forms a white gelatinous precipitate of aluminium hydroxide, amphoterically soluble in excess NaOH but insoluble in excess ammonia."
    },
    "ZN": {
        "group_en": "Analytical Group III / IV (Basic Sulfide Group)",
        "summary_en": "Forms a white precipitate of zinc hydroxide, amphoterically soluble in excess NaOH and also soluble in excess ammonia."
    },
    "CA": {
        "group_en": "Analytical Group V (Ammonium Carbonate Group)",
        "summary_en": "Precipitates as white calcium carbonate with ammonium carbonate. Imparts a characteristic brick-red coloration to the Bunsen flame."
    },
    "BA": {
        "group_en": "Analytical Group V (Ammonium Carbonate Group)",
        "summary_en": "Precipitates as white barium carbonate with ammonium carbonate and white barium sulfate with dil. H₂SO₄. Imparts an apple-green flame."
    },
    "MG": {
        "group_en": "Analytical Group VI (Soluble / Magnesium Group)",
        "summary_en": "Precipitates as white crystalline magnesium ammonium phosphate (MgNH₄PO₄) in ammoniacal medium."
    },
    "NH4": {
        "group_en": "Analytical Group VI (Volatile Cation Group)",
        "summary_en": "Evolves pungent ammonia gas upon warming with NaOH, turning moist red litmus blue and forming a brown precipitate with Nessler's reagent."
    },
    "NA": {
        "group_en": "Analytical Group VI (Alkali Metals Group)",
        "summary_en": "All common salts are water-soluble. Imparts an intense, persistent golden-yellow coloration to the non-luminous Bunsen flame."
    },
    "K": {
        "group_en": "Analytical Group VI (Alkali Metals Group)",
        "summary_en": "All common salts are water-soluble. Imparts a characteristic lilac / pale violet coloration to the Bunsen flame (viewed through cobalt glass)."
    }
}

SALT_EN = {
    ("CU", "SO4"): {
        "appearance_en": "Bright blue crystals (turns white upon strong heating due to loss of water of crystallization).",
        "solubility_en": "Readily soluble in cold water; aqueous solution is weakly acidic.",
        "info_en": [
            "Commercially known as Blue Vitriol.",
            "Used in preparing Fehling's reagent, as an agricultural fungicide, and in electroplating."
        ]
    },
    ("CU", "CL"): {
        "appearance_en": "Deliquescent blue-green crystals.",
        "solubility_en": "Highly soluble in water and alcohol.",
        "info_en": [
            "Concentrated solution is yellowish-green due to [CuCl₄]²⁻, turning sky blue upon dilution with water.",
            "Imparts a characteristic azure blue-green color to the Bunsen flame."
        ]
    },
    ("CU", "NO3"): {
        "appearance_en": "Deliquescent dark blue crystals.",
        "solubility_en": "Extremely soluble in water.",
        "info_en": [
            "Decomposes upon strong heating into black CuO, brown NO₂ fumes, and oxygen gas.",
            "Strong oxidizing agent."
        ]
    },
    ("FE2", "SO4"): {
        "appearance_en": "Pale green crystals.",
        "solubility_en": "Soluble in cold water.",
        "info_en": [
            "Traditionally known as Green Vitriol.",
            "Strong reducing agent used as the primary reagent in the Brown Ring test for nitrate identification.",
            "Slowly oxidizes upon air exposure, forming a brownish-yellow basic iron(III) sulfate crust."
        ]
    },
    ("FE3", "CL"): {
        "appearance_en": "Highly deliquescent brownish-yellow crystalline masses.",
        "solubility_en": "Readily dissolves in water with heat release.",
        "info_en": [
            "Aqueous solution is strongly acidic due to cationic hydrolysis.",
            "Key diagnostic reagent for phenols (violet color), acetates (reddish-brown), and thiocyanate (blood-red)."
        ]
    },
    ("NA", "CO3"): {
        "appearance_en": "White powder or clear efflorescent crystals.",
        "solubility_en": "Easily soluble in cold water; aqueous solution is alkaline.",
        "info_en": [
            "Thermally stable; does not decompose upon standard laboratory heating.",
            "Commercially known as Washing Soda; used in glass, paper manufacturing, and water softening."
        ]
    },
    ("NA", "HCO3"): {
        "appearance_en": "Fine white crystalline powder.",
        "solubility_en": "Moderately soluble in cold water; weakly alkaline.",
        "info_en": [
            "Decomposes on gentle heating into sodium carbonate, water vapor, and CO₂ gas.",
            "Used in laboratories as the standard effervescence test for carboxylic acids (Bicarbonate Test)."
        ]
    },
    ("NH4", "CO3"): {
        "appearance_en": "White solid crystals with a distinct ammonia odor in air.",
        "solubility_en": "Completely soluble in cold water.",
        "info_en": [
            "Primary group reagent for precipitating Analytical Group V cations (Ca²⁺, Ba²⁺, Sr²⁺).",
            "Completely volatilizes on heating into ammonia, carbon dioxide, and water vapor with zero residue."
        ]
    },
    ("NA", "SO3"): {
        "appearance_en": "White powder or crystals.",
        "solubility_en": "Readily soluble in cold water.",
        "info_en": [
            "Powerful reducing agent that decolorizes acidified KMnO₄ and turns K₂Cr₂O₇ emerald green.",
            "Gradually oxidizes in atmospheric air to sodium sulfate (Na₂SO₄)."
        ]
    },
    ("NA", "S2O3"): {
        "appearance_en": "Colorless transparent or white prismatic crystals.",
        "solubility_en": "Highly soluble in cold water.",
        "info_en": [
            "Standard primary reagent in iodometric titrations due to instantaneous quantitative reduction of iodine.",
            "Used as a photographic fixer (hypo) to dissolve unreacted silver halides."
        ]
    },
    ("NA", "NO2"): {
        "appearance_en": "White to slightly yellowish crystalline granules.",
        "solubility_en": "Highly soluble in cold water.",
        "info_en": [
            "Essential reagent in diazotization reactions with primary aromatic amines to form azo dyes.",
            "Exhibits both oxidizing and reducing behaviors depending on the chemical environment."
        ]
    },
    ("NA", "CL"): {
        "appearance_en": "White cubic crystals or colorless transparent cubes.",
        "solubility_en": "Soluble in water with neutral pH; solubility barely changes with temperature.",
        "info_en": [
            "Common table salt and rock salt (Halite).",
            "Primary source of chlorine and sodium in chemical industries; colors Bunsen flame intense golden-yellow."
        ]
    },
    ("NH4", "CL"): {
        "appearance_en": "White crystalline powder or fibrous masses.",
        "solubility_en": "Readily soluble in cold water with significant heat absorption.",
        "info_en": [
            "Sublimes completely upon direct heating into NH₃ and HCl, reforming white fumes at cooler tube surfaces.",
            "Constituent of buffer solutions with NH₄OH for Group III cation precipitation."
        ]
    },
    ("ZN", "CL"): {
        "appearance_en": "Extremely deliquescent white granular solid.",
        "solubility_en": "Highly soluble in water with heat release; strongly acidic solution.",
        "info_en": [
            "Active component of Lucas reagent (anhydrous ZnCl₂ + conc. HCl) used to distinguish primary, secondary, and tertiary alcohols."
        ]
    },
    ("AL", "CL"): {
        "appearance_en": "White to yellowish-white deliquescent crystalline powder.",
        "solubility_en": "Very soluble in water with strong acidic hydrolysis.",
        "info_en": [
            "Aqueous solution turns blue litmus red; forms gelatinous white Al(OH)₃ with NaOH, soluble in excess."
        ]
    },
    ("CA", "CL"): {
        "appearance_en": "Highly hygroscopic white granules or fused masses.",
        "solubility_en": "Very soluble in water with high heat liberation.",
        "info_en": [
            "Potent laboratory desiccant in desiccators; imparts brick-red flame coloration; used to precipitate calcium oxalate and sulfate."
        ]
    },
    ("BA", "CL"): {
        "appearance_en": "Heavy white crystalline platelets.",
        "solubility_en": "Readily soluble in cold water.",
        "info_en": [
            "Primary laboratory reagent for detecting sulfate (SO₄²⁻) and phosphate (PO₄³⁻) anions.",
            "Toxic compound that imparts an apple-green coloration to the Bunsen flame."
        ]
    },
    ("K", "BR"): {
        "appearance_en": "White cubic crystals.",
        "solubility_en": "Readily soluble in water with neutral pH.",
        "info_en": [
            "Standard laboratory bromide source and matrix for IR spectroscopy pellets.",
            "Imparts a characteristic lilac / pale violet flame coloration."
        ]
    },
    ("K", "I"): {
        "appearance_en": "White crystals, may slightly yellow upon prolonged atmospheric exposure.",
        "solubility_en": "Highly soluble in cold water.",
        "info_en": [
            "Used to dissolve elemental iodine via formation of the triiodide ion (I₃⁻).",
            "Excellent confirmatory reagent for lead (yellow PbI₂) and copper (white CuI + brown I₂)."
        ]
    },
    ("PB", "NO3"): {
        "appearance_en": "Heavy, non-deliquescent white crystals.",
        "solubility_en": "The only common lead salt (along with lead acetate) readily soluble in cold water.",
        "info_en": [
            "Decrepitates (crackles) upon dry heating, yielding brown NO₂ gas and yellow lead(II) oxide (PbO)."
        ]
    },
    ("NH4", "NO3"): {
        "appearance_en": "White deliquescent granules or prills.",
        "solubility_en": "Extremely soluble in water with marked endothermic cooling.",
        "info_en": [
            "Contains nitrogen in two oxidation states: reduced ammonium cation (-3) and oxidized nitrate anion (+5)."
        ]
    },
    ("MG", "SO4"): {
        "appearance_en": "Colorless or white needle-like crystals.",
        "solubility_en": "Highly soluble in cold water.",
        "info_en": [
            "Medically and commercially known as Epsom Salt.",
            "Key laboratory reagent for differentiating carbonate (white precipitate in the cold) from bicarbonate (white precipitate only on boiling)."
        ]
    },
    ("ZN", "SO4"): {
        "appearance_en": "Colorless or efflorescent white crystals.",
        "solubility_en": "Easily soluble in cold water.",
        "info_en": [
            "Historically known as White Vitriol.",
            "Yields white Zn(OH)₂ with NaOH, soluble in excess NaOH and in excess aqueous ammonia."
        ]
    },
    ("AL", "SO4"): {
        "appearance_en": "White crystalline powder or plates.",
        "solubility_en": "Soluble in water with acidic reaction.",
        "info_en": [
            "Key constituent of potassium alum used in municipal drinking water coagulation and purification."
        ]
    },
    ("NH4", "SO4"): {
        "appearance_en": "White transparent crystals.",
        "solubility_en": "Readily soluble in cold water.",
        "info_en": [
            "Widely used in biochemical protein salting-out and in synthesis of Mohr's salt (ferrous ammonium sulfate)."
        ]
    },
    ("NA", "PO4"): {
        "appearance_en": "White crystalline powder.",
        "solubility_en": "Easily soluble in cold water; strongly alkaline solution.",
        "info_en": [
            "Used as a confirmatory test reagent for magnesium cations in ammoniacal medium (forming crystalline MgNH₄PO₄)."
        ]
    },
    ("CA", "CO3"): {
        "appearance_en": "Fine white amorphous or microcrystalline powder.",
        "solubility_en": "Insoluble in pure water, but dissolves immediately in dilute HCl with vigorous effervescence.",
        "info_en": [
            "Natural form of limestone, calcite, and marble.",
            "Forms as the temporary white precipitate when CO₂ is bubbled into clear lime water."
        ]
    },
    ("MG", "CO3"): {
        "appearance_en": "Light, fragile white powder.",
        "solubility_en": "Insoluble in water; dissolves in dilute acids with effervescence.",
        "info_en": [
            "Precipitates as a white solid when magnesium sulfate is treated with sodium carbonate in the cold."
        ]
    },
    ("CA", "SO4"): {
        "appearance_en": "White powder or fibrous crystals.",
        "solubility_en": "Sparingly soluble in water (insoluble for qualitative precipitation).",
        "info_en": [
            "Naturally occurs as gypsum (CaSO₄·2H₂O); partial dehydration yields Plaster of Paris (CaSO₄·0.5H₂O)."
        ]
    },
    ("FE2", "S"): {
        "appearance_en": "Dark grayish-black solid lumps or coarse powder.",
        "solubility_en": "Insoluble in water; dissolves in dilute HCl evolving H₂S gas.",
        "info_en": [
            "Used in Kipp's apparatus in qualitative laboratories to generate H₂S gas for Group II and IV cation precipitation."
        ]
    }
}


for _k, _v in ANION_EN.items():
    if _k in ANIONS_DATA:
        ANIONS_DATA[_k].update(_v)

for _k, _v in CATION_EN.items():
    if _k in CATIONS_DATA:
        CATIONS_DATA[_k].update(_v)

for _k, _v in SALT_EN.items():
    if _k in SALTS_DATABASE:
        SALTS_DATABASE[_k].update(_v)


def build_final_salt_outcome(cation_key, anion_key):
    """تبني النتيجة النهائية الكاملة للملح بعد انتهاء شجرتي الأنيون والكاتيون مع دعم كامل للغتين العربية والإنجليزية"""
    c_data = CATIONS_DATA[cation_key]
    a_data = ANIONS_DATA[anion_key]

    # 1. التحقق من الاستقرار الكيميائي أولاً
    if (cation_key, anion_key) in INCOMPATIBLE_SALTS:
        inc = INCOMPATIBLE_SALTS[(cation_key, anion_key)]
        all_eqs_ar = inc["equations"] + a_data["equations"] + c_data["equations"]
        all_eqs_en = inc.get("equations_en", inc["equations"]) + a_data["equations"] + c_data["equations"]
        all_notes_ar = [
            f"الشق الحامضي الذي تم رصده: {a_data['name_ar']} ({a_data['symbol']})",
            f"الشق القاعدي الذي تم رصده: {c_data['name_ar']} ({c_data['symbol']})",
            "تحقق من عدم حدوث تلوث في أنابيب الاختبار أو تأكسد العينة."
        ]
        all_notes_en = [
            f"Detected Acidic Radical: {a_data['name_en']} ({a_data['symbol']})",
            f"Detected Basic Radical: {c_data['name_en']} ({c_data['symbol']})",
            "Verify test tube cleanliness and sample integrity against oxidation or cross-contamination."
        ]
        return outcome(
            title=inc["title"],
            subtitle=inc["subtitle"],
            summary=inc["reason"],
            equations=all_eqs_ar,
            notes=all_notes_ar,
            notes_ar=all_notes_ar,
            swatch=BROWN,
            formula=False,
            badge="تحذير علمي: عدم توافق كيميائي",
            equations_en=all_eqs_en,
            notes_en=all_notes_en,
            summary_en=inc.get("reason_en", inc["reason"]),
            badge_en="Scientific Warning: Incompatible Salt"
        )

    # 2. إذا كان الملح ضمن قائمة الـ 30 ملحاً المرجعية المفصلة
    if (cation_key, anion_key) in SALTS_DATABASE:
        salt = SALTS_DATABASE[(cation_key, anion_key)]
        all_equations_ar = (
            [f"معادلة الملح: {salt['ionic_equation']}"] +
            [f"--- معادلات الشق الحامضي ({a_data['name_ar']}) ---"] + a_data["equations"] +
            [f"--- معادلات الشق القاعدي ({c_data['name_ar']}) ---"] + c_data["equations"]
        )
        all_equations_en = (
            [f"Salt Formation Equation: {salt['ionic_equation']}"] +
            [f"--- Acidic Radical Reactions ({a_data['name_en']}) ---"] + a_data["equations"] +
            [f"--- Basic Radical Reactions ({c_data['name_en']}) ---"] + c_data["equations"]
        )

        all_notes_ar = [
            f"الشق الحامضي (Anion): {a_data['name_ar']} ({a_data['symbol']}) — {a_data['group']}",
            f"الشق القاعدي (Cation): {c_data['name_ar']} ({c_data['symbol']}) — {c_data['group']}",
            f"المظهر الفيزيائي: {salt['appearance']}",
            f"الذوبانية في الماء: {salt['solubility']}"
        ] + salt.get("info", [])

        all_notes_en = [
            f"Acidic Radical (Anion): {a_data['name_en']} ({a_data['symbol']}) — {a_data.get('group_en', a_data['group'])}",
            f"Basic Radical (Cation): {c_data['name_en']} ({c_data['symbol']}) — {c_data.get('group_en', c_data['group'])}",
            f"Physical Appearance: {salt.get('appearance_en', salt['appearance'])}",
            f"Solubility in Water: {salt.get('solubility_en', salt['solubility'])}"
        ] + salt.get("info_en", salt.get("info", []))

        return outcome(
            title=salt["formula"],
            subtitle=f"{salt['name_ar']} — {salt['name_en']}",
            summary=f"{a_data['summary']} كما أن الكاتيون {c_data['summary']}",
            equations=all_equations_ar,
            notes=all_notes_ar,
            notes_ar=all_notes_ar,
            swatch=salt["swatch"],
            formula=True,
            badge="تم تشخيص الملح بنجاح",
            equations_en=all_equations_en,
            notes_en=all_notes_en,
            summary_en=f"{a_data.get('summary_en', a_data['summary'])} Furthermore, {c_data.get('summary_en', c_data['summary'])}",
            badge_en="Salt Identified Successfully"
        )

    # 3. توليد ديناميكي لأي ملح آخر صحيح من تقاطع الـ 12 كاتيون × 12 أنيون
    formula = auto_balance_formula(cation_key, anion_key)
    name_ar = f"{a_data['name_ar']} {c_data['name_ar']}"
    name_en = f"{c_data['name_en']} {a_data['name_en']}"
    all_equations_ar = (
        [f"الصيغة الموزونة المستنتجة: {formula}"] +
        [f"--- معادلات الشق الحامضي ({a_data['name_ar']}) ---"] + a_data["equations"] +
        [f"--- معادلات الشق القاعدي ({c_data['name_ar']}) ---"] + c_data["equations"]
    )
    all_equations_en = (
        [f"Balanced Salt Formula: {formula}"] +
        [f"--- Acidic Radical Reactions ({a_data['name_en']}) ---"] + a_data["equations"] +
        [f"--- Basic Radical Reactions ({c_data['name_en']}) ---"] + c_data["equations"]
    )
    all_notes_ar = [
        f"الشق الحامضي (Anion): {a_data['name_ar']} ({a_data['symbol']}) — {a_data['group']}",
        f"الشق القاعدي (Cation): {c_data['name_ar']} ({c_data['symbol']}) — {c_data['group']}",
        f"تفسير الأنيون: {a_data['summary']}",
        f"تفسير الكاتيون: {c_data['summary']}"
    ]
    all_notes_en = [
        f"Acidic Radical (Anion): {a_data['name_en']} ({a_data['symbol']}) — {a_data.get('group_en', a_data['group'])}",
        f"Basic Radical (Cation): {c_data['name_en']} ({c_data['symbol']}) — {c_data.get('group_en', c_data['group'])}",
        f"Anion Diagnostics: {a_data.get('summary_en', a_data['summary'])}",
        f"Cation Diagnostics: {c_data.get('summary_en', c_data['summary'])}"
    ]

    return outcome(
        title=formula,
        subtitle=f"{name_ar} — {name_en}",
        summary=f"تم استنتاج الملح من دمج الشق الحامضي ({a_data['name_ar']}) مع الشق القاعدي ({c_data['name_ar']}).",
        equations=all_equations_ar,
        notes=all_notes_ar,
            notes_ar=all_notes_ar,
        swatch=WHITE,
        formula=True,
        badge="تشخيص قياسي مكتمل",
        equations_en=all_equations_en,
        notes_en=all_notes_en,
        summary_en=f"Salt deduced by combining acidic radical ({a_data['name_en']}) and basic radical ({c_data['name_en']}).",
        badge_en="Standard Diagnostic Deduction"
    )