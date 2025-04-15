import cv2
from numpy import asarray
from pupil_apriltags import Detection
from pupil_apriltags import Detector
import math

# Initialize the detector and the video capture object.
at_detector = Detector(
    families="tag36h11",
    nthreads=1,
    quad_decimate=1.0,
    quad_sigma=0.0,
    refine_edges=1,
    decode_sharpening=0.25,
    debug=0
)
cap = cv2.VideoCapture(0)

# Keep looping until the user quits.
while cap.isOpened():
    # Capture the next frame.
    succes, image = cap.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    tags=at_detector.detect(asarray(gray),False,)
    color_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

    # Check if the tags list is not empty.
    if len(tags) == 2:
        # Find the center points of the two tags.
        tag1_center = tags[0].center
        tag2_center = tags[1].center

        # Calculate the distance between the two center points.
        distance = math.sqrt((tag1_center[0] - tag2_center[0])**2 + (tag1_center[1] - tag2_center[1])**2)

        # Display the distance.
        cv2.putText(
            color_img,
            str(distance),
            org=(
                tag1_center[0],
                tag1_center[1] + 20,
            ),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1,
            color=(0, 255, 0),
        )

    cv2.imshow("image1",color_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
