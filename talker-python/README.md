Buy Sell Stock
Brute Force O(N2)
Greedy Solution
l = r we would want to buy at the lowest

Shortest Word Distance 2
2 Key and 1 scale related scale Optimizations in Your WordDistance Implementation:
We are precomputing the list of indices so the lookup is O(1) and to find the shortest distance we are traversing the array once - O(N)
If you expect millions of shortest() queries between the same word pairs, you could cache the results using a dictionary or functools.lru_cache (if you refactor).
Pattern - Prefix Sum 
Prefix Sum in 4 minutes | LeetCode Pattern
Cumulative sum from start of array to given index
How?
prefix[0] = arr[0]
prefix[i] = prefix[i-1] + arr[i] NOTE - i =1…arr.length
Memory constraint - arr[i] = arr[i-1] + arr[i]
When?
Range Sum Queries 
Compute Sum of  elements between two indices frequently [3,4,5,7,9] -> i…..j
Subarray Sum Problems
Find or count the number of subarrays that add upto a specific value 





Python for Coding Interviews - Everything you need to Know
Python is dynamically typed language
Type checking happens at runtime: The type of a variable is determined when the code is executed, not during compilation.
You don't declare variable types: You don't need to explicitly tell Python what type of data a variable will hold (e.g., int x; or string name;). You simply assign a value, and Python infers its type.
Variable types can change: A variable can hold an integer at one point and then be reassigned to hold a string or a list later in the program.
This dynamic typing offers flexibility and can make Python code quicker to write, but it also means that type-related errors might not be caught until the program is running.
This one main tradeoffs of dynamically typed languages like Python. Let's look at an example in Python where a type-related error might go unnoticed until runtime, and then see how Go (Golang) addresses this with its static typing.


Why hashmap keys are immutable?
HashMap keys are required to be immutable to ensure the integrity, reliability, and performance of the map. This requirement is rooted in how hash-based collections work.
map computes the key’s hash code
map again computes the hash code of the key you provide and looks in the corresponding bucket.
Consistency: Immutable keys guarantee that the hash code and equality remain constant throughout the key's lifetime in the map, ensuring reliable storage and retrieval
Thread Safety: Immutable objects are inherently thread-safe, which is beneficial if the map is accessed by multiple threads
If immutable, the object's hashcode won't change and it allows caching the hashcode of different keys which makes the overall retrieval process very fast.
Best Practice: Common key types like String, Integer, and other wrapper classes are immutable for this reason





