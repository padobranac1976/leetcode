def findReplaceString(s, indices, sources, targets):
    target_hash = {}
    output = ""

    for i, idx in enumerate(indices):
        if s[idx:idx + len(sources[i])] == sources[i]:
            target_hash[idx] = (targets[i], sources[i])

    i = 0
    while i < len(s):
        if i in target_hash:
            output += target_hash[i][0]
            i += len(target_hash[i][1])
        else:
            output += s[i]
            i += 1
    return output


if __name__ == '__main__':
    string = "abcd"
    inds = [0, 2]
    srcs = ["a", "cd"]
    ts = ["eee", "ffff"]
    print(findReplaceString(string, inds, srcs, ts))