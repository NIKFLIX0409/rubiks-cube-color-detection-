import cv2
from face_mapper import extract_face_colors

faces_order = ["U", "R", "F", "D", "L", "B"]
cube = {}

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not opening")
    exit()

print("Rubik's Cube Face Scanning")
print("Press 'c' to capture a face")
print("Press 'q' to quit")

face_index = 0

while face_index < len(faces_order):
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Show Cube Face", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        face_name = faces_order[face_index]
        img = cv2.resize(frame, (300, 300))

        face_colors = extract_face_colors(img)
        cube[face_name] = face_colors

        print(f"\nCaptured face {face_name}:")
        for row in face_colors:
            print(row)

        face_index += 1
        print("\nShow next face...")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("\nFinal Cube Data:")
for face, data in cube.items():
    print(f"\n{face} face:")
    for row in data:
        print(row)
