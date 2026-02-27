# "Stopwatch: The Game"

import simplegui

# defining global variables

time=0
timershow='0:00.0'
x=0
y=0
minutes =0
seconds =0
tenths =0
running=False
 

    
def format(t):
    '''
    helper function format that converts time
    in tenths of seconds into formatted string A:BC.D
    '''
    global seconds,minutes,tenths
    
    minutes = t / 600
    seconds = (t % 600) / 10
    tenths = t % 10
    
    if seconds < 10:
        
        return str(minutes) + ":0" + str(seconds) + "." + str(tenths)
    
    else:
        
        return str(minutes) + ":" + str(seconds) + "." + str(tenths)



def start():
    '''
    Starts the stopwatch
    '''
    
    timer.start()
    
    return

def stop():
    '''
    Stops the stopwatch and upadtes the score
    
    '''
    
    global x,y,tenths,running
    
    if running ==True and tenths==0:
        
        x+=1
        
    if running==True:
        
        y+=1
        running=False
        
    timer.stop()
    
    return

def reset():
    '''
    Resets the stopwatch and scores
    
    '''
    
    global timershow,time,x,y
    
    time=0 
    stop()
    timershow=format(0)
    x=0
    y=0
    
    return


def create_timer():
    '''
    event handler for timer with 0.1 sec interval
    '''
    
    global time,timershow,running
    
    running=True
    timershow=format(time)
    int(time)
    time+=1
    
    return

#draw handler

def draw_handler(canvas):
    
    global time,timershow
    
    canvas.draw_text(str(timershow),(120,160),30,'white')
    canvas.draw_text(str(x)+'/'+str(y),(240,50),30,'red')
    
#create frame

frame = simplegui.create_frame('Stopwatch', 300, 300)

# registering event handlers

timer = simplegui.create_timer(100, create_timer)
frame.set_draw_handler(draw_handler)
frame.add_button("start",start,180)
frame.add_button("stop",stop,180)
frame.add_button("reset",reset,180)

# start frame
frame.start()


