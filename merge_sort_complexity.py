import matplotlib.pyplot as plt
from merge_sort import merge_sort
import time
import random 

def merge_sort_complexity():
    x, y = [], []

    for i in range (10000, 100000, 10000):
        sample_data = random.sample(range(i), i )
                
        start_time = time.time()
        merge_sort(sample_data)
        end_time = time.time()
      
        x.append(i)
        y.append(end_time-start_time)

    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    merge_sort_complexity()
