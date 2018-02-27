# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.
      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.
        getAction chooses among the best options according to the evaluation function.
        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.
        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.
        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.
        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        #Local Declarations
        newWalls = successorGameState.getWalls()
        # foodList = list()
        foodDist = 0.0
        foodCoord = (0, 0)
        ghostPositions = successorGameState.getGhostPositions()
        ghostDist = 0.0
        ghostCoord = (0, 0)
        dom = 0
        rng = 0
        resultScore = 0
        targetDistance = 0
        oldDistance = 999999

        #Game win/lose evaluation
        if (successorGameState.isLose()):
            return -999999
        if (successorGameState.isWin()):
            return 999999

        first = False

        foodCount = 0

        for i in range(0, newFood.width):
            for j in range(0, newFood.height):
                if newFood[i][j]:
                    foodCount += 1

        #loop through food list to find lowest min value (closest to food by pacman)
        for i in range(0, newFood.width):
            for j in range(0, newFood.height):
                if not (newWalls[i][j]):

                    if not first:
                        temp1 = util.manhattanDistance(newPos, (i, j))
                        # print ("Food_Man_Dist: ", temp1)
                        if temp1 == 1:
                            first = True
                            foodDist -= 1000000

                    #foodDist += util.manhattanDistance(newPos, (i, j))
                    if util.manhattanDistance(newPos, (i, j)) <= 100:
                        foodDist += 1000000 - util.manhattanDistance(newPos, (i, j))*10000
                    if newFood[i][j]:
                        #update to smallest variable if true
                        if (foodDist < oldDistance):
                            oldDistance = foodDist
                            foodDist = 0

        foodDist = oldDistance
        # print "FoodDist: ", foodDist

        for i in range(0, len(ghostPositions)):
            temp2 = util.manhattanDistance(newPos, ghostPositions[i])

            if (temp2 <= 1):
                ghostDist -= 999999
            if (temp2 > 1 and temp2 < 8):
                ghostDist -= temp2 + 10000
            ghostDist -= temp2 + 100
            #update to smallest variable if true
            if (ghostDist <= oldDistance):
                oldDistance = ghostDist
                ghostDist = 0

        ghostDist = oldDistance

        resultScore += (ghostDist/foodDist) + successorGameState.getScore()
        return resultScore

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.
      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.
      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.
      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.
          Here are some method calls that might be useful when implementing minimax.
          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1
          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action
          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        #Local Declarations
        numAgents = gameState.getNumAgents()
        indexAgent = numAgents
        optimalAction = self.valueProcessor(gameState, 0, indexAgent, numAgents)
        return optimalAction[1]
        util.raiseNotDefined()

    #Check for termination whether win, lose, or no more child nodes to visit
    def checkForTerminal(self, state, depth):
        #check if state has reached a terminal, if it is then clear and return a value in a list
        if (state.isWin() or state.isLose() or (depth > self.depth)):
            return 1
        return 0

    #valueProcessor function will start the minimax algorithm
    def valueProcessor(self, state, depth, indexAgent, numAgents):
        #Local Variables
        value = (0, None)
        #Decide if the number of agents has been reached, if so then reset the agent index
        if (indexAgent >= numAgents):
            indexAgent = indexAgent%numAgents
            value = self.maxValue(state, depth+1, indexAgent, numAgents) 
        else:
            indexAgent = indexAgent%numAgents
            value = self.minValue(state, depth, indexAgent, numAgents)
        #return value is tuple (val, action)
        return value

    #min value for minimax evaluation
    def minValue(self, state, depth, indexAgent, numAgents):
        #Local Declarations
        count = 0
        minVal = 999999
        actionList = list()
        #Check for terminal
        if (self.checkForTerminal(state, depth)):
            return (self.evaluationFunction(state), ".")
        #get list of actions and length
        actionList = state.getLegalActions(indexAgent)
        actionLength = len(actionList)
        #loop to get through the action items
        while (count < actionLength):
            temp  = self.valueProcessor(state.generateSuccessor(indexAgent, actionList[count]), depth, indexAgent+1, numAgents)
            minVal = min(minVal, temp[0])
            action = actionList[count]
            count = count + 1
        count = 0
        #return minimum value tuple
        return (minVal, action)

    #max value for minimax evaluation
    def maxValue(self, state, depth, indexAgent, numAgents):
        #local Declarations
        count = 0
        maxVal = -999999
        actionList = list()
        result = {}
        #check for terminal
        if(self.checkForTerminal(state, depth)):
            return (scoreEvaluationFunction(state), ".")
        #get action list and length for loop iteration
        actionList = state.getLegalActions(indexAgent)
        actionLength = len(actionList)
        #loop through list of actions for pacman state and get max optimized value from list of min value of agents
        while (count < actionLength):
            temp = self.valueProcessor(state.generateSuccessor(indexAgent, actionList[count]), depth, indexAgent+1, numAgents)
            maxVal = max(maxVal, temp[0])
            result[actionList[count]] = temp[0]
            count = count + 1
        count = 0
        bestAction = max(result, key = result.get)
        #return max value from tuple
        return (maxVal, bestAction)

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        #Local Declarations
        alpha = -999999
        beta = 999999
        optimalAction = None
        numAgents = gameState.getNumAgents()
        optimalAction = self.valueProcess(gameState, alpha, beta, 0, 0, numAgents, 1)
        return optimalAction[1]
        util.raiseNotDefined()

    #Check for termination whether win, lose, or no more child nodes to visit
    def checkForTerminal(self, state, depth):
        #check if state has reached a terminal, if it is then clear and return a value in a list
        if (state.isWin() or state.isLose() or (depth >= self.depth)):
            return 1
        return 0

    #Value process for alpha beta agent
    def valueProcess(self, gameState, alpha, beta, myDepth, indexAgent, numAgents, maximizingAgent):
        value = (0, None)
        if (indexAgent >= numAgents):
            value = self.alphaBetaProcess(gameState, alpha, beta, myDepth+1, 0, numAgents, 1)
        else:
            value = self.alphaBetaProcess(gameState, alpha, beta, myDepth, indexAgent, numAgents, maximizingAgent) 
        return value

    #Start process for the alphabeta pruning algorithm
    def alphaBetaProcess(self, state, alpha, beta, depth, indexAgent, numAgents, maximizingAgent):
        #local Declarations
        count = 0
        result = {}
        actionList = list()
        #check for terminal
        if(self.checkForTerminal(state, depth)):
            return (self.evaluationFunction(state), ".")
        #get action list and length for loop iteration
        actionList = state.getLegalActions(indexAgent)
        actionLength = len(actionList)
        #if index is 0, then maximize outcomes, else minimize outcomes
        if (maximizingAgent == 1):
            value = -999999.9
            #loop through the action lists for max or min
            while (count < actionLength):
                temp = self.valueProcess(state.generateSuccessor(indexAgent, actionList[count]), alpha, beta, depth, indexAgent+1, numAgents, 0)
                value = max(value, temp[0])
                result[actionList[count]] = temp[0]
                count = count + 1
                if (beta < value):
                    return (value, 0)
                alpha = max(alpha, value)
            count = 0
            bestAction = max(result, key = result.get)
            return (value, bestAction)
        else:
            value = 999999.9
            #loop through the action lists for max or min
            while (count < actionLength):
                temp = self.valueProcess(state.generateSuccessor(indexAgent, actionList[count]), alpha, beta, depth, indexAgent+1, numAgents, 0)
                value = min(value, temp[0])
                action = actionList[count]
                count = count + 1
                if (value < alpha):
                    if not (value == alpha):
                        return (value, action)
                beta = min(beta, value)
            count = 0
            return (value, action)

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction
          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        #Local Variables
        numAgents = gameState.getNumAgents()
        indexAgent = numAgents
        optimalAction = self.valueProcessExp(gameState, 0, indexAgent, numAgents)
        return optimalAction[1]
        util.raiseNotDefined()

    #Check for termination whether win, lose, or no more child nodes to visit
    def checkForTerminal(self, state, depth):
        #check if state has reached a terminal, if it is then clear and return a value in a list
        if (state.isWin() or state.isLose() or (depth > self.depth)):
            return 1
        return 0

    #get probability distribution for the state; this function considers equal probability
    def probabilityFinder(self, actionLength):
        return 1.0/actionLength

    #start process for expectimax searching
    def valueProcessExp(self, state, depth, indexAgent, numAgents):
        #Local Declarations
        value = (0, None)
        if (indexAgent >= numAgents):
            #MAX
            indexAgent = indexAgent%numAgents
            value = self.expectimaxMax(state, depth+1, indexAgent, numAgents)
        else:
            #MIN
            indexAgent = indexAgent%numAgents
            value = self.expectimaxExp(state, depth, indexAgent, numAgents)
        return value

    #expectimax searching for MAX
    def expectimaxMax(self, state, depth, indexAgent, numAgents):
        #local Declarations
        count = 0
        result = {}
        actionList = list()
        #check for terminal
        if(self.checkForTerminal(state, depth)):
            return (self.evaluationFunction(state), ".")
        #get action list and length for loop iteration
        actionList = state.getLegalActions(indexAgent)
        actionLength = len(actionList)
        #if the maximizing agent then take the max over the childs when they are recursively done
        value = -999999.0
        #loop through actionlength and obtain the max value
        while (count < actionLength):
            action = actionList[count]
            newState = state.generateSuccessor(indexAgent, action)
            temp = self.valueProcessExp(newState, depth, indexAgent+1, numAgents)
            value = max(value, temp[0])
            result[actionList[count]] = temp[0]
            count = count + 1
        #get best value and return it
        bestAction = max(result, key = result.get)
        return (value, bestAction)

    #expectimax searching for Exp
    def expectimaxExp(self, state, depth, indexAgent, numAgents):
        #local Declarations
        count = 0
        actionList = list()
        #check for terminal
        if(self.checkForTerminal(state, depth)):
            return (self.evaluationFunction(state), ".")
        #get action list and length for loop iteration
        actionList = state.getLegalActions(indexAgent)
        actionLength = len(actionList)
        value = 0.0
        #If NOT maximizing agent then take the additive sum and product of the resursive value when done
        while (count < actionLength):
            probability = self.probabilityFinder(actionLength)
            action = actionList[count]
            newState = state.generateSuccessor(indexAgent, action)
            temp = self.valueProcessExp(newState, depth, indexAgent+1, numAgents)
            value = value + (probability*temp[0])
            count = count + 1
        return (value, action)

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).
      DESCRIPTION: For all successors of the given state:
                   PacMan scans the field for food while evaluating how far the ghost is from it.
                   It places heavy emphasis on food that is near it, and heavy emphasis when the ghost is near the agent.
                   The distance modifier of the ghost is then divided by the food distance to influence pacman's state choice.
                   return average result per successor state. The dist to the ghost becomes irrelevant if the ghost is scared so any choice is good.
                   We also want to avoid stopping in the direction needlessly and try urge pacman to try a different path.
    """
    "*** YOUR CODE HERE ***"
    #Local Declarations
    actionList = currentGameState.getLegalActions(0)
    resultList = list()
    count = 0
    avgResult = 0.0

    #Game win/lose evaluation
    if (currentGameState.isLose()):
        return -9999999
    if (currentGameState.isWin()):
        return 9999999

    for action in actionList:
        count = count + 1
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        newWalls = successorGameState.getWalls()
        foodDist = 0.0
        ghostPositions = successorGameState.getGhostPositions()
        ghostDist = 0.0
        dom = 0
        rng = 0
        resultScore = 0
        oldDistance = 9999999
        oldFoodDist = 9999999
        first = False
        foodCount = 0

        #Get food left on the grid?
        for i in range(0, newFood.width):
            for j in range(0, newFood.height):
                if newFood[i][j]:
                    foodCount = foodCount + 1

        #loop through food list to find lowest min value (closest to food by pacman)
        for i in range(0, newFood.width):
            for j in range(0, newFood.height):
                #check if wall is there or not
                if not (newWalls[i][j]):
                    if not first:
                        foodDistTemp = util.manhattanDistance(newPos, (i, j))
                        if foodDistTemp <= 1:
                            first = True
                            foodDist += 1000
                    if util.manhattanDistance(newPos, (i, j)) <= 100:
                        foodDist += 1000 - util.manhattanDistance(newPos, (i, j))*10
                    if newFood[i][j]:
                        #update to smallest variable if true (closest to food)
                        if (foodDist < oldDistance):
                            oldDistance = foodDist
        foodDist = oldDistance

        #Get ghost position and evaluate the distance from ghost
        for i in range(0, len(ghostPositions)):
            ghostDistTemp = util.manhattanDistance(newPos, ghostPositions[i])
            #different positions evaluate to different output choices for pacman
            if (ghostDistTemp <= 1):
                ghostDist -= 1000
            elif (ghostDistTemp > 1 and ghostDistTemp < 9):
                ghostDist -= ghostDistTemp + 10
            else:
                ghostDist = ghostDist*2.25
            ghostDist -= ghostDistTemp
            #update to smallest variable if true
            if (ghostDist <= oldDistance):
                oldDistance = ghostDist
        ghostDist = abs(oldDistance)

        #consider Stop condition, bad if pacman stops, must keep moving!
        if action == Directions.STOP:
            foodDist = foodDist+1
            ghostDist = ghostDist+2

        #consider scared condition
        if newScaredTimes < 5:
            ghostDist = 1
        else:
            ghostDist = ghostDist+2
        #get the result score and append it to the list
        resultScore += (ghostDist/foodDist) + successorGameState.getScore()
        resultList.append(resultScore)

    #avg the results and return the value
    if len(resultList) != 0:
        avgResult = sum(resultList)/len(resultList)
    return avgResult
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction