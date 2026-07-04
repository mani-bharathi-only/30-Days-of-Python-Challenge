#Super class

class Shape:
    def __init__(self,color,filled):
        self.color=color
        self.filled=filled
        
    
class Square(Shape):
    def __init__(self,color,filled,size):
        super().__init__(color,filled)
        self.size=size

square=Square("Blue","True",21)
print(square.color)
print(square.filled)
print(square.size)

