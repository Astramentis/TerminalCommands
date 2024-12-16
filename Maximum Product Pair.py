#https://www.techiedelight.com/?problem=MaximumProductPair

'''

Given an integer array, find a pair with the maximum product in it.

Each input can have multiple solutions. The output should match with either one of them.

Input : [-10, -3, 5, 6, -2]
Output: (-10, -3) or (-3, -10) or (5, 6) or (6, 5)

Input : [-4, 3, 2, 7, -5]
Output: (3, 7) or (7, 3)

If no pair exists, the solution should return an empty tuple.

Input : [1]
Output: ()

'''




from typing import List, Tuple
import time


class Solution:
    def findPair(self, nums: List[int]) -> Tuple[int]:
        next_largest = -999
        to_beat = -2**63
        largest_num = -999
        for i in nums:
            current = i
            print(i)
            for i in nums:
                if current == i:
                    break
                elif i > largest_num:
                    largest_num = i
                elif i > next_largest:
                    next_largest = i
                    to_beat = i
                    print(next_largest)
                else:
                    pass
        return((next_largest,largest_num))


if __name__ == "__main__":
    sol = Solution()

    #Case 1
    print("case 1 run:")
    nums = [-4, 3, 2, 7, -5]
    target = (3, 7) or (7, 3)
    start_time = time.time()
    print(sol.findPair(nums))  # Output should be (8, 2) or (7, 3)
    end_time = time.time()
    print("runtime: ", end_time-start_time)
'''
    #Case 2
    print('case 2 solution:', sol)
    nums = [-4, 3, 2, 7, -5]
    target = (3, 7) or (7, 3)
    start_time = time.time() 
    print(sol.findPair(nums, target))  # Output should be (8, 2) or (7, 3)
    end_time = time.time() 
    print("runtime: ", end_time-start_time)'''