# https://dojopuzzles.com/problems/anagramas/
def anagramas(palavra):
    if len(palavra) <=1:
        return palavra
    else:
        tmp = []
        for aux in anagramas(palavra[1:]):
            for i in range(len(palavra)):
                tmp.append(aux[:i] + palavra[0:1] + aux[i:])
        return tmp
teste = input('Digite o anagrama: ')
print(anagramas(teste))