import arcade
import arcade.key

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "PinPong"

class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('/Users/macTSF/Desktop/UrbanProject/UrbanProject/practise/practica2game/ball2.png', 0.2)
        self.change_x = 5
        self.change_y = 5  

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        
        if self.right >= SCREEN_WIDTH:
            self.change_x = - self.change_x
        if self.left <= 0:
            self.change_x = - self.change_x
        if self.top >= SCREEN_HEIGHT:
            self.change_y = - self.change_y
        if self.top <= 0:
            self.change_y = - self.change_y

class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('/Users/macTSF/Desktop/UrbanProject/UrbanProject/practise/practica2game/bar2.png', 0.4)
        
        
        
    def update(self):
        self.center_x += self.change_x
        
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left <= 0:
            self.left = 0
        

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bar = Bar()
        self.ball = Ball()
        self.setup()

    def setup(self):
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 3

    def on_draw(self):
        self.clear((255, 255, 255))
        self.bar.draw()
        self.ball.draw()

    def update(self, delta):
        if arcade.check_for_collision(self.bar,self.ball):
            self.ball.change_y = - self.ball.change_y
        self.ball.update()
        self.bar.update()
        
    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.bar.change_x = 6

        if key == arcade.key.LEFT:
            self.bar.change_x = -6
            
    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0





if __name__ == "__main__":
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
