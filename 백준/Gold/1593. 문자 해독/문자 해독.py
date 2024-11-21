# 문자 해독
#골드 5


import sys

W, S = map(int, sys.stdin.readline().rstrip().split())
word = sys.stdin.readline().rstrip()
sentence = sys.stdin.readline().rstrip()

answer = 0

word_state = [0] * 52
sentence_state = [0] * 52

for w in word:
    if 'a' <= w <= 'z':
        word_state[ord(w) - ord('a')] += 1
    else:
        word_state[ord(w) - ord('A') + 26] += 1


start = 0
length = 0

for s in sentence:
    if 'a' <= s <= 'z':
        sentence_state[ord(s) - ord('a')] += 1
    else:
        sentence_state[ord(s) - ord('A') + 26] += 1

    length += 1

    if length == len(word):
        if word_state == sentence_state:    # 구성이 같은 것을 찾기! 그것이 순열의 부분집합이 같다는 의미이다.
            answer += 1

        length -= 1
        start_character = sentence[start]
        if 'a' <= start_character <= 'z':
            sentence_state[ord(start_character) - ord('a')] -= 1

        else:
            sentence_state[ord(start_character) - ord('A') + 26] -= 1

        start += 1

print(answer)