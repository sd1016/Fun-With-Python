from collections import OrderedDict

# Declare an OrderedDict where keys are str and values are int
# Keys are strings, values are integers - Type hint / Type Annotation  saying od is an OrderedDict mapping str → int
od: OrderedDict[str, int] = OrderedDict({'a': 1, 'b': 2, 'c': 3})
print(od)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Move key 'a' to the end (acts like marking it as most recently used)
od.move_to_end('a')
print(od)  # Output: OrderedDict([('b', 2), ('c', 3), ('a', 1)])

# Move key 'c' to the beginning (least recently used)
od.move_to_end('c', last=False)
print(od)  # Output: OrderedDict([('c', 3), ('b', 2), ('a', 1)])

# Retrieve value associated with 'a' — no side effects on order
print(od.get('a'))  # Output: 1

# Pop the last inserted item (default behavior: LIFO)
print(od.popitem())  # Output: ('a', 1)

# Pop the first inserted item (FIFO behavior using last=False)
print(od.popitem(last=False))  # Output: ('c', 3)

# Order matters in OrderedDict; even if key-value pairs match,
# different key orders make two OrderedDicts unequal
od1: OrderedDict[str, int] = OrderedDict({'a': 1, 'b': 2})
od2: OrderedDict[str, int] = OrderedDict({'b': 2, 'a': 1})
print(od1 == od2)  # Output: False (order is different)

# Define a custom OrderedDict that reorders keys on update
class LUODict(OrderedDict):  # LUO = Last Updated OrderedDict
    def __setitem__(self, key: str, value: int) -> None:
        # Call the parent OrderedDict to actually set the value
        # super() gives us access to the parent class (OrderedDict) method
        super().__setitem__(key, value)
        # Move the key to the end to reflect it was "recently updated"
        self.move_to_end(key)

# Create an instance of LUODict with initial values
luo_dict: LUODict = LUODict({'a': 1, 'b': 2, 'c': 3})

# Update value for 'a' — also moves it to the end due to __setitem__ override
luo_dict['a'] = 111
print(luo_dict)  # Output: LUODict([('b', 2), ('c', 3), ('a', 111)])

# Update value for 'c' — now 'c' moves to the end
luo_dict['c'] = 5555
print(luo_dict)  # Output: LUODict([('b', 2), ('a', 111), ('c', 5555)])

# -------------------------------
# Interview Revision Highlights:
# -------------------------------
# - Type hinting with OrderedDict[str, int] improves clarity and static checking
# - popitem(last=False) is unique to OrderedDict and enables FIFO behavior
# - move_to_end(key, last=True|False) is useful for implementing LRU/MRU caches
# - super().__setitem__ allows overriding dict behavior while preserving core logic


# popitem(last=False) for FIFO: 
# The standard dict only offers popitem() which, 
# in Python 3.7+, removes the last inserted item (LIFO). 
# OrderedDict uniquely provides popitem(last=False) to efficiently remove the first inserted item (FIFO). 
# This is crucial for implementing things like LRU caches.

# move_to_end() for Reordering: OrderedDict has the move_to_end(key, last=True) method, 
# which allows you to easily move an existing key to either the end (making it "most recently used") or the beginning (making it "least recently used") 
# of the ordered dictionary. There's no direct equivalent for efficiently 
# reordering elements within a standard dict without recreating it.

# Variable Annotations
# age: int = 30                  # 'age' is an integer
# name: str = "Alice"            # 'name' is a string
# scores: list[int] = [90, 85]   # 'scores' is a list of integers (Python 3.9+)
