from gpiozero import Button
button = Button(19)

button.wait_for_press()
print('You pushed me')