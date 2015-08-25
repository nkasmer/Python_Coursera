# template for "Stopwatch: The Game"
import simplegui

# define global variables
counter = 0
successes = 0
efforts = 0
running = False


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minutes = t / 600
    seconds = (t % 600)/10
    tenths = t % 10
    str_mins = str(minutes)
    if seconds < 10:
        str_secs = "0" + str(seconds) 
    else:
        str_secs = str(seconds)
    str_tenths = str(tenths)
    return str_mins + ":" + str_secs + "." + str_tenths
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global running
    timer.start()
    running = True
    

def stop():
    global successes, efforts, counter, running
    timer.stop()
    if running:
        efforts += 1
        if counter % 10 == 0:
            successes += 1
    running = False
    

def reset():
    global counter, successes, efforts
    timer.stop()
    counter = 0
    successes = 0
    efforts = 0
    


# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter += 1
    


# define draw handler
def draw(canvas):
    canvas.draw_text(format(counter), [86, 174], 48, "White")
    canvas.draw_text(str(successes) + "/" + str(efforts), [250, 30], 24, "Red")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 300)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)

# start frame
frame.start()

# Please remember to review the grading rubric
