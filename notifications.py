# ============================================
# BIOLOOP AFRICA - NOTIFICATION ENGINE
# SMS/WhatsApp/Email architecture (API-ready)
# ============================================

import csv
from datetime import datetime

class NotificationSystem:
    """Handles user alerts, rewards notifications, and community broadcasts"""
    
    def __init__(self):
        self.log_file = "notifications.log"
    
    def send_sms_alert(self, phone, message):
        """Simulates SMS alert (Swap with Twilio/Africa's Talking API later)"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[SMS] {timestamp} | To: {phone} | Msg: {message}\n"
        self._write_log(log_entry)
        print(f"📱 SMS Sent to {phone}: {message}")
    
    def send_whatsapp_alert(self, phone, message):
        """Simulates WhatsApp Business alert (Swap with WhatsApp Cloud API later)"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[WHATSAPP] {timestamp} | To: {phone} | Msg: {message}\n"
        self._write_log(log_entry)
        print(f"💬 WhatsApp Sent to {phone}: {message}")
    
    def send_reward_notification(self, user_name, points, tier):
        """Auto-notifies users when they level up"""
        msg = f"🎉 {user_name}, you've earned {points} Eco Points! Current Tier: {tier}. Keep recycling!"
        # In production, replace with real SMS/WhatsApp API call
        print(f"🔔 Reward Alert: {msg}")
    
    def broadcast_community_update(self, message):
        """Sends system-wide updates (e.g., collection days, events)"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[BROADCAST] {timestamp} | {message}\n"
        self._write_log(log_entry)
        print(f"📢 Broadcast: {message}")
    
    def _write_log(self, entry):
        """Appends notification to log file for audit & debugging"""
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(entry)

# Quick test runner
if __name__ == "__main__":
    notify = NotificationSystem()
    notify.send_sms_alert("+254700000000", "Your 10kg waste log earned 50 Eco Points!")
    notify.send_reward_notification("Amina Juma", 60, "Silver")
    notify.broadcast_community_update("Community cleanup event this Saturday at 8AM.")