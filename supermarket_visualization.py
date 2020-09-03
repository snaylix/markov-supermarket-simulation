import cv2
import pandas as pd
from random import choices, randint
import time

LOCATION = {'entrance': (700, 850),
            'fruits': (400, 850),
            'spices': (400, 625),
            'dairy': (400, 375),
            'drinks': (400, 150),
            'checkout': (700, 400)}

# TEMPORARY FOR INPUTTING TRANSITION MATRIX.
# TO DO -- change into class?

MATRIX = pd.read_csv('supermarket_transitions.csv', index_col=0).T.to_dict()


class Location:

    def __init__(self, y=700, x=850, current_location='entrance'):
        self.x = x
        self.y = y
        self.current_location = current_location

    def next_location(self):
        '''
        MCMC simulation of customer behaviour
        current_loc: where is customer at start
        probabilities:
        '''
        history = []
        probabilities = MATRIX[self.current_location]
        while self.current_location != 'checkout':
            self.current_location = choices(self.current_location, probabilities)[0]
            history.append(self.current_location)
        return history


class Customer:

    def __init__(self, y=700, x=850, current_location='entrance'):
        self.y = LOCATION[current_location][0]
        self.x = LOCATION[current_location][1]
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.current_location = current_location

    def draw(self, frame):
        frame[self.y:self.y+20, self.x:self.x+20] = self.color

    def move(self):
        """moves depending on next location"""
        next = choices(['fruits', 'spices', 'dairy', 'drinks', 'checkout'])
        self.y = LOCATION[next[0]][0]
        self.x = LOCATION[next[0]][1]

    def __repr__(self):
        return f"customer at {self.x}/{self.y}"


c1 = Customer()

market = cv2.imread('market.png')

while True:
    frame = market.copy()

    c1.move()
    c1.draw(frame)

    cv2.imshow('frame', frame)

    time.sleep(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
