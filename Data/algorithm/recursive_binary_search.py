import time

def recursive_binary_search(list,target):
    if len(list)==0:
        return False

    mid_point=len(list)//2
    if list[mid_point]==target:
        return True
    elif list[mid_point]<target:
        return recursive_binary_search(list[mid_point+1:],target)
    else:
        return recursive_binary_search(list[:mid_point], target)

list_=[x for x in range(90000000000000)]
start_time = time.time()
res=recursive_binary_search(list_,900000000)
print(f"{res}====={time.time() - start_time}")
