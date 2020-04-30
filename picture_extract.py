import numpy as np
import cv2
from PIL import Image

img = cv2.imread('darknet/dataset/1.jpg',cv2.IMREAD_COLOR)

print(img.shape)


# Left=892, Top=458, Right=982, Bottom=706


def make_dots(x1,y1,x2,y2):
    cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),5)
    a=(x1+x2)/2
    print(a)
    b=(y1+y2)/2
    print(b)
    cv2.circle(img,(int(a),int(b)), 10, (0,255,0), -1)


x1=1156
y1=235
x2=1174
y2=280

#make_dots(175,540,238,703)
#make_dots(358,536,429,682)
make_dots(x1,y1,x2,y2)
#cv2.imshow('image',img)

watch_face = img[y1:y2,x1:x2]
print(watch_face.shape)
img1 = Image.new('RGB', (4096, 4096), color = 'white')
img1.save('img1.jpg')
img1 = cv2.imread('img1.jpg')
img1= watch_face
print(img1.shape)
cv2.imshow('image',img)
cv2.imshow('image1',img1)
cv2.imwrite('img1.jpg',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()



cv2.waitKey(0)
cv2.destroyAllWindows()
