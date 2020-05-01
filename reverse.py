import numpy as np
import cv2
img = cv2.imread('/home/ahmed/Desktop/Planning/1.jpg',cv2.IMREAD_COLOR)

#cv2.rectangle(img,(894,458),(982,706),(0,0,255),5)
#975.17032471,339.61942762
#976.98126274,237.94703286
#882.88791445,334.29773593
a=882
b=334
cv2.circle(img,(int(a),int(b)), 10, (0,255,0), -1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Left=892, Top=458, Right=982, Bottom=706
