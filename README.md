# Chemistry Diagnosis Lab ⚗️🧪
### Expert System for Organic & Inorganic Qualitative Analysis
نظام خبير متكامل لتشخيص وتحديد العينات الكيميائية المجهولة (العضوية وغير العضوية)

---

## 🔬 Features | المميزات الرئيسية
- **Dual Analytical Inference Engine:**
  - **Organic Qualitative Analysis (الكشف العضوي):** Covers 25 laboratory organic compounds (11 Liquids + 14 Solids) with functional group identification, confirmatory tests, and chemical structures.
  - **Inorganic Qualitative Analysis (الكشف غير العضوي):** Identifies 28 principal cations and anions (Acidic & Basic Radicals).
  - **Flame Charring Pre-check (فحص اللهب والتفحم):** Automatic routing between organic and inorganic classes.
- **Interactive 5-Stage Diagnostic Workflow:**
  1. Analytical Path Selection
  2. Physical Observations & Sequential Reagents
  3. Family & Group Reagent Filtering
  4. Confirmatory Protocol Testing (with structural formula preview)
  5. Comprehensive Laboratory Report Generation (with printable output, chemical structures, and balanced equations).
- **Interactive Reaction Simulator (محاكي التفاعلات):** Real-time prediction of ion-reagent reactions and precipitate colors.
- **Flame Test Guide (دليل كشف اللهب):** Visual spectroscopic reference for characteristic metallic flames.

---

## 📁 Chemical Library | مكتبة المركبات
### 1. Organic Compounds (25 المركبات العضوية)
- **Liquids (11):** Formic acid, Acetic acid, Formaldehyde, Acetaldehyde, Benzaldehyde, Acetone, Acetophenone, Methanol, Ethanol, Glycerol, Aniline.
- **Solids (14):** Oxalic acid, Tartaric acid, Citric acid, Benzoic acid, Salicylic acid, Phenol, Resorcinol, $\alpha$-Naphthol, $\beta$-Naphthol, Glucose, Fructose, Sucrose, Starch, Urea.

### 2. Inorganic Species (28 الأيونات غير العضوية)
- **Cations:** $\text{Cu}^{2+}, \text{Fe}^{2+}, \text{Fe}^{3+}, \text{Zn}^{2+}, \text{Al}^{3+}, \text{Ca}^{2+}, \text{Mg}^{2+}, \text{Pb}^{2+}, \text{Ag}^+, \text{NH}_4^+, \text{Ba}^{2+}, \text{Ni}^{2+}, \text{Co}^{2+}, \text{Mn}^{2+}$
- **Anions:** $\text{CO}_3^{2-}, \text{HCO}_3^-, \text{S}^{2-}, \text{S}_2\text{O}_3^{2-}, \text{NO}_2^-, \text{Cl}^-, \text{Br}^-, \text{I}^-, \text{NO}_3^-, \text{SO}_4^{2-}, \text{PO}_4^{3-}, \text{CrO}_4^{2-}, \text{CH}_3\text{COO}^-$

---

## 🚀 How to Run | طريقة التشغيل

### 1. Install Dependencies | تثبيت المتطلبات
```bash
pip install -r requirements.txt
```
# python run_global.py

### 2. Run Options | خيارات التشغيل

#### Option A: تشغيل محلي (Local Development)
لتشغيل النظام على جهازك المحلي فقط:
```bash
python app.py
```
ثم افتح المتصفح على:
`http://localhost:5000`

---

#### Option B: تشغيل برابط عالمي عام (Global Public Link)
لتشغيل الخادم وتوليد رابط فوري سريع لمشاركته مع أي شخص أو فتحه من الهاتف عبر الإنترنت (Cloudflare Tunnel):
```bash
python run_global.py
```
يقوم السكريبت بتشغيل سيرفر Waitress وإنشاء رابط إنترنت عام ونسخه إلى الحافظة تلقائياً! 🌐

---

## 🛠️ Tech Stack | التقنيات المستخدمة
- **Backend:** Python / Flask
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla ES6+), Responsive Grid
- **Knowledge Engine:** Rule-based expert decision tree & pattern matching

