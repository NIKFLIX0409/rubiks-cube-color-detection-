import cv2
from face_mapper import extract_face_colors

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not opening")
    exit()

print("Press 'c' to capture cube face")
print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Camera - Show Cube Face", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        img = cv2.resize(frame, (300, 300))
        face = extract_face_colors(img)

        print("\nDetected Cube Face:")
        for row in face:
            print(row)

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
