'''minimizes discomfort between individuals.
Randomly swaps participants and rejects if this raises the discomfort'''
import numpy as np
import copy as cp
from random import randint
#from people_matrix import r_matrix, N_GUESTS, guest_names
from import_people import r_matrix, N_GUESTS, guest_names

#state is list of chair numbers ordered by person number


def discomfort(r_matrix, d_ab):
  '''function to be minimized. Arguments are relationship r_matrix, and distance d_ab
  discomfort = sum r_ab * d_ab'''
  d = np.einsum('ij,ij',r_matrix, d_ab)
  return d

def d_points(i, j):
  '''distance between chairs i and j
  can be made more accurate than just the diff in chair number'''
  return abs(i-j)

def get_d_ab(state):
  '''gets distance between person a and b'''
  d = np.array([d_points(i, j) for i in state for j in state])
  return d.reshape(N_GUESTS, N_GUESTS)

def swap_ab(state, a, b):
  '''swaps places between people a and b'''
  new_state = cp.deepcopy(state)
  new_state_b = new_state[a]
  new_state_a = new_state[b]
  new_state[a] = new_state_a
  new_state[b] = new_state_b
  return new_state

def get_discomfort(r_matrix, state):
  '''get discomfort of the state'''
  d_ab = get_d_ab(state)
  d = discomfort(r_matrix, d_ab)
  return d


if __name__ == '__main__':
  initial_state = np.arange(N_GUESTS) #initially ordered by guest no
  print 'initial discomfort'
  print get_discomfort(r_matrix, initial_state)

  print 'do some monte carlo'
  current_state = initial_state
  current_discomfort = get_discomfort(r_matrix, initial_state)
  #do some monte carlo
  for step in range(10000):
    a = (randint(0,N_GUESTS - 1))
    b = (randint(0,N_GUESTS - 1))
    provisional_state = swap_ab(current_state, a, b)
    provisional_discomfort = get_discomfort(r_matrix, provisional_state)
    if provisional_discomfort < current_discomfort:
      current_state = provisional_state
      current_discomfort = provisional_discomfort

  print 'final state'
  print current_state
  print 'final discomfort'
  print current_discomfort

  for i in range(N_GUESTS):
    print guest_names[i], current_state[i]
