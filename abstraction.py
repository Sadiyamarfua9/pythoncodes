from abc import ABC,abstractmethod
class shapes(ABC):
  @abstractmethod
  def sides(self,side):
    pass
class triangle(shapes):
  def sides(self,side):
    print(f"triangle has {side} sides")
class square(shapes):
  def sides(self,side):
    print(f"square has {side} sides")
class pentagon(shapes):
  def sides(self,side):
    print(f"pentagon has {side} sides")
class hexagon(shapes):
  def sides(self,side):
    print(f"hexagon has {side} sides")
s1=triangle()
s1.sides(3)
s2=square()
s2.sides(4)
s3=pentagon()
s3.sides(5)
s4=hexagon()
s4.sides(6)
