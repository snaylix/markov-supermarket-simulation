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

MATRIX = pd.read_csv('supermarket_transitions.csv', index_col=0)

POSS_STATES = ['entrance', 'dairy', 'fruit', 'spices', 'drinks', 'checkout']

COORDS = {'entrance': (700, 650, 855, 855),
'fruit': (800, 180, 900, 460),
'spices': (570, 180, 670, 460),
'dairy': (350, 180, 450, 460),
'drinks': (110, 180, 210, 460),
'checkout': (180, 670, 460, 740)
}

class Customer:

    def __init__(self, current_location='entrance'):
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.current_location = current_location

    def draw(self, frame):
        frame[self.y:self.y+20, self.x:self.x+20] = self.color


    def next_location(self):
        '''
        MCMC simulation of customer behaviour
        current_loc: where is customer at start
        probabilities: get these from the pre-defined transition matrix
        '''
        probabilities = MATRIX.loc[self.current_location]
        if self.current_location != 'checkout':
            self.current_location = choices(POSS_STATES, weights=probabilities)[0]

    def get_coords(self):
        self.x = randint(COORDS[str(self.current_location)][0], COORDS[str(self.current_location)][2])
        self.y = randint(COORDS[str(self.current_location)][1], COORDS[str(self.current_location)][3])

    def __repr__(self):
        return f"customer at {self.x}/{self.y}"


market = cv2.imread('market.png')

c1 = Customer()

while True:
    print('about to launch')
    frame = market.copy()

    print('making customer')
    c1.get_coords()
    c1.draw(frame)
    c1.next_location()

    cv2.imshow('frame', frame)

    time.sleep(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
