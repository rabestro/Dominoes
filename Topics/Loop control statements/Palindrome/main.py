word = input()
is_palindrome = word[::-1] == word
print("Palindrome" if is_palindrome else "Not palindrome")
