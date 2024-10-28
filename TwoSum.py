'''
https://www.techiedelight.com/?problem=TwoSum
Given an unsorted integer array, find a pair with the given sum in it.

• Each input can have multiple solutions. The output should match with either one of them.

Input : nums[] = [8, 7, 2, 5, 3, 1], target = 10
Output: (8, 2) or (7, 3)

• The solution can return pair in any order. If no pair with the given sum exists, the solution should return an empty tuple.

Input : nums[] = [5, 2, 6, 8, 1, 9], target = 12
Output: ()

'''
from typing import List, Tuple
import time

class Solution:
	def findPair(self, nums: List[int], target: int) -> Tuple[int]:
            for num in nums:
                counter = 0
                i = num
                for num in nums:
                    if i == num:
                        counter = counter + 1
                        if counter > 1:
                            if i+i == target:
                                return(i,i)
                    elif i + num == target:
                        return(i,num)
                    elif i + num != target:
                        pass
                    else:
                        pass
            return(())

# Testing the function
if __name__ == "__main__":
    sol = Solution()

    #Case 1
    print('case1')
    nums = [8, 7, 2, 5, 3, 1]
    target = 10
    start_time = time.time()
    print(sol.findPair(nums, target))  # Output should be (8, 2) or (7, 3)
    end_time = time.time()
    print("runtime: ", end_time-start_time)

    #Case 2
    print('case2')
    nums = [5, 2, 6, 8, 1, 9]
    target = 12
    start_time = time.time() 
    print(sol.findPair(nums, target))  # Output should be (8, 2) or (7, 3)
    end_time = time.time() 
    print("runtime: ", end_time-start_time)

    #Case 3
    print('case3')
    nums = [0, 1, 1, 8, 1, 9]
    target = 2
    start_time = time.time()
    print(sol.findPair(nums, target))  # Output should be (8, 2) or (7, 3)
    end_time = time.time()
    print("runtime: ", end_time-start_time)

    #Case 3
    #nums = range[0,101]
    #target = 22
    #start_time = time.time() 
    #print(sol.findPair(nums, target))  # Output should be (8, 2) or (7, 3)
    #end_time = time.time()