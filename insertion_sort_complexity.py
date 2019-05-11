import matplotlib.pyplot as plt
from insertion_sort import insertion_sort
import time
import random 

def insertion_sort_complexity():
    x, y = [], []

    for i in range (1000, 10000, 1000):
        sample_data = random.sample(range(i), i )
                
        start_time = time.time()
        insertion_sort(sample_data)
        end_time = time.time()
        
        x.append(i)
        y.append(end_time-start_time)

    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    insertion_sort_complexity()
