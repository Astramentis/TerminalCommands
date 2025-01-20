'''

Given an integer array, find the maximum sum among all its non-contiguous subarrays

Input : [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The maximum sum subarray is [4, -1, 2, 1]

Input : [-7, -3, -2, -4]
Output: -2
Explanation: The maximum sum subarray is [-2]

Input : [-2, 2, -1, 2, 1, 6, -10, 6, 4, -8]
Output: 10
Explanation: The maximum sum subarray is [2, -1, 2, 1, 6] or [6, 4] or [2, -1, 2, 1, 6, -10, 6, 4]

'''
from typing import List, Tuple
import time

class Solution:
    def findMaxSubarraySum(self, nums: List[int]) -> int:
        positive = []
        index = 0
        index_2 = 0
        valmax = 0
        try:
            for num in nums:
                index_2 = index-1
                num2 = nums[index_2]
                index += 2
                if num > valmax:
                    valmax = num
                if num + num2 > 0:
                    print('>0 ', (num,num2))
                    positive.append((num,num2))
        except Exception as e:
            print(e)
        finally:
            print(positive)
            b = 0
            for i in positive[b]:
                print(i , "in the positive")
                b+1
                #p1 = i[0]
                #p2 = i[1]
                #value = sum(p1,p2)
                pass
            return(6)


if __name__ == "__main__":
    sol = Solution()
    #Case 1
    print("Case 1:")
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    target = [6] #REMEMBER TO TURN TEST CASE INTO ACTUAL LIST OF TUPLES
    start_time = time.time()
    solution = sol.findMaxSubarraySum(nums)
    end_time = time.time()
    print("runtime:  ", end_time-start_time)
    #print((solution[0:len(solution)]))  # Return full solutions
    for i in target:
        if solution in target:
            print("Test 1 successful, solution is:", (solution))
            print("\n")
            break
    else:
        print("Test failed.", "Solutions: ", target)
        print("invalid solution", (solution))  # Return full solutions
        print("\n")





'''
if __name__ == "__main__":
    sol = Solution()
    #Case 1
    print("Case 1:")
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    target = [(6)] #REMEMBER TO TURN TEST CASE INTO ACTUAL LIST OF TUPLES
    start_time = time.time()
    solution = sol.findMaxSubarraySum(nums)  # Output should be (-10, -3) or (-3, -10) or (5, 6) or (6, 5)
    end_time = time.time()
    print("runtime:  ", end_time-start_time)
    #print((solution[0:len(solution)]))  # Return full solutions
    for i in target:
        if solution in target:
            print("Test 1 successful, solution is:", (solution[0:len(solution)]))
            print("\n")
            break
    else:
        
        print("Test failed.", "Solutions: ", target)
        print("invalid solution", (solution[0:len(solution)]))  # Return full solutions
        print("\n")

    #Case 2
    print("Case 2:")
    nums = [-7, -3, -2, -4]
    target = [-2]
    start_time = time.time()
    solution = sol.findMaxSubarraySum(nums)  # Output should be (8, 2) or (7, 3)
    end_time = time.time()
    print("runtime:  ", end_time-start_time)
    for i in target:
        if solution in target:
            print("Test 2 successful, solution is:", (solution[0:len(solution)]))
            print("\n")
            break
    else:
        print("Test failed")
        print((solution[0:len(solution)]))  # Return full solutions
        print("\n")

    #Case 3
    print("Case 3:")
    nums = [-2, 2, -1, 2, 1, 6, -10, 6, 4, -8]
    target = [10]
    start_time = time.time()
    solution = sol.findMaxSubarraySum(nums)  # Output should be ()
    end_time = time.time()
    print("runtime:  ", end_time-start_time)
    for i in target:
        if solution in target:
            print("Test 3 successful, solution is:", (solution[0:len(solution)]))
            print("\n")
            break
    else:
        print("Test failed")
        print((solution[0:len(solution)]))  # Return full solutions
        print("\n")
'''