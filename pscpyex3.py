from psychopy import visual, core, event
import pandas as pd
import os
from datetime import datetime

# === Setup window ===
win = visual.Window(
    size=[800, 600],
    color=[0, 0, 0],
    units='pix',
    fullscr=False
)

# === Colors (PsychoPy uses [-1, 1] range) ===
grey = [0, 0, 0]
white = [1, 1, 1]
red = [1, -1, -1]

# === Plus sign parameters ===
line_length = 40
line_width = 6

horiz_line = visual.Line(
    win,
    start=(-line_length / 2, 0),
    end=(line_length / 2, 0),
    lineColor=red,
    lineWidth=line_width
)

vert_line = visual.Line(
    win,
    start=(0, -line_length / 2),
    end=(0, line_length / 2),
    lineColor=red,
    lineWidth=line_width
)

# === Show instruction screen ===
win.color = grey
horiz_line.draw()
vert_line.draw()

message = visual.TextStim(win, text='Press "s" to start', color=white)
message.draw()
win.flip()

while True:
    keys = event.getKeys()
    if 's' in keys:
        break
    elif 'escape' in keys or 'q' in keys:
        win.close()
        core.quit()

# === Show started message ===
win.color = grey
horiz_line.draw()
vert_line.draw()

start_message = visual.TextStim(win, text='Started! Press keys to record times.\nPress "q" or ESC to quit.', color=white)
start_message.draw()
win.flip()

# === Record keypress times ===
key_times = []
last_time = core.getTime()

print("Waiting for keys... (press 'q' or ESC to quit)")

while True:
    keys = event.getKeys(timeStamped=True)

    for key, timestamp in keys:
        if key in ['escape', 'q']:
            print("Exiting...")
            break

        dt = (timestamp - last_time) * 1000  # time diff in ms
        last_time = timestamp

        print(f'Key "{key}" pressed after {dt:.2f} ms')
        key_times.append((key, dt))

    if keys and keys[0][0] in ['escape', 'q']:
        break

# === Save ===
print("Recorded key times:", key_times)

if key_times:
    df = pd.DataFrame(key_times, columns=['Key', 'TimeDifference_ms'])

    now = datetime.now()
    date_str = now.strftime('%Y%m%d')
    time_str = f"{core.getTime():.4f}".replace('.', '')
    filename = f"{date_str}_{time_str}.csv"

    save_folder = os.getcwd()
    save_path = os.path.join(save_folder, filename)

    print(f"Saving to: {save_path}")
    df.to_csv(save_path, index=False)
    print(f'Saved keypress times to {save_path}')
else:
    print('No keys recorded.')

# === Cleanup ===
win.close()
core.quit()
