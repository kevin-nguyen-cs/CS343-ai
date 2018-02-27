# search.py
# ---------
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
#
# Additional modifications and implementations by Kevin Nguyen (kdn433) for
# Spring 2017 course, CS343 Artificial Intelligence, University of Texas at Austin.
#
"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
import util
from util import Stack
from util import Queue
from util import PriorityQueue

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def searchProcess(problem, fringe):
    """
    Graph searching implementation
    """
    #Local Declarations
    count = 0
    deadEndComplete = 0
    deadEnd = 0
    index = 0
    actionList = list()
    visitedList = set()
    myFringe = fringe   
    #loop forever until goal is found, adding and popping list for each iteration until goal is found
    while (True):
        if (myFringe.isEmpty()):
            del actionList[:]
            return actionList
        #Get item from queue
        item = myFringe.pop()
        #Delete the dead end path 
        if (deadEndComplete > 1 and len(actionList) > 2):
            del actionList[item[2]+1:len(actionList)]
            deadEndComplete = 3
        tempNode = (item[0], item[1], index)
        #check if item is the goal and return the list of actions if yes
        if (problem.isGoalState(item[0])):
            actionList.append(item)
            break
        #If item has been seen before then skip entirely, if not then add to visited and action list
        if not (item[0] in visitedList):
            visitedList.add(item[0])
            visitedList.add(tempNode)
            successorList = problem.getSuccessors(item[0])
            #loop add successors to the queue if any
            while (count < len(successorList)):
                successorItem = successorList[count]
                #Alter the indexing if deadend was reached so it increments accordingly
                if (deadEndComplete == 3):
                    index = item[2]+1
                    successorItem = (successorItem[0], successorItem[1], index)
                    deadEndComplete = 0
                else:
                    successorItem = (successorItem[0], successorItem[1], index)
                #skip adding child if it has already been seen
                if (successorItem[0] in visitedList):
                    deadEnd = deadEnd + 1
                    count = count + 1
                    continue
                myFringe.push(successorItem)
                count = count + 1
            #if all childs are seen already then it is a dead end no matter what
            if (deadEnd >= len(successorList)):
                deadEndComplete = 1
            count = 0
            deadEnd = 0
            #Insert into action list
            if (successorList):
                actionList.append(tempNode)
            if ((deadEndComplete > 0 and tempNode[0] in visitedList) and not problem.isGoalState(item[0]) and successorList):
                deadEndComplete = 2   
        index = index + 1
    return actionList

def reformatList(actionList):
    """
    Take an unformatted list and reform it into the correct resulting list
    """
    count = 0
    temp = list()
    #Reform the resulting list with correct values and return it
    while (count < len(actionList)):
        item = actionList[count]
        temp.append(item[1])
        count = count + 1
    count = 0
    return temp

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #Local Declarations
    count = 0
    actionList = list()
    myStack = util.Stack()
    successorList = problem.getSuccessors(problem.getStartState())
    #Push initial childs into the fringe
    while (count < len(successorList)):
        myStack.push(successorList[count])
        count = count + 1
    count = 0
    #Get unformatted action list
    actionList = searchProcess(problem, myStack)
    #Return a formatted action list
    return reformatList(actionList);
    util.raiseNotDefined()

def searchProcessBFS(problem, fringe):
    """
    Search process for Breadth First Search
    """
    #Local Declarations
    count = 0
    listPresent = 0
    actionList = list()
    visitedList = set()
    successorList = list()
    path = {}
    startItem = (problem.getStartState(), '0', 0.0)
    #try state if it has single element or more elements inside it
    try:
        startState = startItem[0]
        if (type(startState[1]) is list):
            startItem = (startState[0], '0', 0.0)
            listPresent = 1
        path[startItem] = None
        startItem = (startState, '0', 0.0)
    except IndexError:
        startItem = startItem
        path[startItem] = None

    myFringe = fringe
    myFringe.push(startItem)
    #Loop forever until fringe is empty
    while not (myFringe.isEmpty()):
        item = myFringe.pop()
        itemTemp = item #original copy
        if (listPresent == 1):
            itemState = item[0]
            itemCoord = itemState[0]
            itemTemp = (itemState, item[1], item[2])
            item = (itemCoord, item[1], item[2])

        #Get successors from current item and add to visited set
        if (listPresent == 1):
            #check for goal state and return if yes
            if (problem.isGoalState(itemTemp[0])):
                actionList = pathFinder(item, path)
                return actionList
            successorList = problem.getSuccessors(itemTemp)
        else:
            #check for goal state and return if yes
            if (problem.isGoalState(item[0])):
                actionList = pathFinder(item, path)
                return actionList
            successorList = problem.getSuccessors(item[0])
        visitedList.add(item[0])
        #Loop over all children/successors of current item/node
        while (count < len(successorList)):
            #Get child from list of children
            successorItem = successorList[count]
            successorItemOriginal = successorItem #copy
            if (listPresent == 1):
                successState = successorItem[0]
                successCoord = successState[0]
                successorItem = (successCoord, successorItem[1], successorItem[2])
            #skip if child has already been queued or seen already
            if (successorItem[0] in visitedList):
                count = count + 1
                continue
            #append a path by a dictionary, from child node to parent node (current node); must also push to fringe
            if not (path.has_key(successorItem)):
                visitedList.add(successorItem[0])
                path[successorItem] = item
                if (listPresent == 1):
                    myFringe.push(successorItemOriginal)
                else:
                    myFringe.push(successorItem)
            #increment counter
            count = count + 1
        #reset counter
        count = 0
    return actionList

