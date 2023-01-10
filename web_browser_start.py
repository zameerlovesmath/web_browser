import os
print("What would you like your startup page to be?")
print("1. Google")
print("2. Bing")
print("3. DuckDuckGo")
print("4. Custom")
choice = input()
if choice == "1":
    os.system("python ./web_browser_google_version.py")
if choice == "2":
    os.system("python ./web_browser_bing_version.py")
if choice == "3":
    os.system("python ./web_browser_duckduckgo_version.py")
if choice == "4":
    os.system("python ./web_browser_custom_version.py")