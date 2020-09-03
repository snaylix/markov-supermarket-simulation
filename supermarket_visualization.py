import cv2
import pandas as pd
from random import choices


##### TEMPORARY FOR INPUTTING TRANSITION MATRIX.
## TO DO -- change into class?

MATRIX = pd.read_csv('supermarket_transitions.csv', index_col=0).to_dict()

class Location:

    def __init__(self):
        ...

    def next_loc(self, current_loc, probabilities):
        '''
        MCMC simulation of customer behaviour
        current_loc: where is customer at start
        probabilities:
        '''
        self.current_loc = current_loc
        self.probabilities = MATRIX[self.current_loc]
        ...
        # next_loc =

class Customer:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


    def draw(self, frame):
        frame[self.x:self.x+20, self.y:self.y+20] = self.color

    def move(self):
        """moves depending on next location"""
        ...

    def __repr__(self):
        return f"customer at {self.x}/{self.y}"


locations = {'entrance': (700, 850),
             'fruits': (400, 850),
             'spices': (400, 625),
             'dairy': (400, 375),
             'drinks': (400, 150),
             'checkout': (700, 400)}

color = {1: (212, 38, 167),
         2: (222, 30, 78),
         3: (169, 74, 37),
         4: (222, 165, 30),
         5: (178, 212, 29),
         6: (205, 114, 255)}

c1 = Customer(locations['entrance'][0], locations['entrance'][1], color[1])
c2 = Customer(locations['fruits'][0], locations['fruits'][1], color[2])
c3 = Customer(locations['spices'][0], locations['spices'][1], color[3])
c4 = Customer(locations['dairy'][0], locations['dairy'][1], color[4])
c5 = Customer(locations['drinks'][0], locations['drinks'][1], color[5])
c6 = Customer(locations['checkout'][0], locations['checkout'][1], color[6])



market = cv2.imread('market.png')

while True:
    frame = market.copy()

    c1.move()
    c1.draw(frame)
    c2.move()
    c2.draw(frame)
    c3.move()
    c3.draw(frame)
    c4.move()
    c4.draw(frame)
    c5.move()
    c5.draw(frame)
    c6.move()
    c6.draw(frame)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
