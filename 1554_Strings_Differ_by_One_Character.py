def differByOne(words):
    all_words = {}

    for w in words:
        for i in range(len(w)):
            new_word = w[:i] + "#" + w[i+1:]
            if new_word in all_words:
                return True
            all_words[new_word] = 1
    return False


if __name__ == '__main__':
    string = ["abcde","abaaa","aaade"]
    print(differByOne(string))
