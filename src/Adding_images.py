import cv2

from Transforming_images import img_transform

def overlayImage(bgImage_path, fgImage_path):

    bgImage = cv2.imread(bgImage_path)
    bgImage_aplha = cv2.cvtColor(bgImage, cv2.COLOR_BGR2BGRA)

    # bg_h, bg_w, bg_c = bgImage.shape
    # overlay = np.zeros((bg_h, bg_w, 4), dtype='uint8')

    fg_transformed = img_transform(fgImage_path, bgImage_path)
    fgImage_alpha = cv2.cvtColor(fg_transformed, cv2.COLOR_BGR2BGRA)

    weighted_image = cv2.addWeighted(fgImage_alpha, 0.5, bgImage_aplha, 1, 0)

    frame = cv2.cvtColor(weighted_image, cv2.COLOR_BGRA2BGR)
    return frame

