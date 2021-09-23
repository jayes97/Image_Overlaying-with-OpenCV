import glob
import cv2
import os
from pathlib import Path

from Adding_images import overlayImage

bgImg_path = Path('Media/background_images/')
fgImg_path = Path('Media/threat_images/')

bgImage_list = list(bgImg_path.glob(r'*.jpg'))
fgImage_list = list(fgImg_path.glob(r'*.jpg'))

for i, bgImage in enumerate(bgImage_list):
    for j, fgImage in enumerate(fgImage_list):
        finalImg = overlayImage(str(bgImage), str(fgImage))
        label = os.path.split(bgImage)[1] + os.path.split(fgImage)[1]
        cv2.imwrite('Media/processed_images/'+label, finalImg)
