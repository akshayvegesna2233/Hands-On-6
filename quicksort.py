import random
import time
import matplotlib.pyplot as plt
import statistics

def quicksort_fixed_pivot(elements):
    """
    Quicksort implementation using a fixed pivot (middle element).
    """
    if len(elements) <= 1:
        return elements
    pivot = elements[len(elements) // 2]
    left = [x for x in elements if x < pivot]
    center = [x for x in elements if x == pivot]
    right = [x for x in elements if x > pivot]
    return quicksort_fixed_pivot(left) + center + quicksort_fixed_pivot(right)

def quicksort_random_pivot(elements):
    """
    Quicksort implementation using a random pivot.
    """
    if len(elements) <= 1:
        return elements
    pivot = random.choice(elements)
    left = [x for x in elements if x < pivot]
    center = [x for x in elements if x == pivot]
    right = [x for x in elements if x > pivot]
    return quicksort_random_pivot(left) + center + quicksort_random_pivot(right)

def evaluate_sort_performance(sort_function, input_sets, repetitions=3):
    """
    Evaluate the performance of a sorting algorithm over multiple repetitions.
    """
    execution_times = []
    for input_set in input_sets:
        trial_times = []
        for _ in range(repetitions):
            start_time = time.perf_counter()
            sort_function(input_set.copy())  # Use a copy to maintain original input set
            end_time = time.perf_counter()
            trial_times.append(end_time - start_time)
        execution_times.append(statistics.median(trial_times))
    return execution_times

# Experiment parameters
MAXIMUM_SET_SIZE = 250
SET_SIZES = list(range(1, MAXIMUM_SET_SIZE + 1))

# Generate input sets
best_case_data = [list(range(1, n + 1)) for n in SET_SIZES]
worst_case_data = [list(range(n, 0, -1)) for n in SET_SIZES]
average_case_data = [random.sample(range(1, n + 1), n) for n in SET_SIZES]

# Prepare the visualization
plt.figure(figsize=(14, 6))

# Visualize fixed pivot quicksort performance
plt.subplot(1, 2, 1)
plt.plot(SET_SIZES, evaluate_sort_performance(quicksort_fixed_pivot, best_case_data), label='Best Case')
plt.plot(SET_SIZES, evaluate_sort_performance(quicksort_fixed_pivot, worst_case_data), label='Worst Case')
plt.plot(SET_SIZES, evaluate_sort_performance(quicksort_fixed_pivot, average_case_data), label='Average Case')
plt.xlabel('Input Set Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Fixed Pivot Quicksort Performance')
plt.legend()

# Visualize random pivot quicksort performance
plt.subplot(1, 2, 2)
plt.plot(SET_SIZES, evaluate_sort_performance(quicksort_random_pivot, best_case_data), label='Best Case')
plt.plot(SET_SIZES, evaluate_sort_performance(quicksort_random_pivot, worst_case_data), label='Worst Case')
plt.plot(SET_SIZES, evaluate_sort_performance(quicksort_random_pivot, average_case_data), label='Average Case')
plt.xlabel('Input Set Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Random Pivot Quicksort Performance')
plt.legend()

plt.tight_layout()
plt.show()