
def multi_egyp(nb1, nb2):
    A = nb2
    B = nb1
    C = 0
    while A != 0:
        if A % 2 == 1:
            C = C+B
        A = A//2
        B = B+B
    print(C)


nb1 = int(input())
nb2 = int(input())
multi_egyp(nb1, nb2)
