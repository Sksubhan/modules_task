def reverse_string(s):
    rs=''
    for i in s:
        rs=i+rs
    return rs

def is_palindrome(s):
    return 'Is a palindrome' if s==reverse_string(s) else 'Not a palindrome'

def captialize(s):
    return s.capitalize()

