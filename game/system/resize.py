from . import globals_file as gf
# screen_starting_w / starting_w = x
# screen_w / x = return
def resize_x(starting_screen_width, size_for_the_starting_screen_width, screen_width):
    """you can resize the width of your objects with the original screen width and the width of the object in that screen width
    -> returns int or float <-"""
    x = starting_screen_width / size_for_the_starting_screen_width
    return screen_width / x

# screen_starting_h / starting_h = y
# screen_h / y = return
def resize_y(starting_screen_height, size_for_the_starting_screen_height, screen_height):
    """you can resize the height of your objects with the original screen height and the height of the object in that screen height
    -> returns int or float <-"""
    y = starting_screen_height / size_for_the_starting_screen_height
    return screen_height / y

#-----------------------------------------------------------------------------------#
def resize(
    screen,
    original_screen_width = 900,
    original_screen_height = 500,
    size_for_the_original_screen_width = 10,
    size_for_the_original_screen_height = 10
    ):
    """you can resize your objects with the original screen size and the size of this object for the original screen size
    -> return a tuple of the width and hight of the object in the current screen resolution <-"""
    width = resize_x(original_screen_width, size_for_the_original_screen_width, screen.get_width())
    hight = resize_y(original_screen_height, size_for_the_original_screen_height, screen.get_height())
    return (width, hight)

#-----------------------------------------------------------------------------------#
def change_xy(screen_width, screen_height, width_before, height_before, obj):
    """
    for none static objects only!
    change the pos of the object based on the resizing of the screen
    -> return object, width_before and height_before <-
    """
    if (screen_width != width_before) or (screen_height != height_before):
        objx = obj.x
        objy = obj.y
        sw = screen_width
        sh = screen_height
        firstsetpx = objx / width_before
        firstsetpy = objy / height_before
        obj.x = firstsetpx * sw
        obj.y = firstsetpy * sh
        gf.width_before = sw
        gf.height_before = sh
        return obj