merge(all, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [] x (n1) #n1 = len(L)
    R = [] x (n2) #n2 = len(R)

    for i in range(0,len(L)): # range (0,n1)
        L[i] = all[l + i]
        
    for j in range (0,len(R)):
        R[j] = all[m + 1 + j]


