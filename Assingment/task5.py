

#Question2.. 4. Define a function is_palindrome() that recognizes palindromes (i.e. words that
# look the same written backwards). For example, is_palindrome("radar") should
# return True(Try to implement it with custom code and logic instead of Python
# provided​ ​ libraries).

def is_palindrome():
    check = input("enter word")
    if check[0::] == check[::-1]:
        print("plaindrome")
    else:
        print("not palindrome")

is_palindrome()

