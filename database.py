# ============================================
# BIOLOOP AFRICA - DATABASE SYSTEM
# Handles all data storage
# ============================================

import json
import os
from datetime import datetime

class BioLoopDatabase:
    """Manages all data storage for BioLoop Africa"""
    
    def __init__(self):
        self.data_file = "bioloop_data.json"
        self.data = self.load_data()
    
    def load_data(self):
        """Load existing data or create new database"""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
        else:
            return {
                "users": {},
                "waste_records": [],
                "total_stats": {
                    "total_waste_kg": 0,
                    "total_co2_saved": 0,
                    "total_energy_generated": 0,
                    "total_users": 0
                }
            }
    
    def save_data(self):
        """Save all data to file"""
        with open(self.data_file, 'w') as file:
            json.dump(self.data, file, indent=4)
    
    def add_user(self, user_id, user_data):
        """Add a new user to database"""
        self.data["users"][user_id] = user_data
        self.data["total_stats"]["total_users"] = len(self.data["users"])
        self.save_data()
    
    def get_user(self, user_id):
        """Get user data by ID"""
        return self.data["users"].get(user_id)
    
    def add_waste_record(self, record):
        """Add waste tracking record"""
        self.data["waste_records"].append(record)
        self.data["total_stats"]["total_waste_kg"] += record["weight_kg"]
        self.data["total_stats"]["total_co2_saved"] += record["co2_saved"]
        self.data["total_stats"]["total_energy_generated"] += record["energy_generated"]
        self.save_data()
    
    def get_user_records(self, user_id):
        """Get all waste records for a user"""
        return [r for r in self.data["waste_records"] if r["user_id"] == user_id]
    
    def get_total_stats(self):
        """Get system-wide statistics"""
        return self.data["total_stats"]