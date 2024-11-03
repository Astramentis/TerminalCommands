from typing import List, Tuple
import time

class Solution:
	def rearrange(self, nums: List[int]) -> None:
            try:
                counter = 0
                new_nums = []
                zeroes = 0
                for i in nums:              
                    counter += 1
                    if i != 0:
                       new_nums.append(i)
                    if i == 0:
                        zeroes += 1
            finally:
                for i in range(0, zeroes):
                    new_nums.append(0)
                print("finished: ", new_nums)
                nums = new_nums
                return(nums)

# Testing the function
if __name__ == "__main__":
    sol = Solution()

    #Case 1
    nums = [6, 0, 8, 2, 3, 0, 4, 0, 1]
    target = [6, 8, 2, 3, 4, 1, 0, 0, 0]
    print('case 1... ', nums)
    print()
    start_time = time.time()
    print(sol.rearrange(nums))
    end_time = time.time()
    #print("runtime: ", end_time-start_time)
'''
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
    print("runtime: ", end_time-start_time)'''