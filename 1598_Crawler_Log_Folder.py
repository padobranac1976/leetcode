def minOperations(logs: list[str]) -> int:
	counter = 0
	for log in logs:
		if log == "../":
			counter = max(counter - 1, 0)
		elif log == "./":
			continue
		else:
			counter += 1
	return counter


if __name__ == '__main__':
    n = ["d1/","d2/","../","d21/","./"]
    result = minOperations(n)
    print(result)
    
    n = ["d1/","d2/","./","d3/","../","d31/"]
    result = minOperations(n)
    print(result)
    
    n = ["d1/","../","../","../"]
    result = minOperations(n)
    print(result)


