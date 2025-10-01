from collections import defaultdict


def expressiveWords(s, words):
    def make_dict(string):
        string_dict = defaultdict(int)
        w_i = -1
        for c in string:
            if c + str(w_i) not in string_dict:
                w_i += 1
            string_dict[c + str(w_i)] += 1
        return string_dict

    s_dict = make_dict(s)
    result = 0

    for w in words:
        found = 0
        word = make_dict(w)
        if s_dict.keys() != word.keys():
            continue
        for key in word:
            found += word[key] == s_dict[key] or (word[key] < s_dict[key] and s_dict[key] >= 3)
        if found == len(s_dict):
            result += 1

    return result


if __name__ == '__main__':
    n = "sass"
    l = ["sa"]
    print(expressiveWords(n, l))