def pathFinder(goal, path):
    """
    pathFinder will unwind the path from the dictionary from goal --> root node/item
    """
    #Local Declarations
    actionList = list()
    item = goal
    #Loop forever and extract the paths from goal to root node; must reverse list when finished
    while not (path[item] == None):
        actionList.append(item[1])
        item = path[item]
    actionList.reverse()
    #return list
    return actionList

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    myQueue = util.Queue()
    return searchProcessBFS(problem, myQueue)
    util.raiseNotDefined()

def searchProcessUCS(problem, fringe):
    """
    Search process for Uniform Cost search
    """
    #local declarations
    count = 0
    cost = 0
    costSoFar = 0
    actionList = list()
    visitedList = set()
    successorList = list()
    path = {}
    startItem = (problem.getStartState(), '0', 0.0)
    path[startItem] = None
    myFringe = fringe
    myFringe.push(startItem, 0.0)
    #Loop forever and process search functionality
    while not (myFringe.isEmpty()):
        item = myFringe.pop()
        cost = item[2] + costSoFar
        #check for goal state
        if (problem.isGoalState(item[0])):
            actionList = pathFinder(item, path)
            return actionList
        #get successors of the current node or item, must add popped item to visited
        successorList = problem.getSuccessors(item[0])
        visitedList.add(item[0])
        #loop to iterate over all children/successors in list
        while (count < len(successorList)):
            successorItem = successorList[count]
            #if seen already or not goal then skip everything below
            if (successorItem[0] in visitedList and not (problem.isGoalState(successorItem[0]))):
                count = count + 1
                continue
            #if no key has been generated between the child and current node, then do so and update the fringe
            if not (path.has_key(successorItem)):
                visitedList.add(successorItem[0])
                path[successorItem] = item
                cost = cost + successorItem[2]
                myFringe.update(successorItem, cost)
            #update counters
            count = count + 1
            cost = item[2] + costSoFar
        #reset counters
        count = 0
        costSoFar = item[2]
    return actionList

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #Local Declarations
    myPQ = util.PriorityQueue()
    #call search function and return the path
    return searchProcessUCS(problem, myPQ)
    util.raiseNotDefined()

def searchProcessAStar(problem, fringe, heuristic):
    """
    A Star Search implementation
    """
    #local declarations
    count = 0
    cost = 0.0
    actionList = list()
    visitedList = set()
    successorList = list()
    path = {}
    startItem = (problem.getStartState(), '0', 0.0)
    path[startItem] = None
    myFringe = fringe
    myFringe.push(startItem, 0.0)
    #Loop forever and process search functionality
    while not (myFringe.isEmpty()):
        item = myFringe.pop()
        #check for goal state
        if (problem.isGoalState(item[0])):
            actionList = pathFinder(item, path)
            return actionList
        #get successors of the current node or item, must add popped item to visited
        successorList = problem.getSuccessors(item[0])
        visitedList.add(item[0])
        #loop to iterate over all children/successors in list
        while (count < len(successorList)):
            successorItem = successorList[count]
            #if seen already or not goal then skip everything below
            if (successorItem[0] in visitedList and not (problem.isGoalState(successorItem[0]))):
                count = count + 1
                continue
            #if no key has been generated between the child and current node, then do so and update the fringe
            if not (path.has_key(successorItem)):
                visitedList.add(successorItem[0])
                path[successorItem] = item
                cost = heuristic(successorItem[0], problem) + problem.getCostOfActions(pathFinder(successorItem, path))
                myFringe.update(successorItem, cost)
            #update counters
            count = count + 1
        #reset counters
        count = 0
    return actionList    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #Local Declarations
    myPQ = util.PriorityQueue()
    #call search function and obtain path
    return searchProcessAStar(problem, myPQ, heuristic)
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch