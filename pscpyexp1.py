from psychopy import visual, core, event

# Set up window
win = visual.Window(
    size=[800, 600],  # or your screen resolution, e.g., [1920, 1200]
    color=[-1, -1, -1],  # start with black
    units='pix',
    fullscr=False  # set True if you want fullscreen
)

# Define colors (RGB, range: -1 to 1 for PsychoPy)
colors = {
    'black': [-1, -1, -1],
    'white': [1, 1, 1],
    'yellow': [1, 1, -1],
    'red': [1, -1, -1],
    'grey': [0, 0, 0]
}

# Background color sequence
bg_colors = [colors['black'], colors['white'], colors['yellow'], colors['red'], colors['grey']]

# X cross parameters
cross_length = 40
line_width = 6
cross_color = colors['red']

# Line endpoints for the X (two lines, each with 2 endpoints)
# Line 1: top-left to bottom-right
# Line 2: bottom-left to top-right
line1 = [[-cross_length, -cross_length], [cross_length, cross_length]]
line2 = [[-cross_length, cross_length], [cross_length, -cross_length]]

# Create line stimuli
line1_stim = visual.Line(win, start=line1[0], end=line1[1], lineColor=cross_color, lineWidth=line_width)
line2_stim = visual.Line(win, start=line2[0], end=line2[1], lineColor=cross_color, lineWidth=line_width)

# Display loop
for bg in bg_colors:
    win.color = bg
    win.flip()
    
    line1_stim.draw()
    line2_stim.draw()
    
    win.flip()
    core.wait(3)

# Cleanup
win.close()
core.quit()
