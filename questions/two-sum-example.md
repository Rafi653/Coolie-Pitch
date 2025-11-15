# Two Sum

**Difficulty**: Easy
**Company**: Google, Amazon, Meta
**Topic**: Arrays, Hash Tables

## Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

## Solution Approach

### Approach 1: Hash Map (Optimal)
1. Use a hash map to store numbers and their indices
2. For each number, check if `target - num` exists in the map
3. If found, return the indices
4. Otherwise, add current number to map

## Code

```python
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

## Complexity
- Time: O(n) - single pass through array
- Space: O(n) - hash map storage

## Key Insights
- Hash map provides O(1) lookup time
- Store indices, not just values
- One-pass solution is possible
- Consider edge cases: empty array, no solution

## Similar Problems
- Three Sum
- Four Sum
- Two Sum II (sorted array)
