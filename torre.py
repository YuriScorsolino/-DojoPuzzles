# https://dojopuzzles.com/problems/torres-de-hanoi/
def torres(n, A, B, C):
    if n == 1:
        print('Disco 1 de', A, 'para', B)
        return
    torres(n-1, A, C, B)
    print('Disco', n, 'de', A, 'para', B)
    torres(n-1, C, B, A)

torres(3, 'A', 'B', 'C')