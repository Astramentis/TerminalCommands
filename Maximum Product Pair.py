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
        next_largest = 0
        largest_num = 0
        largest_neg = 0
        next_largest_neg = 0
        #counter = 0
        #for i in nums:
            #compare = nums[counter]
        for i in nums:
            #if i == nums[0]:
                #pass
            if i < 0:
                print('negative found, ',i)
                if i < largest_neg:
                    next_largest_neg = largest_neg 
                    largest_neg = i
                elif i < next_largest_neg:
                    next_largest_neg = i
                else:
                    pass
            elif i > 0:
                print('positive found: ', i)
                if i > largest_num:
                    next_largest = largest_num
                    largest_num = i
                else:
                    pass    
            else:
                pass 
        max_positive = next_largest * largest_num
        max_negative = largest_neg * next_largest_neg
        print(max_negative, "max negative")
        print(max_positive, "max positive")

        if len(nums) <= 1:
            return(())
        #elif len(nums) == 2:
            #return((nums[0],nums[1]))
        elif max_positive > max_negative:
            return((next_largest, largest_num))
        elif max_negative > max_positive: 
            return((next_largest_neg,largest_neg))
        else:
            return((next_largest_neg,largest_neg))     

class Solution2: #this one is big shit
    def findPair(self, nums: List[int]) -> Tuple[int]:
        next_largest = nums[-1]
        largest_num = nums[0]
        #from_0 = abs(next_largest) + abs(largest_num)
        for i in nums:
            current = i
            for i in nums:
                if current == i:
                    #print(i,"break")
                    i = next_largest
                    break
                elif i > largest_num:
                    largest_num = i
                elif i > next_largest:
                    next_largest = i
                else:
                    pass
        if len(nums) <= 1:
            return(())
        if len(nums) <= 2:
            return((nums[0],nums[1]))
        return((next_largest,largest_num))

if __name__ == "__main__":
    sol = Solution()

    #Case 1
    print("Case 1:")
    nums = [-10, -3, 5, 6, -2]
    target = [(-10, -3),(-3, -10),(5, 6),(6, 5)] #REMEMBER TO TURN TEST CASE INTO ACTUAL LIST OF TUPLES
    start_time = time.time()
    solution = sol.findPair(nums)  # Output should be (-10, -3) or (-3, -10) or (5, 6) or (6, 5)
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
    nums = [-4, 3, 2, 7, -5]
    target = [(3, 7), (7, 3)]
    start_time = time.time()
    solution = sol.findPair(nums)  # Output should be (8, 2) or (7, 3)
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
    nums = [10, 3, -5, -6, 2]
    target = [(-6, -5) , (-5, -6) , (3, 10) , (10, 3)]
    start_time = time.time()
    solution = sol.findPair(nums)  # Output should be ()
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
