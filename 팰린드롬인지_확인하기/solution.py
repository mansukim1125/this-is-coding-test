def solution():
    sentence = input()
    reversed_sentence = list(sentence)
    reversed_sentence.reverse()
    reversed_sentence = ''.join(reversed_sentence)

    print(int(sentence == reversed_sentence))


if __name__ == '__main__':
    solution()