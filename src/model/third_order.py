import numpy as np
# import pandas
# from scipy import stats
# from scipy.integrate import quad
# from haversine import haversine, Unit
# from pathlib import Path
# from random import sample
# import json

# from numpy.random import random 


def switch(i,j,k):
    if k == i:
        return j
    elif k == j:
        return i
    else:
        return k

class thirdOrder:
    def __init__(self, n): # n number of tracks
        self.dim = n
        self.prob_mat = np.zeros((self.dim, self.dim, self.dim, self.dim, self.dim, self.dim), dtype=float)

        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    self.prob_mat[i,i,j,j,k,k] = 1

    def update(self, i, j, p): #track_i and track_j exchange with probability p
        new_mat = np.zeros((self.dim, self.dim, self.dim, self.dim, self.dim, self.dim), dtype=float)
        for obj_1 in range(self.dim):
            for track_1 in range(self.dim):
                for obj_2 in range(self.dim):
                    for track_2 in range(self.dim):
                        for obj_3 in range(self.dim):
                            for track_3 in range(self.dim):
                                new_mat[obj_1, track_1, obj_2, track_2, obj_3, track_3] = (1-p) * self.prob_mat[obj_1, track_1, obj_2, track_2, obj_3, track_3] + p * self.prob_mat[obj_1, switch(i,j,track_1), obj_2, switch(i,j,track_2), obj_3, switch(i,j,track_3)]

        self.prob_mat = new_mat                        
        
    def observation(self, i, j, prob): #obj_i on track_j with probability prob
        pass

        # self.prob_mat[obj_i, : ] = np.ones(self.dim, dtype=float) * ((1-prob) / (self.dim-1))
        # self.prob_mat[obj_i, track_j] = prob

    def inference(self): # returns the most likely permutation
        pass