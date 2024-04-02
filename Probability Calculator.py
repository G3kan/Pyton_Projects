import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            for i in range(count):
                self.contents.append(color)

    def draw(self, number):
        draw_list = []
        copy_list = copy.deepcopy(self.contents) 
        for i in range(min(number, len(copy_list))):
            random_item = random.choice(copy_list)
            copy_list.remove(random_item)
            draw_list.append(random_item)
        return draw_list
               

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_successes = 0
    for _ in range(num_experiments):
        drawn_balls = hat.draw(num_balls_drawn)
        drawn_balls_count = {}
        for ball in set(drawn_balls):
            drawn_balls_count[ball] = drawn_balls.count(ball)
        success = True
        for ball, count in expected_balls.items():
            if drawn_balls_count.get(ball, 0) < count:
                success = False
                break
        if success:
            num_successes += 1
    return num_successes / num_experiments



hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)