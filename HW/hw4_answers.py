# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 21:23:25 2022

@author: edwar
"""

# Homework 4 Answers.

# TWO SORT ALGORITHMS.
    # 1. Bubble Sort. - O(n^2) time (quadratic).
    
    # 2. Counting Sort. - O(n) time (linear).

#%% Import packages.
import random
import time
import timeit
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter1d
    

#%% TEST CASE.
testlist = list(range(100))
random.shuffle(testlist)

testlist2 = testlist.copy()
testlist2.append(-50)
testlist2.append(5)
testlist2.append(-25)


#%% Bubble sort implementation.

def BubbleSort(list1):
    # Copy `list` by creating a soon-to-be-sorted copied list object.
    ## Use 'copy()' because otherwise the original list will be modified as well.
    ## This occurs because the simpler command `sorted_list = list1` doesn't create
    ## a new object. It creates a new reference back to the original object.
    sorted_list = list1.copy()
    # Base the number of iterations on the number of items in list.
    it_num = len(list1)
    # Iterate through list as many times as the number of elements in the list.
    for i in range(it_num):
        # Now go through all elements of the list from iteration `0` to `it_num - k - 1`.
        ## For each element in the list, compare it with the subsequent element.
        ## If the subsequent element is greater, switch the initial and subsequent elements. 
        ## Then repeat this for the next iteration, so on and so forth.
        ## NOTE: I use 'k - 1' because the last iteration in the list is not switched.
        ### This is because we check it in the initial algorithm. If the previous element is
        ### greater than the final element, then we switch them and know that the final algorithm
        ### is now the largest in the list since we looked through all prior elements in the list.
        for k in range(it_num - i - 1):
            # If current iteration `k` is smaller than subseqent iteration `k + 1`, switch them.
            if sorted_list[k] > sorted_list[k + 1]:
                # I found this method of swapping locations using the following source:
                # https://www.studytonight.com/python-programs/python-program-to-swap-two-elements-in-a-list
                sorted_list[k], sorted_list[k + 1] = sorted_list[k + 1], sorted_list[k]
    return(sorted_list)
# This function should iterate through all elements of the list until all are sorted from smallest to largest.

# Test using testlist & testlist2.

#test_output = BubbleSort(testlist2) # WORKS!
#print(test_output)

#%% Counting Sort Implementation.

def CountingSort(list1):
    # Make sure input is a list.
    
    # Make sure that all list entries are integers.
    int_check = []
    for num1 in list1:
        int_check.append(not isinstance(num1, int))
    if any(int_check):
        raise Exception("List contains non-integer elements!")    
    # I want this to work for lists that include negative numbers as well. 
    input_minimum = min(list1)
    input_maximum = max(list1)
    # Create list to store counts of each element that's 
    # as long as the range of numbers in the list.
    c_list = []
    for num2 in range(input_maximum - input_minimum + 1):
        c_list.append(0)
    # Count the number of times that each number appears in the original 
    # input list, then add these to elements with the corresponding index in the c_list.
    # NOTE: we locate the correct index in c_list using the input minimum, since we allow
    # the input list to contain negative numbers.
    for i in range(0, len(list1)):
        inner1 = list1[i] - input_minimum
        c_list[inner1] += 1
    # Now we have counts for each number in the input list.
    # Next, cumulatively sum each element in c_list from the first to last integer.
    # This allows us to locate the positions of each element in the final output list.
    for j in range(1, len(c_list)):
        c_list[j] += c_list[j - 1]
    # Create list of zeroes that's as long as the original input list.
    output_list = []
    for num3 in range(len(list1)):
        output_list.append(0)
    # Finally, fill output_list with now-ordered numbers from the original input list.
    # After number from original list is added to output list, subtract 1 from corresponding
    # c_list count for that number.
    for k in range(len(list1) - 1, -1, -1):
        inner2 = list1[k] - input_minimum
        output_list[c_list[inner2] - 1] = list1[k]
        c_list[inner2] -= 1
    # Return output_list.
    return output_list

# TEST FUNCTION.
#test_output = BubbleSort([2, 1]) # WORKS!
#print(test_output)
#test_output = BubbleSort([2, 1]) # WORKS!
#print(test_output)
#del(test_output)


#%% Run simulations for both functions.

# Choose N: maximum size of unsorted list.
N = 2000

# Create list of 'N' unsorted lists in increasing sizes.




# create lists for each sorting method. 
# Each element corresponds to increasing values of N.
bubble_simtime = []
counting_simtime = []
# Run simulations for each.
for size in range(2, N):
    print(f"Simulation {size} of {N}")
    # Create unsorted list of size 'size'.
    unsorted_list = list(range(size))
    random.shuffle(unsorted_list)
    # Run each sort function and record the time it takes to run.
##### FIRST: bubble sort.
    beginning = time.process_time()
    BubbleSort(unsorted_list)
    end = time.process_time()
    # Find duration of time it took.
    duration = end - beginning
    # Append duration to bubble_simtime.
    bubble_simtime.append(duration)
##### SECOND: counting sort.
    beginning = time.process_time()
    CountingSort(unsorted_list)
    end = time.process_time()
    # Find duration of time it took.
    duration = end - beginning
    # Append duration to counting_simtime.
    counting_simtime.append(duration) 
del(size)

# DIFFERENTIAL SCALES graph.
bubble_simtime_scaled = [x * 10 for x in bubble_simtime] # 1/10 seconds, or decisecond
counting_simtime_scaled = [x * 100 for x in counting_simtime] #1/1000 second, or millisecond

#%% GRAPH TIME vs. N.


# TRUE SCALE GRAPH - NOT SMOOTHED.

## Define x-axis (# elements in list).
x1 = range(2, N)
x2 = range(2, N)
## Define y-axis: time.
y1 = bubble_simtime # bubble sort.
y2 = counting_simtime # counting sort.
# Actually plot the data connecting with lines.
plt.plot(x1, y1) # Bubble lines
plt.plot(x2, y2) # counting lines 
# labels, titles, legend, etc.
plt.legend(["Bubble Sort\n(Quadratic Time)", "Counting Sort\n(Linear Time)"])
plt.ylabel("Run Time (Seconds)")
plt.xlabel("Size of Input List")
plt.title("How Algorithms Effect Runtime\n(UNSCALED, UNSMOOTHED)")
plt.savefig('C:\\Users\\edwar\\Documents\\GitHub\\python_summer2022\\HW\\HW4_plot1.pdf')



# UNSCALED SMOOTHED graph:

x1 = range(2, N)
x2 = range(2, N)
## Define y-axis: time.
## SMOOTHED using a gaussian filter.
y1smoothed = gaussian_filter1d(bubble_simtime, sigma=2)
y2smoothed = gaussian_filter1d(counting_simtime, sigma=2)
# Actually plot the data connecting with lines.
plt.plot(x1, y1smoothed) # Bubble lines
plt.plot(x2, y2smoothed) # counting lines 
# labels, titles, legend, etc.
plt.legend(["Bubble Sort\n(Quadratic Time)", "Counting Sort\n(Linear Time)"])
plt.ylabel("Run Time (Seconds)")
plt.xlabel("Size of Input List")
plt.title("How Algorithms Effect Runtime\n(UNSCALED, SMOOTHED)")
plt.savefig('C:\\Users\\edwar\\Documents\\GitHub\\python_summer2022\\HW\\HW4_plot2.pdf')


# SCALED NOT SMOOTHED graph.

## Define x-axis (# elements in list).
x1 = range(2, N)
x2 = range(2, N)
## Define y-axis: time.
y1 = bubble_simtime_scaled # bubble sort.
y2 = counting_simtime_scaled # counting sort.
# Actually plot the data connecting with lines.
plt.plot(x1, y1) # Bubble lines
plt.plot(x2, y2) # counting lines 
# labels, titles, legend, etc.
plt.legend(["Bubble Sort\n(Quadratic Time)", "Counting Sort\n(Linear Time)"])
plt.ylabel("Run Time\n(Bubble: 1/10 Sec, Counting: 1/100 Sec)")
plt.xlabel("Size of Input List")
plt.title("How Algorithms Effect Runtime\n(UNSCALED, UNSMOOTHED)")
plt.savefig('C:\\Users\\edwar\\Documents\\GitHub\\python_summer2022\\HW\\HW4_plot3.pdf')


# SCALED SMOOTHED graph.

x1 = range(2, N)
x2 = range(2, N)
## Define y-axis: time.
## SMOOTHED using a gaussian filter.
y1smoothed = gaussian_filter1d(bubble_simtime_scaled, sigma=2)
y2smoothed = gaussian_filter1d(counting_simtime_scaled, sigma=2)
# Actually plot the data connecting with lines.
plt.plot(x1, y1smoothed) # Bubble lines
plt.plot(x2, y2smoothed) # counting lines 
# labels, titles, legend, etc.
plt.legend(["Bubble Sort\n(Quadratic Time)", "Counting Sort\n(Linear Time)"])
plt.ylabel("Run Time\n(Bubble: 1/10 Sec, Counting: 1/100 Sec)")
plt.xlabel("Size of Input List")
plt.title("How Algorithms Effect Runtime\n(UNSCALED, SMOOTHED)")
plt.savefig('C:\\Users\\edwar\\Documents\\GitHub\\python_summer2022\\HW\\HW4_plot4.pdf')

