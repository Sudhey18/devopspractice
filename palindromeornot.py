s = input("Enter string: ").replace(" ", "").lower() 
print("Palindrome" if s == s[::-1] else "Not a palindrome")