import cv2, os
cap = cv2.VideoCapture(0)

DATA_DIR = "./training_data"
NUM_CLASSES = 26
DATASET_SIZE = 100

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

cap = cv2.VideoCapture(0)

classes_to_letters = {}

for j in range(NUM_CLASSES):
    # make data directories and populate the dictionary
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))
    classes_to_letters[j] = chr(ord("a") + j)
    print("Collecting data for class {}:".format(classes_to_letters[j]))

    while True:
        # waiting window
        ret, frame = cap.read()
        cv2.putText(frame, "Press S to start collecting", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow("frame", frame)
        if cv2.waitKey(25) == ord("s"): break

    c = 0
    while c < DATASET_SIZE:
        # data collection window
        ret, frame = cap.read()
        cv2.imshow("frame", frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(j), "{}.jpg".format(c)), frame)
        c += 1

# releasing resources and closing windows
cap.release()
cv2.destroyAllWindows()
print(classes_to_letters)
