#!/usr/bin/env python
# coding: utf-8

# In[8]:


def matchingSocks(socks): 
    # edge case
    if len(socks) == 0 or len(socks) == 1:
        return 0
    # get set of unique colors in socks
    singles = set(socks)
    pairs = 0
    for x in singles:
        # get no of pairs of that color
        y = socks.count(x) // 2
        # add to total pairs
        pairs += y        
    return pairs


print(matchingSocks([10,20,20,10,10,30,50,10,20]))
print(matchingSocks([1,2,1,3,4,2,5,4,1,3]))
print(matchingSocks([]))
print(matchingSocks([8]))
print(matchingSocks([1,2,4,3,7,4,3,7,2,7,2,5,2,0,9,5]))
print(matchingSocks([1,2,3,4,5,6,2,8,9,11,11,1,24,14,15,16,39,18,19,7,8,22,22,8,25,8,9,5,4,30]))


# In[ ]:




