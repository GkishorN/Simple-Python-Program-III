from collections import Counter
l=[5,7,3,5,7,9,2,6,8,4,6,3,1,1,2,7,9,5,3,2,7,5,1,9,0,4,1,0,5,5,3]
d=Counter(l)
new_list = list([item for item in d if d[item]>1])
print(new_list)
        

