# template for "Stopwatch: The Game"
import simplegui
# define global variables
t = 0
x = 0
y = 0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = t / 600
    n = t - A * 600
    B = n /100
    C = (n - B * 100) / 10
    D = n - B * 100 - C * 10
    return str(A)+':'+str(B)+str(C)+':'+str(D)
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def button_handler1():
    timer.start()
def button_handler2():
    global x
    global y
    timer.stop()
    y += 1
    if t%10 == 0:
        x += 1
def button_handler3():
    global t
    global x
    global y
    t = 0
    x = 0
    y = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(t), (50, 80) ,30, 'White','serif')
    canvas.draw_text(str(x)+'/'+str(y), (160,20),20,'Red','serif')
    
# create frame
frame = simplegui.create_frame('Stopwatch',200,150)

# register event handlers
button1 = frame.add_button('Start', button_handler1)
button2 = frame.add_button('Stop', button_handler2)
button3 = frame.add_button('Reset', button_handler3)

# start frame
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, timer_handler)
frame.start()

# Please remember to review the grading rubric
