class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = { "}" : "{", ")": "(", "]" : "["}
        stack = []


        for c in s: 

            # If character is closing 
            if c in brackets and stack: 
                # Get last item in stack
                last = stack[-1] 
                required_opening = brackets[c]

                # If last is opening of curr, pop 
                if last == required_opening:
                    stack.pop()
                else:
                    return False
            else: 
                # Append character to our stack, since it will be an opening
                stack.append(c)

        if stack:
            return False

        return True # If loop passes, we win those