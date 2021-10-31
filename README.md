### Finding the maximum element with different classes of algorithmic approaches

The webpage below describes how to solve the problem of finding 
the maximum value in an array, illustrating different approaches

- brute force

For index i, test if A[i] is greater than or equal to every element in the array. When you find such an A[i], return it. For this algorithm, T(n) = n*Theta(n) = Theta(n2) if implemented in the most natural way.

- divide and conquer

If A has only one element, return it. Otherwise, let m1 be the maximum of A[1]..A[n/2]. Let m2 be the maximum of A[n/2+1]..A[n]. Return the larger of m1 and m2. The running time is given by T(n) = 2T(n/2) + Theta(1) = Theta(n).

- decrease and conquer

If A has only one element, return it. Otherwise, let m be the maximum of A[2]..A[n]. Return the larger of A[0] and m. Now the running time is given by T(n) = T(n-1) + Theta(1) = Sigmai=1 to n Theta(1) = Theta(n).

- transform and conquer

Sort the array, then return A[n]. Using an optimal comparison-based sort, this takes Theta(n log n) + Theta(1) = Theta(n log n) time. The advantage of this approach is that you probably don't have to code up the sort.

- use space

Insert all elements into a balanced binary search tree, then return the rightmost element. Cost is Theta(n log n) to do n insertions, plus Theta(log n) to find the rightmost element, for a total of Theta(n log n). Sorting is equivalent and probably easier.

- dynamic programming

Create an auxiliary array B with indices 1 to n. Set B[1] = A[1]. As i goes from 2 to n, set B[i] to the larger of B[i-1] and A[i]. Return B[n]. Cost: Theta(n).

- greedy method

Let max = A[1]. For each element A[i] in A[2..n], if A[i] > max, set max = A[i]. Return the final value of max. Cost: Theta(n); this algorithm is pretty much identical to the previous one.


source: https://www.cs.yale.edu/homes/aspnes/pinewiki/AlgorithmDesignTechniques.html
