from psychopy import visual, core, event
import os
import random
from glob import glob

# === Setup window ===
win = visual.Window(
    size=[800, 600],
    color=[0, 0, 0],  # will change to grey below
    units='pix',
    fullscr=False
)

# === Colors ===
grey = [0, 0, 0]
red = [1, -1, -1]

# === Plus sign drawing ===
def draw_plus():
    line_length = 20
    line_width = 4
    horiz = visual.Line(
        win,
        start=(-line_length, 0),
        end=(line_length, 0),
        lineColor=red,
        lineWidth=line_width
    )
    vert = visual.Line(
        win,
        start=(0, -line_length),
        end=(0, line_length),
        lineColor=red,
        lineWidth=line_width
    )
    horiz.draw()
    vert.draw()

# === Show start screen ===
win.color = grey
draw_plus()
start_text = visual.TextStim(win, text='Press "s" to start', color=[1,1,1])
start_text.draw()
win.flip()

# Wait for 's' key to start or quit on 'escape' or 'q'
while True:
    keys = event.getKeys()
    if 's' in keys:
        break
    elif 'escape' in keys or 'q' in keys:
        win.close()
        core.quit()

# === Get image files in current script folder ===
script_folder = os.path.dirname(os.path.abspath(__file__))
extensions = ['*.png', '*.jpg', '*.jpeg', '*.bmp', '*.tif']
img_files = []
for ext in extensions:
    img_files.extend(glob(os.path.join(script_folder, ext)))

# === Randomize image order ===
random.shuffle(img_files)

# === Loop through images ===
for img_path in img_files:
    win.color = grey
    draw_plus()
    win.flip()
    core.wait(random.uniform(0.8, 1.5))

    image_stim = visual.ImageStim(win, image=img_path)
    image_stim.draw()
    win.flip()
    core.wait(0.3)

# === Final red plus on grey background ===
win.color = grey
draw_plus()
win.flip()
core.wait(1)

# === Cleanup ===
win.close()
core.quit()
