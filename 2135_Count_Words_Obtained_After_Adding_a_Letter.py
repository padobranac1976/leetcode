def wordCount(startWords, targetWords):
    lookup = set()

    for word in startWords:
        frozen = frozenset(word)
        lookup.add(frozen)

    count = 0
    for word in targetWords:
        for i in range(len(word)):
            new_word = word[:i] + word[i + 1:]

            if frozenset(new_word) in lookup:
                count += 1
                break

    return count


if __name__ == '__main__':
    sW = ["ant","act","tack"]
    tW = ["tack","act","acti"]
    print(wordCount(sW, tW))