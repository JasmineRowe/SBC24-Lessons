

import unittest

# **Palindrome Check** - Write a test and function to check if a string is a palindrome.

   # Code for checking palindrome:

def isPalindrome(string):
            if(string == string[::-1]):
                   return True
               

class TestPalindrome(unittest.TestCase):
    def test_isPalindrome(self):
        self.assertFalse(isPalindrome("kaylak"), False)
        self.assertTrue(isPalindrome("kayak"), True)


# 2. **Alphabet Check** - Write a test and function to verify if a string contains only alphabetic characters.

def isAlpha(string):
            if(string.isalpha):
                   return True
               

class TestisAlpha(unittest.TestCase):
    def test_isAlpha(self):
        self.assertFalse(isAlpha("hello1"), False)
        self.assertTrue(isAlpha("hello"), True)


# 3. **Math Operations** - Write tests for basic math functions like multiplication and division.



# 4. **Fibonacci Sequence** - Write tests and implement a function to calculate the nth Fibonacci number.





# 5. **Anagram Check** - Write tests and implement a function to check if two strings are anagrams.//




if __name__ == '__main__':
    unittest.main()
