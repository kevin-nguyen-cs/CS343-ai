

Name 1: Nilo Lisboa
UTEID 1: nl6867

Name 2: Kevin  Nguyen
UTEID: kdn433


SLIP DAYS USED: 0



Implementation:

	For our implementation, we had to implement classifiers for images. The classifier train function is suppose to determine which is the correct item and label. We also did some research with the lecture slides and materials over classify functionality. For the first part of the implementation, we wanted to iterate over vectors for features and weights and take the dot product. The value is a score that should be compared with the actual score and update the weights accordingly. The weights for the actual label and computed label should both be updated. Next we tested our classifier with MIRA to alter weights by alternate computations. The algorithm only makes adjustments to computations to adjust the weights; however, the classifier implementation remains untouched. The issue surfaces when given abstract images and the classifier has limited features to work with. As a result, we added additional features that checks for "clusters" in a pixel grid. We loop through the grid and for each pixel, we check all directions to make sure it's enclosed. If so, we add that feature with a value of one otherwise, a value of zero. Cluster checking will enable a slightly more accurate test run with the classifier. After that, we test how classifier would handle a state and action feature rather than coordinates. Classifier should run as normal. However, we also had to impplement new features by considering "resources" to take in. These features merely simulates what Pacman can use and we store them as features to run with the classifier. Overall, classifier train function should be untouched after the first part. In fact, most of this implementation revolves around classifier train method; otherwise, the entire implementation could've been wrong.



How to run:
	
	To run the program, go to the folder of where the extracted materials are in your terminal with 'cd' command. Then, type in 'python autograder.py' to run the autograder. You may also do 'python autograder.py -q q#' where # is some value between 1 and 6; runs a specific test case.