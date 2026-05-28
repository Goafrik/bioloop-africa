# ============================================
# BIOLOOP AFRICA - ANALYTICS & REPORTING
# Handles impact breakdowns & CSV export
# ============================================

import csv
from database import BioLoopDatabase

class Analytics:
    """Generates reports, breakdowns, and data exports"""
    
    def __init__(self, database):
        self.db = database
    
    def get_waste_type_breakdown(self):
        """Calculate waste distribution by type"""
        records = self.db.data.get("waste_records", [])
        breakdown = {}
        
        for rec in records:
            w_type = rec["waste_type_name"]
            breakdown[w_type] = breakdown.get(w_type, 0) + rec["weight_kg"]
            
        return breakdown
    
    def display_impact_summary(self):
        """Show detailed analytics dashboard"""
        print("\n" + "="*65)
        print("📊 BIOLOOP AFRICA IMPACT ANALYTICS")
        print("="*65)
        
        # 1. Waste breakdown
        breakdown = self.get_waste_type_breakdown()
        if breakdown:
            print("\n🗑️ Waste Distribution by Type:")
            total = sum(breakdown.values())
            for w_type, weight in sorted(breakdown.items(), key=lambda x: x[1], reverse=True):
                percent = (weight / total) * 100 if total > 0 else 0
                print(f"   {w_type:<15}: {weight:.1f} kg ({percent:.1f}%)")
        else:
            print("\n📭 No waste data for analytics yet.")
        
        # 2. Top Contributor
        users = self.db.data.get("users", {})
        if users:
            top_user = max(users.values(), key=lambda u: u["eco_points"])
            print(f"\n🥇 Top Contributor: {top_user['name']} ({top_user['eco_points']} pts)")
            print(f"📍 Location: {top_user['location']}")
            print(f"🗑️ Total Waste: {top_user['total_waste_kg']} kg")
        
        # 3. System Health
        stats = self.db.get_total_stats()
        print(f"\n🔋 System Health:")
        print(f"   Active Users: {stats['total_users']}")
        print(f"   Records Logged: {len(self.db.data.get('waste_records', []))}")
        
        print("="*65)
    
    def export_to_csv(self, filename="bioloop_impact_report.csv"):
        """Export all waste records to CSV for partners/investors"""
        records = self.db.data.get("waste_records", [])
        users = self.db.data.get("users", {})
        
        if not records:
            print("❌ No waste records to export.")
            return False
        
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                
                # Header
                writer.writerow([
                    "Record ID", "User Name", "User Location", "Waste Type", 
                    "Weight (kg)", "Points Earned", "CO2 Saved (kg)", 
                    "Energy Generated (kWh)", "Description", "Timestamp"
                ])
                
                # Data rows
                for rec in records:
                    user_info = users.get(rec["user_id"], {})
                    writer.writerow([
                        rec["record_id"],
                        user_info.get("name", "Unknown"),
                        user_info.get("location", "Unknown"),
                        rec["waste_type_name"],
                        rec["weight_kg"],
                        rec["points_earned"],
                        f"{rec['co2_saved']:.2f}",
                        f"{rec['energy_generated']:.2f}",
                        rec.get("description", ""),
                        rec["timestamp"]
                    ])
            
            print(f"\n✅ Report exported successfully!")
            print(f"📄 File: {filename}")
            print(f"📊 Total records: {len(records)}")
            return True
            
        except Exception as e:
            print(f"❌ Export failed: {e}")
            return False