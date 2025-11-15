# Hash Tables

## Overview
Hash tables (hash maps, dictionaries) are data structures that provide efficient key-value storage and retrieval.

## Key Concepts

### Time Complexity
- **Average Case**: O(1) for insert, delete, lookup
- **Worst Case**: O(n) when many collisions occur

### Hash Function
A function that maps keys to array indices:
```python
hash(key) % table_size = index
```

### Collision Resolution

1. **Chaining**: Store multiple values at same index using linked lists
2. **Open Addressing**: Find next available slot
   - Linear probing
   - Quadratic probing
   - Double hashing

## Common Use Cases

- Counting frequencies
- Storing unique elements
- Fast lookups (O(1))
- Caching and memoization
- Mapping relationships

## Python Implementation

```python
# Built-in dictionary
hash_map = {}
hash_map['key'] = 'value'

# Common operations
hash_map.get('key', default_value)
hash_map.pop('key')
'key' in hash_map  # Check existence
len(hash_map)
```

## Interview Tips

- Great for optimization (reducing time complexity)
- Consider using when you need fast lookups
- Watch out for hash collisions
- Understand space-time tradeoffs
- Remember: unordered in most implementations

## Common Patterns

1. **Two Sum Pattern**: Store complements
2. **Frequency Counter**: Count occurrences
3. **Group Anagrams**: Use sorted string as key
4. **LRU Cache**: Combine with doubly linked list

## Related Problems
- Two Sum
- Group Anagrams
- Valid Anagram
- First Unique Character
- LRU Cache
