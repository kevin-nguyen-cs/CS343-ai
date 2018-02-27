Name 1: Nilo Lisboa
UTEID 1: nl6867

Name 2: Kevin  Nguyen
UTEID: kdn433


SLIP DAYS USED: 1


IMPLEMENTATION

	For the implementation, we had to understand bayesian routines, sampling, and inferencing to fully implement this project. The project incorporates exact inferencing, particle filtering, and joint particle filtering. For Exact Inferencing, we had to implement initializeuniformly which was done by equally distributing all particles among all positions. As a result, we kept track of a list that held those distributions; this is achieved by using two loops and merely placing the distributions as they are seen. We didn't use a dictionary because there could have been multiple samples or particles with the same position. Observe function was implemented next and we had to understand how to compute the weights in terms of Likelihood. To compute the weights, we multiplied the parent beliefs that was obtained in getBeliefDistribution function and by evidence given the position. We also looped through each position to compute each respective weights and store them as beliefs; we also normalized the beliefs so they would be more accurate. After that, getBeliefDistribution function will get the probabalistic beliefs for each position. This method has loops that will count up the number of occurances of a position or set and store them into a temp list. That list is then normalized and returned as the result list of beliefs. Particle Filtering is almost identical and we now look at multiple indepdendent particles (samples). The process remains the same but now we loop through multiple particles to compute the weight and the belief distributions. Join Distributions is slightly different because we have to go through each set of positions for mutliple ghosts. These are not independent data; as a result, each ghost can have their own set od data to be used. Uniform distributions and getBeliefDistribution functions remain roughly the same; however, because we deal with tuples of positions, we also had to shuffle the positions. In observe state function, we compute the weights for each individual ghost with their respective evidences by multiplying. The weight is then stored as a belief and normalized; it is set as the weight for the tuple position. We also had to handle two special cases and they were to handle when the ghost is eaten and when the all weights are 0. When the ghost is eaten, we had to set the positions in our lists to be the jail position (may also have to set the belief to be 1.0). It is accomplished by looping through the position list and manually replacing the entire positions to reflect the ghost being eaten. If the weights are 0 then we have to reobtain the uniform distribution because we want to obtain new set of samples to evaluate over. Otherwise, we resample manually by called util.sample for all positions through a loop. When it's all implemented correctly, pacman should be able to pursue and capture ghosts.

HOW TO RUN

	To run the program, extract the files to a specified directory. In the terminal, (please make sure you are in your directory of where you extracted the files) type in "python autograder.py" to grade the entire implementation. You may also try "python autograder.py -q q#" where # is a number from 1 to 7. It will run the tests only for a particular question if desired.

