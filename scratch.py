import cv2
from numpy import asarray
from pupil_apriltags import Detection
from pupil_apriltags import Detector
import math

# image = cv2.imread('images/example_03.png')
x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
y2 = 0
y1 = 0
y3 = 0
y4 = 0
y5 = 0

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

at_detector = Detector(
    families="tag36h11",
    nthreads=1,
    quad_decimate=1.0,
    quad_sigma=0.0,
    refine_edges=1,
    decode_sharpening=0.25,
    debug=0
)
while cap.isOpened():
    succes, image = cap.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    tags = at_detector.detect(asarray(gray), False, )
    color_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

    for tag in tags:
        for idx in range(len(tag.corners)):
            cv2.line(
                color_img,
                tuple(tag.corners[idx - 1, :].astype(int)),
                tuple(tag.corners[idx, :].astype(int)),
                (255, 0, 0), 2
            )
        cv2.putText(
            color_img,
            str(tag.tag_id),
            org=(
                tag.corners[0, 0].astype(int) ,
                tag.corners[0, 1].astype(int) ,
            ),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=3,
            color=(0, 255,0),
        )
        cv2.circle(
            color_img,
            (
                int(tag.center[0]),
                int(tag.center[1]),
            ), 5, (0, 0, 255), -1)
        axis = "X =" + str(int(tag.center[0])) + " Y =" + str(int(tag.center[1]))
        cv2.putText(
            color_img,
            axis,
            (40, 30),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=1,
            color=(0, 255, 0), thickness=2
        )
        # for number in range(0,tag.tag_id):
        #  i=30
        #  cv2.putText(color_img, "X =", (0, i+20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
        #  cv2.putText(color_img, str(int(tag.center[0])), (40, i+20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
        #  cv2.putText(color_img, "Y =", (100, i+20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
        #  cv2.putText(color_img, str(int(tag.center[1])), (140, i+20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
        # num2 = 2
        # num3 = 3
        #
        if str(tag.tag_id) == "5":
            x1, y1 = tag.center[0].astype(int), tag.center[1].astype(int)
            # print("x1",x1,"y1",y1)
        if str(tag.tag_id) == "4":
            x2, y2 = tag.center[0].astype(int), tag.center[1].astype(int)
            # print("x2",x2,"y2",y2)
        if str(tag.tag_id) == "2":
            x3, y3 = tag.center[0].astype(int), tag.center[1].astype(int)
            # print("x3",x3,"y3",y3)
        if str(tag.tag_id) == "3":
            x4, y4 = tag.center[0].astype(int), tag.center[1].astype(int)
            # print("x4",x4,"y4",y4)
        if str(tag.tag_id) == "1":
                x5, y5 = tag.center[0].astype(int), tag.center[1].astype(int)
                # print("x5", x5, "y5", y5)

    distance_x = x2 - x1
    # print(distance_x)
    real_x = 76 * x5 / 555
    real_y = 55 * y5 /421
    print(real_x,real_y)
    # distance_y = y2 - y1
    # print(distance_y)
    # distance = math.sqrt((x2 - x1) * 2) + ((y2 - y1) * 2)3
      # print(distance)

    cv2.imshow("image1", color_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# print(int(tag.center[0]))
# print(int(tag.center[1]))
# print(tag.tag_id)

# print(at_detector)
cap.release()
cv2.destroyAllWindows()
