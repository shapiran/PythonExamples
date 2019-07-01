# -*- coding: utf-8 -*-
from functools import reduce
import math

def vector_add(v, w):
    """adds corresponding elements"""    
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
    """subtracts corresponding elements"""    
    return [v_i - w_i for v_i, w_i in zip(v, w)] 

def vector_sum(vectors):
    """sums all corresponding elements"""    
    result = vectors[0]                         # start with the first vector    
    for vector in vectors[1:]:                  # then loop over the others        
        result = vector_add(result, vector)     # and add them to the result    
    return result

v1=[0,1,2,3]
v2=[1,2,3,4]
v3=[2,3,4,5]

print(vector_add(v1,v2))
print(vector_sum((v1,v2)))
print(vector_sum((v1,v2,v3)))

def vector_sum_reduce(vectors):    
    return reduce(vector_add, vectors) 

l_sum= vector_sum_reduce((v1,v2,v3))

print(l_sum)

def scalar_multiply(c, v):    
    """c is a number, v is a vector"""    
    return [c * v_i for v_i in v] 

print(scalar_multiply(4,[0,1,4]))


def vector_mean(vectors):   
    """compute the vector whose ith element is the mean of the    
    ith elements of the input vectors"""    
    n = len(vectors)   
    return scalar_multiply(1/n, vector_sum(vectors)) 

print(vector_mean((v1,v3)))

def dot(v, w):    
    """v_1 * w_1 + ... + v_n * w_n"""    
    return sum(v_i * w_i               
               for v_i, w_i in zip(v, w))
    
print(dot(v1,v2))    

def sum_of_squares(v):    
    """v_1 * v_1 + ... + v_n * v_n"""    
    return dot(v, v)

print(sum_of_squares(v1))

def magnitude(v):    
    return math.sqrt(sum_of_squares(v))

print(magnitude(v1))

def squared_distance(v, w):   
    """(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""    
    return sum_of_squares(vector_subtract(v, w))
                          
def distance(v, w):    
    return magnitude(vector_subtract(v, w))                           



