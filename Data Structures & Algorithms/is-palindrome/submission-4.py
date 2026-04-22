class Solution:
    def isPalindrome(self, s: str) -> bool:

        text = ''.join(char.lower() for char in s if char.isalnum())
        print(text)

        r = len(text) - 1

        for l, c in enumerate(text):
            if text[l] != text[r]:
                return False
            r -= 1

        return True
    

        