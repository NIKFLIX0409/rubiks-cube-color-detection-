import cv2
import numpy as np
from color_detector import get_color

def extract_face_colors(image):
    h, w, _ = image.shape
    step_x = w // 3
    step_y = h // 3

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    face = []

    for row in range(3):
        face_row = []
        for col in range(3):
            cx = col * step_x + step_x // 2
            cy = row * step_y + step_y // 2

            y1 = max(cy - 5, 0)
            y2 = min(cy + 5, hsv.shape[0])
            x1 = max(cx - 5, 0)
            x2 = min(cx + 5, hsv.shape[1])

            roi = hsv[y1:y2, x1:x2]

            h_val = int(roi[:, :, 0].mean())
            s_val = int(roi[:, :, 1].mean())
            v_val = int(roi[:, :, 2].mean())

            color = get_color(h_val, s_val, v_val)
            face_row.append(color)

        face.append(face_row)

    return face
