def wordsTyping(sentence, rows, cols):
    completed = 0
    current_row = 0
    current_col = 0
    current_word = 0
    word = sentence[0]
    answer = []
    line = []
    while current_row < rows:
        if len(word) + current_col <= cols:
            current_col += len(word) + 1
            line.append(word)
            line.append("-")
        else:
            current_row += 1
            if current_row == rows:
                break
            current_col = len(word) + 1
            answer.append(line)
            line = [word, "-"]

        if current_word < len(sentence) - 1:
            current_word += 1
        else:
            current_word = 0
            completed += 1
        word = sentence[current_word]

    return completed


if __name__ == '__main__':
    s = ["f","p","a"]
    r = 8
    c = 7
    result = wordsTyping(s, r, c)
    print(result)


