from livewires import games
games.init(screen_width=640, screen_height=480, fps=50)

wall_image = games.load_image("wall.jpg", transparent=False)
games.screen.background = wall_image
games.screen.mainloop()


#! NOT AVAILABLE for python 3

""" 
Object          Description

screen          Provides access to the graphics screen—the region on which graphics objects may exist, move, and interact.
mouse           Provides access to the mouse.
keyboard        Provides access to the keyboard.

Sprite          For graphics objects that can be displayed on the graphics screen.
Text            A subclass of Sprite. For text objects displayed on the graphics screen.
Message         A subclass of Text. For text objects displayed on the graphics screen that disappear after a set period of time.
"""

""" 
Property        Description

width           Width of screen.
height          Height of screen.
fps             Frames per second screen is updated. (the number of times the screen will update itself every second)
background      Background image of screen.
all             objects List of all the sprites on the screen.
event_grab      Boolean that determines if input is grabbed to screen. True for input grabbed to screen.False for input not grabbed to screen.
"""

""" 
Method          Description

add(sprite)     Adds sprite, a Sprite object (or an object of a Sprite subclass), to the graphics screen.
clear()         Removes all sprites from the graphics screen.
mainloop()      Starts the graphics screen’s main loop.
quit()          Closes the graphics window.
"""

# Sprite
""" 
Property                    Description

angle                       Facing in degrees.
x                           x-coordinate.
y                           y-coordinate.
dx                          x velocity.
dy                          y velocity.
left                        x-coordinate of left sprite edge.
right                       x-coordinate of right sprite edge.
top                         y-coordinate of top sprite edge.
bottom                      y-coordinate of bottom sprite edge.
image                       Image object of sprite.
overlapping_sprites         List of other objects that overlap sprite.
is_collideable              Whether or not sprite is collideable. True means sprite will register in collisions. False means sprite will not show up in collisions.
"""
""" 
Method          Description
update()        Updates sprite. Automatically called every mainloop() cycle.
destroy()       Removes sprite from the screen.
"""

# Text
""" 
Property        Description
value           Value to be displayed as text.
color           Color of text.
"""

# Color
""" 
Attributes      Description
lifetime        Number of mainloop() cycles before object destroys itself. 0 means never destroy itself. The default value is 0.
after_death     Function or method to be run after object destroys itself. The default value is None.
"""

# mouse
""" 
Property        Description
x               x-coordinate of mouse pointer.
y               y-coordinate of mouse pointer.
is_visible      Boolean value for setting visibility of mouse pointer. True is visible while False is not visible. Default value is True.
"""
