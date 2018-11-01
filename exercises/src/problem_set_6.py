# Prereqs: Computational Complexity, Searching and Sorting
# Problem Set 6

# Problem 1 - 1
# The ONLY thing we are interested in when designing programs is that it returns the correct answer.
# True or False

# Problem 1 - 2
# When determining asymptotic complexity, we discard all terms except for the one with the largest growth rate.
# True or False

# Problem 1 - 3
# Bisection search is an example of linear time complexity
# True or False

# Problem 1 - 4
# For large values of n, an algorithm that takes 20000n ^ 2 steps has better time complexity(takes less time) than one that takes 0.001n ^ 5 steps
# True or False

# Problem 2 - 1
# Indirection, as talked about in lecture, means you have to traverse the list more than once.
# True or False

# Problem 2 - 2
# The complexity of binary search on a sorted list of n items is O(log n).
# True or False

# Problem 2 - 3
# The worst case time complexity for selection sort is O(n**2).
# True or False

# Problem 2 - 4
# The base case for the recursive version of merge sort from lecture is checking ONLY for the list being empty.
# True or False


# Problem 3
# Describe each of the different orders of growth.


# Problem 4 - 1
# Consider the following Python procedure. Specify its order of growth.


# def modten(n):
#     return n % 10


# Problem 4 - 2
# Consider the following Python procedure. Specify its order of growth.


# def multlist(m, n):
#     '''
#     m is the multiplication factor
#     n is a list.
#     '''
#     result = []
#     for i in range(len(n)):
#         result.append(m * n[i])
#     return result


# Problem 4 - 3
# Consider the following Python procedure. Specify its order of growth.


# def foo(n):
#     if n <= 1:
#         return 1
#     return foo(n / 2) + 1


# Problem 4 - 4
# Consider the following Python procedure. Specify its order of growth.


# def recur(n):
#     if n <= 0:
#         return 1
#     else:
#         return n * recur(n - 1)


# Problem 4 - 5
# Consider the following Python procedure. Specify its order of growth.


# def baz(n):
#     for i in range(n):
#         for j in range(n):
#             print(i, j)


# Problem 5

# Here is code for linear search that uses the fact that a set of elements is sorted in increasing order:


# def search(L, e):
#     for i in range(len(L)):
#         if L[i] == e:
#             return True
#         if L[i] > e:
#             return False
#     return False


# Consider the following code, which is an alternative version of search.


# def newsearch(L, e):
#     size = len(L)
#     for i in range(size):
#         if L[size - i - 1] == e:
#             return True
#         if L[i] < e:
#             return False
#     return False


# Which of the following statements is correct? You may assume that each function is tested with a list L whose
#     elements are sorted in increasing order
#     for simplicity, assume L is a list of positive integers.

# search and newsearch return the same answers for all L and e.
# search and newsearch return the same answers provided L is non - empty.
# search and newsearch return the same answers provided L is non - empty and e is in L.
# search and newsearch never return the same answers.
# search and newsearch return the same answers for lists L of length 0, 1, or 2.


# Problem 6 - 1

# Answer the questions below based on the following sorting function. If it helps, you may paste the code in your
#     programming environment. Study the output to make sure you understand the way it sorts.


# def swapSort(L):
#     """ L is a list on integers """
#     print("Original L: ", L)
#     for i in range(len(L)):
#         for j in range(i + 1, len(L)):
#             if L[j] < L[i]:
#                 # the next line is a short
#                 # form for swap L[i] and L[j]
#                 L[j], L[i] = L[i], L[j]
#                 print(L)
#     print("Final L: ", L)


# Does this function sort the list in increasing or decreasing order? (items at lower indices being smaller means it sorts in increasing order, and vice versa)
# Increasing
# Decreasing


# Problem 6 - 2

# What is the worst case time complexity of swapSort? Consider different kinds of lists when the length of the list is large.
# O(n**2)
# O(n)
# O(log n)
# O(1)


# Problem 6 - 3

# If we make a small change to the line for j in range(i + 1, len(L)): such that the code becomes:


# def modSwapSort(L):
#     """ L is a list on integers """
#     print("Original L: ", L)
#     for i in range(len(L)):
#         for j in range(len(L)):
#             if L[j] < L[i]:
#                 # the next line is a short
#                 # form for swap L[i] and L[j]
#                 L[j], L[i] = L[i], L[j]
#                 print(L)
#     print("Final L: ", L)


# What happens to the behavior of swapSort with this new code?
# No change
# modSwapSort now orders the list in descending order for all lists.
# modSwapSort now orders the list in descending order for SOME lists but not all
# modSwapSort enters an infinite loop.


# Problem 6 - 4

# What happens to the time complexity of this modSwapSort?
# Best and worst cases stay the same.
# Worst case stays the same but best case changes.
# Best and worst cases change.
