from typing import Iterator, Tuple

#  function returns an iterator where each item is a tuple.
def zip_simple() -> Iterator[Tuple]:
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    return zip(list1, list2)

result = zip_simple() 
print(result) # This will print a zip object, which is an iterator
print(list(result)) # Convert the zip object to a list to see the pairs
# For example, if the function combines two lists [1, 2, 3] and ['a', 'b', 'c'], 
# the iterator will yield tuples like (1, 'a'), (2, 'b'), (3, 'c').