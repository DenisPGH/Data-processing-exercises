import random

def split(list_):
    mid=len(list_)//2
    left=list_[:mid]
    right=list_[mid:]
    return left,right


def merge(left,right):
    list_final=[]
    l=0
    r=0
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            list_final.append(left[l])
            l+=1
        else:
            list_final.append(right[r])
            r += 1

    while l<len(left):
        list_final.append(left[l])
        l+=1
    while r<len(right):
        list_final.append(right[r])
        r+=1
    return list_final







def merge_sort(list_):
    if len(list_)<=1:
        return list_

    left_part,right_part=split(list_)
    left=merge_sort(left_part)
    right=merge_sort(right_part)

    return merge(left,right)




#lll=[random.randint(1,20000000) for x in range(300000)]
lll=["a","h",'d','b','e','c','A','B','d']
result=merge_sort(lll)
print(result)
