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

        #Local Declarations
        startState = mdp.getStartState()
        count = 0
        self.actions = dict()
        qVals = dict()
        #loop to iterate through iterations
        while count < self.iterations:
          stateList = self.mdp.getStates()
          #iterate through state list to get each action list
          for s in stateList:
            self.actions[s] = list()
            actionList = self.mdp.getPossibleActions(s)
            #iterate through each action in action list
            for action in actionList:
              temp = self.computeQValueFromValues(s, action)
              self.actions[s].append((action, temp))
            if self.actions[s]:
              qVals[s] = max(self.actions[s], key=lambda d: d[1])[1]
          #update self.values dictionary
          for s in stateList:
            if self.mdp.isTerminal(s):
              self.values[s] = self.mdp.getReward(s, None, None)
            else:
              self.values[s] = qVals[s]
          count += 1

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        #Local Declarations
        resultValue = 0.0
        TransValList = self.mdp.getTransitionStatesAndProbs(state, action)
        #iterate through each list of tuples based on the current action and state
        for pair in TransValList:
          nextState = pair[0]
          transValue = pair[1]
          rewardValue = self.mdp.getReward(state, action, nextState)
          resultValue += transValue * (rewardValue + self.discount * self.getValue(nextState))
        return resultValue
        util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.
          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        #local declarations
        if self.mdp.isTerminal(state) or not self.mdp.getPossibleActions(state):
          return None
        if not (bool(self.actions)):
          return None
        action = max(self.actions[state], key=lambda d: d[1])[0]
        # print "ACTION --> ", action
        return action
        util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)