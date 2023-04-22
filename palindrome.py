# Given an integer x, return true if x is a palindrome, and false otherwise.

# funtion takes in a number
def isPalindrome(x):
        # convert x to string
        x = str(x)
        # create and assign y to reversed x
        y = x[::-1]
        # compare x and y
        if x == y:
            return True
        else:
            return False


print(isPalindrome(121))
print(isPalindrome(10))