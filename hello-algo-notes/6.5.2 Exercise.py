from collections import defaultdict

def is_match(s:str, t:str) -> bool:
    compare_dict = defaultdict(int)
    if len(s) != len(t):
        return False
    else:
        for char in s:
           compare_dict[char] += 1 
        for char in t:
            compare_dict[char] -= 1
    return all(v == 0 for v in compare_dict.values())

s = "appleisme"
t = "ismeapple"
print(is_match(s,t))
