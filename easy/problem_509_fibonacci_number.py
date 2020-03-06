"""Below are my solutions to Leetcode problem 509: Fibonacci Number."""

#General recursive solution
class Solution:
    def fib(self, N: int) -> int:
        if N < 2:
            return N
        return self.fib(N - 1) + self.fib(N - 2)


#Overall time complexity: O(2 ^ n)
#Each call to fib(N) makes two more calls to the same function. Each of these two calls
#makes two calls each, and so on and so forth. This leads to an exponential
#number of function calls as the depth of the recursion calls approaches N.

#Overall space complexity: O(n)
#Explanation: You need space proportional to N to store the function calls on the
#function call stack.


#top down solution using memoization
class Solution:    
    def fib(self, N: int) -> int:
        cache = {}
        def calculate_fib(N, cache):
            if N in cache:
                return cache[N]
            if N < 2:
                result = N
            else:
                result = calculate_fib(N - 1, cache) + calculate_fib(N - 2, cache)
            cache[N] = result
            return cache[N]
        return calculate_fib(N, cache)
        

#Overall time complexity: O(n)
#Explanation: Due to caching the compuations of each function call, we end up
#making only n calls to the inner function, leading to a time complexity of O(n).

#Overall space complexity: O(n)
#Explanation: You need space proportional to N to store the function calls on the
#function call stack. You also store the values of all "n" function calls in the cache
#so that makes the space complexity O(2n). But, since we drop coefficients, this becomes O(n)



#bottom up solution
class Solution:    
    def fib(self, N: int) -> int:
        sequence = [0, 1]
        if N < 2:
            return N
        for index in range(2, N + 1):
            sequence.append(sequence[index - 1] + sequence[index - 2])
        return sequence[-1]


#Overall time complexity: O(n)
#Explanation: You perform n - 1 iterations to build your solution, making the time
#complexity O(n - 1). But since we drop constant in Big O, this becomes O(n)

#Overall space complexity: O(n)
#Explanation: This solution requires you to build a list of N + 1 fibonacci numbers in
#order to find your answer, making the space complexity O(n + 1). But, since we
#drop constant for Big O, this is O(n)
