'''
Copyright Andrew Martin 2016
uses simulated annealing to minimize discomfort.
Similar to the minimize_discomfort.py: it randomly swaps participants,
but simulated annealing sometimes accepts swap
even if this raises the discomfort. Prevents sticking in local minimum

"input.csv" should exist and contain an upper-triangular array of people scores

usage: python simulated_annealing_discomfort.py
'''

import numpy as np
import copy as cp
from random import randint, random
#from people_matrix import r_matrix, N_GUESTS, guest_names
from import_people import r_matrix, N_GUESTS, guest_names
from minimize_discomfort import get_discomfort, swap_ab

print 'number of guests'
print N_GUESTS

def prob_accept(e_prime, e, T):
  '''the acceptence probability'''
  return np.exp(-(e_prime - e)/T)

if __name__ == '__main__':
  initial_state = np.arange(N_GUESTS) #initially ordered by guest no
  print 'initial discomfort'
  print get_discomfort(r_matrix, initial_state)

  print 'start simulated annealing'
  current_state = initial_state
  current_discomfort = get_discomfort(r_matrix, initial_state)

  n_steps = 100000
  Ti = 25 #the initial "temperature"
  Tf = 1. #the final "temperature"
  temps = np.linspace(Ti, Tf, n_steps)
  #do some simulated annealing
  for step in range(n_steps):
    a = (randint(0,N_GUESTS - 1))
    b = (randint(0,N_GUESTS - 1))
    provisional_state = swap_ab(current_state, a, b)
    provisional_discomfort = get_discomfort(r_matrix, provisional_state)
    if provisional_discomfort < current_discomfort:
      current_state = provisional_state
      current_discomfort = provisional_discomfort
    else:
      #draw random and accept if less than p(t)
      p_draw = random()
      T = temps[step]
      if p_draw < prob_accept(provisional_discomfort, current_discomfort, T):
        #print 'accept', provisional_discomfort, current_discomfort
        #print p_draw, prob_accept(provisional_discomfort, current_discomfort, T)
        current_state = provisional_state
        current_discomfort = provisional_discomfort
      else:
        #print 'reject', provisional_discomfort, current_discomfort
        #print p_draw, prob_accept(provisional_discomfort, current_discomfort, T)
        pass


  print 'final state'
  print current_state
  print 'final discomfort'
  print current_discomfort

  seating_order = []
  for i in range(N_GUESTS):
    seating_order.append((guest_names[i], current_state[i]))
    #print guest_names[i], current_state[i]
  ordered_order = sorted(seating_order, key=lambda tup: tup[1])
  print ordered_order



