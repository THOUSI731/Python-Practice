class Solution:
    def romanToInt(self,s):
          roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
          total = 0
          i = 0
          
          while i < len(s):
               if i < len(s) - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                    total += roman_to_int[s[i + 1]] - roman_to_int[s[i]]
                    i += 2 
               else:
                    total += roman_to_int[s[i]]
                    i += 1
          
          return total

a=Solution()
print(a.romanToInt("MCMXCIV"))