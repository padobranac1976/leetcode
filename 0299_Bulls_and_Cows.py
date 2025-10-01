def getHint(secret, guess):
    bulls = 0
    cows = 0
    secret_letters = {}

    for l in secret:
        if l in secret_letters:
            secret_letters[l] += 1
        else:
            secret_letters[l] = 1

    for i, ch in enumerate(guess):
        if ch in secret_letters:
            if secret[i] == ch:
                bulls += 1
                cows -= int(secret_letters[ch] <= 0)
            else:
                cows += int(secret_letters[ch] > 0)

            secret_letters[ch] -= 1

    return str(bulls) + "A" + str(cows) + "B"


if __name__ == '__main__':
    s = "1807"
    g = "7810"
    result = getHint(s, g)
    print(result)


