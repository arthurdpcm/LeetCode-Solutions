# This is a famous problem where you receive an integer array and you must
# return the pair indexes which the sum between them is equal to the target.

def TwoSum(nums, target):
  # The first option of most developers is to use a nested loop but it will have a complexity that isn't good O(n²).
  # In this file you'll find a solution with O(n) which is much better than the other.
  
  # Dictionary to store the index of the complement of a number
  complements_index = {}
  # enumerate return the index and the value in the current item.
  for i, num in enumerate(nums):
    # Calculate complement for the current number
    complement = target - num
    # Check if the complement is a number in the dictionary using a hash query that has O(1).
    if complement in complements_index:
      # If succeed return an array with the two indexes 
      return [complements_index[complement], i]
    # The dictionary has a key with the num and the value is your index in the array given nums.
    complements_index[num] = i
    
  # If in the end of the loop not find the pair, return an empty array  
  return []

sample = [2, 7, 9, 0]
target = 9

print(TwoSum(sample, target))