import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"

POINT_1 = (SCREEN_WIDTH / 2, SCREEN_HEIGHT-10)
POINT_2 = (10, 10)
POINT_3 = (SCREEN_WIDTH - 10, 10)
STARTING_POINT = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

POINT_SIZE = 5


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_vector_to_midpoint(self, point):
        delta_x = (point.x - self.x)
        delta_y = (point.y - self.y)
        return delta_x // 2, delta_y // 2


class MySim(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)
        # self.set_update_rate(1)
        # If you have sprite lists, you should create them here,
        # and set them to None
        self.point_list = []
        self.shape_list = arcade.ShapeElementList()
        self.zeros_count = 0
        self.ones_count = 0
        self.twos_count = 0

    def setup(self):
        # Create your sprites and sprite lists here
        self.point_1 = Point(*POINT_1)
        self.point_2 = Point(*POINT_2)
        self.point_3 = Point(*POINT_3)
        self.starting_point = Point(*STARTING_POINT)
        self.point_list.append(self.point_1)
        self.point_list.append(self.point_2)
        self.point_list.append(self.point_3)
        self.point_list.append(self.starting_point)

        for point in self.point_list:
            shape = arcade.create_ellipse_filled(point.x, point.y, POINT_SIZE, POINT_SIZE, arcade.color.DARK_BLUE)
            self.shape_list.append(shape)

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()

        # Call draw() on all your sprite lists below
        self.shape_list.draw()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        random_number = random.randint(0, 2)
        old_point = self.point_list[-1]

        if random_number == 0:
            x, y = old_point.get_vector_to_midpoint(self.point_1)
            self.zeros_count += 1
        elif random_number == 1:
            x, y = old_point.get_vector_to_midpoint(self.point_2)
            self.ones_count += 1
        elif random_number == 2:
            x, y = old_point.get_vector_to_midpoint(self.point_3)
            self.twos_count += 1

        new_point = Point(old_point.x + x, old_point.y + y)
        # print(x, y)
        print(f"Zeros: {self.zeros_count}")
        print(f"Ones: {self.ones_count}")
        print(f"Twos: {self.twos_count}")

        self.point_list.append(new_point)
        shape = arcade.create_ellipse_filled(old_point.x + x, old_point.y + y, POINT_SIZE, POINT_SIZE, arcade.color.WHITE)
        self.shape_list.append(shape)


def main():
    """ Main method """
    sim = MySim(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    sim.setup()
    arcade.run()


if __name__ == "__main__":
    main()
