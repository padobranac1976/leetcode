def reorderLogFiles(logs):
    def get_key(log):
        _id, rest = log.split(" ", maxsplit=1)
        return (0, rest, _id) if rest[0].isalpha() else (1,)

    return sorted(logs, key=get_key)


if __name__ == '__main__':
    ns1 = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    print(reorderLogFiles(ns1))