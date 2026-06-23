class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = ''.join(char for char in s if char.isalnum()).lower()
        length = len(cleaned_str) - 1
        for i in range(len(cleaned_str) // 2):
            if cleaned_str[i] != cleaned_str[length - i]: return False
        
        return True





    
        