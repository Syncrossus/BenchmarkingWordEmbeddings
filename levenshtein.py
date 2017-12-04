def levenshtein(l1, l2):
    m = np.zeros(shape=(len(l1),len(l2)))
    m[0,:] = range(0,len(l2))
    m[:,0] = range(0,len(l1))
    for i in range(1,len(l1)):
        for j in range(1,len(l2)):
            cost = 0
            if l1[i]!=l2[j]:
                cost = 1
            m[i, j] = min(m[i-1, j] + cost, m[i, j-1] + cost, m[i-1, j-1] + cost)
    return m[len(l1)-1, len(l2)-1]
