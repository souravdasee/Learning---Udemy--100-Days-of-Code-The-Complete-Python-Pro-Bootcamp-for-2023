def turn_right():
    turn_left()
    turn_left()
    turn_left()
def cycle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
repeat 6 :
    cycle()
