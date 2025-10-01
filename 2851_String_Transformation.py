def numberOfWays(s: str, t: str, k: int) -> int:

    return len(s)

if __name__ == '__main__':
    s = "abcd"
    t = "cdab"
    k = 2
    
    # For function solution
    output = numberOfWays(s, t, k)
    
    # # For Class solution
    # output = []
    # for i, inpt in enumerate(input1):
    #     if inpt == "HitCounter":
    #         obj = HitCounter()
    #         output.append(None)
    #     elif inpt == "hit":
    #         result = obj.hit(input2[i][0])
    #         output.append(result)
    #     else:
    #         result = obj.getHits(input2[i][0])
    #         output.append(result)

    print(output)



