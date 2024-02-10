import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)

    def draw(self, nr):
        if nr >= len(self.contents):
            return self.contents
        result = []
        for _ in range(nr):
            item = random.choice(self.contents)
            self.contents.remove(item)
            result.append(item)
        return result
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        ok = True
        drawn_balls = hat_copy.draw(num_balls_drawn)
        for color, value in expected_balls.items():
            if drawn_balls.count(color) < value:
                ok = False
                break
        if ok:
            success += 1
            
    return success / num_experiments