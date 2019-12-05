import os
import sys
sys.version_info
print("Check Python Environment")
if sys.version_info.major != 3:
    print("Python3 REQUIRED!!!!!")
    exit()
print("Finish")

print("-----------------------------------------")
print("install dependency")
os.system("python3 -m venv venv")
os.system("source venv/bin/activate")
os.system("venv/bin/pip3 install -r venv_requirements")
print("Finish")

print("-----------------------------------------")
print("start...")
os.system("python3 app.py")
