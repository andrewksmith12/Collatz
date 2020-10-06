import sys

def collatz_read(s):
    a = s.split()
    return [int(a[0]), int(a[1])]

evalDict = {}

def collatz_eval(i, j):
    localDict = {}
    if i > j:
            tmp = j
            j = i
            i = tmp
    for n in range (i,j+1):
        i = n
        c = 1
        while i >= 1:
            if i == 1:
                evalDict[n] = c
                localDict[n] = c
                break
            if i in evalDict.keys():
                dictVal = evalDict[i]
                c = c + dictVal - 1
                i = 1
            else:
                if (i % 2 == 0):
                    i = i//2
                    c = c + 1
                else:
                    i = (3 * i) + 1
                    c = c + 1
    return max(localDict.values())

def collatz_print(w, i, j, v):
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

def collatz_solve(r, w):
    for s in r:
        if not s.strip():
            continue
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)

collatz_solve(sys.stdin, sys.stdout)