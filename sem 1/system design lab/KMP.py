def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    pi = [0] * M
    j = 0
    computepiArray(pat, M, pi)
    print(pi)
    i = 0
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            print("Found pattern at index " + str(i - j))
            j = pi[j - 1]


        elif i < N and pat[j] != txt[i]:

            if j != 0:
                j = pi[j - 1]
            else:
                i += 1


def computepiArray(pat, M, pi):
    len = 0
    pi[0]
    i = 1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            pi[i] = len
            i += 1
        else:
            if len != 0:
                len = pi[len - 1]
            else:
                pi[i] = 0
                i += 1
txt = input("enter any string")
pat = input("enter pattern")
KMPSearch(pat, txt)
