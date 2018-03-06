# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*
        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.
          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        """
        1. loop on iterations through states, starting from startState
        2. T(s,a,s') = mdp.getTransitionStatesAndProbs
        3. actions = mdp.getPossibleActions(state)
        4. R(s,a,s') = mdp.getReward(state, action, nextState) ; nextState is from Transition value tuple
        5. PLUS GAMMA (Discount Factor) * ????
        6. FINAL FORMULATION: Summation of T(s,a,s')*(R(s,a,s')+GAMMA*????) ---> is the value in the tuple, action is the current iteration of the state
        7. Do comparison on current value and previous value from Step 6.
        8. Maintain a tuple that saves the highest value associated with an action; return value
        max(self.actions[state], key=lambda d: d[1])
        """
        "*** YOUR CODE HERE ***"
    -------CODE REMOVED UNTIL COURSE FINISHES IN SPRING 2018------------
