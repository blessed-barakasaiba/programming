from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
from kivymd.app import MDApp
from kivy.lang import Builder
import random

# Set window size
Window.size = (360, 600)

# Paddle Widget
class Paddle(Widget):
    pass

# Ball Widget
class Ball(Widget):
    speed_y = NumericProperty(0)

    def move(self):
        self.y += self.speed_y

class GameScreen(FloatLayout):
    score = NumericProperty(0)
    ball_speed = NumericProperty(-4)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update, 1 / 60)

    def on_touch_move(self, touch):
        if touch.x < Window.width - self.ids.paddle.width / 2 and touch.x > self.ids.paddle.width / 2:
            self.ids.paddle.center_x = touch.x

    def spawn_ball(self):
        ball = Ball()
        ball.size_hint = (None, None)
        ball.size = (50, 50)
        ball.x = random.randint(0, Window.width - ball.width)
        ball.y = Window.height
        ball.speed_y = self.ball_speed
        self.add_widget(ball)

    def update(self, dt):
        # Move all balls
        for child in self.children[:]:
            if isinstance(child, Ball):
                child.move()

                # Check if the ball goes below the screen
                if child.y < 0:
                    self.remove_widget(child)

                # Check if the ball hits the paddle
                if child.collide_widget(self.ids.paddle):
                    self.remove_widget(child)
                    self.score += 1

        # Spawn balls at random intervals
        if random.randint(1, 100) < 3:
            self.spawn_ball()

class CatchTheBallApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        return Builder.load_file('catch.kv')

if __name__ == '__main__':
    CatchTheBallApp().run()
