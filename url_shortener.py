# url_shortener.py
"""
URL Shortener
Author: Vishwarajan
Description:
This script converts long URLs into short links using the TinyURL service via PyShorteners library.
"""

import pyshorteners

def shorten_url(long_url):
    """Converts a long URL into a shortened URL."""
    try:
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(long_url)
        return short_url
    except Exception as e:
        return f"Error: {e}"

def main():
    print("=== URL Shortener ===")
    long_url = input("Enter the long URL: ")
    short_url = shorten_url(long_url)
    print(f"Short URL: {short_url}")

if __name__ == "__main__":
    main()
