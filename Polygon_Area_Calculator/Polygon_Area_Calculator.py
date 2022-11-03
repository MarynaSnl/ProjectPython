import math
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        return
        
    def set_width(self, width):
        self.width = width
        return

    def set_height(self, height):
        self.height = height
        return
    
    def get_area(self):
        return self.width * self.height
                   
    def get_perimeter(self):               
        return (2 * self.width + 2 * self.height)
    
    def get_diagonal(self):                     
        return ((self.width ** 2 + self.height ** 2) ** 0.5)
                   
    def get_amount_inside(self, enother_rect):
        if enother_rect.width > self.width and enother_rect.height > self.height:
          return 0
        else:
          return math.floor(self.width/enother_rect.width) * math.floor(self.height/enother_rect.height)
    
    def get_picture(self): 
        if self.width > 50 or self.height > 50:
            return("Too big for picture.")
        ss = ('*'*self.width + '\n')*self.height
        return ss
                   
    def __str__(self):
        return (f"Rectangle(width={self.width}, height={self.height})")

class Square(Rectangle):
    def __init__(self,  height):
        super().__init__(self,  height)
        self.width = height
        self.height= height
        return
        
    def set_width(self, width):
        self.set_side( width)
        return

    def set_height(self, height):
        self.set_side( height)
        return
    
    def set_side(self, height):
        self.width = height
        self.height= height
        print("OK")
        return
        
    def __str__(self):
        return (f"Square(side={self.height})")