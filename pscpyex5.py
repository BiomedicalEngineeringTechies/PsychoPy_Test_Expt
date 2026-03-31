from psychopy import visual, core, event
import numpy as np
import random

# === Setup window ===
win = visual.Window(
    size=[800, 600],
    color=[0.5, 0.5, 0.5],  # grey background
    units='pix',
    fullscr=False
)

# Colors
grey = [0.5, 0.5, 0.5]
red = [1, -1, -1]
white = [1, 1, 1]

# Fixation cross parameters
cross_length = 20
cross_width = 4
xCenter, yCenter = 0, 0

# Shapes and styles
shapes = ['circle', 'square', 'triangle']
styles = ['solid', 'dashed', 'dotted']
num_trials = 5

def draw_fixation_cross():
    horiz_line = visual.Line(win, start=(-cross_length, 0), end=(cross_length, 0), lineColor=red, lineWidth=cross_width)
    vert_line = visual.Line(win, start=(0, -cross_length), end=(0, cross_length), lineColor=red, lineWidth=cross_width)
    horiz_line.draw()
    vert_line.draw()

def draw_circle(style):
    radius = 75
    if style == 'solid':
        circle = visual.Circle(win, radius=radius, edges=128, fillColor=white, lineColor=white)
        circle.draw()
    elif style == 'dashed':
        for angle in range(0, 360, 20):
            arc = visual.Arc(win, radius=radius*2, startAngle=angle, endAngle=angle+10, lineColor=white, lineWidth=2)
            arc.draw()
    elif style == 'dotted':
        for angle in range(0, 360, 20):
            rad = np.deg2rad(angle)
            x = radius * np.cos(rad)
            y = radius * np.sin(rad)
            dot = visual.Circle(win, radius=2, pos=(x, y), fillColor=white, lineColor=white)
            dot.draw()

def draw_square(style):
    size = 150
    half = size / 2
    if style == 'solid':
        rect = visual.Rect(win, width=size, height=size, fillColor=white, lineColor=white)
        rect.draw()
    elif style == 'dashed':
        dash_len = 10
        gap = 5
        x_starts = np.arange(-half, half, dash_len + gap)
        for x in x_starts:
            line = visual.Line(win, start=(x, half), end=(min(x + dash_len, half), half), lineColor=white, lineWidth=2)
            line.draw()
            line = visual.Line(win, start=(x, -half), end=(min(x + dash_len, half), -half), lineColor=white, lineWidth=2)
            line.draw()
        y_starts = np.arange(-half, half, dash_len + gap)
        for y in y_starts:
            line = visual.Line(win, start=(-half, y), end=(-half, min(y + dash_len, half)), lineColor=white, lineWidth=2)
            line.draw()
            line = visual.Line(win, start=(half, y), end=(half, min(y + dash_len, half)), lineColor=white, lineWidth=2)
            line.draw()
    elif style == 'dotted':
        step = 15
        xs = np.arange(-half, half + 1, step)
        ys = np.arange(-half, half + 1, step)
        for x in xs:
            dot_top = visual.Circle(win, radius=1.5, pos=(x, half), fillColor=white, lineColor=white)
            dot_top.draw()
            dot_bottom = visual.Circle(win, radius=1.5, pos=(x, -half), fillColor=white, lineColor=white)
            dot_bottom.draw()
        for y in ys:
            dot_left = visual.Circle(win, radius=1.5, pos=(-half, y), fillColor=white, lineColor=white)
            dot_left.draw()
            dot_right = visual.Circle(win, radius=1.5, pos=(half, y), fillColor=white, lineColor=white)
            dot_right.draw()

def draw_triangle(style):
    base = 100
    height = 100
    coords = np.array([
        [0, -height / 2],
        [-base / 2, height / 2],
        [base / 2, height / 2]
    ])

    if style == 'solid':
        tri = visual.ShapeStim(win, vertices=coords, fillColor=white, lineColor=white, closeShape=True)
        tri.draw()
    elif style == 'dashed':
        dash_len = 10
        gap = 5
        for i in range(3):
            p1 = coords[i]
            p2 = coords[(i + 1) % 3]
            vec = p2 - p1
            length = np.linalg.norm(vec)
            direction = vec / length
            dist = 0
            while dist < length:
                start = p1 + direction * dist
                end = p1 + direction * min(dist + dash_len, length)
                line = visual.Line(win, start=start, end=end, lineColor=white, lineWidth=2)
                line.draw()
                dist += dash_len + gap
    elif style == 'dotted':
        spacing = 15
        for i in range(3):
            p1 = coords[i]
            p2 = coords[(i + 1) % 3]
            vec = p2 - p1
            length = np.linalg.norm(vec)
            direction = vec / length
            dist = 0
            while dist < length:
                pos = p1 + direction * dist
                dot = visual.Circle(win, radius=1.5, pos=pos, fillColor=white, lineColor=white)
                dot.draw()
                dist += spacing

# === Show start screen ===
start_text = visual.TextStim(win, text='Press "s" to start', color=white)
win.color = grey
draw_fixation_cross()
start_text.draw()
win.flip()

# Wait for 's' key
while True:
    keys = event.getKeys()
    if 's' in keys:
        break
    elif 'escape' in keys or 'q' in keys:
        win.close()
        core.quit()

# === Main trials ===
try:
    for _ in range(num_trials):
        shape = random.choice(shapes)
        style = random.choice(styles)

        # Draw fixation cross
        win.color = grey
        draw_fixation_cross()
        win.flip()

        core.wait(random.uniform(0.8, 1.5))

        # Draw shape + fixation cross
        win.color = grey
        draw_fixation_cross()

        if shape == 'circle':
            draw_circle(style)
        elif shape == 'square':
            draw_square(style)
        elif shape == 'triangle':
            draw_triangle(style)

        win.flip()
        core.wait(0.3)

    win.close()
    core.quit()

except Exception as e:
    win.close()
    core.quit()
    raise e
