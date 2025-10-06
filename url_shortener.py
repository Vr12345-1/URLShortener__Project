import json
import string
import random
import os
import webbrowser

DATA_FILE = "urls.json"

# Load existing data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        urls = json.load(f)
else:
    urls = {}

def generate_short_id(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def shorten_url():
    long_url = input("Enter the long URL: ")
    short_id = generate_short_id()
    urls[short_id] = long_url
    with open(DATA_FILE, "w") as f:
        json.dump(urls, f)
    print(f"\n✅ Short URL created: {short_id}")
    print("Use this code to open your link later.\n")

def open_url():
    code = input("Enter your short code: ")
    if code in urls:
        print(f"🌐 Opening: {urls[code]}")
        webbrowser.open(urls[code])
    else:
        print("❌ Code not found!")

def view_all():
    if not urls:
        print("No URLs found!")
    else:
        print("\n--- All Shortened URLs ---")
        for short, long in urls.items():
            print(f"{short} → {long}")
        print("--------------------------\n")

def main():
    while True:
        print("=== URL Shortener ===")
        print("1. Shorten a new URL")
        print("2. Open a shortened URL")
        print("3. View all URLs")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            shorten_url()
        elif choice == '2':
            open_url()
        elif choice == '3':
            view_all()
        elif choice == '4':
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
