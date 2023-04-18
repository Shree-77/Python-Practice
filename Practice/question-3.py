"""
3.Selection sort using lists.
"""

my_list=[2,3,5,1,4]

for i in range (len(my_list)):
    min_index=i
    for j in range (i+1 , len(my_list)):
                    if my_list[j]< my_list[min_index]:
                        min_index=j;
                        
    my_list[i] , my_list[min_index] = my_list[min_index],my_list[i]
    
print(my_list)                  




                 