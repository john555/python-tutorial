class Square:
  def show(self):
    print ("Square")

class Circle:
  def show(self):
    print ("Circle")

def render(shape):
  shape.show()

render(Square())
render(Circle())
