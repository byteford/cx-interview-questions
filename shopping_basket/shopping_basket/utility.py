def sortItems(catalog, items):
    if len(items) > 1:
        mid = len(items)//2
        L = items[:mid]
        R = items[mid:]

        sortItems(catalog, L)
        sortItems(catalog, R)

        i = j = k = 0

        while i < len(L) and j < len(R):

            if catalog[L[i]] > catalog[R[j]]:
                items[k] = L[i]
                i +=1
            else:
                items[k] = R[j]
                j+=1
            k+=1
        
        while i < len(L):
            items[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            items[k] = R[j]
            j+=1
            k+=1
    print(items)
    return items
def DicToList(items):
    arr=[]
    for key, value in items.items():
            for i in range(value):
                arr.append(key)
    return arr