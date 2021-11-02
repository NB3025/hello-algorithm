def checkdiff(query, key):
    diff = 0
    for a,b in zip(query, key):
        if a!=b:
            diff += 1
    return diff == 1       
def solution(begin, target, words):
    answer = []

    # words에 target 단어가 없으면 반환 못함
    if target not in words:
        return 0

    #target에서 알파벳 하나만 바꾸어 begin으로 갈 수 있는지
    def search(target, words, depth):
        for word in words:
            #target이 하나만 바꾸면 begin이 되는지
            if word == target and checkdiff(begin, word):
                answer.append(depth)
            #words안에 단어 중 target과 한글자가 다른 경우
            elif checkdiff(target,word):
                #depth을 하나 더 늘리고 target을 제외한 words 에서 한개만 다른 사이 다시 확인
                search(word, [w for w in words if w != target], depth+1)
    search(target, words, 1)

    return min(answer)

begin="hit"
target="cog"
words=["hot", "dot", "dog", "lot", "log", "cog"]

print (solution(begin, target, words))