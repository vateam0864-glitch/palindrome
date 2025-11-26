def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")
    return s == s[::-1]

if __name__ == "__main__":
    text = "madam"
    if is_palindrome(text):
        print(f"{text} is a palindrome")
    else:
        print(f"{text} is NOT a palindrome")

print("🔄 Deploy triggered automatically!")
