# ============================================
# BIOLOOP AFRICA - AI PREDICTION ENGINE
# ============================================

class BioLoopAI:
    def predict_next_month(self, current_waste_kg, growth_rate=0.10):
        prediction = current_waste_kg * (1 + growth_rate)
        return round(prediction, 2)

    def estimate_revenue(self, waste_kg, rate_per_kg=0.05):
        return round(waste_kg * rate_per_kg, 2)

    def get_community_health_score(self, total_users, total_waste):
        if total_users == 0: return 0
        score = (total_users * 5) + (total_waste * 2)
        return min(score, 100)