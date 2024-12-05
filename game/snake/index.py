# snake.py

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
from random import randint
 
SNAKE_SIZE = 20
CELL_SIZE = 20
GRID_SIZE = (20, 20)
UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class SnakeGame(Widget):
    def __init__(self, **kwargs):
        super(SnakeGame, self).__init__(**kwargs)
        self.snake = [(5, 5)]
        self.direction = RIGHT
        self.apple_pos = self.generate_apple()
        self.score = 0
        self.bind(on_touch_down=self.on_touch_down)
        Clock.schedule_interval(self.update, 1/10)

    def on_touch_down(self, instance, touch):
        x, y = touch.pos
        if abs(x - self.snake[0][0]) > abs(y - self.snake[0][1]):
            self.direction = LEFT if x < self.snake[0][0] else RIGHT
        else:
            self.direction = DOWN if y < self.snake[0][1] else UP

    def generate_apple(self):
        return (randint(0, GRID_SIZE[0] - 1), randint(0, GRID_SIZE[1] - 1))

    def update(self, dt):
        new_head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])

        if new_head in self.snake or not (0 <= new_head[0] < GRID_SIZE[0]) or not (0 <= new_head[1] < GRID_SIZE[1]):
            self.snake = [(5, 5)]
            self.direction = RIGHT
            self.score = 0

        self.snake.insert(0, new_head)

        if new_head == self.apple_pos:
            self.score += 1
            self.apple_pos = self.generate_apple()
        else:
            self.snake.pop()

        self.canvas.clear()
        with self.canvas:
            for segment in self.snake:
                Rectangle(pos=(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE), size=(SNAKE_SIZE, SNAKE_SIZE))
            Rectangle(pos=(self.apple_pos[0] * CELL_SIZE, self.apple_pos[1] * CELL_SIZE), size=(SNAKE_SIZE, SNAKE_SIZE))

class SnakeApp(App):
    def build(self):
        game = SnakeGame()
        Window.size = (GRID_SIZE[0] * CELL_SIZE, GRID_SIZE[1] * CELL_SIZE)
        return game

if __name__ == '__main__':
    SnakeApp().run()
