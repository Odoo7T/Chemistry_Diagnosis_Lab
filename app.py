from flask import Flask, render_template, jsonify, request
import knowledge_base as kb

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/data", methods=["GET"])
def get_all_data():
    """Returns the full knowledge base dataset for client-side fluid navigation."""
    # Build a serialized version of reactions database for quick lookups
    reactions_serialized = {
        f"{ion}_{reagent}": data
        for (ion, reagent), data in kb.REACTIONS.items()
    }
    
    return jsonify({
        "unified": {
            "tree": kb.UNIFIED_DECISION_TREE,
            "outcomes": kb.ALL_OUTCOMES
        },
        "cations": {
            "tree": kb.CATION_DECISION_TREE,
            "outcomes": kb.CATION_OUTCOMES
        },
        "anions": {
            "tree": kb.ANION_DECISION_TREE,
            "outcomes": kb.ANION_OUTCOMES
        },
        "prediction": {
            "ions": kb.IONS,
            "cations": kb.CATIONS_LIST,
            "anions": kb.ANIONS_LIST,
            "reagents": kb.REAGENTS,
            "reactions": reactions_serialized
        },
        "reference_notes": {
            "Na": {
                "ion": "Na⁺",
                "name": "Sodium — أيون الصوديوم",
                "flame": "Characteristic persistent yellow-gold flame.",
                "arabic_flame": "لهب أصفر ذهبي ساطع ومستمر.",
                "swatch": kb.YELLOW
            },
            "K": {
                "ion": "K⁺",
                "name": "Potassium — أيون البوتاسيوم",
                "flame": "Characteristic pale violet / lilac flame (visible through cobalt glass).",
                "arabic_flame": "لهب بنفسجي باهت / ليلكي (يُرى بوضوح عبر زجاج الكوبالت الأزرق).",
                "swatch": kb.VIOLET
            }
        },
        "confirmatory_tests": kb.CONFIRMATORY_TESTS,
        "initial_color_hints": kb.INITIAL_COLOR_HINTS,
        "anions_data": kb.ANIONS_DATA,
        "cations_data": kb.CATIONS_DATA,
        "salts_database": {
            f"{c}_{a}": s for (c, a), s in kb.SALTS_DATABASE.items()
        },
        "incompatible_salts": {
            f"{c}_{a}": s for (c, a), s in kb.INCOMPATIBLE_SALTS.items()
        }
    })

@app.route("/api/salt_outcome", methods=["POST"])
def salt_outcome():
    """Endpoint for inorganic salt diagnosis final outcome generation."""
    payload = request.get_json(silent=True) or {}
    cation = payload.get("cation", "")
    anion = payload.get("anion", "")
    
    if not cation or not anion:
        return jsonify({
            "error": "Both 'cation' and 'anion' fields are required."
        }), 400
        
    result = kb.build_final_salt_outcome(cation, anion)
    return jsonify(result)

@app.route("/api/predict", methods=["POST"])
def predict():
    """Endpoint for reaction prediction."""
    payload = request.get_json(silent=True) or {}
    ion_str = payload.get("ion", "")
    reagent_str = payload.get("reagent", "")
    
    if not ion_str or not reagent_str:
        return jsonify({
            "error": "Both 'ion' and 'reagent' fields are required."
        }), 400
        
    result = kb.predict_reaction(ion_str, reagent_str)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
