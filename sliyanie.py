a = [7,4,9,3,5,6,7,3,4]
def merge_sort(a):
    if len(a)<2:
        return a[:]
    else:
        median = int(len(a)/2)
        left = a[:median]
        right = a[median:]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left,right)

def merge(left,right):
    res = []
    i,j = 0, 0
    while i <len(left) and j < len(right):
        if left[i]<right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    while i < len(left):
        res.append(left[i])
        print(res)
        i+=1
    while j<len(right):
        res.append(right[j])
        j+=1
    return res

merge_sort(a)