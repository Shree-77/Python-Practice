dict_1={"apple":1 , "orange" : 2, "grape ": 4}
dict_2={"bannana": 20,"watermelon":2,"zebrafruit":9}

merge_dict= dict_1.copy()
merge_dict.update(dict_2)
sorted_dict = dict(sorted(merge_dict.items()))
print(sorted_dict)