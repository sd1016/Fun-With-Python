# Buy Sell Stock

### Brute Force O(N²)
- Greedy Solution: `l = r` we would want to buy at the lowest.

---

# Shortest Word Distance 2

### Key Optimizations in Your WordDistance Implementation:
1. **Precomputing Indices**: 
    - Lookup is O(1).
    - To find the shortest distance, traverse the array once - O(N).
2. **Caching Results**:
    - If you expect millions of `shortest()` queries between the same word pairs, cache the results using:
      - A dictionary.
      - `functools.lru_cache` (if refactored).

---

# Pattern - Prefix Sum

### Prefix Sum in 4 Minutes | LeetCode Pattern
- **Definition**: Cumulative sum from the start of the array to a given index.
- **How?**
  - `prefix[0] = arr[0]`
  - `prefix[i] = prefix[i-1] + arr[i]` (for `i = 1…arr.length`)
  - **Memory Constraint**: `arr[i] = arr[i-1] + arr[i]`
- **When?**
  - **Range Sum Queries**: Compute the sum of elements between two indices frequently.  
     Example: `[3, 4, 5, 7, 9] -> i…..j`
  - **Subarray Sum Problems**: Find or count the number of subarrays that add up to a specific value.

---

# Python for Coding Interviews - Everything You Need to Know

### Key Characteristics of Python:
1. **Dynamically Typed Language**:
    - Type checking happens at runtime.
    - Variable types are determined during execution, not compilation.
2. **No Variable Type Declaration**:
    - Python infers the type based on the assigned value.
3. **Variable Types Can Change**:
    - A variable can hold an integer at one point and later be reassigned to hold a string or a list.

### Tradeoffs:
- **Flexibility**: Makes Python code quicker to write.
- **Risk**: Type-related errors might not be caught until runtime.

### Example:
- Python's dynamic typing can lead to runtime errors.
- Go (Golang), with its static typing, addresses this by catching type-related errors at compile time.

---

# Why Are HashMap Keys Immutable?

### Reasons for Immutability:
1. **Consistency**:
    - Immutable keys ensure that the hash code and equality remain constant throughout the key's lifetime in the map.
2. **Thread Safety**:
    - Immutable objects are inherently thread-safe, beneficial for multi-threaded access.
3. **Performance**:
    - Immutable keys allow caching of hash codes, making retrieval faster.

### Best Practices:
- Common key types like `String`, `Integer`, and other wrapper classes are immutable for these reasons.

### How HashMap Works:
1. Computes the key’s hash code.
2. Uses the hash code to locate the corresponding bucket.
3. Ensures reliable storage and retrieval due to immutability.





### Source

This content is sourced from the following document:  
[Google Document Link](https://docs.google.com/document/d/1CeyAfQd4PCdCFaPmieTyOxE_J02NMUeF_LsPRmjFrUo/edit?tab=t.0)
