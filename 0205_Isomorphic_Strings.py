def isIsomorphic(s: str, t: str) -> bool:    
    dictionary = {}
    seen = set()
    output = ""
    for i, c in enumerate(s):                
        if c not in dictionary:
            if t[i] in seen:
                return False
            dictionary[c] = t[i]
            seen.add(t[i])
        output += dictionary[c]
    return output == t
        
        
s = "egg"
t = "add"

print(isIsomorphic(s, t))
print(isIsomorphic("paper", "title"))
print(isIsomorphic("foo", "bar"))
