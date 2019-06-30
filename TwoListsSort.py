# -*- coding: utf-8 -*-

list1 = [1, 2, 5, 4, 4, 3, 6]
list2 = [3, 2, 1, 2, 1, 7, 8]
list3 = list();
k = 0;

list1.sort()
list2.sort()

for i in list1:  
    while i > list2[k]:
        list3.append(list2[k])
        k = k + 1
    
    list3.append(i) 

while k < len(list2):
    list3.append(list2[k])
    k=k+1
        
print(list3)

