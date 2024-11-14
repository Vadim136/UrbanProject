import arcade


SCREEN_WIDTH = 800
SCREEN_HIGTH = 600
SCREEN_TITLE = "PinPong"

class Bar(arcade.Sprite):
    
    def __init__(self):
        super().__init__('bar.png', 1.0)
        
    
    pass




class Game(arcade.Window):
    
    def __init__(self, width, higth, title):
        super().__init__(width, higth, title)
        self.bar = Bar()

    def on_draw(self):
        self.clear((255,255,255))
        self.bar.draw()
    pass

if __name__ == "__main__":
    window = Game(SCREEN_WIDTH, SCREEN_HIGTH, SCREEN_TITLE)
    arcade.run()