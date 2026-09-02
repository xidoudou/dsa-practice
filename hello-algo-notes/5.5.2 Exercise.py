"""
1.building a mapping from each closing bracket to its matching opening bracket
2. walk through the string one char at a time:
  - if the char is an opening bracket, push it onto the stack
  - if it's a closing bracket, check two things in order:
    2.1: if the stack is empty, retrun False
    2.2: does the top of the stack match the expected opening bracket, if not, return false
    otherwise, pop the stack
3. after the loop, if the stack is not empty, return false
4. if we made it through the checks, return true
"""

bkt_match ={
    ')' : '(',
    '}' : '{',
    ']' : '[',
}
def is_bracket_matching(s:str) -> bool:

    def isOpening(character) -> bool:
        return character=='(' or character=="{" or character=="["

    def isClosing(character) -> bool:
        return character==')' or character=="}" or character=="]"

    open_bkt =[]

    for char in s:
        if isOpening(char): 
            open_bkt.append(char)
        elif isClosing(char):
            if len(open_bkt) == 0:
                return False
            tmp = open_bkt.pop()
            if bkt_match[char] != tmp:
                return False
    if len(open_bkt) != 0:
        return False
    return True







