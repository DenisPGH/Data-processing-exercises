import time




def binary_search(collection,target):
    first_index=0
    last_index=len(collection)-1
    while first_index<=last_index:
        mid_point=(first_index+last_index)//2
        if collection[mid_point]==target:
            return mid_point
        elif collection[mid_point]<target:
            first_index=mid_point+1
        else:
            last_index=mid_point-1
    return  None



names=[]
with open('names_sort.csv', 'r') as name:
    names=name.readlines()


#print(names)
start_time = time.process_time()
#print(start_time)
index=binary_search(names,'wQUVe\n')

end=(time.process_time() - start_time)
print(f"{index}==={end}")

