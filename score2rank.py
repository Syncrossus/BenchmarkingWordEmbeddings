import numpy as np


def score2rank(m):
    """ args:
            - m, a numpy matrix with 2 columns the 2nd of which should be numeric
        returns:
            - m with the second column's numbers switched for ranks
        example:
            m = [[a,5],    return = [[a,2],
                 [b,1],              [b,5],
                 [c,3],              [c,3],
                 [d,7],              [d,1],
                 [e,2]]              [e,4]]
    """
    m[np.argsort(m[:, 1], axis=0), 1] = [[i] for i in range(m.shape[0], 0, -1)]
    return m
