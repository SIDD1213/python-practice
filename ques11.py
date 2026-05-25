#PALINDROME
def is_palindrome(lst):
    n=input():
    rev=' '
    for char in n:
        if n==rev:
            print("Yes,it is Palindrome")
        else:
            print("No,its not Palindrome")