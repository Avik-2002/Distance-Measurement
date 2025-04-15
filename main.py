import cv2
from numpy import asarray
from pupil_apriltags import Detection
from pupil_apriltags import Detector
# image = cv2.imread('images/example_03.png')
x1=0
x2=0
y1=0
y2=0
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


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
    succes, image =cap.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    tags=at_detector.detect(asarray(gray),False,)
    color_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

    for tag in tags:
         for idx in range(len(tag.corners)):
            cv2.line(
                color_img,
                tuple(tag.corners[idx - 1, :].astype(int)),
                tuple(tag.corners[idx, :].astype(int)),
                (255, 0, 0),2
            )

         cv2.putText(
            color_img,
            str(tag.tag_id),
            org=(
                tag.corners[0, 0].astype(int) ,
                tag.corners[0, 1].astype(int) ,
            ),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1,
            color=(0, 255,0)
         )
         cv2.circle(
            color_img,
            (
                int(tag.center[0]),
                int(tag.center[1]),

            ), 5, (0, 0, 255), -1)
         axis ="X =" + str(int(tag.center[0])) + " Y =" + str(int(tag.center[1]))
         new_axis = "X'=" + str(int((1 / 1.8) * (tag.center[0]))) + "Y'=" + str(int((1 / 1.6) * (tag.center[1])))
         print(axis + "\t\t\t" + new_axis)
         cv2.putText(
            color_img,
            axis,
             org=(
                 tag.corners[0, 0].astype(int),
                 tag.corners[0, 1].astype(int),
             )
             ,
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=1,
            color=(0, 255,0),thickness=1
         )
         # for number in range(0,tag.tag_id):
         #  i=30
         #  cv2.putText(color_img, "X =", (0, i+20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
         #  cv2.putText(color_img, str(int(tag.center[0])), (40, i+20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
         #  cv2.putText(color_img, "Y =", (100, i+20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
         #  cv2.putText(color_img, str(int(tag.center[1])), (140, i+20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)

    cv2.imshow("image1",color_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# print(int(tag.center[0]))
# print(int(tag.center[1]))
# print(tag.tag_id)

# print(at_detector)
cap.release()
cv2.destroyAllWindows()
