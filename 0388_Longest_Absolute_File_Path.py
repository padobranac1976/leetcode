def lengthLongestPath(input):
    num_files = input.count(".")
    if num_files < 1:
        return 0
    parts = input.split("\n")
    max_len = 0
    for i, p in enumerate(parts):
        if "." in p:
            path = []
            indentation = p.count("\t")
            path.append(p.replace("\t", ""))
            while indentation > 0:
                i -= 1
                if parts[i].count("\t") < indentation:
                    indentation -= 1
                    path.append(parts[i].replace("\t", ""))
            absolute_path = "/".join(path[::-1])
            max_len = max(max_len, len(absolute_path))

    return max_len


if __name__ == '__main__':
    inpt = "a"
    result = lengthLongestPath(inpt)
    print(result)



