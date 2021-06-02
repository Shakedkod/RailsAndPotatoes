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
    -> return object <-
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

#-----------------------------------------------------------------------------------#
def tiles_xy(self):
    def change(self):
        objx = self.x
        objy = self.y
        sw = gf.screen_width
        sh = gf.screen_height
        firstsetpx = objx / gf.width_before
        firstsetpy = objy / gf.height_before
        self.x = firstsetpx * sw
        self.y = firstsetpy * sh
        return self
    
    if (gf.screen_width != gf.width_before) or (gf.screen_height != gf.height_before):
        #T1M1
        self.T1M1F1 = change(self.T1M1F1)
        self.T1M1F2 = change(self.T1M1F2)
        self.T1M1F3 = change(self.T1M1F3)
        self.T1M1F4 = change(self.T1M1F4)
        #T1M2
        self.T1M2F1 = change(self.T1M2F1)
        self.T1M2F2 = change(self.T1M2F2)
        self.T1M2F3 = change(self.T1M2F3)
        self.T1M2F4 = change(self.T1M2F4)
        #T1M3
        self.T1M3F1 = change(self.T1M3F1)
        self.T1M3F2 = change(self.T1M3F2)
        self.T1M3F3 = change(self.T1M3F3)
        self.T1M3F4 = change(self.T1M3F4)
        #T1M4
        self.T1M4F1 = change(self.T1M4F1)
        self.T1M4F2 = change(self.T1M4F2)
        self.T1M4F3 = change(self.T1M4F3)
        self.T1M4F4 = change(self.T1M4F4)
        #T2M1
        self.T2M1F1 = change(self.T2M1F1)
        self.T2M1F2 = change(self.T2M1F2)
        self.T2M1F3 = change(self.T2M1F3)
        self.T2M1F4 = change(self.T2M1F4)
        #T2M2
        self.T2M2F1 = change(self.T2M2F1)
        self.T2M2F2 = change(self.T2M2F2)
        self.T2M2F3 = change(self.T2M2F3)
        self.T2M2F4 = change(self.T2M2F4)
        #T2M3
        self.T2M3F1 = change(self.T2M3F1)
        self.T2M3F2 = change(self.T2M3F2)
        self.T2M3F3 = change(self.T2M3F3)
        self.T2M3F4 = change(self.T2M3F4)
        #T2M4
        self.T2M4F1 = change(self.T2M4F1)
        self.T2M4F2 = change(self.T2M4F2)
        self.T2M4F3 = change(self.T2M4F3)
        self.T2M4F4 = change(self.T2M4F4)
        #T3M1
        self.T3M1F1 = change(self.T3M1F1)
        self.T3M1F2 = change(self.T3M1F2)
        self.T3M1F3 = change(self.T3M1F3)
        self.T3M1F4 = change(self.T3M1F4)
        #T3M2
        self.T3M2F1 = change(self.T3M2F1)
        self.T3M2F2 = change(self.T3M2F2)
        self.T3M2F3 = change(self.T3M2F3)
        self.T3M2F4 = change(self.T3M2F4)
        #T3M3
        self.T3M3F1 = change(self.T3M3F1)
        self.T3M3F2 = change(self.T3M3F2)
        self.T3M3F3 = change(self.T3M3F3)
        self.T3M3F4 = change(self.T3M3F4)
        #T3M4
        self.T3M4F1 = change(self.T3M4F1)
        self.T3M4F2 = change(self.T3M4F2)
        self.T3M4F3 = change(self.T3M4F3)
        self.T3M4F4 = change(self.T3M4F4)
        #T4M1
        self.T4M1F1 = change(self.T4M1F1)
        self.T4M1F2 = change(self.T4M1F2)
        self.T4M1F3 = change(self.T4M1F3)
        self.T4M1F4 = change(self.T4M1F4)
        #T4M2
        self.T4M2F1 = change(self.T4M2F1)
        self.T4M2F2 = change(self.T4M2F2)
        self.T4M2F3 = change(self.T4M2F3)
        self.T4M2F4 = change(self.T4M2F4)
        #T4M3
        self.T4M3F1 = change(self.T4M3F1)
        self.T4M3F2 = change(self.T4M3F2)
        self.T4M3F3 = change(self.T4M3F3)
        self.T4M3F4 = change(self.T4M3F4)
        #T4M4
        self.T4M4F1 = change(self.T4M4F1)
        self.T4M4F2 = change(self.T4M4F2)
        self.T4M4F3 = change(self.T4M4F3)
        self.T4M4F4 = change(self.T4M4F4)
        #T5M1
        self.T5M1F1 = change(self.T5M1F1)
        self.T5M1F2 = change(self.T5M1F2)
        self.T5M1F3 = change(self.T5M1F3)
        self.T5M1F4 = change(self.T5M1F4)
        #T5M2
        self.T5M2F1 = change(self.T5M2F1)
        self.T5M2F2 = change(self.T5M2F2)
        self.T5M2F3 = change(self.T5M2F3)
        self.T5M2F4 = change(self.T5M2F4)
        #T5M3
        self.T5M3F1 = change(self.T5M3F1)
        self.T5M3F2 = change(self.T5M3F2)
        self.T5M3F3 = change(self.T5M3F3)
        self.T5M3F4 = change(self.T5M3F4)
        #T5M4
        self.T5M4F1 = change(self.T5M4F1)
        self.T5M4F2 = change(self.T5M4F2)
        self.T5M4F3 = change(self.T5M4F3)
        self.T5M4F4 = change(self.T5M4F4)
        #T6M1
        self.T6M1F1 = change(self.T6M1F1)
        self.T6M1F2 = change(self.T6M1F2)
        self.T6M1F3 = change(self.T6M1F3)
        self.T6M1F4 = change(self.T6M1F4)
        #T6M2
        self.T6M2F1 = change(self.T6M2F1)
        self.T6M2F2 = change(self.T6M2F2)
        self.T6M2F3 = change(self.T6M2F3)
        self.T6M2F4 = change(self.T6M2F4)
        #T6M3
        self.T6M3F1 = change(self.T6M3F1)
        self.T6M3F2 = change(self.T6M3F2)
        self.T6M3F3 = change(self.T6M3F3)
        self.T6M3F4 = change(self.T6M3F4)
        #T6M4
        self.T6M4F1 = change(self.T6M4F1)
        self.T6M4F2 = change(self.T6M4F2)
        self.T6M4F3 = change(self.T6M4F3)
        self.T6M4F4 = change(self.T6M4F4)
        #T7M1
        self.T7M1F1 = change(self.T7M1F1)
        self.T7M1F2 = change(self.T7M1F2)
        self.T7M1F3 = change(self.T7M1F3)
        self.T7M1F4 = change(self.T7M1F4)
        #T7M2
        self.T7M2F1 = change(self.T7M2F1)
        self.T7M2F2 = change(self.T7M2F2)
        self.T7M2F3 = change(self.T7M2F3)
        self.T7M2F4 = change(self.T7M2F4)
        #T7M3
        self.T7M3F1 = change(self.T7M3F1)
        self.T7M3F2 = change(self.T7M3F2)
        self.T7M3F3 = change(self.T7M3F3)
        self.T7M3F4 = change(self.T7M3F4)
        #T7M4
        self.T7M4F1 = change(self.T7M4F1)
        self.T7M4F2 = change(self.T7M4F2)
        self.T7M4F3 = change(self.T7M4F3)
        self.T7M4F4 = change(self.T7M4F4)
        #T8M1
        self.T8M1F1 = change(self.T8M1F1)
        self.T8M1F2 = change(self.T8M1F2)
        self.T8M1F3 = change(self.T8M1F3)
        self.T8M1F4 = change(self.T8M1F4)
        #T8M2
        self.T8M2F1 = change(self.T8M2F1)
        self.T8M2F2 = change(self.T8M2F2)
        self.T8M2F3 = change(self.T8M2F3)
        self.T8M2F4 = change(self.T8M2F4)
        #T8M3
        self.T8M3F1 = change(self.T8M3F1)
        self.T8M3F2 = change(self.T8M3F2)
        self.T8M3F3 = change(self.T8M3F3)
        self.T8M3F4 = change(self.T8M3F4)
        #T8M4
        self.T8M4F1 = change(self.T8M4F1)
        self.T8M4F2 = change(self.T8M4F2)
        self.T8M4F3 = change(self.T8M4F3)
        self.T8M4F4 = change(self.T8M4F4)
        #T9M1
        self.T9M1F1 = change(self.T9M1F1)
        self.T9M1F2 = change(self.T9M1F2)
        self.T9M1F3 = change(self.T9M1F3)
        self.T9M1F4 = change(self.T9M1F4)
        #T9M2
        self.T9M2F1 = change(self.T9M2F1)
        self.T9M2F2 = change(self.T9M2F2)
        self.T9M2F3 = change(self.T9M2F3)
        self.T9M2F4 = change(self.T9M2F4)
        #T9M3
        self.T9M3F1 = change(self.T9M3F1)
        self.T9M3F2 = change(self.T9M3F2)
        self.T9M3F3 = change(self.T9M3F3)
        self.T9M3F4 = change(self.T9M3F4)
        #T9M4
        self.T9M4F1 = change(self.T9M4F1)
        self.T9M4F2 = change(self.T9M4F2)
        self.T9M4F3 = change(self.T9M4F3)
        self.T9M4F4 = change(self.T9M4F4)
        #T10M1
        self.T10M1F1 = change(self.T10M1F1)
        self.T10M1F2 = change(self.T10M1F2)
        self.T10M1F3 = change(self.T10M1F3)
        self.T10M1F4 = change(self.T10M1F4)
        #T10M2
        self.T10M2F1 = change(self.T10M2F1)
        self.T10M2F2 = change(self.T10M2F2)
        self.T10M2F3 = change(self.T10M2F3)
        self.T10M2F4 = change(self.T10M2F4)
        #T10M3
        self.T10M3F1 = change(self.T10M3F1)
        self.T10M3F2 = change(self.T10M3F2)
        self.T10M3F3 = change(self.T10M3F3)
        self.T10M3F4 = change(self.T10M3F4)
        #T10M4
        self.T10M4F1 = change(self.T10M4F1)
        self.T10M4F2 = change(self.T10M4F2)
        self.T10M4F3 = change(self.T10M4F3)
        self.T10M4F4 = change(self.T10M4F4)
        #T11M1
        self.T11M1F1 = change(self.T11M1F1)
        self.T11M1F2 = change(self.T11M1F2)
        self.T11M1F3 = change(self.T11M1F3)
        self.T11M1F4 = change(self.T11M1F4)
        #T11M2
        self.T11M2F1 = change(self.T11M2F1)
        self.T11M2F2 = change(self.T11M2F2)
        self.T11M2F3 = change(self.T11M2F3)
        self.T11M2F4 = change(self.T11M2F4)
        #T11M3
        self.T11M3F1 = change(self.T11M3F1)
        self.T11M3F2 = change(self.T11M3F2)
        self.T11M3F3 = change(self.T11M3F3)
        self.T11M3F4 = change(self.T11M3F4)
        #T11M4
        self.T11M4F1 = change(self.T11M4F1)
        self.T11M4F2 = change(self.T11M4F2)
        self.T11M4F3 = change(self.T11M4F3)
        self.T11M4F4 = change(self.T11M4F4)
        #T12M1
        self.T12M1F1 = change(self.T12M1F1)
        self.T12M1F2 = change(self.T12M1F2)
        self.T12M1F3 = change(self.T12M1F3)
        self.T12M1F4 = change(self.T12M1F4)
        #T12M2
        self.T12M2F1 = change(self.T12M2F1)
        self.T12M2F2 = change(self.T12M2F2)
        self.T12M2F3 = change(self.T12M2F3)
        self.T12M2F4 = change(self.T12M2F4)
        #T12M3
        self.T12M3F1 = change(self.T12M3F1)
        self.T12M3F2 = change(self.T12M3F2)
        self.T12M3F3 = change(self.T12M3F3)
        self.T12M3F4 = change(self.T12M3F4)
        #T12M4
        self.T12M4F1 = change(self.T12M4F1)
        self.T12M4F2 = change(self.T12M4F2)
        self.T12M4F3 = change(self.T12M4F3)
        self.T12M4F4 = change(self.T12M4F4)
        #T13M1
        self.T13M1F1 = change(self.T13M1F1)
        self.T13M1F2 = change(self.T13M1F2)
        self.T13M1F3 = change(self.T13M1F3)
        self.T13M1F4 = change(self.T13M1F4)
        #T13M2
        self.T13M2F1 = change(self.T13M2F1)
        self.T13M2F2 = change(self.T13M2F2)
        self.T13M2F3 = change(self.T13M2F3)
        self.T13M2F4 = change(self.T13M2F4)
        #T13M3
        self.T13M3F1 = change(self.T13M3F1)
        self.T13M3F2 = change(self.T13M3F2)
        self.T13M3F3 = change(self.T13M3F3)
        self.T13M3F4 = change(self.T13M3F4)
        #T13M4
        self.T13M4F1 = change(self.T13M4F1)
        self.T13M4F2 = change(self.T13M4F2)
        self.T13M4F3 = change(self.T13M4F3)
        self.T13M4F4 = change(self.T13M4F4)
        #T14M1
        self.T14M1F1 = change(self.T14M1F1)
        self.T14M1F2 = change(self.T14M1F2)
        self.T14M1F3 = change(self.T14M1F3)
        self.T14M1F4 = change(self.T14M1F4)
        #T14M2
        self.T14M2F1 = change(self.T14M2F1)
        self.T14M2F2 = change(self.T14M2F2)
        self.T14M2F3 = change(self.T14M2F3)
        self.T14M2F4 = change(self.T14M2F4)
        #T14M3
        self.T14M3F1 = change(self.T14M3F1)
        self.T14M3F2 = change(self.T14M3F2)
        self.T14M3F3 = change(self.T14M3F3)
        self.T14M3F4 = change(self.T14M3F4)
        #T14M4
        self.T14M4F1 = change(self.T14M4F1)
        self.T14M4F2 = change(self.T14M4F2)
        self.T14M4F3 = change(self.T14M4F3)
        self.T14M4F4 = change(self.T14M4F4)
        #T15M1
        self.T15M1F1 = change(self.T15M1F1)
        self.T15M1F2 = change(self.T15M1F2)
        self.T15M1F3 = change(self.T15M1F3)
        self.T15M1F4 = change(self.T15M1F4)
        #T15M2
        self.T15M2F1 = change(self.T15M2F1)
        self.T15M2F2 = change(self.T15M2F2)
        self.T15M2F3 = change(self.T15M2F3)
        self.T15M2F4 = change(self.T15M2F4)
        #T15M3
        self.T15M3F1 = change(self.T15M3F1)
        self.T15M3F2 = change(self.T15M3F2)
        self.T15M3F3 = change(self.T15M3F3)
        self.T15M3F4 = change(self.T15M3F4)
        #T15M4
        self.T15M4F1 = change(self.T15M4F1)
        self.T15M4F2 = change(self.T15M4F2)
        self.T15M4F3 = change(self.T15M4F3)
        self.T15M4F4 = change(self.T15M4F4)
        #T16M1
        self.T16M1F1 = change(self.T16M1F1)
        self.T16M1F2 = change(self.T16M1F2)
        self.T16M1F3 = change(self.T16M1F3)
        self.T16M1F4 = change(self.T16M1F4)
        #T16M2
        self.T16M2F1 = change(self.T16M2F1)
        self.T16M2F2 = change(self.T16M2F2)
        self.T16M2F3 = change(self.T16M2F3)
        self.T16M2F4 = change(self.T16M2F4)
        #T16M3
        self.T16M3F1 = change(self.T16M3F1)
        self.T16M3F2 = change(self.T16M3F2)
        self.T16M3F3 = change(self.T16M3F3)
        self.T16M3F4 = change(self.T16M3F4)
        #T16M4
        self.T16M4F1 = change(self.T16M4F1)
        self.T16M4F2 = change(self.T16M4F2)
        self.T16M4F3 = change(self.T16M4F3)
        self.T16M4F4 = change(self.T16M4F4)

        gf.width_before = gf.screen_width
        gf.height_before = gf.screen_height
        return self