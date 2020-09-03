import cv2
import pandas as pd
from random import choices

LOCATION = {'entrance': (700, 850),
            'fruits': (400, 850),
            'spices': (400, 625),
            'dairy': (400, 375),
            'drinks': (400, 150),
            'checkout': (700, 400)}

COLOR = {1: (212, 38, 167),
         2: (222, 30, 78),
         3: (169, 74, 37),
         4: (222, 165, 30),
         5: (178, 212, 29),
         6: (205, 114, 255)}

##### TEMPORARY FOR INPUTTING TRANSITION MATRIX.
## TO DO -- change into class?

MATRIX = pd.read_csv('supermarket_transitions.csv', index_col=0).T.to_dict()


class Location:
    history = []

    def __init__(self):
        ...

    def next_loc(self, current_loc, probabilities):
        '''
        MCMC simulation of customer behaviour
        current_loc: where is customer at start
        probabilities:
        '''
        probabilities = MATRIX[self.current_loc]
        while self.current_loc != 'checkout':
            self.current_loc = choices(self.current_loc, probabilities)[0]
            history.append(self.current_loc)


class Customer:

    def __init__(self, x=850, y=700, name='entrance'):
        self.x = x
        self.y = y
        self.name = name

    def draw(self, frame):
        frame[self.y:self.y+20, self.x:self.x+20] = self.color

    def move(self):
        """moves depending on next location"""
        ...

    def __repr__(self):
        return f"customer at {self.x}/{self.y}"


c1 = Customer(Location(), COLOR[1])



market = cv2.imread('market.png')

while True:
    frame = market.copy()

    c1.move()
    c1.draw(frame)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
