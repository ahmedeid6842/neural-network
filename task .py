import numpy as np

class Neural:
    def sigmoidFunction(self,x):
        return 1 / ( 1 + np.exp(-x) )


    # input dataset
    training_inputs = np.array([[0,0,1],
                                [1,1,1],
                                [1,0,1],
                                [0,1,1]])

    # output dataset
    training_outputs = np.array([[0,1,1,0]]).T

    np.random.seed(1)

    random_weights = 2 * np.random.random((3,1))-1

   
    print(random_weights)

    def result(self) :
        for iterx in range(1):
            output = np.dot(self.training_inputs , self.random_weights)
            activiation_output = self.sigmoidFunction(output)
            print(activiation_output)
final= Neural()
final.result()