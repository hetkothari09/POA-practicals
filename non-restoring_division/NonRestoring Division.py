n = 6
def cbin(num:int, n_bits=n):
    
    return bin(num)[2:].zfill(n_bits) if num >= 0 else bin((1 << n_bits) - (-num))[2:]

def twoc(bits:str, n_bits=n):
    
    return cbin((1 << n_bits) - int(bits, 2))

def left_shift(A:str, Q:str):
    
    return A[1:] + Q[0], Q[1:] + '0'

def add(A:str, M:str):
    
    S = cbin(int(A, 2) + int(M, 2))
    n_bits = globals()["n"] + 1
    if len(S) > n_bits:
        S = S[1:]
    return S

def division(Q:int, M:int):
    
    n_bits:int = globals()["n"] + 1
    Q = cbin(Q)
    M = cbin(M, n_bits)
    M2 = twoc(M, n_bits)
    A = '0' * n_bits
    count:int = globals()["n"]
    print("n\tA\tQ\tAction")
    action = "Initialize"
    print(count,A, Q, action, sep='\t')
    while count > 0:
        A, Q = left_shift(A, Q)
        action = "Left Shift"
        print(count,A, Q, action, sep='\t')
        if A[0] == "0":
            action = "A = A - M"
            A = add(A, M2)
        else:
            action = "A = A + M"
            A = add(A, M)
        print(count,A, Q, action, sep='\t')
        if A[0] == '1':
            action = "A < 0, Q[0] = 0"
            Q = Q[:-1] + '0'
        else:
            action = "A >= 0, Q[0] = 1"
            Q = Q[:-1] + '1'
        print(count,A, Q, action, sep='\t')
        count -= 1
    if A[0] == "1":
        A = add(A, M)
    print("The quotient =", Q, "=", int(Q, 2), "and the remainder is", A, "=", int(A, 2))

inputText = "Enter a number from less than " + str(2**n) + ": "
x = int(input(inputText))
y = int(input(inputText))
division(x, y)