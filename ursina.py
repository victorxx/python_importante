from ursina import *


app=Ursina()
cube=Entity(
    model='cube',
    color=color.red,
    scale=2
)
def update():
    cube.rotation_x+=1

app.run()
