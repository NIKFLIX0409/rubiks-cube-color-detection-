import cv2
from face_mapper import extract_face_colors

img = cv2.imread("cube.jpg")

if img is None:
    print("Image not found")
    exit()

img = cv2.resize(img, (300, 300))

face = extract_face_colors(img)

print("Detected Cube Face:")
for row in face:
    print(row)

cv2.imshow("Cube Face", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
