def primeira_unica_letra(s: str) -> int:
    hashmap = {}

    """ i = posicao (chave), char = caractere (valor)"""

    for i, char in enumerate(s):
        if not hashmap.get(char):
            hashmap[char] = [i, 1]
        else:
            hashmap[char][1] += 1
        #print(char)

    for i, val in hashmap.items():
        if val[1] == 1:
            return val[0]
        print(val)

    return -1


s = "leetcode"
primeira_unica_letra(s)

