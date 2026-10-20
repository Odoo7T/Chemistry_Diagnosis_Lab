"""
Organic Chemistry Expert System — Knowledge Base & Decision Tree
Qualitative Organic Analysis Covering 25 Laboratory Compounds (11 Liquids + 14 Solids)
"""

# Helper constructors
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

def outcome(title, subtitle, summary, equations=(), notes=(), swatch=None, formula=False, badge=None, arabic_summary=None):
    return {
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

NONE = "none"

# =========================================================================
# 1. ORGANIC OUTCOMES (25 COMPOUNDS: 11 Liquids + 14 Solids)
# =========================================================================

ORGANIC_OUTCOMES = {
    # ------------------ 11 LIQUIDS ------------------
    "ORG_FORMIC": outcome(
        "HCOOH",
        "حمض الفورميك (حمض النمليك) — Formic Acid",
        "Colorless liquid carboxylic acid; reduces acidified KMnO4 and forms silver mirror with Tollen's reagent.",
        [
            "HCOOH + 2[Ag(NH₃)₂]⁺ + 2OH⁻ → 2Ag ↓ + CO₂ ↑ + 4NH₃ + 2H₂O",
            "5HCOOH + 2MnO₄⁻ + 6H⁺ → 2Mn²⁺ + 5CO₂ ↑ + 8H₂O"
        ],
        notes=[
            "يحتوي على مجموعة كربوكسيل متصلة مباشرة بذرة هيدروجين، مما يمنحه خواص الألدهيدات الاختزالية الفريدة.",
            "يفور بقوة مع NaHCO₃ ويزيل لون برمنجنات البوتاسيوم ويكوّن مرآة فضية لامعة مع كاشف تولن."
        ],
        swatch=NONE,
        formula=True,
        badge="Liquid Carboxylic Acid",
        arabic_summary="حمض كربوكسيلي سائل عديم اللون يمتزج بالماء ويفور مع NaHCO₃؛ يختزل برمنجنات البوتاسيوم وتولن لوجود الرابطة الألدهيدية المباشرة."
    ),

    "ORG_ACETIC": outcome(
        "CH₃COOH",
        "حمض الأسيتيك (حمض الخليك) — Acetic Acid",
        "Colorless liquid with vinegar odor; gives intense blood-red color with neutral FeCl3.",
        [
            "3CH₃COO⁻ + Fe³⁺ + 2H₂O → [Fe₃(OH)₂(CH₃COO)₆]⁺ + 2H⁺",
            "[Fe₃(OH)₂(CH₃COO)₆]⁺ + 4H₂O → 3Fe(OH)₂CH₃COO ↓ + 3CH₃COOH + H⁺"
        ],
        notes=[
            "رائحة الخل المميزة النفاذة، يقاوم الأكسدة بمحلول برمنجنات البوتاسيوم المحمض.",
            "يعطي لوناً أحمر دامي كثيف مع كلوريد الحديد الثلاثي المتعادل، يتحول إلى راسب بني محمر عند الغليان."
        ],
        swatch=NONE,
        formula=True,
        badge="Liquid Carboxylic Acid",
        arabic_summary="حمض كربوكسيلي سائل ذو رائحة الخل المعروفة، يمتزج بالماء ويفور مع NaHCO₃، ويعطي لوناً أحمر دامي مع FeCl₃ المتعادل."
    ),

    "ORG_FORMALDEHYDE": outcome(
        "HCHO",
        "الفورمالدهيد (فورمالين) — Formaldehyde",
        "Pungent miscible aldehyde; forms silver mirror with Tollen's and brick-red ppt with Fehling's, negative iodoform.",
        [
            "HCHO + 2[Ag(NH₃)₂]⁺ + 2OH⁻ → HCOO⁻ + 2Ag ↓ + 4NH₃ + 2H₂O",
            "HCHO + 2Cu²⁺ + 5OH⁻ → HCOO⁻ + Cu₂O ↓ + 3H₂O"
        ],
        notes=[
            "غاز يذاب في الماء بنسبة 40% (الفورمالين)، ذو رائحة نفاذة خانقة ومدمعة للعين.",
            "يعطي راسباً أحمر طوبياً مع كاشف فهلنج ومرآة فضية مع تولن، وسلبي تماماً مع اختبار اليودوفورم."
        ],
        swatch=NONE,
        formula=True,
        badge="Liquid Aldehyde",
        arabic_summary="ألدهيد سائل ذو رائحة نفاذة خانقة، متعادل ويمتزج بالماء، إيجابي مع 2,4-DNP وفهلنج وتولن، وسلبي مع اختبار اليودوفورم."
    ),

    "ORG_ACETALDEHYDE": outcome(
        "CH₃CHO",
        "الأسيتالدهيد (إيثانال) — Acetaldehyde",
        "Miscible aldehyde; forms silver mirror with Tollen's and positive yellow iodoform precipitate.",
        [
            "CH₃CHO + 2[Ag(NH₃)₂]⁺ + 2OH⁻ → CH₃COO⁻ + 2Ag ↓ + 4NH₃ + 2H₂O",
            "CH₃CHO + 3I₂ + 4NaOH → CHI₃ ↓ + HCOONa + 3NaI + 3H₂O"
        ],
        notes=[
            "سائل متطاير يمتزج بالماء بجميع النسب، يعطي مرآة فضية لامعة مع كاشف تولن.",
            "إيجابي في اختبار اليودوفورم فيعطي راسباً أصفر من CHI₃ لاحتوائه على مجموعة CH₃-C=O الميثيل كربونيلية."
        ],
        swatch=NONE,
        formula=True,
        badge="Liquid Aldehyde",
        arabic_summary="ألدهيد سائل متطاير يمتزج بالماء، يعطي مرآة فضية مع تولن، وراسب يودوفورم أصفر بلوري مميز مع اليود وهيدروكسيد الصوديوم."
    ),

    "ORG_BENZALDEHYDE": outcome(
        "C₆H₅CHO",
        "البنزالدهيد (زيت اللوز المر) — Benzaldehyde",
        "Aromatic liquid aldehyde with bitter almond odor; smoky flame, positive Tollen's, negative Fehling's.",
        [
            "C₆H₅CHO + 2[Ag(NH₃)₂]⁺ + 2OH⁻ → C₆H₅COO⁻ + 2Ag ↓ + 4NH₃ + 2H₂O",
            "C₆H₅CHO + NaHSO₃ → C₆H₅CH(OH)SO₃Na ↓"
        ],
        notes=[
            "سائل زيتي شحيح الذوبان في الماء، رائحة اللوز المر الأروماتية المميزة، يحترق بلهب مدخن أسود كثيف.",
            "يكوّن مرآة فضية مع تولن ولكنه سلبي مع محلول فهلنج لكونه ألدهيداً أروماتياً."
        ],
        swatch="#fef08a",
        formula=True,
        badge="Aromatic Aldehyde",
        arabic_summary="ألدهيد أروماتي سائل شحيح الذوبان في الماء برائحة اللوز المر واللهب المدخن؛ يكوّن مرآة فضية مع تولن وسلبي مع فهلنج."
    ),

    "ORG_ACETONE": outcome(
        "CH₃COCH₃",
        "الأسيتون (بروبانون) — Acetone",
        "Volatile miscible aliphatic ketone; positive iodoform and ruby-red sodium nitroprusside reaction.",
        [
            "CH₃COCH₃ + 3I₂ + 4NaOH → CHI₃ ↓ + CH₃COONa + 3NaI + 3H₂O",
            "CH₃COCH₃ + [Fe(CN)₅NO]²⁻ + 2OH⁻ → [Fe(CN)₅NO-CH₂COCH₃]⁴⁻ + H₂O"
        ],
        notes=[
            "سائل متطاير ذو رائحة مميزة، يمتزج بالماء تماماً، متعادل مع عباد الشمس والبيكربونات.",
            "لا يتفاعل مع كواشف الأكسدة الضعيفة (تولن وفهلنج)، ويعطي راسب يودوفورم أصفر ولوناً أحمر ياقوتياً مع نيتروبروسيد الصوديوم."
        ],
        swatch=NONE,
        formula=True,
        badge="Liquid Ketone",
        arabic_summary="كيتون أليفاتي سائل سريع التطاير يمتزج بالماء؛ سلبي مع تولن وفهلنج، ويعطي راسب يودوفورم أصفر وتفاعل نيتروبروسيد أحمر ياقوتي."
    ),

    "ORG_ACETOPHENONE": outcome(
        "C₆H₅COCH₃",
        "الأسيتوفينون (ميثيل فينيل كيتون) — Acetophenone",
        "Aromatic liquid/solid (mp ~20°C); smoky flame, negative Tollen's, positive yellow iodoform precipitate.",
        [
            "C₆H₅COCH₃ + 3I₂ + 4NaOH → CHI₃ ↓ + C₆H₅COONa + 3NaI + 3H₂O"
        ],
        notes=[
            "سائل زيتي شحيح الذوبان في الماء (قد يتجمد في الأجواء المعملية الباردة لأن درجة انصهاره 20°م تقريباً).",
            "يحترق بلهب مدخن أسود، سلبي مع تولن، ويعطي راسباً أصفر في اختبار اليودوفورم لوجود مجموعة الأسيتيل CH₃-CO المرتبطة بحلقة البنزين."
        ],
        swatch=NONE,
        formula=True,
        badge="Aromatic Ketone",
        arabic_summary="كيتون أروماتي سائل/صلب شحيح الذوبان في الماء، لهب مدخن، سلبي مع تولن، ويعطي راسب يودوفورم أصفر مميز."
    ),

    "ORG_METHANOL": outcome(
        "CH₃OH",
        "الميثانول (كحول الخشب) — Methanol",
        "Light miscible alcohol; negative iodoform test, forms methyl salicylate (wintergreen odor) with salicylic acid.",
        [
            "C₆H₄(OH)COOH + CH₃OH → C₆H₄(OH)COOCH₃ + H₂O"
        ],
        notes=[
            "سائل خفيف متطاير يمتزج بالماء بجميع النسب، متعادل وسلبي مع 2,4-DNP.",
            "سلبي قاطع في اختبار اليودوفورم؛ عند تسخينه مع حمض الساليسيليك وحمض الكبريتيك المركز يكوّن ساليسيلات الميثيل (زيت الكافور / أبو فاس).",
            "تنبيه أمان: الميثانول مركب عالي السمية، يجب عدم استنشاق أبخرته بعمق أو تذوقه بتاتاً."
        ],
        swatch=NONE,
        formula=True,
        badge="Liquid Alcohol",
        arabic_summary="كحول أليفاتي سائل خفيف يمتزج بالماء، متعادل وسلبي في اختبار اليودوفورم، يعطي رائحة ساليسيلات الميثيل عند تفاعل الأسترة."
    ),

    "ORG_ETHANOL": outcome(
        "C₂H₅OH",
        "الإيثانول (الكحول الإيثيلي) — Ethanol",
        "Light miscible alcohol; positive iodoform test, rapidly reduces acidic dichromate to green Cr(III).",
        [
            "C₂H₅OH + 4I₂ + 6NaOH → CHI₃ ↓ + HCOONa + 5NaI + 5H₂O",
            "3C₂H₅OH + Cr₂O₇²⁻ + 8H⁺ → 3CH₃CHO + 2Cr³⁺ (أخضر) + 7H₂O"
        ],
        notes=[
            "سائل متطاير يمتزج بالماء تماماً، متعادل مع عباد الشمس والبيكربونات وسلبي مع 2,4-DNP.",
            "إيجابي مميز في اختبار اليودوفورم (راسب أصفر بلوري ذو رائحة مطهرة)، ويحوّل لون ثاني كرومات البوتاسيوم البرتقالي إلى الأخضر الزمردي."
        ],
        swatch=NONE,
        formula=True,
        badge="Liquid Alcohol",
        arabic_summary="كحول أليفاتي سائل خفيف يمتزج بالماء؛ إيجابي في اختبار اليودوفورم (راسب أصفر) ويخضر لون ثاني كرومات البوتاسيوم المحمضة."
    ),

    "ORG_GLYCEROL": outcome(
        "C₃H₅(OH)₃",
        "الجليسرول (الجلسرين) — Glycerol",
        "Viscous syrupy trihydric alcohol; non-volatile, decolorizes borax-phenolphthalein on cold, evolves acrolein with KHSO4.",
        [
            "C₃H₅(OH)₃ → CH₂=CH-CHO ↑ (أكرولين نفاذ مدمع للعين) + 2H₂O"
        ],
        notes=[
            "سائل لزج ثقيل شفاف (قوام شرباتي)، غير متطاير، يمتزج بالماء تماماً ومتعادل.",
            "يزيل اللون الوردي لمحلول البوراكس والفينولفثالين على البارد ويعود اللون بالتسخين، ويتصاعد غاز الأكرولين النفاذ اللاذع جداً عند تسخينه مع مسحوق KHSO₄ الجاف."
        ],
        swatch=NONE,
        formula=True,
        badge="Trihydric Alcohol",
        arabic_summary="كحول ثلاثي الهيدروكسيل لزج القوام غير متطاير، يزيل وردية البوراكس على البارد ويعود بالحرارة، وينتج الأكرولين النفاذ مع KHSO₄."
    ),

    "ORG_ANILINE": outcome(
        "C₆H₅NH₂",
        "الأنيلين (أمينوبنزين) — Aniline",
        "Aromatic oily liquid amine; dissolves in dilute HCl, smoky flame, forms scarlet azo dye upon diazotization and coupling.",
        [
            "C₆H₅NH₂ + HNO₂ + HCl → C₆H₅N₂⁺Cl⁻ + 2H₂O",
            "C₆H₅N₂⁺Cl⁻ + C₁₀H₇O⁻ → C₆H₅-N=N-C₁₀H₆OH ↓ (صبغة آزو حمراء برتقالية) + Cl⁻"
        ],
        notes=[
            "سائل زيتي أصفر يغمق إلى البني المحمر عند التعرض للهواء والضوء، شحيح الذوبان بالماء لكنه يذوب تماماً في حمض HCl المخفف.",
            "يحترق بلهب مدخن أسود؛ عند أزوتته في حمام ثلجي (0-5°م) مع NaNO₂/HCl وإضافته إلى بيتا-نافثول في NaOH يعطي صبغة آزو برتقالية حمراء ساطعة."
        ],
        swatch="#78350f",
        formula=True,
        badge="Aromatic Amine",
        arabic_summary="أمين أروماتي سائل زيتي يذوب في HCl المخفف ولهبه مدخن؛ يعطي صبغة الآزو الحمراء البرتقالية الساطعة بالتفاعل مع النيتروز وبيتا-نافثول."
    ),

    # ------------------ 14 SOLIDS ------------------
    "ORG_OXALIC": outcome(
        "(COOH)₂·2H₂O",
        "حمض الأكساليك (حمض الحميض) — Oxalic Acid",
        "White crystalline dibasic acid; water soluble, effervesces with NaHCO3, decolorizes hot KMnO4, forms calcium oxalate.",
        [
            "(COO⁻)₂ + Ca²⁺ → CaC₂O₄ ↓ (أبيض)",
            "5(COOH)₂ + 2MnO₄⁻ + 6H⁺ → 2Mn²⁺ + 10CO₂ ↑ + 8H₂O"
        ],
        notes=[
            "حمض كربوكسيلي أليفاتي ثنائي القاعدية، صلب بلوري أبيض يذوب بسهولة في الماء البارد ويفور مع NaHCO₃.",
            "يحترق بلهب غير مدخن؛ يعطي راسباً أبيض فورياً مع CaCl₂ لا يذوب في حمض الخليك، ويزيل لون برمنجنات البوتاسيوم الساخنة عند 60-70°م."
        ],
        swatch=NONE,
        formula=True,
        badge="Dicarboxylic Acid",
        arabic_summary="حمض كربوكسيلي صلب أبيض يذوب في الماء البارد ويفور مع NaHCO₃، راسب أبيض فوري مع CaCl₂ لا يذوب بالأسيتيك، ويزيل لون KMnO₄ الساخن."
    ),

    "ORG_TARTARIC": outcome(
        "C₄H₆O₆",
        "حمض الطرطريك — Tartaric Acid",
        "White crystalline acid; highly water soluble, chars with burnt sugar odor, positive Fenton's test.",
        [
            "C₄H₄O₆²⁻ + Fe²⁺ + H₂O₂ + 2NaOH → [Fe-Tartrate Complex] (لون بنفسجي أرجواني داكن)"
        ],
        notes=[
            "حمض هيدروكسي كربوكسيلي صلب شديد الذوبان في الماء البارد ويفور مع NaHCO₃.",
            "يتفحم بشدة عند التسخين المباشر مع انبعاث رائحة السكر المحروق؛ تفاعل فنتون (FeSO₄ + H₂O₂ + NaOH) يعطي لوناً بنفسجياً مميزاً."
        ],
        swatch=NONE,
        formula=True,
        badge="Hydroxy Acid",
        arabic_summary="حمض صلب أبيض عالي الذوبان بالماء البارد ويفور مع NaHCO₃؛ يتفحم برائحة السكر المحروق وتفاعل فنتون يعطي لوناً بنفسجياً داكناً."
    ),

    "ORG_CITRIC": outcome(
        "C₆H₈O₇",
        "حمض الستريك (حمض الليمون) — Citric Acid",
        "White crystalline tribasic acid; water soluble, effervesces with NaHCO3, calcium citrate precipitates ONLY on boiling.",
        [
            "2C₆H₅O₇³⁻ + 3Ca²⁺ → Ca₃(C₆H₅O₇)₂ ↓ (يتكون أثناء الغليان فقط)"
        ],
        notes=[
            "حمض ثلاثي الكربوكسيل صلب يذوب بسهولة بالماء ويفور مع NaHCO₃، يتفحم ببطء دون انبعاث رائحة السكر المحروق.",
            "مع كلوريد الكالسيوم CaCl₂ في محلول متعادل: لا يتكون أي راسب على البارد، ولكن يتكون راسب أبيض فقط بعد الغليان لعدة دقائق، ويذوب ثانية بالتبريد."
        ],
        swatch=NONE,
        formula=True,
        badge="Tricarboxylic Acid",
        arabic_summary="حمض صلب أبيض يذوب بالماء ويفور مع NaHCO₃؛ يتميز بأن راسب كلوريد الكالسيوم يظهر فقط بالغليان الشديد ويختفي بالتبريد."
    ),

    "ORG_BENZOIC": outcome(
        "C₆H₅COOH",
        "حمض البنزويك — Benzoic Acid",
        "White crystalline aromatic acid; sparingly soluble in cold water, smoky flame, buff/flesh precipitate with neutral FeCl3.",
        [
            "3C₆H₅COO⁻ + Fe³⁺ + H₂O → (C₆H₅COO)₂FeOH ↓ (راسب بيج / بني مصفر) + C₆H₅COOH"
        ],
        notes=[
            "حمض أروماتي صلب ذو بلورات إبرية أو قشرية بيضاء، شحيح الذوبان في الماء البارد لكنه يذوب في الماء الساخن ويفور مع NaHCO₃.",
            "يحترق بلهب مدخن أسود؛ يعطي محلوله المتعادل راسباً لحمياً (بيج / بني مصفر - Buff ppt) مع FeCl₃ المتعادل يذوب في الأحماض المخففة."
        ],
        swatch=NONE,
        formula=True,
        badge="Aromatic Acid",
        arabic_summary="حمض أروماتي صلب شحيح الذوبان بالماء البارد ويفور مع NaHCO₃، لهب مدخن، ويعطي راسباً بيج لحمياً مميزاً مع FeCl₃ المتعادل."
    ),

    "ORG_SALICYLIC": outcome(
        "C₆H₄(OH)COOH",
        "حمض الساليسيليك — Salicylic Acid",
        "White crystalline phenolic acid; sparingly soluble in cold water, smoky flame, intense permanent violet color with neutral FeCl3.",
        [
            "C₆H₄(OH)COOH + Fe³⁺ → [Fe(Salicylate)₂]⁺ (لون بنفسجي كثيف وثابت)"
        ],
        notes=[
            "حمض فينولي صلب شحيح الذوبان في الماء البارد ويفور مع NaHCO₃، يحترق بلهب مدخن.",
            "يعطي لوناً بنفسجياً داكناً ثابتاً جداً لا يزول مع كلوريد الحديد الثلاثي المتعادل لاحتوائه على مجموعة الهيدروكسيل الفينولية المجاورة للكربوكسيل."
        ],
        swatch=NONE,
        formula=True,
        badge="Phenolic Acid",
        arabic_summary="حمض فينولي صلب شحيح الذوبان بالماء البارد ويفور مع NaHCO₃؛ لهب مدخن، ويعطي لوناً بنفسجياً كثيفاً وثابتاً مع FeCl₃ المتعادل."
    ),

    "ORG_PHENOL": outcome(
        "C₆H₅OH",
        "الفينول (حمض الكربوليك) — Phenol",
        "Deliquescent pinkish solid with carbolic odor; partially soluble in cold water, white ppt with bromine water, violet with FeCl3.",
        [
            "C₆H₅OH + 3Br₂ → C₆H₂Br₃OH ↓ (راسب أبيض من 2,4,6-ثلاثي بروموفينول) + 3HBr",
            "6C₆H₅OH + Fe³⁺ → [Fe(OC₆H₅)₆]³⁻ (لون بنفسجي) + 6H⁺"
        ],
        notes=[
            "بلورات متميعة وردية أو بيضاء ذات رائحة كربولية طبية مميزة جداً، تذوب جزئياً في الماء البارد (~8 جم/100 مل) وتذوب تماماً في NaOH.",
            "لا يفور مع NaHCO₃؛ يعطي راسباً أبيض كثيفاً فورياً مع ماء البروم المشبع، ويعطي لوناً بنفسجياً مع كلوريد الحديد الثلاثي المتعادل."
        ],
        swatch="#f472b6",
        formula=True,
        badge="Monohydric Phenol",
        arabic_summary="فينول صلب متميع برائحة كربولية مميزة، يذوب جزئياً بالماء البارد وفي NaOH بدون فوران؛ يعطي راسباً أبيض مع ماء البروم ولوناً بنفسجياً مع FeCl₃."
    ),

    "ORG_RESORCINOL": outcome(
        "C₆H₄(OH)₂",
        "الريسورسينول (1,3-ثنائي هيدروكسي بنزين) — Resorcinol",
        "White/beige solid; highly water soluble, dark violet with FeCl3, intense green fluorescein in phthalein test.",
        [
            "C₆H₄(CO)₂O + 2C₆H₄(OH)₂ → Fluorescein (فلورسين أخضر مشع) + 2H₂O"
        ],
        notes=[
            "فينول ثنائي الهيدروكسيل، صلب أبيض إلى بيج، شديد الذوبان في الماء البارد (عكس الفينول والنافثولات)، يذوب في NaOH بدون فوران مع NaHCO₃.",
            "يعطي لوناً بنفسجياً غامقاً مع FeCl₃؛ وتفاعل الفثالين (التسخين مع أنهيدريد الفثاليك وH₂SO₄ ثم الصب في NaOH) يعطي محلول فلورسين أخضر فسفورياً ساطعاً."
        ],
        swatch=NONE,
        formula=True,
        badge="Dihydric Phenol",
        arabic_summary="فينول صلب شديد الذوبان في الماء البارد بدون فوران مع NaHCO₃؛ يعطي لوناً بنفسجياً مع FeCl₃، وتفاعل الفثالين ينتج فلورسين أخضر فسفورياً مبهراً."
    ),

    "ORG_ALPHA_NAPHTHOL": outcome(
        "α-C₁₀H₇OH",
        "ألفا-نافثول (1-نافثول) — 1-Naphthol",
        "Aromatic solid insoluble in cold water; dissolves in NaOH, dark violet coloration with bleaching powder / NaOCl solution.",
        [
            "C₁₀H₇OH + ClO⁻ → تلون بنفسجي داكن يتحول إلى راسب بني محمر"
        ],
        notes=[
            "مسحوق صلب لا يذوب في الماء البارد إطلاقاً، يذوب في هيدروكسيد الصوديوم، يحترق بلهب مدخن أسود كثيف.",
            "عند إضافة محلول مسحوق القصر (هيبوكلوريت الكالسيوم أو الصوديوم) يعطي تلوناً بنفسجياً داكناً فورياً يتحول إلى راسب بني محمر."
        ],
        swatch=NONE,
        formula=True,
        badge="Naphthol (Phenol)",
        arabic_summary="نافثول أروماتي صلب لا يذوب في الماء البارد ويذوب في NaOH؛ لهب مدخن، ويعطي تلوناً بنفسجياً داكناً مع مسحوق القصر / هيبوكلوريت الصوديوم."
    ),

    "ORG_BETA_NAPHTHOL": outcome(
        "β-C₁₀H₇OH",
        "بيتا-نافثول (2-نافثول) — 2-Naphthol",
        "Aromatic solid insoluble in cold water; dissolves in NaOH, negative with bleaching powder, brilliant scarlet dye with diazonium salt.",
        [
            "C₁₀H₇O⁻ + C₆H₅N₂⁺ → C₆H₅-N=N-C₁₀H₆OH ↓ (صبغة آزو قرمزية حمراء ساطعة)"
        ],
        notes=[
            "مسحوق بلوري أبيض أو وردي باهت عديم الرائحة تقريباً، لا يذوب في الماء البارد ويذوب في هيدروكسيد الصوديوم، لهب مدخن كثيف.",
            "سلبي مع مسحوق القصر (لا يعطي أي لون بنفسجي بعكس ألفا-نافثول)، يعطي لوناً أخضر باهتاً مع FeCl₃، وراسباً قرمزي/أحمر برتقالي ساطع مع أملاح الديازونيوم."
        ],
        swatch=NONE,
        formula=True,
        badge="Naphthol (Phenol)",
        arabic_summary="نافثول صلب لا يذوب في الماء البارد ويذوب في NaOH بدون تفاعل مع مسحوق القصر؛ يعطي صبغة آزو قرمزية حمراء ساطعة مع أملاح الديازونيوم."
    ),

    "ORG_GLUCOSE": outcome(
        "C₆H₁₂O₆",
        "الجلوكوز (سكر العنب / دكستروز) — D-Glucose",
        "Soluble aldohexose reducing sugar; chars with burnt sugar smell, reduces Fehling's, needle-cluster osazone in 5-10 min.",
        [
            "C₆H₁₂O₆ + 2Cu²⁺ + 5OH⁻ → C₆H₁₁O₇⁻ + Cu₂O ↓ (أحمر طوبي) + 3H₂O",
            "C₆H₁₂O₆ + 3C₆H₅NHNH₂ → Glucosazone ↓ (بلورات إبرية صفراء) + C₆H₅NH₂ + NH₃ + 2H₂O"
        ],
        notes=[
            "سكر أحادي ألدوزي صلب أبيض يذوب بالماء، يتفحم مع انبعاث رائحة السكر المحروق وتفاعل موليش إيجابي بحلقة بنفسجية.",
            "يختزل محلول فهلنج ومحلول بارفويد سريعاً (راسب أحمر طوبي)؛ تفاعل سيلوانوف سلبي في أول دقيقتين؛ يكوّن بلورات الجلوكوزازون الإبرية بعد 5-10 دقائق."
        ],
        swatch=NONE,
        formula=True,
        badge="Monosaccharide (Aldose)",
        arabic_summary="سكر أحادي ألدوزي يذوب بالماء ويتفحم برائحة السكر المحروق؛ يختزل فهلنج سريعاً، سلبي في أول دقيقتين مع سيلوانوف، وبلورات أوزازون إبرية."
    ),

    "ORG_FRUCTOSE": outcome(
        "C₆H₁₂O₆",
        "الفركتوز (سكر الفاكهة) — D-Fructose",
        "Soluble ketohexose reducing sugar; rapid intense cherry-red color with Seliwanoff's test within 1-2 minutes.",
        [
            "C₆H₁₂O₆ + 2Cu²⁺ + 5OH⁻ → Cu₂O ↓ (أحمر طوبي) + أحماض سكرية"
        ],
        notes=[
            "سكر أحادي كيتوزي صلب يذوب في الماء، يتفحم برائحة السكر المحروق وموليش إيجابي.",
            "يختزل فهلنج؛ ويتميز بتفاعل سيلوانوف فائق السرعة حيث يعطي لوناً أحمر كرزياً داكناً خلال 60-90 ثانية من الغليان مع كاشف سيلوانوف (ريسورسينول وHCl)."
        ],
        swatch=NONE,
        formula=True,
        badge="Monosaccharide (Ketose)",
        arabic_summary="سكر أحادي كيتوزي يذوب بالماء ويتفحم برائحة السكر المحروق؛ يختزل فهلنج سريعاً، وإيجابي وسريع جداً مع اختبار سيلوانوف (أحمر كرزي < دقيقتين)."
    ),

    "ORG_SUCROSE": outcome(
        "C₁₂H₂₂O₁₁",
        "السكروز (سكر القصب / المائدة) — Sucrose",
        "Soluble disaccharide; non-reducing directly with Fehling's, reduces Fehling's after acid hydrolysis.",
        [
            "C₁₂H₂₂O₁₁ + H₂O → C₆H₁₂O₆ (Glucose) + C₆H₁₂O₆ (Fructose)"
        ],
        notes=[
            "سكر ثنائي صلب بلوري أبيض يذوب في الماء بسهولة، يتفحم برائحة السكر المحروق وتفاعل موليش إيجابي بحلقة بنفسجية.",
            "سكر غير مختزل مباشرة (سلبي تماماً مع فهلنج وبارفويد)؛ وعند غليه مع قطرات من HCl المركز ثم معادلته بهيدروكسيد الصوديوم يتحلل مائياً ويختزل فهلنج فورياً."
        ],
        swatch=NONE,
        formula=True,
        badge="Disaccharide",
        arabic_summary="سكر ثنائي غير مختزل يذوب بالماء ويتفحم برائحة السكر المحروق؛ سلبي مع فهلنج مباشرة، ويصبح إيجابياً ومختزلاً بعد التحلل المائي الحمضي والمعادلة."
    ),

    "ORG_STARCH": outcome(
        "(C₆H₁₀O₅)ₙ",
        "النشا — Starch",
        "Insoluble polysaccharide; forms colloidal solution on boiling, reversible deep blue color with iodine.",
        [
            "Starch + I₂/KI ⇌ [Starch-Iodine Complex] (أزرق نيلي يزول بالتسخين ويعود بالتبريد)"
        ],
        notes=[
            "كربوهيدرات عديدة التسكر صلبة مسحوقية بيضاء لا تذوب في الماء البارد وتكوّن معلقاً غروياً عند الغليان، تتفحم برائحة السكر المحروق وموليش إيجابي.",
            "تعطي لوناً أزرق نيلياً كثيفاً مع محلول اليود، يختفي اللون تماماً عند التسخين ويعود للظهور بمجرد التبريد، وسلبي مع فهلنج."
        ],
        swatch=NONE,
        formula=True,
        badge="Polysaccharide",
        arabic_summary="كربوهيدرات عديدة صلبة لا تذوب بالماء البارد؛ تتفحم برائحة السكر المحروق، وتعطي لوناً أزرق نيلياً مميزاً مع اليود يختفي بالحرارة ويعود بالتبريد."
    ),

    "ORG_UREA": outcome(
        "CO(NH₂)₂",
        "اليوريا (كارباميد) — Urea",
        "White crystalline diamide; highly soluble, neutral, chars evolving NH3, positive rose-violet Biuret reaction.",
        [
            "2CO(NH₂)₂ → NH₂CONHCONH₂ (Biuret) + NH₃ ↑",
            "Biuret + Cu²⁺ + 2OH⁻ → [Cu(Biuret)₂]²⁻ (لون وردي بنفسجي)"
        ],
        notes=[
            "مركب أميدي نيتروجيني صلب أبيض شديد الذوبان في الماء ومتعادل تماماً مع عباد الشمس والبيكربونات، سلبي مع موليش و2,4-DNP.",
            "ينصهر ويتصاعد منه غاز النشادر بالتسخين الجاف، ويعطي تفاعل البيوريت الإيجابي (لون وردي بنفسجي مع NaOH وCuSO₄)، ويفور مع HNO₂ أو هيبوبروميت الصوديوم بتصاعد غاز النيتروجين N₂."
        ],
        swatch=NONE,
        formula=True,
        badge="Amide",
        arabic_summary="أميد صلب أبيض عالي الذوبان ومتعادل؛ ينصهر ويتصاعد منه غاز النشادر بالتسخين، ويعطي لوناً وردياً بنفسجياً في تفاعل البيوريت ويفور مع حمض النيتروز."
    )
}

# =========================================================================
# 2. ORGANIC CONFIRMATORY TESTS (25 PROTOCOLS)
# =========================================================================

ORGANIC_CONFIRMATORY_TESTS = {
    "ORG_FORMIC": {
        "ion": "HCOOH",
        "name": "حمض الفورميك (Formic Acid)",
        "reagent": "محلول نترات الفضة النشادرية (كاشف تولن) أو برمنجنات البوتاسيوم KMnO₄ المحمضة",
        "procedure": "أضف 1 مل من كاشف تولن إلى أنبوبة نظيفة تحتوي على بضع قطرات من الحمض، وسخّن بلطف في حمام مائي لمدة دقيقتين.",
        "expected_sign": "تكون مرآة فضية لامعة على الجدار الداخلي للأنبوبة أو راسب رمادي/أسود من الفضة، واختزال KMnO₄ المحمضة وزوال لونها البنفسجي.",
        "equations": [
            "HCOOH + 2[Ag(NH₃)₂]⁺ + 2OH⁻ → 2Ag ↓ + CO₂ ↑ + 4NH₃ + 2H₂O",
            "5HCOOH + 2MnO₄⁻ + 6H⁺ → 2Mn²⁺ + 5CO₂ ↑ + 8H₂O"
        ]
    },

    "ORG_ACETIC": {
        "ion": "CH₃COOH",
        "name": "حمض الأسيتيك / الخليك (Acetic Acid)",
        "reagent": "محلول كلوريد الحديد الثلاثي المتعادل (Neutral FeCl₃)",
        "procedure": "عادل قطرات من الحمض بمحلول مخفف من هيدروكسيد الأمونيوم حتى زوال الحموضة وسخّن لطرد الأمونيا الزائدة، ثم أضف قطرات من محلول FeCl₃ المتعادل.",
        "expected_sign": "ظهور لون أحمر دامي كثيف (Blood-red color)، يتحول إلى راسب بني محمر من أسيتات الحديديك القاعدية عند الغليان.",
        "equations": [
            "3CH₃COO⁻ + Fe³⁺ + 2H₂O → [Fe₃(OH)₂(CH₃COO)₆]⁺ + 2H⁺",
            "[Fe₃(OH)₂(CH₃COO)₆]⁺ + 4H₂O → 3Fe(OH)₂CH₃COO ↓ + 3CH₃COOH + H⁺"
        ]
    },

    "ORG_FORMALDEHYDE": {
        "ion": "HCHO",
        "name": "الفورمالدهيد (Formaldehyde)",
        "reagent": "محلول فهلنج (Fehling's A & B) أو كاشف شيف (Schiff's Reagent)",
        "procedure": "أضف حجوم متساوية من فهلنج A وفهلنج B إلى 1 مل من العينة وسخّن حتى الغليان، واختبر عينة أخرى بإضافة كاشف شيف على البارد.",
        "expected_sign": "تكون راسب أحمر طوبي كثيف من Cu₂O، وظهور لون قرمزي/وردي بنفسجي فوري مع كاشف شيف، مع سلبية تامة لاختبار اليودوفورم.",
        "equations": [
            "HCHO + 2Cu²⁺ + 5OH⁻ → HCOO⁻ + Cu₂O ↓ + 3H₂O"
        ]
    },

    "ORG_ACETALDEHYDE": {
        "ion": "CH₃CHO",
        "name": "الأسيتالدهيد (Acetaldehyde)",
        "reagent": "محلول اليود في يوديد البوتاسيوم (I₂/KI) مع هيدروكسيد الصوديوم (اختبار اليودوفورم)",
        "procedure": "أضف 2 مل من محلول اليود إلى قطرات من العينة، ثم أضف هيدروكسيد الصوديوم قطرة قطرة حتى يزول لون اليود ويصبح أصفر باهتاً، وسخّن بلطف عند 60°م.",
        "expected_sign": "تكون راسب أصفر متبلور من اليودوفورم (CHI₃) ذو رائحة دوائية مطهرة مميزة فور التبريد.",
        "equations": [
            "CH₃CHO + 3I₂ + 4NaOH → CHI₃ ↓ + HCOONa + 3NaI + 3H₂O"
        ]
    },

    "ORG_BENZALDEHYDE": {
        "ion": "C₆H₅CHO",
        "name": "البنزالدهيد (Benzaldehyde)",
        "reagent": "محلول بيكبريتيت الصوديوم المشبع (NaHSO₃) أو كاشف تولن",
        "procedure": "رج 1 مل من البنزالدهيد مع 2 مل من محلول بيكبريتيت الصوديوم المشبع بشدة في حمام ثلجي.",
        "expected_sign": "تكون مركب إضافة بلوري أبيض ناصع من بيكبريتيت البنزالدهيد، مع تكون مرآة فضية مع كاشف تولن وسلبية تامة مع فهلنج.",
        "equations": [
            "C₆H₅CHO + NaHSO₃ → C₆H₅CH(OH)SO₃Na ↓",
            "C₆H₅CHO + 2[Ag(NH₃)₂]⁺ + 2OH⁻ → C₆H₅COO⁻ + 2Ag ↓ + NH₄⁺ + 3NH₃ + H₂O"
        ]
    },

    "ORG_ACETONE": {
        "ion": "CH₃COCH₃",
        "name": "الأسيتون (Acetone)",
        "reagent": "نيتروبروسيد الصوديوم Na₂[Fe(CN)₅NO] وهيدروكسيد الصوديوم (Legal's Test)",
        "procedure": "أضف بضع قطرات من محلول نيتروبروسيد الصوديوم الطازج إلى 1 مل من العينة، ثم أضف قطرات من NaOH المركز، يليه قطرات من حمض الخليك الثلجي.",
        "expected_sign": "ظهور لون أحمر ياقوتي كثيف، يتحول إلى لون أزرق بنفسجي عند تحميضه بحمض الخليك.",
        "equations": [
            "CH₃COCH₃ + [Fe(CN)₅NO]²⁻ + 2OH⁻ → [Fe(CN)₅NO-CH₂COCH₃]⁴⁻ + H₂O",
            "CH₃COCH₃ + 3I₂ + 4NaOH → CHI₃ ↓ + CH₃COONa + 3NaI + 3H₂O"
        ]
    },

    "ORG_ACETOPHENONE": {
        "ion": "C₆H₅COCH₃",
        "name": "الأسيتوفينون (Acetophenone)",
        "reagent": "اختبار اليودوفورم (I₂/NaOH) وكاشف 2,4-DNP",
        "procedure": "أضف محلول اليود وهيدروكسيد الصوديوم وسخّن عند 60°م، وافحص العينة الصلبة/السائلة (درجة الانصهار ~20°م).",
        "expected_sign": "تكون راسب أصفر واضح من اليودوفورم ذو رائحة مطهرة، مع تكوين بلورات برتقالية حمراء مع كاشف 2,4-DNP وعدم التفاعل مع تولن.",
        "equations": [
            "C₆H₅COCH₃ + 3I₂ + 4NaOH → CHI₃ ↓ + C₆H₅COONa + 3NaI + 3H₂O"
        ]
    },

    "ORG_METHANOL": {
        "ion": "CH₃OH",
        "name": "الميثانول (Methanol)",
        "reagent": "حمض الساليسيليك وحمض الكبريتيك المركز (تكوين إستر ساليسيلات الميثيل)",
        "procedure": "أضف 0.5 جم من حمض الساليسيليك إلى 1 مل من الميثانول في أنبوبة جافة، ثم أضف بحرص 1 مل من H₂SO₄ المركز وسخّن في حمام مائي لمدة 3 دقائق، ثم اسكب المحتويات في كأس به ماء بارد وبيكربونات. (تنبيه أمان: لا تستنشق البخار بعمق، الميثانول عالي السمية).",
        "expected_sign": "انبعاث رائحة زيت الكافور الطبية المميزة (Wintergreen / أبو فاس) طافية على السطح، مع سلبية تامة لاختبار اليودوفورم.",
        "equations": [
            "C₆H₄(OH)COOH + CH₃OH → C₆H₄(OH)COOCH₃ + H₂O"
        ]
    },

    "ORG_ETHANOL": {
        "ion": "C₂H₅OH",
        "name": "الإيثانول (Ethanol)",
        "reagent": "محلول ثاني كرومات البوتاسيوم المحمض (K₂Cr₂O₇/H₂SO₄) واختبار اليودوفورم",
        "procedure": "أضف 1 مل من محلول ثاني كرومات البوتاسيوم المحمض بقطرات من H₂SO₄ المخفف إلى 1 مل من الإيثانول وسخّن بلطف.",
        "expected_sign": "تحول لون المحلول من البرتقالي إلى الأخضر الزمردي نتيجة تكون Cr³⁺ مع تصاعد رائحة الأسيتالدهيد، وإيجابية اختبار اليودوفورم (راسب أصفر).",
        "equations": [
            "3C₂H₅OH + Cr₂O₇²⁻ + 8H⁺ → 3CH₃CHO + 2Cr³⁺ + 7H₂O",
            "C₂H₅OH + 4I₂ + 6NaOH → CHI₃ ↓ + HCOONa + 5NaI + 5H₂O"
        ]
    },

    "ORG_GLYCEROL": {
        "ion": "C₃H₅(OH)₃",
        "name": "الجليسرول / الجلسرين (Glycerol)",
        "reagent": "كبريتات البوتاسيوم الهيدروجينية KHSO₄ الصلبة (اختبار الأكرولين) ومحلول البوراكس-فينولفثالين",
        "procedure": "ضع بضع قطرات من الجليسرول مع ضعف وزنه من مسحوق KHSO₄ الجاف في أنبوبة اختبار وسخّن تسخيناً شديداً ومباشراً.",
        "expected_sign": "تصاعد أبخرة نفاذة ولاذعة جداً ومدمعة للعين من غاز الأكرولين (Acrolein)، واختفاء لون الفينولفثالين الوردي مع البوراكس على البارد وعودته بالتسخين.",
        "equations": [
            "C₃H₅(OH)₃ → CH₂=CH-CHO ↑ + 2H₂O"
        ]
    },

    "ORG_ANILINE": {
        "ion": "C₆H₅NH₂",
        "name": "الأنيلين (Aniline)",
        "reagent": "حمض النيتروز (NaNO₂/HCl على البارد 0-5°م) ومحلول بيتا-نافثول في NaOH (تفاعل الأزوتة والازدواج)",
        "procedure": "أذب قطرات من الأنيلين في 2 مل من HCl المخفف وبرد في الثلج إلى 0-5°م، أضف قطرات من محلول NaNO₂ المبرد، ثم أضف الخليط ببطء إلى محلول بيتا-نافثول في هيدروكسيد الصوديوم.",
        "expected_sign": "تكون راسب برتقالي مائل للحمرة فوري ساطع لصبغة الآزو غير الذائبة (Scarlet/Orange Azo Dye).",
        "equations": [
            "C₆H₅NH₂ + HNO₂ + HCl → C₆H₅N₂⁺Cl⁻ + 2H₂O",
            "C₆H₅N₂⁺Cl⁻ + C₁₀H₇O⁻ → C₆H₅-N=N-C₁₀H₆OH ↓ + Cl⁻"
        ]
    },

    "ORG_OXALIC": {
        "ion": "(COOH)₂",
        "name": "حمض الأكساليك (Oxalic Acid)",
        "reagent": "محلول كلوريد الكالسيوم (CaCl₂) ومحلول برمنجنات البوتاسيوم المحمض (KMnO₄/H₂SO₄)",
        "procedure": "أضف محلول CaCl₂ إلى محلول الحمض المتعادل ثم أضف حمض الخليك المخفف، واختبر عينة أخرى بإضافة قطرات من KMnO₄ المحمض عند 60-70°م.",
        "expected_sign": "تكون راسب أبيض ناصع من أكسالات الكالسيوم لا يذوب في حمض الخليك ويذوب في HCl، وزوال لون البرمنجنات البنفسجي سريعاً عند التسخين.",
        "equations": [
            "(COO⁻)₂ + Ca²⁺ → CaC₂O₄ ↓",
            "5(COOH)₂ + 2MnO₄⁻ + 6H⁺ → 2Mn²⁺ + 10CO₂ ↑ + 8H₂O"
        ]
    },

    "ORG_TARTARIC": {
        "ion": "C₄H₆O₆",
        "name": "حمض الطرطريك (Tartaric Acid)",
        "reagent": "كبريتات الحديدوز وبيروكسيد الهيدروجين وهيدروكسيد الصوديوم (تفاعل فنتون - Fenton's Test)",
        "procedure": "أضف قطرة من محلول كبريتات الحديدوز FeSO₄ الطازج إلى محلول الحمض، ثم قطرة من H₂O₂ (ماء الأكسجين)، ثم أضف وفرة من هيدروكسيد الصوديوم NaOH.",
        "expected_sign": "ظهور لون بنفسجي أو أرجواني داكن مميز جداً، ويتفحم بشدة عند التسخين المباشر مع انبعاث رائحة السكر المحروق.",
        "equations": [
            "C₄H₄O₆²⁻ + Fe²⁺ + H₂O₂ + NaOH → [Fe-Tartrate Complex] (Violet Color)"
        ]
    },

    "ORG_CITRIC": {
        "ion": "C₆H₈O₇",
        "name": "حمض الستريك / الليمون (Citric Acid)",
        "reagent": "محلول كلوريد الكالسيوم (CaCl₂) مع الغليان، وكاشف دينيجيه (Denigès Reagent: HgSO₄/H₂SO₄)",
        "procedure": "أضف محلول CaCl₂ إلى محلول الحمض المتعادل على البارد ولاحظ، ثم سخّن الأنبوبة حتى الغليان الشديد لمدة دقيقتين.",
        "expected_sign": "لا يتكون أي راسب على البارد، ولكن يتكون راسب أبيض بلوري من سترات الكالسيوم فقط أثناء الغليان، يذوب ثانية بالتبريد.",
        "equations": [
            "2C₆H₅O₇³⁻ + 3Ca²⁺ → Ca₃(C₆H₅O₇)₂ ↓ (يتكون بالغليان فقط)"
        ]
    },

    "ORG_BENZOIC": {
        "ion": "C₆H₅COOH",
        "name": "حمض البنزويك (Benzoic Acid)",
        "reagent": "محلول كلوريد الحديد الثلاثي المتعادل (Neutral FeCl₃)",
        "procedure": "أذب بلورات الحمض في قليل من هيدروكسيد الأمونيوم وسخّن حتى تطاير النشادر تماماً (محلول متعادل)، ثم أضف قطرات من محلول FeCl₃ المتعادل.",
        "expected_sign": "تكون راسب بيج / بني مصفر لحمي مميز (Buff / Flesh precipitate) من بنزوات الحديديك القاعدية يذوب في الأحماض المعدنية.",
        "equations": [
            "3C₆H₅COO⁻ + Fe³⁺ + H₂O → (C₆H₅COO)₂FeOH ↓ + C₆H₅COOH"
        ]
    },

    "ORG_SALICYLIC": {
        "ion": "C₆H₄(OH)COOH",
        "name": "حمض الساليسيليك (Salicylic Acid)",
        "reagent": "محلول كلوريد الحديد الثلاثي المتعادل (FeCl₃)",
        "procedure": "أضف بضع قطرات من محلول كلوريد الحديديك إلى المحلول المائي للحمض.",
        "expected_sign": "ظهور لون بنفسجي داكن كثيف وثابت جداً لا يزول (لوجود المجموعة الفينولية المجاورة للكربوكسيل).",
        "equations": [
            "C₆H₄(OH)COOH + Fe³⁺ → [Fe(Salicylate)₂]⁺ (Deep Violet Complex)"
        ]
    },

    "ORG_PHENOL": {
        "ion": "C₆H₅OH",
        "name": "الفينول (حمض الكربوليك / Phenol)",
        "reagent": "ماء البروم المشبع (Bromine Water) ومحلول كلوريد الحديديك FeCl₃",
        "procedure": "أضف ماء البروم قطرة قطرة مع الرج إلى محلول مائي مخفف من الفينول.",
        "expected_sign": "تكون راسب أبيض ناصع كثيف من 2,4,6-ثلاثي بروموفينول مع زوال لون البروم، وظهور لون بنفسجي مع FeCl₃ المتعادل.",
        "equations": [
            "C₆H₅OH + 3Br₂ → C₆H₂Br₃OH ↓ + 3HBr"
        ]
    },

    "ORG_RESORCINOL": {
        "ion": "C₆H₄(OH)₂",
        "name": "الريسورسينول (Resorcinol)",
        "reagent": "أنهيدريد الفثاليك وحمض الكبريتيك المركز مع هيدروكسيد الصوديوم (تفاعل الفثالين - Phthalein Test)",
        "procedure": "اخلط كمية متساوية من الريسورسينول مع أنهيدريد الفثاليك في أنبوبة جافة وأضف قطرتين من H₂SO₄ المركز، سخّن لمدة دقيقة حتى الانصهار، ثم برد واسكب المحتويات في كأس به ماء وهيدروكسيد صوديوم مخفف.",
        "expected_sign": "تكون محلول مشع ذو لون أخضر فلوريسيني ساطع وساحر (Fluorescein) تحت الضوء المنعكس.",
        "equations": [
            "C₆H₄(CO)₂O + 2C₆H₄(OH)₂ → Fluorescein + 2H₂O"
        ]
    },

    "ORG_ALPHA_NAPHTHOL": {
        "ion": "α-C₁₀H₇OH",
        "name": "ألفا-نافثول (1-Naphthol)",
        "reagent": "محلول هيبوكلوريت الكالسيوم أو الصوديوم (مسحوق القصر / Bleaching Powder) أو كلوريد الحديديك FeCl₃",
        "procedure": "أضف قطرات من محلول مسحوق القصر المصفى (أو كلوريد الحديديك) إلى محلول ألفا-نافثول القلوي أو في قليل من الكحول.",
        "expected_sign": "ظهور تلون بنفسجي داكن يتحول إلى راسب قرمزي / بني محمر كثيف، وازدواجه مع ملح الديازونيوم يعطي صبغة حمراء بنية.",
        "equations": [
            "C₁₀H₇OH + [O] / ClO⁻ → Dark Violet/Red-Brown Condensation Product"
        ]
    },

    "ORG_BETA_NAPHTHOL": {
        "ion": "β-C₁₀H₇OH",
        "name": "بيتا-نافثول (2-Naphthol)",
        "reagent": "محلول كلوريد الحديد الثلاثي FeCl₃ وتفاعل الأزوتة مع كلوريد البنزين ديازونيوم",
        "procedure": "أضف قطرات من محلول كلوريد الحديديك إلى محلول بيتا-نافثول، واختبر عينة أخرى في NaOH بإضافة كلوريد البنزين ديازونيوم المبرد.",
        "expected_sign": "تكون لون أخضر باهت مع FeCl₃ (ولا يعطي أي لون بنفسجي مع مسحوق القصر)، وتكون راسب قرمزي/أحمر برتقالي ساطع لصبغة الآزو.",
        "equations": [
            "2C₁₀H₇OH + FeCl₃ → Pale Green Complex",
            "C₁₀H₇O⁻ + C₆H₅N₂⁺ → C₆H₅-N=N-C₁₀H₆OH ↓"
        ]
    },

    "ORG_GLUCOSE": {
        "ion": "C₆H₁₂O₆",
        "name": "الجلوكوز (D-Glucose)",
        "reagent": "كاشف بارفويد (Barfoed's Reagent) أو تكوين الأوزازون مع فينيل هيدرازين",
        "procedure": "سخّن محلول الجلوكوز مع كاشف بارفويد في حمام مائي مغلي، أو سخّن مع فينيل هيدرازين هيدروكلوريد وأسيتات الصوديوم لمدة 10 دقائق ثم اترك الأنبوبة تبرد ببطء.",
        "expected_sign": "تكون راسب أحمر مع بارفويد خلال دقيقتين (سكر أحادي)، وتكون بلورات صفراء ذهبية إبرية مميزة من الجلوكوزازون (Needle clusters) تفحص بالمجهر.",
        "equations": [
            "C₆H₁₂O₆ + 3C₆H₅NHNH₂ → Glucosazone ↓ + C₆H₅NH₂ + NH₃ + 2H₂O"
        ]
    },

    "ORG_FRUCTOSE": {
        "ion": "C₆H₁₂O₆",
        "name": "الفركتوز (D-Fructose)",
        "reagent": "كاشف سيلوانوف (Seliwanoff's Reagent: ريسورسينول في حمض HCl 6M)",
        "procedure": "أضف 2 مل من كاشف سيلوانوف إلى 0.5 مل من محلول الفركتوز، وضع الأنبوبة في حمام مائي مغلي لمدة 60-90 ثانية فقط.",
        "expected_sign": "ظهور لون أحمر كرزي/قرمزي داكن فوري وسريع جداً خلال أقل من دقيقتين مع تكون راسب أحمر عند استمرار الغليان.",
        "equations": [
            "Fructose → 5-HMF + Resorcinol → Cherry-red Condensation Complex"
        ]
    },

    "ORG_SUCROSE": {
        "ion": "C₁₂H₂₂O₁₁",
        "name": "السكروز (سكر القصب / Cane Sugar)",
        "reagent": "التحلل المائي الحمضي (Hydrolysis) ثم اختبار فهلنج",
        "procedure": "تأكد أولاً أن فهلنج سلبي على البارد والساخن، ثم أضف 3 قطرات من HCl المركز إلى 2 مل من محلول السكروز وسخّن حتى الغليان لمدة 3 دقائق، ثم عادل بـ NaOH حتى يصبح قلوياً وأضف فهلنج وسخّن.",
        "expected_sign": "سلبية فهلنج تماماً قبل التحلل، ثم ظهور راسب أحمر طوبي كثيف من Cu₂O بعد التحلل المائي لتفككه إلى جلوكوز وفركتوز.",
        "equations": [
            "C₁₂H₂₂O₁₁ + H₂O → C₆H₁₂O₆ (Glucose) + C₆H₁₂O₆ (Fructose)"
        ]
    },

    "ORG_STARCH": {
        "ion": "(C₆H₁₀O₅)ₙ",
        "name": "النشا (Starch)",
        "reagent": "محلول اليود في يوديد البوتاسيوم (Lugol's Iodine: I₂/KI)",
        "procedure": "حضر معلقاً نشوياً بتسخين القليل من النشا في ماء مغلي حتى يتكون محلول غروي ثم برده، وأضف قطرة واحدة من محلول اليود المخفف، ثم سخّن الأنبوبة وبردها ثانية تحت الصنبور.",
        "expected_sign": "ظهور لون أزرق نيلي كثيف على البارد، يزول اللون تماماً عند التسخين، ويعود للظهور بمجرد التبريد.",
        "equations": [
            "Starch + I₂/I₃⁻ ⇌ [Starch-Iodine Complex] (Blue Color, reversible with heat)"
        ]
    },

    "ORG_UREA": {
        "ion": "CO(NH₂)₂",
        "name": "اليوريا (Carbamide)",
        "reagent": "تفاعل البيوريت (Biuret Test: التسخين الجاف ثم هيدروكسيد الصوديوم وكبريتات النحاس CuSO₄)",
        "procedure": "سخّن كمية صغيرة من بلورات اليوريا في أنبوبة اختبار جافة حتى تنصهر ويتصاعد غاز النشادر ثم تتصلب الكتلة، برد الأنبوبة، أذب الناتج في 2 مل ماء مقطر، ثم أضف 1 مل من NaOH وقطرة واحدة فقط من محلول CuSO₄ المخفف.",
        "expected_sign": "ظهور لون وردي بنفسجي ساحر ومميز جداً (معقد البيوريت مع النحاس)، وتصاعد فقاعات غاز النيتروجين مع هيبوبروميت الصوديوم.",
        "equations": [
            "2NH₂CONH₂ → NH₂CONHCONH₂ (Biuret) + NH₃ ↑",
            "Biuret + Cu²⁺ + 2OH⁻ → [Cu(Biuret)₂]²⁻ (Rose-violet / Purple Complex)"
        ]
    }
}

# =========================================================================
# 3. ORGANIC DECISION TREE (Full Sequential Filtering Architecture)
# =========================================================================

ORGANIC_DECISION_TREE = {
    # Step 1: Physical State (سائل vs صلب)
    "org_q_state": question(
        "org_q_state",
        "What is the physical state of the organic sample at room temperature?",
        [
            option("سائل (Liquid) — يحصر البحث في 11 مركباً عضparse", "org_liq_q_water_sol", arabic_label="سائل (Liquid)"),
            option("مادة صلبة (Solid) — يحصر البحث في 14 مركباً عضparse", "org_sol_q_water_sol", arabic_label="مادة صلبة (Solid)")
        ],
        hint="حدد الحالة الفيزيائية للعينة العضوية النقية في درجة حرارة الغرفة (25°م).",
        arabic_text="الكشف العضوي — الخطوة 1: ما هي الحالة الفيزيائية للعينة أمامك؟"
    ),

    # -------------------------------------------------------------------------
    # LIQUID BRANCH (11 COMPOUNDS)
    # -------------------------------------------------------------------------
    "org_liq_q_water_sol": question(
        "org_liq_q_water_sol",
        "Is the liquid organic sample miscible with cold distilled water?",
        [
            option("يمتزج تماماً مع الماء البارد (Miscible — طبقة واحدة شفافة)", "org_liq_misc_q_acidity", arabic_label="يمتزج تماماً بالماء البارد"),
            option("لا يمتزج / شحيح الذوبان (Immiscible — ينفصل في طبقتين أو قطرات زيتية)", "org_liq_immisc_q_nature", arabic_label="لا يمتزج / شحيح الذوبان (طبقتين)")
        ],
        hint="أضف 0.5 مل من السائل المجهول إلى 2 مل من الماء المقطر في أنبوبة اختبار ورج جيداً. هل يمتزج بالكامل أم ينفصل كطبقة زيتية؟",
        arabic_text="السوائل العضوية — الخطوة 2: اختبر قابلية امتزاج السائل بالماء البارد:"
    ),

    # Miscible Liquids: Formic, Acetic, Formaldehyde, Acetaldehyde, Acetone, Methanol, Ethanol, Glycerol
    "org_liq_misc_q_acidity": question(
        "org_liq_misc_q_acidity",
        "Add a few drops of 5% Sodium Bicarbonate (NaHCO3) solution to the miscible liquid. What do you observe?",
        [
            option("فوران وتصاعد فقاعات غاز ثاني أكسيد الكربون CO2 (حمض كربوكسيلي سائل)", "org_liq_acid_q_test", arabic_label="فوران وتصاعد غاز CO2 (حمض كربوكسيلي)"),
            option("لا يحدث فوران (المركب متعادل — ألدهيد، كيتون، أو كحول)", "org_liq_neutral_q_dnp", arabic_label="لا يحدث فوران (متعادل)")
        ],
        hint="بيكربونات الصوديوم تكشف حامضية مجموعة الكربوكسيل الحرة في الأحماض العضوية بتصاعد غاز CO₂.",
        arabic_text="السوائل الممتزجة بالماء — الخطوة 3: أضف محلول بيكربونات الصوديوم (NaHCO₃) إلى السائل:"
    ),

    # Formic vs Acetic
    "org_liq_acid_q_test": question(
        "org_liq_acid_q_test",
        "Test with acidified Potassium Permanganate (KMnO4) or Tollen's reagent, and observe the odor:",
        [
            option("يزيل لون KMnO4 المحمض البنفسجي، أو يكوّن مرآة فضية مع تولن (خواص اختزالية)", "ORG_FORMIC", arabic_label="يختزل KMnO4 المحمضة أو كاشف تولن (فورميك)"),
            option("لا يزيل لون KMnO4، وله رائحة الخل المميزة (يعطي لوناً أحمر دامي مع FeCl3 المتعادل)", "ORG_ACETIC", arabic_label="رائحة الخل المميزة ولا يزيل KMnO4 (أسيتيك)")
        ],
        hint="حمض الفورميك يمتلك مجموعة هيدروجين ألدهيدية متصلة بالكربوكسيل (H-COOH) تمنحه قدرة اختزالية قوية يفتقر إليها حمض الأسيتيك.",
        arabic_text="الأحماض السائلة — تجربة التمييز الفاصلة بين حمض الفورميك وحمض الأسيتيك:"
    ),

    # Neutral Miscible Liquids -> 2,4-DNP (Formaldehyde, Acetaldehyde, Acetone vs Methanol, Ethanol, Glycerol)
    "org_liq_neutral_q_dnp": question(
        "org_liq_neutral_q_dnp",
        "Add 2,4-Dinitrophenylhydrazine (2,4-DNP) reagent to the liquid sample. What do you observe?",
        [
            option("يتكون راسب أصفر أو برتقالي فوري متبلور (مركب كربونيل: ألدهيد أو كيتون أليفاتي)", "org_liq_carbonyl_q_tollens", arabic_label="راسب أصفر / برتقالي فوري (ألدهيد أو كيتون)"),
            option("لا يتكون أي راسب ويظل المحلول رائقاً أصفر شفافاً (كحول أليفاتي)", "org_liq_alcohol_q_viscosity", arabic_label="لا يتكون راسب (كحول أليفاتي)")
        ],
        hint="كاشف 2,4-DNP يرسب الألدهيدات والكيتونات في صورة هيدرازونات صفراء أو برتقالية، بينما لا تتفاعل الكحولات معه إطلاقاً.",
        arabic_text="السوائل المتعادلة الممتزجة — الخطوة 4: أضف كاشف 2,4-ثنائي نيتروفينيل هيدرازين (2,4-DNP):"
    ),

    # Carbonyls: Formaldehyde, Acetaldehyde vs Acetone (Tollen's Test)
    "org_liq_carbonyl_q_tollens": question(
        "org_liq_carbonyl_q_tollens",
        "Add Tollen's reagent (ammoniacal silver nitrate) and warm gently in a water bath for 2-3 minutes:",
        [
            option("تكوّن مرآة فضية لامعة Ag على الجدار الداخلي للأنبوبة أو راسب رمادي (ألدهيد مختزل)", "org_liq_ald_q_iodoform", arabic_label="تكوّن مرآة فضية Ag (ألدهيد)"),
            option("لا تتكون مرآة فضية ويظل المحلول صافياً بدون اختزال (كيتون — أسيتون)", "ORG_ACETONE", arabic_label="سلبي مع تولن وفهلنج (الأسيتون)")
        ],
        hint="الألدهيدات تختزل أيونات الفضة في كاشف تولن إلى فلز الفضة المترسب كمرآة، بينما الكيتونات (كالأسيتون) لا تُختزل بسهولة بكاشف تولن.",
        arabic_text="مركبات الكربونيل السائلة — الخطوة 5: اختبار تولن (Tollen's Test) للتمييز بين الألدهيد والكيتون:"
    ),

    # Formaldehyde vs Acetaldehyde (Iodoform & Fehling)
    "org_liq_ald_q_iodoform": question(
        "org_liq_ald_q_iodoform",
        "Perform the Iodoform test (add Iodine solution + NaOH drops with mild warming to 60°C):",
        [
            option("تكوّن راسب أصفر متبلور من اليودوفورم CHI3 ذو رائحة مطهرة مميزة (أسيتالدهيد)", "ORG_ACETALDEHYDE", arabic_label="راسب أصفر في اختبار اليودوفورم (أسيتالدهيد)"),
            option("سلبي تماماً مع اليودوفورم، وله رائحة نفاذة خانقة مدمعة ويعطي راسباً أحمر مع فهلنج (فورمالدهيد)", "ORG_FORMALDEHYDE", arabic_label="سلبي مع اليودوفورم ورائحة خانقة (فورمالدهيد)")
        ],
        hint="الأسيتالدهيد (CH₃CHO) يحتوي على مجموعة ميثيل كربونيل تعطي اختبار اليودوفورم إيجابياً، بينما الفورمالدهيد (HCHO) لا يحتوي عليها.",
        arabic_text="الألدهيدات السائلة — التجربة التأكيدية الفاصلة بين الأسيتالدهيد والفورمالدهيد:"
    ),

    # Alcohols: Methanol, Ethanol vs Glycerol (Viscosity & Borax Test)
    "org_liq_alcohol_q_viscosity": question(
        "org_liq_alcohol_q_viscosity",
        "Observe the physical viscosity of the alcohol, its volatility, and response to the Borax-Phenolphthalein test:",
        [
            option("سائل لزج جداً وثقيل (قوام شرباتي)، غير متطاير، يزيل اللون الوردي للبوراكس-فينولفثالين على البارد", "ORG_GLYCEROL", arabic_label="سائل لزج جداً غير متطاير (الجليسرول)"),
            option("سائل خفيف القوام وسريع التطاير وذو رائحة كحولية معروفة (كحول أحادي الهيدروكسيل)", "org_liq_monoalcohol_q_iodoform", arabic_label="سائل خفيف سريع التطاير (كحول أحادي)")
        ],
        hint="الجليسرول كحول ثلاثي الهيدروكسيل عالي اللزوجة وقليل التطاير، بينما الميثانول والإيثانول سوائل خفيفة سريعة التطاير.",
        arabic_text="الكحولات السائلة — الخطوة 5: فحص اللزوجة وقوام السائل العضوي:"
    ),

    # Methanol vs Ethanol (Iodoform test & Salicylic Esterification)
    "org_liq_monoalcohol_q_iodoform": question(
        "org_liq_monoalcohol_q_iodoform",
        "Perform the Iodoform test (Iodine solution + NaOH with gentle warming), and check oxidation behavior:",
        [
            option("تكوّن راسب أصفر بلوري من اليودوفورم CHI3 برائحة مطهرة، ويخضر لون ثاني كرومات البوتاسيوم (إيثانول)", "ORG_ETHANOL", arabic_label="راسب أصفر في اختبار اليودوفورم (إيثانول)"),
            option("سلبي تماماً مع اليودوفورم؛ وعند تسخينه مع حمض الساليسيليك وH2SO4 يعطي رائحة إستر الكافور (ميثانول)", "ORG_METHANOL", arabic_label="سلبي مع اليودوفورم ورائحة زيت الكافور (ميثانول)")
        ],
        hint="الإيثانول (CH₃CH₂OH) يعطي اختبار اليودوفورم إيجابياً لاحتوائه على وحدة CH₃-CH(OH)-، بينما الميثانول (CH₃OH) لا يعطيه مطلقاً.",
        arabic_text="الكحولات الأحادية الخفيفة — التجربة التأكيدية الفاصلة بين الإيثانول والميثانول:"
    ),

    # Immiscible Liquids: Benzaldehyde, Acetophenone, Aniline
    "org_liq_immisc_q_nature": question(
        "org_liq_immisc_q_nature",
        "Test solubility in dilute Hydrochloric Acid (HCl 10%), and observe color and flame behavior:",
        [
            option("يذوب تماماً في حمض HCl المخفف؛ سائل زيتي أصفر يغمق بالهواء ولهب مدخن (قاعدة أمينية — أنيلين)", "ORG_ANILINE", arabic_label="يذوب في حمض HCl المخفف (الأنيلين)"),
            option("لا يذوب في حمض HCl المخفف؛ مركب أروماتي متعادل يتفاعل إيجابياً مع كاشف 2,4-DNP", "org_liq_aromatic_carbonyl_q", arabic_label="لا يذوب في HCl ويتفاعل مع 2,4-DNP (كربونيل أروماتي)")
        ],
        hint="الأنيلين قاعدة عضوية أروماتية تذوب في الأحماض المعدنية بتكوين ملح الأنيلينيوم الذائب، بينما مركبات الكربونيل الأروماتية لا تذوب بالأحماض.",
        arabic_text="السوائل غير الممتزجة بالماء — الخطوة 3: اختبار الذوبان في حمض الهيدروكلوريك المخفف (HCl):"
    ),

    # Benzaldehyde vs Acetophenone
    "org_liq_aromatic_carbonyl_q": question(
        "org_liq_aromatic_carbonyl_q",
        "Perform Tollen's test and the Iodoform test on the insoluble aromatic liquid:",
        [
            option("رائحة اللوز المر المميزة؛ يكوّن مرآة فضية لامعة مع كاشف تولن، وسلبي مع اليودوفورم وفهلنج (بنزالدهيد)", "ORG_BENZALDEHYDE", arabic_label="رائحة اللوز المر ومرآة فضية مع تولن (بنزالدهيد)"),
            option("سلبي مع كاشف تولن؛ يعطي راسباً أصفر متبلوراً في اختبار اليودوفورم (قد يتجمد في الشتاء < 20°م) (أسيتوفينون)", "ORG_ACETOPHENONE", arabic_label="راسب يودوفورم أصفر وسلبي مع تولن (أسيتوفينون)")
        ],
        hint="البنزالدهيد ألدهيد أروماتي يختزل تولن، بينما الأسيتوفينون كيتون ميثيلي أروماتي يعطي اختبار اليودوفورم ولا يختزل تولن.",
        arabic_text="مركبات الكربونيل الأروماتية غير الذائبة — التجربة الفاصلة بين البنزالدهيد والأسيتوفينون:"
    ),

    # -------------------------------------------------------------------------
    # SOLID BRANCH (14 COMPOUNDS)
    # -------------------------------------------------------------------------
    "org_sol_q_water_sol": question(
        "org_sol_q_water_sol",
        "Is the solid organic sample soluble in cold distilled water?",
        [
            option("تذوب بسهولة وبشكل كامل في الماء البارد (Water-Soluble Organic Solids)", "org_sol_soluble_q_reagent", arabic_label="تذوب تماماً في الماء البارد (ذائبة)"),
            option("شحيحة الذوبان أو عديمة الذوبان في الماء البارد (Insoluble / Sparingly Soluble Solids)", "org_sol_insoluble_q_acidity", arabic_label="لا تذوب / شحيحة الذوبان في الماء البارد")
        ],
        hint="ضع بلورات قليلة من المادة الصلبة في 2 مل من الماء المقطر البارد ورج بشدة لمدة دقيقة كاملة.",
        arabic_text="المواد الصلبة العضوية — الخطوة 2: اختبر قابلية ذوبان المادة الصلبة في الماء البارد:"
    ),

    # ------------------ Soluble Solids (8 Compounds) ------------------
    # Oxalic, Tartaric, Citric, Resorcinol, Urea, Glucose, Fructose, Sucrose
    "org_sol_soluble_q_reagent": question(
        "org_sol_soluble_q_reagent",
        "Add Sodium Bicarbonate (NaHCO3) solution to the aqueous solution of the soluble solid. What do you observe?",
        [
            option("فوران شديد وتصاعد فقاعات غاز CO2 (حمض كربوكسيلي أليفاتي صلب ذائب بالماء)", "org_sol_acid_soluble_q_cacl2", arabic_label="فوران شديد وتصاعد CO2 (حمض أليفاتي ذائب)"),
            option("لا يحدث أي فوران مع بيكربونات الصوديوم (مركب متعادل، سكر، أو فينول ذائب)", "org_sol_neutral_soluble_q_molisch", arabic_label="لا يحدث فوران (متعادل أو سكر أو ريسورسينول)")
        ],
        hint="الأحماض الكربوكسيلية الأليفاتية الصلبة (أكساليك، طرطريك، ستريك) تفور بقوة مع البيكربونات، بينما الكربوهيدرات واليوريا والريسورسينول لا تفور.",
        arabic_text="المواد الصلبة الذائبة بالماء — الخطوة 3: أضف محلول بيكربونات الصوديوم (NaHCO₃):"
    ),

    # Soluble Acids: Oxalic, Tartaric, Citric (CaCl2 Test)
    "org_sol_acid_soluble_q_cacl2": question(
        "org_sol_acid_soluble_q_cacl2",
        "Neutralize the acid solution with dilute ammonia and add Calcium Chloride (CaCl2) solution. Observe cold and boil:",
        [
            option("راسب أبيض فوري على البارد لا يذوب في حمض الخليك، ويزيل لون KMnO4 الساخن (حمض الأكساليك)", "ORG_OXALIC", arabic_label="راسب أبيض على البارد لا يذوب بالأسيتيك (أكساليك)"),
            option("راسب أبيض على البارد يذوب في هيدروكسيد الصوديوم، وتفاعل فنتون يعطي لوناً بنفسجياً ويتفحم برائحة سكر محروق (حمض الطرطريك)", "ORG_TARTARIC", arabic_label="راسب أبيض يذوب في NaOH وتفاعل فنتون بنفسجي (طرطريك)"),
            option("لا يتكون أي راسب على البارد، ولكن يتكون راسب أبيض فقط بعد الغليان الشديد لعدة دقائق (حمض الستريك)", "ORG_CITRIC", arabic_label="راسب أبيض يتكون بالغليان فقط (ستريك)")
        ],
        hint="أكسالات الكالسيوم تترسب فورياً على البارد ولا تذوب بالأسيتيك؛ طرطرات الكالسيوم تذوب في القلوي وتتفحم بالسكر المحروق؛ بينما سترات الكالسيوم تتطلب الغليان للترسيب.",
        arabic_text="الأحماض الأليفاتية الذائبة — التجربة الفاصلة بكلوريد الكالسيوم (CaCl₂):"
    ),

    # Neutral / Soluble Non-Acids -> Molisch Test (Sugars vs Resorcinol, Urea)
    "org_sol_neutral_soluble_q_molisch": question(
        "org_sol_neutral_soluble_q_molisch",
        "Perform Molisch's test (add alpha-naphthol solution, then pour concentrated H2SO4 down the inner tube wall):",
        [
            option("تكوّن حلقة بنفسجية مميزة عند السطح الفاصل تتفحم بالحرارة برائحة السكر المحروق (كربوهيدرات / سكر ذائب)", "org_sol_sugar_q_fehling", arabic_label="حلقة بنفسجية مميزة وتفحم بالسكر المحروق (كربوهيدرات)"),
            option("لا تتكون حلقة بنفسجية (سلبي مع موليش — ليس كربوهيدرات: ريسورسينول أو يوريا)", "org_sol_nonsugar_q_fecl3", arabic_label="سلبي مع موليش (ريسورسينول أو يوريا)")
        ],
        hint="كاشف موليش يعطي حلقة بنفسجية حصرية مع جميع الكربوهيدرات نتيجة تكون الفسفورال ومشتقاته مع ألفا-نافثول.",
        arabic_text="المواد الذائبة المتعادلة — الخطوة 4: اختبار موليش (Molisch Test) العام للكشف عن السكريات:"
    ),

    # Soluble Sugars: Glucose, Fructose vs Sucrose (Fehling's Test)
    "org_sol_sugar_q_fehling": question(
        "org_sol_sugar_q_fehling",
        "Add Fehling's reagent (A+B) and heat in a boiling water bath for 3-5 minutes. What do you observe?",
        [
            option("تكوّن راسب أحمر طوبي كثيف ومباشر من Cu2O (سكر أحادي مختزل)", "org_sol_reducingsugar_q_seliwanoff", arabic_label="راسب أحمر طوبي مباشر مع فهلنج (سكر مختزل)"),
            option("لا يتكون أي راسب أحمر ويظل المحلول أزرق صافياً (سكر غير مختزل مباشرة — سكروز)", "ORG_SUCROSE", arabic_label="سلبي مع فهلنج مباشرة (السكروز)")
        ],
        hint="الجلوكوز والفركتوز سكريات أحادية مختزلة ترسب Cu₂O الأحمر الطوبي مباشرة، بينما السكروز سكر ثنائي غير مختزل مباشرة.",
        arabic_text="السكريات الذائبة — الخطوة 5: اختبار فهلنج (Fehling's Test) للتمييز بين السكر المختزل وغير المختزل:"
    ),

    # Reducing Sugars: Glucose vs Fructose (Seliwanoff's Test)
    "org_sol_reducingsugar_q_seliwanoff": question(
        "org_sol_reducingsugar_q_seliwanoff",
        "Perform Seliwanoff's test (add Resorcinol in 6M HCl and boil in a water bath for 1-2 minutes):",
        [
            option("ظهور لون أحمر كرزي / قرمزي داكن فوري وسريع جداً خلال أقل من دقيقتين (سكر كيتوزي — فركتوز)", "ORG_FRUCTOSE", arabic_label="لون أحمر كرزي سريع خلال دقيقة أو دقيقتين (فركتوز)"),
            option("لا يظهر لون أحمر خلال أول دقيقتين (يظل المحلول عديم اللون أو وردياً باهتاً جداً بعد وقت طويل) (سكر ألدوزي — جلوكوز)", "ORG_GLUCOSE", arabic_label="سلبي خلال أول دقيقتين، وبلورات أوزازون إبرية (جلوكوز)")
        ],
        hint="الفركتوز كيتوهكسوز ينزع منه الماء بسرعة فائقة في الوسط الحمضي معطياً هيدروكسي ميثيل فيرفورال الذي يتكثف مع الريسورسينول بلون أحمر كرزي في دقيقة واحدة.",
        arabic_text="السكريات المختزلة — التجربة التأكيدية الفاصلة بين الجلوكوز والفركتوز (اختبار سيلوانوف):"
    ),

    # Soluble Non-Sugars: Resorcinol vs Urea (FeCl3 & Ignition/Biuret)
    "org_sol_nonsugar_q_fecl3": question(
        "org_sol_nonsugar_q_fecl3",
        "Add neutral Ferric Chloride (FeCl3) solution to the sample, and test behavior upon dry heating:",
        [
            option("تلوّن فوري بلون بنفسجي داكن مميز، وتفاعل الفثالين يعطي فلورسين أخضر فسفورياً مشعاً (ريسورسينول)", "ORG_RESORCINOL", arabic_label="لون بنفسجي داكن مع FeCl3 وفلورسين أخضر مشع (ريسورسينول)"),
            option("لا يعطي لوناً بنفسجياً مع FeCl3، وينصهر بالتسخين الجاف مع تصاعد النشادر وتفاعل البيوريت وردي بنفسجي (يوريا)", "ORG_UREA", arabic_label="تصاعد النشادر وتفاعل البيوريت وردي بنفسجي (يوريا)")
        ],
        hint="الريسورسينول فينول ثنائي الهيدروكسيل يعطي لوناً بنفسجياً داكناً مع الحديديك وفلورسين أخضر؛ واليوريا أميد صلب ينصهر مع تصاعد غاز النشادر ويعطي تفاعل البيوريت.",
        arabic_text="المواد الذائبة غير السكرية — التجربة الفاصلة بين الريسورسينول واليوريا:"
    ),

    # ------------------ Insoluble / Sparingly Soluble Solids (6 Compounds) ------------------
    # Benzoic, Salicylic, Phenol, alpha-Naphthol, beta-Naphthol, Starch
    "org_sol_insoluble_q_acidity": question(
        "org_sol_insoluble_q_acidity",
        "Test solubility of the solid in 5% NaHCO3 solution and in 10% NaOH solution:",
        [
            option("تفور وتذوب في بيكربونات الصوديوم NaHCO3 مع تصاعد فقاعات CO2 (حمض أروماتي صلب)", "org_sol_aromatic_acid_q_fecl3", arabic_label="فوران وذوبان في بيكربونات الصوديوم (حمض أروماتي)"),
            option("لا تفور مع بيكربونات الصوديوم ولكنها تذوب تماماً في هيدروكسيد الصوديوم NaOH (فينولات ونافثولات)", "org_sol_phenol_q_fecl3", arabic_label="لا تفور مع NaHCO3 ولكن تذوب في NaOH (فينولات ونافثولات)"),
            option("لا تفور مع البيكربونات ولا تذوب في NaOH على البارد، وتكوّن معلقاً غروياً عند الغليان بالماء (نشا)", "ORG_STARCH", arabic_label="معلق غروي بالماء الساخن وأزرق مع اليود (نشا)")
        ],
        hint="الأحماض الكربوكسيلية تفور وتذوب في NaHCO₃؛ الفينولات تذوب في القواعد القوية NaOH فقط ولا تفور مع NaHCO₃؛ النشا لا يذوب فيهما ويعطي معلقاً نشوياً بالحرارة.",
        arabic_text="المواد الصلبة غير الذائبة بالماء — الخطوة 3: اختبار الذوبان في NaHCO₃ وهيدروكسيد الصوديوم NaOH:"
    ),

    # Insoluble Aromatic Acids: Benzoic vs Salicylic (FeCl3 Test)
    "org_sol_aromatic_acid_q_fecl3": question(
        "org_sol_aromatic_acid_q_fecl3",
        "Neutralize the acid solution with dilute ammonia, boil off excess NH3, and add neutral FeCl3 solution:",
        [
            option("يتكون راسب بيج / بني مصفر لحمي مميز (Buff precipitate) من بنزوات الحديديك (حمض البنزويك)", "ORG_BENZOIC", arabic_label="راسب بيج / بني مصفر لحمي مع FeCl3 (بنزويك)"),
            option("يتكون لون بنفسجي داكن كثيف وثابت جداً لا يزول مع FeCl3 (حمض الساليسيليك)", "ORG_SALICYLIC", arabic_label="لون بنفسجي كثيف وثابت جداً مع FeCl3 (ساليسيليك)")
        ],
        hint="حمض الساليسيليك يحتوي على مجموعة هيدروكسيل فينولية تعطي معقداً بنفسجياً ثابتاً مع Fe³⁺، بينما حمض البنزويك يعطي راسب بنزوات الحديديك البيج.",
        arabic_text="الأحماض الأروماتية غير الذائبة بالماء البارد — التجربة التأكيدية الفاصلة بين البنزويك والساليسيليك:"
    ),

    # Phenols & Naphthols: Phenol vs Naphthols (Solubility, Carbolic Odor & Bromine Water)
    "org_sol_phenol_q_fecl3": question(
        "org_sol_phenol_q_fecl3",
        "Observe sample appearance, carbolic odor, and reaction with Bromine Water and neutral FeCl3:",
        [
            option("بلورات متميعة وردية برائحة كربولية معروفة، تذوب جزئياً بالماء البارد وتعطي راسباً أبيض مع ماء البروم ولوناً بنفسجياً مع FeCl3 (الفينول)", "ORG_PHENOL", arabic_label="رائحة كربولية وراسب أبيض مع ماء البروم ولون بنفسجي (الفينول)"),
            option("مسحوق صلب لا يذوب في الماء البارد إطلاقاً، ذو لهب مدخن شديد (نافثولات أروماتية)", "org_sol_naphthol_q_bleach", arabic_label="مسحوق عديم الذوبان في الماء ولهب مدخن شديد (نافثولات)")
        ],
        hint="الفينول يمتلك ذائبية جزئية واضحة في الماء البارد (~8 جم/100 مل) ورائحة كربولية مألوفة، بينما النافثولات (حلقتا بنزين مدمجتان) لا تذوب في الماء إطلاقاً.",
        arabic_text="الفينولات والنافثولات — الخطوة 4: التمييز بين الفينول أحادي الحلقة والنافثولات ثنائية الحلقات:"
    ),

    # Naphthols: alpha-Naphthol vs beta-Naphthol (Bleaching Powder Test)
    "org_sol_naphthol_q_bleach": question(
        "org_sol_naphthol_q_bleach",
        "Add filtered Bleaching Powder solution (or NaOCl) / FeCl3 to the naphthol sample in dilute alkali or alcohol:",
        [
            option("يعطي تلوناً بنفسجياً داكناً يتحول فورياً إلى راسب بني محمر كثيف مع مسحوق القصر (ألفا-نافثول)", "ORG_ALPHA_NAPHTHOL", arabic_label="تلون بنفسجي داكن مع مسحوق القصر / الهيبوكلوريت (ألفا-نافثول)"),
            option("لا يعطي أي لون بنفسجي مع مسحوق القصر، ويعطي تلوناً أخضر باهتاً مع FeCl3 وصبغة آزو حمراء ساطعة مع الأنيلين (بيتا-نافثول)", "ORG_BETA_NAPHTHOL", arabic_label="سلبي مع مسحوق القصر وصبغة آزو حمراء قرمزية ساطعة (بيتا-نافثول)")
        ],
        hint="ألفا-نافثول يتأكسد بمسحوق القصر (Bleaching Powder / NaOCl) معطياً نواتج تكثيف بنفسجية بنية مميزة، بينما بيتا-نافثول خامل تجاه هذا الكاشف ولا يعطي لوناً بنفسجياً.",
        arabic_text="النافثولات — التجربة التأكيدية الفاصلة بين ألفا-نافثول وبيتا-نافثول:"
    )
}

