# ============================================
# BIOLOOP AFRICA - MAIN APPLICATION (PHASE 2)
# Founder: Christopher Afwande
# ============================================

from config import APP_NAME, VERSION, FOUNDER
from database import BioLoopDatabase
from users import UserManager
from waste import WasteTracker
from rewards import RewardsSystem
from leaderboard import Leaderboard
from analytics import Analytics

class BioLoopAfrica:
    def __init__(self):
        self.db = BioLoopDatabase()
        self.user_manager = UserManager(self.db)
        self.waste_tracker = WasteTracker(self.db, self.user_manager)
        self.rewards_system = RewardsSystem(self.db)
        self.leaderboard = Leaderboard(self.db)
        self.analytics = Analytics(self.db)
        self.current_user = None
    
    def display_banner(self):
        print("\n" + "="*65)
        print(f"🌍 {APP_NAME.upper()}")
        print(f"   Turning Waste into Digital Value")
        print(f"   Version: {VERSION} | Founder: {FOUNDER}")
        print("="*65)
    
    def display_menu(self):
        print("\n📋 MAIN MENU")
        print("-" * 65)
        print("1. 👤 Register New User")
        print("2. 🔑 Login / Select User")
        print("3.  View Profile")
        print("4. ️ Log Waste")
        print("5. 📜 View Waste History")
        print("6. 🏆 Check Rewards Tier")
        print("7. 🌍 System Statistics")
        print("8. 🥇 Leaderboard")
        print("9. 📈 Impact Analytics")
        print("10. 📤 Export Report (CSV)")
        print("11. 💚 Exit")
        print("-" * 65)
    
    def register_user(self):
        print("\n" + "="*65)
        print("👤 NEW USER REGISTRATION")
        print("="*65)
        name = input("Enter your full name: ").strip()
        email = input("Enter your email: ").strip()
        location = input("Enter your location (city, country): ").strip()
        if name and email and location:
            self.current_user = self.user_manager.register_user(name, email, location)
        else:
            print("❌ All fields are required!")
    
    def login_user(self):
        print("\n" + "="*65)
        print("🔑 USER LOGIN")
        print("="*65)
        user_id = input("Enter your User ID: ").strip()
        user = self.db.get_user(user_id)
        if user:
            self.current_user = user
            print(f"\n✅ Welcome back, {user['name']}!")
        else:
            print("❌ User not found!")
    
    def view_profile(self):
        if self.current_user:
            self.user_manager.get_user_profile(self.current_user["user_id"])
        else: print("❌ Please login first!")
    
    def log_waste(self):
        if not self.current_user: print("❌ Please login first!"); return
        print("\n🗑️ LOG WASTE")
        print("Types: organic, plastic, metal, paper, electronic")
        w_type = input("Type: ").strip().lower()
        try:
            weight = float(input("Weight (kg): ").strip())
            desc = input("Description (optional): ").strip()
            if weight > 0:
                self.waste_tracker.log_waste(self.current_user["user_id"], w_type, weight, desc)
                self.current_user = self.db.get_user(self.current_user["user_id"])
        except ValueError: print("❌ Invalid number!")
    
    def view_waste_history(self):
        if self.current_user: self.waste_tracker.get_user_waste_history(self.current_user["user_id"])
        else: print("❌ Please login first!")
    
    def check_rewards(self):
        if self.current_user: self.rewards_system.display_tier_info(self.current_user["user_id"])
        else: print("❌ Please login first!")
    
    def view_system_stats(self):
        stats = self.db.get_total_stats()
        print("\n🌍 SYSTEM STATS")
        print(f"Users: {stats['total_users']} | Waste: {stats['total_waste_kg']:.1f}kg")
        print(f"CO₂ Saved: {stats['total_co2_saved']:.1f}kg | Energy: {stats['total_energy_generated']:.1f}kWh")
    
    def show_leaderboard(self): self.leaderboard.display_leaderboard()
    def show_analytics(self): self.analytics.display_impact_summary()
    def export_data(self): self.analytics.export_to_csv()
    
    def run(self):
        while True:
            self.display_banner()
            if self.current_user:
                print(f" Logged in: {self.current_user['name']} ({self.current_user['eco_points']} pts)")
            self.display_menu()
            choice = input("\nChoice (1-11): ").strip()
            if choice == "1": self.register_user()
            elif choice == "2": self.login_user()
            elif choice == "3": self.view_profile()
            elif choice == "4": self.log_waste()
            elif choice == "5": self.view_waste_history()
            elif choice == "6": self.check_rewards()
            elif choice == "7": self.view_system_stats()
            elif choice == "8": self.show_leaderboard()
            elif choice == "9": self.show_analytics()
            elif choice == "10": self.export_data()
            elif choice == "11":
                print("\n🌱 BioLoop Africa shutting down. - Christopher Afwande\n"); break
            else: print("❌ Invalid choice!")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    BioLoopAfrica().run()