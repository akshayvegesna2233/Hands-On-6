To mathematically derive the average runtime complexity of the non-random pivot variant of quicksort, it is essential to evaluate the anticipated number of comparisons conducted during the partitioning phase. Let us proceed methodically, step by step:
Initially, let us denote T(n) as the anticipated number of comparisons required for quicksort on an array including n entries.
In the non-random pivot variant, a predetermined place for the pivot is usually selected, such as the first or last element. Let us presume that we consistently select the final element as the pivot.
The crucial discovery is that the efficacy of quicksort is contingent upon the pivot's ability to partition the array effectively. We anticipate that the pivot will approximately bisect the array.
In an array of n elements, the pivot can be any of the n elements with equal probability (1/n). Let us examine the outcomes for each potential pivot position:
If the pivot is the minimal element (with a probability of 1/n), we perform n-1 comparisons and thereafter recurse on n-1 elements.
When the pivot is the second smallest (with a probability of 1/n), we perform n-1 comparisons and thereafter recurse on 1 and n-2 elements.
If the pivot is the largest element (with a probability of 1/n), we perform n-1 comparisons and thereafter recurse on n-1 elements.
This can be mathematically stated as:
T(n) = (n-1) + (1/n) * [T(0) + T(n-1) + T(1) + T(n-2) + ... + T(n-1) + T(0)]
(n-1) denotes the comparisons conducted throughout the partitioning process.
Simplification:
T(n) = (n-1) + (2/n) * [T(0) + T(1) + ... + T(n-1)]
Multiply both sides by n.
nT(n) = n(n - 1) + 2T(0) + T(1) + ... + T(n-1)
Let us now examine T(n-1):
(n-1)T(n-1) = (n-1)(n-2) + 2T(0) + T(1) + ... + T(n-2)
Subtracting these equations yields:
nT(n) - (n - 1)T(n-1) = 2n - 2 + 2T(n-1)
Reorganizing: nT(n) = (n + 1)T(n-1) + 2n - 2
Division by n(n+1):
T(n)/(n+1) = T(n-1)/n + 2/(n+1) - 2/n(n+1)
This constitutes a recurrence relation. Summing this from 2 to n results in the cancellation of most terms, yielding:
T(n)/(n+1) - T(1)/2 = 2(Hn - 1) - 2/n + 2/(n+1)
Hn denotes the nth harmonic number.
Determining T(n):
T(n) = 2(n+1)(Hn - 1) - \frac{2(n+1)}{n} + 2 - (n+1)T(1)/2
It is established that Hn = ln(n) + γ, where γ represents Euler's constant. T(n) = 2n ln(n) + O(n)
Consequently, the average-case time complexity of non-random pivot quicksort is O(n log n)