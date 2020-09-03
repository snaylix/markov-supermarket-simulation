import cv2
import pandas as pd
from random import choices


##### TEMPORARY FOR INPUTTING TRANSITION MATRIX.
## TO DO -- change into class?

MATRIX = pd.read_csv('supermarket_transitions.csv', index_col=0).T.to_dict()

class Location:

    def __init__(self, x, y, current_loc='entrance'):
        self.x =
        self.y =
        self.current_loc = current_loc

    def next_loc(self):
        '''
        MCMC simulation of customer behaviour
        current_loc: where is customer at start
        probabilities:
        '''
        probabilities = MATRIX[self.current_loc]
        while self.current_loc != 'checkout':
            self.current_loc = choices(self.current_loc, probabilities)[0]




class Customer:

    def __init__(self, x=850, y=700, name='entrance'):
        self.x = x
        self.y = y
        self.name = name

    def get_next_target():
        if p = '1'


class Customer:

    def __init__(self, location, color):
        self.x = location.x
        self.y = location.y
        self.color = color


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
