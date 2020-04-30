import numpy as np
import cv2
img = cv2.imread('darknet/dataset/1.jpg',cv2.IMREAD_COLOR)




# Left=892, Top=458, Right=982, Bottom=706


def make_dots(x1,y1,x2,y2):
    cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),5)
    a=(x1+x2)/2
    print(a)
    b=(y1+y2)/2
    print(b)
    cv2.circle(img,(int(a),int(b)), 10, (0,255,0), -1)
make_dots(175,540,238,703)
"""

make_dots(297,395,343,519)

make_dots(839,315,870,404)

make_dots(1223,284,1256,361)

make_dots(871,270,896,334)

make_dots(421,294,450,367)

make_dots(853,393,893,517)

make_dots(1156,235,1174,280)

make_dots(992,229,1009,269)

make_dots(775,241,792,294)

make_dots(575,264,594,318)

make_dots(224,318,258,403)

make_dots(1066,295,1099,374)

make_dots(806,273,833,341)

make_dots(1097,236,1117,274)

make_dots(845,225,862,270)

make_dots(215,409,264,535)

make_dots(270,548,342,689)
make_dots(358,536,429,682)

"""
#make_dots(1097,236,1117,274)

#make_dots(744,392,766,449)
#make_dots(588,421,628,530)
#make_dots(141,503,205,669)
#make_dots(655,347,703,474)
"""
make_dots(232,632,298,803)

make_dots(234,629,292,797)
make_dots(581,412,625,544)

make_dots(588,421,628,530)
make_dots(577,403,621,527)

make_dots(744,392,766,449)
make_dots(676,393,699,444)
make_dots(676,393,699,444)
make_dots(646, 401,674, 486)
make_dots(655,347,703,474)
"""

cv2.imshow('image',img)
    
cv2.waitKey(0)
cv2.destroyAllWindows()



