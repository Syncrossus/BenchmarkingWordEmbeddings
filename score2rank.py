import numpy as np


def score2rank(m):
    """ args:
            - m, a numpy matrix with 2 columns the 2nd of which should be numeric
        returns:
            - m with the second column's numbers switched for ranks
        example:
            m = [[3,5],    return = [[3,2],
                 [4,1],              [4,5],
                 [3,3],              [3,3],
                 [8,7],              [8,1],
                 [9,2]]              [9,4]]
    """
    m[np.argsort(m[:, 1], axis=0), 1] = [[i] for i in range(m.shape[0], 0, -1)]
    return m
