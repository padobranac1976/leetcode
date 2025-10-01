from sortedcontainers import SortedList
from collections import defaultdict


def getFolderNames(names):
    hashmap = {}
    for name in names:
        modified = name
        if name in hashmap:
            k = hashmap[name]
            while modified in hashmap:
                k += 1
                modified = f'{name}({k})'
            hashmap[name] = k
        hashmap[modified] = 0

    return hashmap.keys()


if __name__ == '__main__':
    f1 = ["gta","gta(1)","gta","avalon"]
    print(getFolderNames(f1))


