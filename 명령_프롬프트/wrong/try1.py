def solution():
    n = int(input())

    pattern = None
    for _ in range(n):
        new_line = input()
        if pattern is None:
            pattern = new_line.split() # ['string...'] <- 이렇게 되면..
            continue
        for i in range(len(pattern)): # for loop 이 한 번 돌게 되고..
            ch_new_line = new_line[i] # 's'
            ch_pattern = pattern[i] # 'string...'
            if ch_pattern != ch_new_line: # 당연히 다르게 되고..
                pattern[i] = '?' # ?가 추가된다.

    print(''.join(pattern)) # for loop 이 한 번만 동작하므로 '?' 하나만 출력됨..


if __name__ == '__main__':
    solution()
