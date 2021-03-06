from random import choice

class RandomWalk:
    '''class to generate random walk'''

    def __init__(self, num_points=5000):
        self.num_points = num_points

        #start walk at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''calculate all points in the walk'''

        #repeat untill we hit required lenght
        while len(self.x_values)<self.num_points:
            #decide direction and how far to go
            x_step = self._get_step()
            y_step = self._get_step()

            #reject staps that go nowhere
            if x_step == 0 and y_step ==0:
                continue

            #get new position and add it to lists
            x = self.x_values[-1]+x_step
            y = self.y_values[-1]+y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def _get_step(self):
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return distance * direction
