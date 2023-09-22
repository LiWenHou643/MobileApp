from kivy.app import App
from kivy.uix.widget import Widget


class Voice(Widget):
    pass


class VoiceApp(App):
    def build(self):
        return Voice()


def on_touch_down(self, touch):
    if super().on_touch_down(touch):
        return True
    if not self.collide_point(touch.x, touch.y):
        return False
    print('you touched me!')
    return True


if __name__ == '__main__':
    VoiceApp().run()
