"""This file contains my solutions to Leetcode problem 131."""


class Solution:
    def partition(self, string: str) -> List[List[str]]:
        if not string:
            return [""]
        palindrome_partitions = []
        current_partition = []
        self.generate_partitions(
            string,
            0,
            current_partition,
            palindrome_partitions
        )
        return palindrome_partitions
    
    def generate_partitions(self, string, start, current, partitions):
        if start == len(string):
            partitions.append(current.copy())
        else:
            for end in range(start, len(string)):
                if self.is_palindrome(string, start, end):
                    current.append(string[start: end + 1])
                    self.generate_partitions(
                        string,
                        end + 1,
                        current,
                        partitions
                    )
                    current.pop()
    
    def is_palindrome(self, string, start, end):
        while start < end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1
        return True



class Solution:
    def partition(self, string: str) -> List[List[str]]:
        if not string:
            return [""]
        is_palindrome = [
            [False for j in range(len(string))] 
            for i in range(len(string))
        ]
        palindrome_partitions = []
        current_partition = []
        self.generate_partitions(
            string, 0, current_partition, palindrome_partitions, is_palindrome
        )
        return palindrome_partitions
    
    def generate_partitions(
        self, string, start, current, partitions, is_palindrome
    ):
        if start == len(string):
            partitions.append(current.copy())
        else:
            for end in range(start, len(string)):
                self.update_is_palindrome(is_palindrome, string, start, end)
                if is_palindrome[start][end]:
                    current.append(string[start: end + 1])
                    self.generate_partitions(
                        string,
                        end + 1,
                        current,
                        partitions,
                        is_palindrome
                    )
                    current.pop()
        
    def update_is_palindrome(self, is_palindrome, string, start, end):
        if (
            string[start] == string[end] 
            and (end - start <= 2 or is_palindrome[start + 1][end - 1])
        ):
            is_palindrome[start][end] = True
  
                
    
   