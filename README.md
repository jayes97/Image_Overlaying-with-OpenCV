# Image_Overlaying-with-OpenCV
Adding Image over Image with OpenCv

_______________________________________________________________
The result images are stored in result directory.              |
_______________________________________________________________|

This project was created with pycharm environment 
opencv version 4.5.3
Python 3.7.11
Numpy 1.21.2
-------------------------------------------------------------------------------------
Python scripts
-------------------------------------------------------------------------------------
Initial.py

This is the main py file.
-----------------------
variables
-----------------------
bgImg_path :: Path of background images (luggage)
fgImg_path :: Path of foreground images (threat)

bgImage_list :: list of Path of background images
fgImage_list :: list of Path of foreground images

label  :: this is concated string of background image name and foreground image name
------------------

The nested for loops call the overlay function which returns the result 
This result is stored in finalImg variable

cv2.imwrite will save the results in Media/processed_images directory

-----------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------

Adding_images.py

-----------------------
overlayImage function
-----------------------
This function take path of background and foreground image as input arguments
And returns an image containg both foreground and background images over each other

-----------------------
variables
-----------------------

bgImage :: Background image (luggage image)
bgImage_alpha :: b,g,r to b,g,r,a transformed backgorund image (for alpha channel)

fg_transformed :: foreground image after transformation (45 degree angle and rescaling)
fgImage_alpha  :: b,g,r to b,g,r,a transformed foreground image (for alpha channel)
weighted_image :: Image after adding both foreground and background images

frame :: final image after again changing color from bgra to bgr

******Note*******
we can play with alpha, beta values of addweighted to change translucency of background and foreground image

---------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------

Transforming_images.py

-----------------------
img_transform function
-----------------------
This function takes forground image and background image path as input in its argument
and returns an image after cropping its background

-----------------------
variables
-----------------------
img_path :: foreground image path
bg_path  :: background image path

lower, upper :: lower and upper limit for inRange function
inRange function will keep all the white background as it is and transfrom the threat(knife) image to black color

Next with getStructuringElement a kernel is created for finding the region of interest
Then a morphological operation is applied with morphologyEx
I had used MORPH_ERODE (after trial and error)

to convert the image back to white pixel I deleted morph values from 255

then I performed a bitwise_and operation to get color image

Then obtained image was to enlarged as original image so a rectangular boundind box is used to crop intrested part

-----------------------
img_rotate function
-----------------------
This function will return an image after rotating it by 45 degree and also rescale it by half

-----------------------
variables
-----------------------
hh, ww :: height and width of background image
img :: image from image_transform function
bgImg :: background image
mat  :: Rotation matrix to rotate and rescale image
-----------------------------------------
The reason for passing background image to this function is that 
addweighted function needs both overlaying images of same shape to add, So I converted the resultant foreground Image
into size of background image

getRotationMatrix2D will create a matrix to rotate image
warpAffine Applies a Rotation to the image after being transformed. This rotation is with respect to the image center
