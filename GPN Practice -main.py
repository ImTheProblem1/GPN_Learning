# Imports go at the top
from microbit import *
import random

display.show(Image.TARGET)
sleep(1000)
display.clear()

actions = ["press a", "press b"]
action = random.choice(actions)
print(action)

start_time = running_time()
end_time = start_time = 10000
score = 0
while running_time() < end_time:
    print(action)
    if action == "press a":
        display.show(Image.ARROW_W)
        if button_a.is_pressed() == True:
            display.show(Image.SMILE)
            score += 1
        else:
            continue
    
    if action == "press b":
        display.show(Image.ARROW_E)
        if button_b.is_pressed() == True:
            display.show(Image.SMILE)
            score += 1
    sleep(500)
    action = random.choice(actions)

display.scroll(str(score))