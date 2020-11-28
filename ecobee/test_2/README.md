# Steps to get environment on MacOS Big Sur:
1. python3 -m venv .virtual_env_test2
2. source .virtual_env_test2/bin/activate
3. pip install selenium
4. pip install --upgrade pip
5. downloaded chromedriver
6. xattr -d com.apple.quarantine chromedriver
7. python program.py
