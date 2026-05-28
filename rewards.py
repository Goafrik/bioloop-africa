# ============================================
# BIOLOOP AFRICA - REWARDS SYSTEM
# ============================================

class RewardsSystem:
    """Manages eco points and reward tiers"""
    
    REWARD_TIERS = {
        "Bronze": {"min_points": 0, "max_points": 99, "benefit": "Basic Member"},
        "Silver": {"min_points": 100, "max_points": 499, "benefit": "5% Bonus Points"},
        "Gold": {"min_points": 500, "max_points": 1499, "benefit": "10% Bonus Points"},
        "Platinum": {"min_points": 1500, "max_points": 4999, "benefit": "15% Bonus Points"},
        "Diamond": {"min_points": 5000, "max_points": 999999, "benefit": "20% Bonus Points"}
    }
    
    def __init__(self, database):
        self.db = database
    
    def get_tier(self, points):
        """Determine user tier based on points"""
        for tier_name, tier_info in self.REWARD_TIERS.items():
            if tier_info["min_points"] <= points <= tier_info["max_points"]:
                return tier_name, tier_info["benefit"]
        return "Diamond", self.REWARD_TIERS["Diamond"]["benefit"]
    
    def display_tier_info(self, user_id):
        """Display user's tier and benefits"""
        user = self.db.get_user(user_id)
        
        if not user:
            print("❌ User not found!")
            return
        
        points = user["eco_points"]
        tier_name, benefit = self.get_tier(points)
        
        print("\n" + "="*50)
        print("🏆 REWARDS TIER STATUS")
        print("="*50)
        print(f"Current Tier: {tier_name}")
        print(f"Current Points: {points}")
        print(f"Benefit: {benefit}")
        
        tier_list = list(self.REWARD_TIERS.keys())
        current_index = tier_list.index(tier_name)
        
        if current_index < len(tier_list) - 1:
            next_tier = tier_list[current_index + 1]
            points_needed = self.REWARD_TIERS[next_tier]["min_points"] - points
            print(f"\n Next Tier: {next_tier}")
            print(f"   Points Needed: {points_needed}")
        
        print("="*50)