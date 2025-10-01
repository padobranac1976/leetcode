def destCity(paths: list[list[str]]) -> str:
    candidates = []
    removed = []
    for a, b, in paths:        
        removed.append(a)
        if b not in removed:
            candidates.append(b)
        if a in candidates:
            candidates.remove(a)
    
    return candidates[0]


def destCity_Better(paths)
    sec = set(path[1] for path in paths)
    fir = set(path[0] for path in paths)
    ans = sec - fir
    return ans.pop()
    
    
if __name__ == '__main__':
    paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    answer = destCity(paths)
    print(answer)


