# ============================================
# BIOLOOP AFRICA - WASTE TRACKING SYSTEM
# ============================================

from datetime import datetime
from config import POINTS_PER_KG_WASTE, WASTE_CATEGORIES, CO2_SAVED_PER_KG, ENERGY_GENERATED_PER_KG

class WasteTracker:
    """Manages waste tracking and environmental impact"""
    
    def __init__(self, database, user_manager):
        self.db = database
        self.user_manager = user_manager
    
    def log_waste(self, user_id, waste_type, weight_kg, description=""):
        """Log waste contribution"""
        
        if waste_type not in WASTE_CATEGORIES:
            print(f"❌ Invalid waste type. Choose from: {list(WASTE_CATEGORIES.keys())}")
            return None
        
        user = self.db.get_user(user_id)
        if not user:
            print(" User not found!")
            return None
        
        multiplier = WASTE_CATEGORIES[waste_type]["points_multiplier"]
        points_earned = int(weight_kg * POINTS_PER_KG_WASTE * multiplier)
        
        co2_saved = weight_kg * CO2_SAVED_PER_KG
        energy_generated = weight_kg * ENERGY_GENERATED_PER_KG if waste_type == "organic" else 0
        
        waste_record = {
            "record_id": f"WR_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "user_id": user_id,
            "waste_type": waste_type,
            "waste_type_name": WASTE_CATEGORIES[waste_type]["name"],
            "weight_kg": weight_kg,
            "points_earned": points_earned,
            "co2_saved": co2_saved,
            "energy_generated": energy_generated,
            "description": description,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.db.add_waste_record(waste_record)
        
        user = self.user_manager.update_user_points(user_id, points_earned)
        user["total_waste_kg"] += weight_kg
        self.db.save_data()
        
        print("\n" + "="*50)
        print("✅ WASTE LOGGED SUCCESSFULLY!")
        print("="*50)
        print(f"️ Type: {WASTE_CATEGORIES[waste_type]['name']}")
        print(f"⚖️ Weight: {weight_kg} kg")
        print(f"🌱 Eco Points Earned: {points_earned}")
        print(f"🌍 CO₂ Saved: {co2_saved:.2f} kg")
        if energy_generated > 0:
            print(f"⚡ Energy Generated: {energy_generated:.2f} kWh")
        print(f"🕐 Time: {waste_record['timestamp']}")
        print("="*50)
        print(f"🎉 Total Eco Points: {user['eco_points']}")
        print("="*50)
        
        return waste_record
    
    def get_user_waste_history(self, user_id):
        """Get all waste records for a user"""
        records = self.db.get_user_records(user_id)
        
        if not records:
            print("\n📭 No waste records found.")
            return []
        
        print("\n" + "="*60)
        print(f"📊 WASTE HISTORY (Total: {len(records)} records)")
        print("="*60)
        
        total_points = 0
        total_weight = 0
        
        for record in records:
            print(f"\n🗑️ {record['waste_type_name']}")
            print(f"   Weight: {record['weight_kg']} kg")
            print(f"   Points: {record['points_earned']}")
            print(f"   Date: {record['timestamp']}")
            total_points += record['points_earned']
            total_weight += record['weight_kg']
        
        print("\n" + "="*60)
        print(f" TOTALS:")
        print(f"   Total Waste: {total_weight} kg")
        print(f"   Total Points: {total_points}")
        print("="*60)
        
        return records