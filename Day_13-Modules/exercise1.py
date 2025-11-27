
"""
Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
"""

numbers = [-4, -3, -2, -1, -1, -2, 0, 2, 4, 6]

def filter_negative_and_zero(nums: list[int]) -> list[int]:
    return [x for x in nums if x <= 0]

print(filter_negative_and_zero(numbers))
