# ArtOfRallyAI
This project uses OpenCV and fastai to create an Artificial Intelligence that steers the car in the game "art of rally", an arcade rally game. This project uses code from the [Fall Guys AI project](https://github.com/ClarityCoders/Fall-Guys-AI) made by ClarityCoders.

## Image processing

When running the script [create_data.py](https://github.com/Dacarpe03/ArtOfRallyAI/blob/main/create_data.py), a region of the screen will be captured each 0.2 seconds.
In the beginning the image will look like this:  
![Original screen region](/readme_images/original_image.PNG)  

As we want to train the artificial inteligence to stay within the limits of the road, we use the [Canny algorithm](https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html) implemented in OpenCV library to detect the edges of the road. The resulting image is the following:  
![Canny screen region](/readme_images/canny_image.PNG)  

After this, we convert all the images into a numpy arrays and we label them as the key that was being pressed at that moment (A, W, or Nothing)
Finally we convert those numpy array into .png files using [create_images.py](https://github.com/Dacarpe03/ArtOfRallyAI/blob/main/utils/create_images.py) script, that will create three folders (Left, Right, Nothing) that will contain the images showing the car steering left, right or not steering.

## Neuronal Network training

The neuronal network that we will be using will be [resnet18](https://www.mathworks.com/help/deeplearning/ref/resnet18.html), a convolutional neuronal network that has a pretrained version which can classify images into 1000 object categories, including vehicles. The purpose here is that we train the network with our images so that it can detect the edges of the road and position of the car to steer it left or right. Using google colab, which provides free GPU computing, we can run [training.ipynb](https://github.com/Dacarpe03/ArtOfRallyAI/blob/main/training.ipynb) after uploading our images to Google Drive.  
We can choose a learning rate that minimizes the loss of the network using fastai [lr_find](https://fastai1.fast.ai/callbacks.lr_finder.html) built in function and then train it with our images.  
In this case we will train the network with 20k images taken from three different circuits:
![laampi](/readme_images/laampi.PNG) ![noormakku](/readme_images/noormakku.PNG) ![lassila](/readme_images/lassila.PNG)


## Trained agent

Now we are ready to test the artificial intelligence. We will use the [trained_agent.py](https://github.com/Dacarpe03/ArtOfRallyAI/blob/main/trained_agent.py) script to use the trained CNN. Each 0.2 seconds this script will grab a region of the screen and then perform the Canny algorithm on that image as when we did during the image processing. That image will be passed to the neuronal network to predict the direction towards the car will steer.  
Just keep pressed the W button for the car to move forward, the AI will do the rest. 
Final result can be seen in this [VIDEO](https://www.youtube.com/watch?v=-a5efm_LMzo) where we use the AI in this circuit:  
![palus](/readme_images/palus.PNG)
