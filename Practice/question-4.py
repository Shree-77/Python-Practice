"""
4. Bubble sort using lists.
"""

my_list = [5,6,7,21,3421,21]

n = len(my_list)

for i in range (n):
    for j in range (n-i-1):
        if my_list[j]>=my_list[j+1]:
            my_list[j] , my_list[j+1]=my_list[j+1] , my_list[j]
            
print(my_list)            