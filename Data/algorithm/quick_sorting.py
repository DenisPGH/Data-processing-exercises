
list_test=[5,2,6,8,9,100,4,7]
def quicksorting(list_):
    if len(list_)<1:
        return list_
    less_pivot=[]
    great_pivot=[]
    pivot=list_[0]
    for value in list_[1:]:
        if value<pivot:
            less_pivot.append(value)
        else:
            great_pivot.append(value)
    return quicksorting(less_pivot)+[pivot]+quicksorting(great_pivot)

print(quicksorting(list_test))





""" test with csv unsorted names, sort and store in other csv file"""
all_names=[]
with open('names.csv', 'r') as name:
    all_names = name.readlines()

sorted_names=quicksorting(all_names)
#print(sorted_names)
with open('names_sort.csv', mode='w',newline='') as file:
    for a in sorted_names:
        file.write(a)


