'''
https://www.techiedelight.com/?problem=SortBinaryArray
Given a binary array, in-place sort it in linear time and constant space. The output should contain all zeroes, followed by all ones.

Input : [1, 0, 1, 0, 1, 0, 0, 1]
Output: [0, 0, 0, 0, 1, 1, 1, 1]

Input : [1, 1]
Output: [1, 1]

'''
from typing import List, Tuple
import time

class Solution:
	def sortArray(self, nums: List[int]) -> None:
		nums.sort()
		return(nums)

if __name__ == "__main__":
    sol = Solution()

    #Case 1
    print('case 1')
    nums = [1, 0, 1, 0, 1, 0, 0, 1]
    target = [0, 0, 0, 0, 1, 1, 1, 1]
    start_time = time.time()
    print(sol.sortArray(nums))   
    end_time = time.time()
    print("runtime: ", end_time-start_time)