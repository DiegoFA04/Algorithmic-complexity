# Convert the WORD in NUMBER
# For each word: Get the values of dictionary using the key. After that, generate the number
# Example:
#   codex =  {'Y': 1, 'M': 4, 'S': 2, 'N': 9, 'E': 8, 'R': 3, 'D': 7, 'O': 5}
#   word = "SEND"
#     for ch="S" num = S
#     for ch="E" num = S*10 + E
#     for ch="N" num = (S*10 + E)*10 + N
#     for ch="D" num = ((S*10 + E)*10 + N)*10 + D
def conv(codex, word):
    num = 0
    for ch in word:
        num = num*10 + codex[ch]

    return num


def check(perm, alpha: list, w1, w2, w3: str):
    codex = {ch: d for ch, d in zip(alpha, perm)} #dictionary {letter:value}
    # Example codex:
    # codex =  {'Y': 1, 'M': 4, 'S': 2, 'N': 9, 'E': 8, 'R': 3, 'D': 7, 'O': 5}
    a = conv(codex, w1) # a is the numeric value of SEND
    b = conv(codex, w2) # b is the numeric value of MORE
    c = conv(codex, w3) # c is the numeric value of MONEY

    # Print all the possible ADDING (without constraints)
    if a + b == c:
        s = f"{w1}={a:0{len(w1)}} + {w2}={b:0{len(w2)}} = {w3}={c:0{len(w3)}}"
        print(s)
        # Example:
        # SEND=6853 + MORE=0728 = MONEY=07581 [NO VALID]
        # SEND=9567 + MORE=1085 = MONEY=10652 [VALID]


def genPerm(digits, perm: list, r, alpha, w1, w2, w3):
    # perm: is the list for the permutations (empty in the begin)
    
    # Base Condition to Recursivity
    if len(perm) == r: #len of permut == len of alphabet (send + more = money)
        check(perm, alpha, w1, w2, w3)
    else:
        # Call the recursity
        # enumeration: keep a count of iterations (start=0)
        # Example: i,d -> [(0, 0), (1, 1), (2, 2), ...(9:9)]
        for i, d in enumerate(digits):
            #print("i=", i, ", d=", d, ", digits[:i] = ", digits[:i],  ", digits[i+1:] = ", digits[i+1:], ", digits[:i] + digits[i+1:] = ", digits[:i] + digits[i+1:])
            genPerm(digits[:i] + digits[i+1:], perm + [d], r, alpha, w1, w2, w3)
            """
            Example:
            i= 0 , d= 0 , digits[:i] =  [] , digits[i+1:] =  [1, 2, 3, 4, 5, 6, 7, 8, 9] , digits[:i] + digits[i+1:] =  [1, 2, 3, 4, 5, 6, 7, 8, 9]
            i= 0 , d= 1 , digits[:i] =  [] , digits[i+1:] =  [2, 3, 4, 5, 6, 7, 8, 9] , digits[:i] + digits[i+1:] =  [2, 3, 4, 5, 6, 7, 8, 9]
            i= 0 , d= 2 , digits[:i] =  [] , digits[i+1:] =  [3, 4, 5, 6, 7, 8, 9] , digits[:i] + digits[i+1:] =  [3, 4, 5, 6, 7, 8, 9]
            i= 0 , d= 3 , digits[:i] =  [] , digits[i+1:] =  [4, 5, 6, 7, 8, 9] , digits[:i] + digits[i+1:] =  [4, 5, 6, 7, 8, 9]
            i= 0 , d= 4 , digits[:i] =  [] , digits[i+1:] =  [5, 6, 7, 8, 9] , digits[:i] + digits[i+1:] =  [5, 6, 7, 8, 9]
            i= 0 , d= 5 , digits[:i] =  [] , digits[i+1:] =  [6, 7, 8, 9] , digits[:i] + digits[i+1:] =  [6, 7, 8, 9]
            i= 0 , d= 6 , digits[:i] =  [] , digits[i+1:] =  [7, 8, 9] , digits[:i] + digits[i+1:] =  [7, 8, 9]
            i= 0 , d= 7 , digits[:i] =  [] , digits[i+1:] =  [8, 9] , digits[:i] + digits[i+1:] =  [8, 9]
            i= 1 , d= 8 , digits[:i] =  [7] , digits[i+1:] =  [9] , digits[:i] + digits[i+1:] =  [7, 9]
            i= 2 , d= 9 , digits[:i] =  [7, 8] , digits[i+1:] =  [] , digits[:i] + digits[i+1:] =  [7, 8]
            i= 1 , d= 7 , digits[:i] =  [6] , digits[i+1:] =  [8, 9] , digits[:i] + digits[i+1:] =  [6, 8, 9]
            ...
            ...
            ...
            i= 2 , d= 7 , digits[:i] =  [4, 5] , digits[i+1:] =  [] , digits[:i] + digits[i+1:] =  [4, 5]
            i= 3 , d= 7 , digits[:i] =  [4, 5, 6] , digits[i+1:] =  [8, 9] , digits[:i] + digits[i+1:] =  [4, 5, 6, 8, 9]
            i= 0 , d= 4 , digits[:i] =  [] , digits[i+1:] =  [5, 6, 8, 9] , digits[:i] + digits[i+1:] =  [5, 6, 8, 9]
            """  

def solve(w1, w2, w3: str):
    alphabet = set(w1 + w2 + w3) #Use set to avoid the duplicates
    genPerm([i for i in range(10)], [], len(alphabet), alphabet, w1, w2, w3) #(digits as list, empty list, len(alphabet), alphabet, w1, w2, w3)


solve("SEND", "MORE", "MONEY")


# ANSWER:
# SEND=9567 + MORE=1085 = MONEY=10652