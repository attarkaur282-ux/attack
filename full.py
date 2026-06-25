#!/usr/bin/env python3
# full.py - Forces fullscreen mode

import os
import time
import subprocess

def fullscreen_mode():
    print("🖥️ SATVIR RANSOME - Fullscreen Mode")
    print("="*35)
    print("✅ Website will open in fullscreen")
    time.sleep(2)
    
    # Open in fullscreen
    try:
        if os.name == 'nt':
            # Windows
            subprocess.run(['start', 'chrome', '--kiosk', 'index.html'], shell=True)
        else:
            # Linux/Android
            subprocess.run(['google-chrome', '--kiosk', 'index.html'], shell=True)
    except:
        # Fallback
        import webbrowser
        webbrowser.open('index.html')
        print("⚠️ Press F11 manually for fullscreen")

if __name__ == "__main__":
    fullscreen_mode()