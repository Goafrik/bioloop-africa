# ============================================
# BIOLOOP AFRICA - WEB SERVER (PHASE 4 - AI ENABLED)
# ============================================

from flask import Flask, render_template
import json
import os
from ai_engine import BioLoopAI  # Import our AI module

app = Flask(__name__)
ai = BioLoopAI()

DATA_FILE = "bioloop_data.json"

def load_data():
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception as e:
        print(f"Error loading data: {e}")
    return {"users": {}, "waste_records": [], "total_stats": {}}

@app.route('/')
def dashboard():
    data = load_data()
    users = list(data.get("users", {}).values())
    records = data.get("waste_records", [])
    stats = data.get("total_stats", {})

    users_sorted = sorted(users, key=lambda u: u.get("eco_points", 0), reverse=True)
    
    # Waste Chart Data
    waste_types = {}
    for rec in records:
        w_type = rec.get("waste_type_name", "Unknown")
        waste_types[w_type] = waste_types.get(w_type, 0) + rec.get("weight_kg", 0)
        
    chart_labels = list(waste_types.keys())
    chart_values = list(waste_types.values())

    # --- AI PREDICTIONS ---
    current_waste = stats.get("total_waste_kg", 0)
    next_month_forecast = ai.predict_next_month(current_waste)
    potential_revenue = ai.estimate_revenue(current_waste)
    health_score = ai.get_community_health_score(stats.get("total_users", 0), current_waste)

    return render_template('index.html', 
                           users=users_sorted, 
                           stats=stats, 
                           recent_records=records[-5:],
                           labels=chart_labels, 
                           values=chart_values,
                           # AI Data
                           forecast=next_month_forecast,
                           revenue=potential_revenue,
                           score=health_score)

if __name__ == "__main__":
    print("\n🌍 BioLoop Africa Dashboard (AI-Enabled) starting...")
    print("🌐 Open in browser: http://127.0.0.1:5000")
    app.run(debug=True, port=5000)