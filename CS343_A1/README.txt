NAME: Kevin Nguyen
EID: kdn433
Project 1

Implementation:

	The project was to implement a solution path for the game called pac man. The path consists of search algorithms such as Depth-First Search, Breadth-First Search, Uniform cost search, and A* search. These search alogirthms were implemented first because they provide the framework for the latter half of the project. As a result, the search algorithms are similar because they all maintain somekind of stack (DFS), queue (BFS), or priority queue (UCS and A*). Those data structures are used so we avoid using recursion and just maintain an iterative loop. The loop will run until the fringe (frontier) of expanded nodes run empty. We also maintain a visited set that keeps track of nodes that was already seen before. If a node has been seen then it is skipped entirely and never considered to be looked at again. A dictionary is also maintain to keep track of the parents of each child node. The dictionary is used because we want to be able to loop and trace back to the root node; as a result, that gives us the length and list of the actions required to reach the goal. It is also the path from root to goal node.

	The latter half of the project is not completed or finished. The idea for the implementation is maintaining a new state representation to help find all corners. The new state representation has the coordinates and a list of false values that correspond to the corners. The implementation for corners involved keeping track of the corners being visited and when all corners have been visited return true for the goal function. The heuristics idea that I had was to maintain a list of the corners and compute the manhattan distance between all corners and the current position; I am considering the corners that are furthest away. However, I also take the max of the values computed and then did a summation through out the process. The goal is to be admissble but extend the range of possibilities without "overshooting" the process. Unfortuantely, the rest of the program was not finished because of time constraints and they have not been attempted.


How to run:

	To run the code, extract the necessary files to a location. Then in your terminal, type in "python autograder.py" to run the test cases. You can also append "-q q#" where # is a value 1-8 that will invoke only the test cases for that value. If errors occur, ctrl+c can terminate the current runtime. 