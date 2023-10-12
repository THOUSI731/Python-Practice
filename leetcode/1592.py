class Solution:
    def reorderSpaces(self, text: str) -> str:
          list_=list(text.split(' '))
          text_count=len([i for i in list_ if not i == ''])
          space_count=len([i for i in text if  i == ' '])
          
          spaces=int(space_count/(text_count-1))
          list_2=list(text.split())
          result=str()
          for i in range(spaces+1):
               if i == spaces+1:
                    result += list_2[i]
                    break
               result += list_2[i]
               for j in range(spaces):
                    result += ' '
               
               
          return result
    
a=Solution()
print(a.reorderSpaces("  this   is  a sentence "))


# Give Up Answered By Chatgpt

class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        text_count = len(words)
        space_count = text.count(' ')
        
        spaces = ' ' * (space_count // (text_count - 1)) if text_count > 1 else ''
        
        # If there's only one word, all spaces go after that word
        result = spaces.join(words)

        # Add remaining spaces at the end (for cases with only one word)
        result += ' ' * (space_count % (text_count - 1)) if text_count > 1 else ' ' * space_count

        return result

# Example usage
solution = Solution()
print(solution.reorderSpaces("hello world"))  # Output: "hello  world"
