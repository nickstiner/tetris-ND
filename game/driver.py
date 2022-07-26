# hello world
from Board import *
from Shape import *
from LPiece import *
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        self.shape_list = None

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.shape_list = arcade.SpriteList()
        
    
        pass

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        t = arcade.Sprite("assets/Tetris_L.png",0.1)
        t.center_x = 300
        t.center_y = 300

        t.draw()


        # Your drawing code goes here

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()