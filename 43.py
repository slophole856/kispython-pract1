import math
import tkinter as tk

def draw(shader, width, height):
    image = bytearray((0, 0, 0) * width * height)
    for y in range(height):
        for x in range(width):
            pos = (width * y + x) * 3
            color = shader(x / width, y / height)
            normalized = [max(min(int(c * 255), 255), 0) for c in color]
            image[pos:pos + 3] = normalized
    header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
    return header + image

def main(shader):
    label = tk.Label()
    img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
    label.pack()
    label.config(image=img)
    tk.mainloop()

def shader(x, y):
    cx = x - 0.5
    cy = y - 0.5
    
    distance = math.sqrt(cx*cx + cy*cy)

    angle = math.atan2(cy, cx)
    mouth_angle = 30 * math.pi / 180
    
    radius = 0.4

    eye_x = 0.45
    eye_y = 0.25
    eye_radius = 0.07
    
    eye_cx = x - eye_x
    eye_cy = y - eye_y
    eye_distance = math.sqrt(eye_cx*eye_cx + eye_cy*eye_cy)
    
    if distance <= radius:
        if abs(angle) < mouth_angle:
            return 0.0, 0.0, 0.0
        else:
            if eye_distance <= eye_radius:
                return 0.0, 0.0, 0.0
            else:
                return 1.0, 1.0, 0.0
    else:
        return 0.0, 0.0, 0.0

main(shader)