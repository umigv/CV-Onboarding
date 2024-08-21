This documentation provides a comprehensive overview of how we will apply Machine Learning in PyTorch and gives you the chance to build 
your own image classifier. Please read through it and then follow one of the tutorials to construct your own.

-----------------------------------------------------------------------------------------------------------------------

**CUDA:** PyTorch makes it easy to compute operations using the GPU. This helps with speed, as GPUs are designed to perform 
parallel computations, which can lead to a significant speedup in the training of machine learning models. It also helps 
with memory and power. 

if torch.cuda.is_available(): device = 'cuda:0'

-----------------------------------------------------------------------------------------------------------------------

Some important concepts to be familiar with:

- **Tensors:** PyTorch uses tensors, similar to numpy arrays, to perform mathematical operations. You can create a tensor by passing a list or array to the torch.Tensor() function.
- **Train Test Split:** In machine learning, it is common practice to split the available data into a training set and a testing set. The training set is used to train the model, while the testing set is used to evaluate the performance of the trained model on unseen data. This is important because it allows us to get an estimate of how well the model will perform on new, unseen data, which is crucial for evaluating the model's generalization capabilities. We can use the train_test_split function from sklearn to do this.
- **DataLoader:** You can create a PyTorch DataLoader that will handle the loading of the data during training. This is useful because it allows you to easily batch the data and shuffle it before each epoch. For extremely large datasets, it is unrealistic to store the entire dataset in the memory. Dataloaders can allow us to instead store paths to the data.
- **Activation Function:** Activation functions can introduce non-linearity between fully-connected layers, which is key to allowing our models be able to detect non-linear patterns.
- **Loss Function:** The loss function measures the difference between the model's predictions and the true labels. It is used to evaluate the model's performance during training and testing. The goal of the optimization process is to minimize the loss function.
- **Optimizer:** The optimizer plays a crucial role in updating the model's parameters during training. The optimizer's role is to minimize the loss function. The optimizer uses the gradients of the loss with respect to the model's parameters to update the parameters in a direction that reduces the loss. This is done iteratively, during the training process.
- **Convolutions:** Convolutions are used to extract features from images, which can then be used for various tasks such as image classification, object detection, and segmentation. They are a mathematical operation that involves two functions: the input signal and the convolution kernel. The convolution kernel is a small matrix that is used to slide over the input signal and perform element-wise multiplications. The output of the convolution is then summed up, and the result is a single value.

-----------------------------------------------------------------------------------------------------------------------

Convolutional Neural Network:

CNNs are a type of artificial neural network that are designed to work with image data. They are made up of multiple layers, including convolutional layers, activation layers, and pooling layers, that process an image and generate predictions based on the features learned from the image. 

**Example Model Architecture:**
- Convolutional layers: the first layer applies several filters (or kernels) to the input image, creating a feature map that captures the important features of the image such as edges, shapes, and patterns. 
- Max pooling layers: the next layers reduce the spatial dimensions of the feature map by dividing the feature map into a grid and taking the maximum value from each grid. This helps to reduce the computational complexity of the network.
- Fully connected layers: the output of the previous layers is flattened and fed into a fully connected layer, which acts as a classifier by computing the dot product between the weights and the inputs and then passing the result through an activation function.

**Training Process:**
- Zero the gradients: Before we start the training, we zero the gradients from the previous iteration to ensure that they don't accumulate over time.
- Pass the data through the model: Next, we pass the input data through the model to get the predictions.
- Calculate the loss: We then compare the model's predictions with the actual target labels to calculate the loss. The loss is a measure of how well the model is doing and serves as a feedback signal for the model to update its parameters.
- Compute gradients: We then compute the gradients of the loss with respect to the model's parameters. These gradients tell us how to update the model's parameters so that the loss decreases.
- Update parameters: Finally, we use the optimizer to update the model's parameters based on the gradients computed in the previous step. This is called back propagation.
- Return the training loss and accuracy: We also return the training loss and accuracy for this iteration to be used for monitoring purposes.

-----------------------------------------------------------------------------------------------------------------------
These tutorials will take you through the process of **training an image classifier in PyTorch**. Please choose the guided videos or article based depending on which way you feel you learn best.

Guided Video Turorial (Easier to Follow with Limited Knowledge Base):
- [Step By Step Tutorial](https://youtube.com/playlist?list=PL3Dh_99BJkCEhE7Ri8W6aijiEqm3ZoGRq&feature=shared)
  - If you get confused reference the definitions above, those found in the YOLO training notebook, or the informative portion of the article below.

Or

Article Based tutorial:
- [Deep Learning with Pytorch](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)
