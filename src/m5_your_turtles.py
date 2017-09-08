"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Jing Lin.
"""
########################################################################
# done: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
window.delay(20)
one=rg.SimpleTurtle('turtle')
two=rg.SimpleTurtle('turtle')
one.pen=rg.Pen('blue',10)
two.pen=rg.Pen('red',10)
one.speed=100
size=100
angle=90
for k in range(10):
    one.forward(size)
    two.backward(-size)
    one.right(angle-5*k)
    two.right(angle-5*k)
    one.forward(size)
    two.backward(-size)
    size=size-10
window.close_on_mouse_click()