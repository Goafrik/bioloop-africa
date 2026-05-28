# ============================================
# BIOLOOP AFRICA - USER MANAGEMENT SYSTEM
# ============================================

from datetime import datetime
import uuid

class UserManager:
    """Manages user registration and profiles"""
    
    def __init__(self, database):
        self.db = database
    
    def register_user(self, name, email, location):
        """Register a new user"""
        user_id = str(uuid.uuid4())[:8]
        
        user_data = {
            "user_id": user_id,
            "name": name,
            "email": email,
            "location": location,
            "eco_points": 0,
            "total_waste_kg": 0,
            "joined_date": datetime.now().strftime("%Y-%m-%d"),
            "status": "active"
        }
        
        self.db.add_user(user_id, user_data)
        
        print(f"\n✅ Welcome to BioLoop Africa, {name}!")
        print(f"🆔 Your User ID: {user_id}")
        print(f"🌱 Starting Eco Points: 0")
        print(f"📍 Location: {location}")
        
        return user_data
    
    def get_user_profile(self, user_id):
        """Display user profile"""
        user = self.db.get_user(user_id)
        
        if user:
            print("\n" + "="*50)
            print("👤 USER PROFILE")
            print("="*50)
            print(f"Name: {user['name']}")
            print(f"User ID: {user['user_id']}")
            print(f"Email: {user['email']}")
            print(f"Location: {user['location']}")
            print(f"Eco Points: {user['eco_points']} 🌱")
            print(f"Total Waste Contributed: {user['total_waste_kg']} kg")
            print(f"Member Since: {user['joined_date']}")
            print("="*50)
            return user
        else:
            print("❌ User not found!")
            return None
    
    def update_user_points(self, user_id, points):
        """Update user's eco points"""
        user = self.db.get_user(user_id)
        if user:
            user["eco_points"] += points
            self.db.save_data()
            return user
        return None