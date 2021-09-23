
import cv2
import numpy as np

def img_transform(img_path, bg_path):
    img = cv2.imread(img_path)
    bgImg = cv2.imread(bg_path)

    # threshold on white
    # Define lower and uppper limits
    lower = np.array([200, 200, 200])
    upper = np.array([255, 255, 255])

    # Create mask to only select black
    thresh = cv2.inRange(img, lower, upper)

    # apply morphology
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1,1))
    morph = cv2.morphologyEx(thresh, cv2.MORPH_ERODE, kernel)

    # invert morp image
    mask = 255 - morph

    # apply mask to image
    result = cv2.bitwise_and(img, img, mask=mask)

    bbox = cv2.boundingRect(mask)
    x, y, w, h = bbox

    foreground = result[y:y+h, x:x+w]
    # cv2.imshow('thresh', thresh)
    # cv2.imshow('morph', morph)
    # cv2.imshow('mask', mask)
    # cv2.imshow('result', result)
    # cv2.imshow('forgrnd', foreground)

    # return foreground
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return image_rotate(foreground,bgImg)

#
def image_rotate(img, bgImg):
    hh, ww = bgImg.shape[:2]

    # calculate the center of the image
    center = (ww // 1.5, hh // 2)

    angle45 = 45

    scale = 0.5

    # Perform the counter clockwise rotation holding at the center
    # 45 degrees
    mat = cv2.getRotationMatrix2D(center, angle45, scale)

    return cv2.warpAffine(img, mat, (ww, hh))

# cv2.waitKey(0)
# cv2.destroyAllWindows()