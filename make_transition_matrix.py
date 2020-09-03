'''
code to create transition matrix for supermarket simulation

takes cleaned data from all days at the supermarket

returns CSV with transition probabilities
'''

import pandas as pd

INPUT = pd.read_csv('supermarket_data/supermarket_all.csv', index_col=0)

def make_transition_matrix(input):
    matrix = pd.crosstab(INPUT['previous'], INPUT['location'], normalize=0)
    matrix['entrance'] = (0.0,0.0,0.0,0.0,0.0)
    checkout_row = pd.Series(data={'checkout':1.0, 'dairy':0.0, 'drinks':0.0, 'fruit':0.0, 'spices':0.0, 'entrance':0.0}, name='checkout')
    matrix = matrix.append(checkout_row, ignore_index=False)
    matrix = matrix.reindex(sorted(matrix.columns), axis=1)
    matrix = matrix.reindex(sorted(matrix.index), axis=0)
    return matrix

if __name__ == '__main__':
    matrix = make_transition_matrix(INPUT)
    matrix.to_csv('supermarket_transitions.csv')
