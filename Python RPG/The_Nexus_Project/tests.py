from ursina import *

app = Ursina()

def input(key):
    if key == 'space':
        print("Space pressed")
app.run()