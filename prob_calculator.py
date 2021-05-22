import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    self.contents = list()
    for color, number in kwargs.items():
      for i in range(number):
        self.contents.append(color) 

  def draw(self, quant):
    balls_drawn = list()
    if quant >= len(self.contents):
      return self.contents
    for i in range(quant):
      ball = self.contents.pop(random.randint(0,len(self.contents)-1))
      balls_drawn.append(ball)
    return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0

  for i in range(num_experiments):
    ext_hat = copy.deepcopy(hat)
    draw = ext_hat.draw(num_balls_drawn) 
    count_colour = 0  

    for i in expected_balls.keys():
      if draw.count(i) >= expected_balls[i]:
        count_colour += 1 

    if count_colour == len(expected_balls):
      count += 1

  return count/num_experiments
