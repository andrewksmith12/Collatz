#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------


def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------


def collatz_eval(i, j):
    """
    create a dictionary to cache values, 
    return the max value between the range, [i,j]
    """
    evalDict = {}
    for n in range(i, j+1):
        i = n
        c = 1
        while i >= 1:
            if i == 1:
                evalDict[n] = c
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
    return max(evalDict.values())

# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
    """
    Use the sub-functions to solve collatz and process the stinput
    """
    for s in r:
        if not s.strip():
            continue
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
