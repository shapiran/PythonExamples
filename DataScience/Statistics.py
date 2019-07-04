import collections
import matplotlib.pyplot as plt

num_friends = [100, 49, 41, 40, 25,22,19,18,16,13,13,12,12,12,11,10,9,9,9,8,7,7,7,2,3,4,5,6,7,8,1,2,3,4,5,6,7,34,2,2,1,3,5,6,
               6,6,6,6,6,6,6,6,6,5,5,4,4,4,3,3,3,3,3,3,3,3,2,2,2,2,2,2,1,1,1,1,1,3,3,3,3,3,4,4,4,4,4,45,5]


friend_counts = collections.Counter(num_friends)
xs = range(101)                         # largest value is 100 
ys = [friend_counts[x] for x in xs]     # height is just # of friends 
plt.bar(xs, ys) 
plt.axis([0, 101, 0, 25]) 
plt.title("Histogram of Friend Counts") 
plt.xlabel("# of friends") 
plt.ylabel("# of people") 
plt.show()

num_points = len(num_friends) 
print("num point =",num_points)
largest_value = max(num_friends)   
print("largest value=",largest_value)         # 100 
smallest_value = min(num_friends)
sorted_values = sorted(num_friends) 
smallest_value = sorted_values[0]           # 1 
second_smallest_value = sorted_values[1]    # 1 
second_largest_value = sorted_values[-2]

print("smallest value=",smallest_value," second smallest value=",second_smallest_value," second largest value=",second_largest_value)         # 100 

def mean(x):    
    return sum(x) / len(x)

print("mean num friends=",mean(num_friends))

def median(v):    
    """finds the 'middle-most' value of v"""    
    n = len(v)    
    sorted_v = sorted(v)    
    midpoint = n // 2
    if n % 2 == 1:        
        # if odd, return the middle value        
        return sorted_v[midpoint]    
    else:        
        # if even, return the average of the middle values        
        lo = midpoint - 1        
        hi = midpoint        
        return (sorted_v[lo] + sorted_v[hi]) / 2
    
print("median =",median(num_friends))    

def quantile(x, p):    
    """returns the pth-percentile value in x"""    
    p_index = int(p * len(x))    
    return sorted(x)[p_index]

print(quantile(num_friends, 0.10) )
print(quantile(num_friends, 0.25))
print(quantile(num_friends, 0.75))
print(quantile(num_friends, 0.90))

def mode(x):    
    """returns a list, might be more than one mode"""    
    counts = collections.Counter(x)    
    max_count = max(counts.values())    
    return [x_i for x_i, count in counts.items() if count == max_count]

print("mode=",mode(num_friends))

def data_range(x):    
    return max(x) - min(x)

print(data_range(num_friends)) # 99 

def de_mean(x):    
    """translate x by subtracting its mean (so the result has mean 0)"""    
    x_bar = mean(x)    
    return [x_i - x_bar for x_i in x]


def variance(x):    
    """assumes x has at least two elements"""    
    n = len(x)    
    deviations = de_mean(x)    
    return sum_of_squares(deviations) / (n - 1)

print(variance(num_friends)) # 81.54
