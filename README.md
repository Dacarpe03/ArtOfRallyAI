# ArtOfRallyAI
This project uses OpenCV and fastai to create an Artificial Intelligence that steers the car in the game "art of rally", an arcade rally game. This project uses code from the [Fall Guys AI project](https://github.com/ClarityCoders/Fall-Guys-AI) made by ClarityCoders.

## Image processing

When running the script [create_data.py](https://github.com/Dacarpe03/ArtOfRallyAI/blob/main/create_data.py), a region of the screen will be captured each 0.2 seconds.  
At first the image will look like this:    
    ![Original screen region](/readme_images/original_image.PNG)  

As we want to train the artificial inteligence to stay within the limits of the road, we use the [Canny algorithm](https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html) implemented in OpenCV library to detect the edges of the road. The resulting image is the following:  
    ![Canny screen region](/readme_images/canny_image.PNG)  

