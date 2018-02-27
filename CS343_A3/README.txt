Name 1: Nilo Lisboa
UTEID 1: nl6867

Name 2: Kevin Nguyen
UTEID 2: kdn433

SLIP DAYS USED: 0


Implementation:

In this project, we try to implement Q-Learning with Bellman equations. For the first part, we had to understand how the bellman equation works. The equation is defined as having a transition value, reward value, gamma, and several q-values. After understanding how the equation works and reading the necessary materials, we started the implementation. For the first part of the project, we implemented the bellman equations in valueIterationAgents.py and qLearningAgents.py. The implementations were similar to each other depending on whether it was Q-Learning or not. In valueIterationAgents.py we had to make several loops to iterate through the state list, transition value, and actions from each state. We returned None or 0.0 for any illegal references as well. However, in qLearningAgents.py we did not have access to states or transition functions; as a result, we had to compute the values as we see them. We had to implement computeValueFromQValues, computeActionFromQValues, update, and getAction functions for Q-Learning. We kept a list of Q-Values and a mapping of (state, action) tuple pair with Q-Values. We updated the Q-values when we have better samples. Approximate Q-Learning was next in the implementation and we had to consider two vector dictionaries of features and weights. They are similar, but they're used for different computations. Q-Values in Approximate Q-learning are obtained when we did the summation over all features multiplied by the weight. The next step is to compute the approximate Q-Value in the update function and we use the Q-Value that we recently computed in our final computation. The final estimate Q-Value is then written to the weight vector dictionary as a new value given the state and action. An agent should now be able to go through Q-Learning succesfully.



How to run:

To run the program, extract all contents to specific directory. Go to the termianl and make sure you go to the directory where the extracted files are. Type in "python autograder.py" and hit enter; that will run all the test cases.
You can also use "python autograder.py -q q#", where # is a positive integer from 0 to 8 that'll indicate a specific test case.