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

# MATRIX = pd.read_csv('supermarket_transitions.csv', index_col=0).T.to_dict()

MATRIX = pd.read_csv('supermarket_transitions.csv', index_col=0)

POSS_STATES = ['entrance', 'dairy', 'fruit', 'spices', 'drinks', 'checkout']

COORDS = {'entrance': (700, 650, 855, 855),
'fruit': (800, 180, 900, 460),
'spices': (570, 180, 670, 460),
'dairy': (350, 180, 450, 460),
'drinks': (110, 180, 210, 460),
'checkout': (180, 670, 460, 740)
}


# class Location:
#
#     # def __init__(self, y=700, x=850, current_location='entrance'):
#     def __init__(self, current_location='entrance'):
#         # self.x = x
#         # self.y = y
#         self.current_location = current_location
#
#     def next_location(self):
#         '''
#         MCMC simulation of customer behaviour
#         current_loc: where is customer at start
#         probabilities:
#         '''
#         # history = []
#         probabilities = MATRIX[self.current_location]
#         while self.current_location != 'checkout':
#             self.current_location = choices(self.current_location, probabilities)[0]
#             # history.append(self.current_location)
#         # return history
#
#     def get_coords(self, current_location):
#         self.x = randint(COORDS[str(current_location)][0], COORDS[str(current_location)][2])
#         self.y = randint(COORDS[str(current_location)][1], COORDS[str(current_location)][3])
#         # return self.x, self.y



class Customer:

    def __init__(self, current_location='entrance'):
    #def __init__(self, y=700, x=850, current_location='entrance'):
        # self.y = LOCATION[current_location][0]
        # self.x = LOCATION[current_location][1]
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.current_location = current_location

    def draw(self, frame):
        frame[self.y:self.y+20, self.x:self.x+20] = self.color

    # def move(self):
    #     """moves depending on next location"""
    #     # next = choices(['fruits', 'spices', 'dairy', 'drinks', 'checkout'])
    #     self.y = LOCATION[next[0]][0]
    #     self.x = LOCATION[next[0]][1]

    def next_location(self):
        '''
        MCMC simulation of customer behaviour
        current_loc: where is customer at start
        probabilities:
        '''
        # history = []
        probabilities = MATRIX.loc[self.current_location]
        # weights = [MATRIX.loc[self.current_location][x] for x in range(6)]
        if self.current_location != 'checkout':
            self.current_location = choices(POSS_STATES, weights=probabilities)[0]
            # print(f'and I just made a choice, so I am now in {self.current_location}')
            # history.append(self.current_location)
        # return history

    def get_coords(self):
        self.x = randint(COORDS[str(self.current_location)][0], COORDS[str(self.current_location)][2])
        self.y = randint(COORDS[str(self.current_location)][1], COORDS[str(self.current_location)][3])
        # return self.x, self.y

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
