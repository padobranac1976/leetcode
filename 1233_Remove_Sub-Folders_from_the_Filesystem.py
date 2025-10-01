def removeSubfolders(folder):
    directories = {}
    for f in folder:
        directories[f] = True

    for f in folder:
        folder_split = f.split('/')
        if len(folder_split) > 2:
            for i in range(len(folder_split) - 1, 1, -1):
                subfolder = '/'.join(folder_split[:i])
                if subfolder in directories:
                    directories[f] = False
                    break

    out = []
    for k in directories:
        if directories[k]:
            out.append(k)

    return out


if __name__ == '__main__':
    n = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
    result = removeSubfolders(n)
    print(result)


