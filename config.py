# ============================================
# BIOLOOP AFRICA - SYSTEM CONFIGURATION
# Founder: Christopher Afwande
# ============================================

# Points System Rules
POINTS_PER_KG_WASTE = 5  # 1kg waste = 5 eco points

# Waste Categories
WASTE_CATEGORIES = {
    "organic": {"name": "Organic Waste", "points_multiplier": 1.0},
    "plastic": {"name": "Plastic Waste", "points_multiplier": 1.5},
    "metal": {"name": "Metal Waste", "points_multiplier": 2.0},
    "paper": {"name": "Paper Waste", "points_multiplier": 1.2},
    "electronic": {"name": "E-Waste", "points_multiplier": 3.0}
}

# System Info
APP_NAME = "BioLoop Africa"
VERSION = "1.0.0"
FOUNDER = "Christopher Afwande"

# Environmental Impact Factors
CO2_SAVED_PER_KG = 0.5  # kg of CO2 saved per kg of waste
ENERGY_GENERATED_PER_KG = 0.3  # kWh generated per kg organic waste