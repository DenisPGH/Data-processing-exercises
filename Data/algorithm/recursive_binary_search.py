import time
import matplotlib.pyplot as plt
import numpy as np
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

def generate_list(range_value):
    list_ = [x for x in range(range_value)]
    return list_

dict_random={100000 : 30,
             10000000:4000,
             100001:10,
             1000: 50,

             }
target="target"
ranges='ranges'
result='result'
time_calc='time'
results={}
counter=1
for range_,target_ in dict_random.items():
    start_time = time.time()
    res = recursive_binary_search(generate_list(range_), target_)
    time_calculation=time.time() - start_time
    #print(f"{res}====={time_calculation}")
    results[counter]={result:res,ranges:range_,target:target_,time_calc:time_calculation}
    counter+=1

#print(results)
time_show=[x[time_calc] for x in results.values()]
range_show=[x[ranges] for x in results.values()]


# plt.plot(time_show, range_show,'ro')
# plt.show()
# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100

plt.scatter(time_show, range_show, data=results)
plt.xlabel('Time in sec')
plt.ylabel('Range of list')
plt.show()






