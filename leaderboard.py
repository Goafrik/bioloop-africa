# ============================================
# BIOLOOP AFRICA - LEADERBOARD SYSTEM
# Ranks users by eco points & waste impact
# ============================================

from rewards import RewardsSystem

class Leaderboard:
    """Manages user rankings and eco-warrior status"""
    
    def __init__(self, database):
        self.db = database
        self.rewards = RewardsSystem(database)
    
    def get_rankings(self, limit=10):
        """Get top users sorted by eco points"""
        users = self.db.data.get("users", {})
        user_list = list(users.values())
        
        # Sort by eco_points (highest first)
        sorted_users = sorted(user_list, key=lambda x: x.get("eco_points", 0), reverse=True)
        return sorted_users[:limit]
    
    def display_leaderboard(self):
        """Print formatted leaderboard"""
        rankings = self.get_rankings()
        
        if not rankings:
            print("\n No users to display on the leaderboard.")
            return
        
        print("\n" + "="*65)
        print("🏆 BIOLOOP AFRICA LEADERBOARD")
        print("="*65)
        print(f"{'Rank':<5} {'Name':<22} {'Points':<10} {'Tier'}")
        print("-"*65)
        
        for i, user in enumerate(rankings, 1):
            tier_name, _ = self.rewards.get_tier(user["eco_points"])
            print(f"{i:<5} {user['name']:<22} {user['eco_points']:<10} {tier_name}")
        
        print("="*65)
        print("💡 Tip: Keep logging waste to climb the ranks!")