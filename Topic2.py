# Define the Rectangle class to represent a rectangle with length and width
class Rectangle:
    # Initialize with length and width as integers
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
    # Make the class iterable, yielding length and width as dictionaries
    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# Test the Rectangle class
if __name__ == "__main__":
    # Create a Rectangle instance
    rect = Rectangle(14, 31)
    
    # Iterate over the instance
    print("Iterating over rectangle:")
    for item in rect:
        print(item)
    
    # Show as list
    print("\nAs list:")
    print(list(rect))
