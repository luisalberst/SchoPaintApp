n_version = 'version 0.0.2-beta'

from kivy.utils import platform
from kivy.core.window import Window
if platform != 'android':
    ## Normal Screen Start
    Window.size = (1000,600)
## Maximized
#Window.maximized()

import os
from random import random
import sys
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.uix.checkbox import CheckBox

class WindowManager(ScreenManager):
    pass

class MyPaintWidget(Widget):  

    def __init__(self, v = 'none', wline = 1, **kwargs):
        super(MyPaintWidget, self).__init__(**kwargs) 
        self.v = v
        self.wline = wline

    def set_val(self, v = 'none', h = 'none', s = 'none'):
        self.v = v
        self.h = h
        self.s = s
    
    def set_line(self):
        self.wline += 0.5

    def set_d_line(self):
        if self.wline != 1:
            self.wline -= 0.5

    def on_touch_down(self, touch):   
        if self.v == 'none':
            color = (random(), 1, 1)
        else:
            color = (float(self.v), float(self.h), float(self.s))
        with self.canvas:
            Color(*color, mode='hsv')
            d = .5
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            if self.wline == 1:
                touch.ud['line'] = Line(points=(touch.x, touch.y))
            else:
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=(self.wline))
        return super(MyPaintWidget, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        value = 'line'
        if value in touch.ud:
            touch.ud['line'].points += [touch.x, touch.y]
        return super(MyPaintWidget, self).on_touch_move(touch)

class FirstWindow(Screen):
    def __init__(self, **kw):
        super(FirstWindow, self).__init__(**kw)
        if platform != 'android':
            c_label = Label(
                text='FullScreen',
                size_hint = (None, None),
                size= (2340, 150),
                pos_hint= {'center_x': .2, 'center_y': .8},
                pos= (1, 900),
                font_size='15sp',
                bold= True,
                italic= True,
                outline_color= [0,0,0,1],
                outline_width= 2,
            )
            checkbox = CheckBox(
                pos_hint ={"x":.15, "y":.71},
                size_hint = (.1, .1)
            )
            checkbox.bind(active=self.on_checkbox_active)
            self.add_widget(checkbox)
            self.add_widget(c_label)
        
    def on_checkbox_active(self, checkbox, value):
        if value:
            ## FullScreen
            #Window.fullscreen = True
            Window.fullscreen = 'auto'
        else:
            ## FullScreen
            Window.fullscreen = False
            ## Windows size
            Window.size = (1000,600)

class SecondWindow(Screen):

    def __init__(self, **kw):
        super(SecondWindow, self).__init__(**kw)
        self.painter = MyPaintWidget()  
        self.ver_life = self.painter.wline
        ## Label
        self.title_label = Label(
            text='- Dibujo Libre -',
            size_hint = (None, None),
            size= (2340, 150),
            pos_hint= {'center_x': .5, 'center_y': .95},
            pos= (1, 900),
            font_size='35sp',
            bold= True,
            italic= True,
            outline_color= [0,0,0,1],
            outline_width= 5,
        )
        with self.title_label.canvas.before:  
            background_color= 1,1,1,1,          
            Color(rgba=background_color)
            Rectangle(pos=self.title_label.pos, size=self.title_label.size)    
        ## Size button
        ### More Size
        self.more_size = Button(text="Aumentar",
                    pos_hint={"center_x": .75, "center_y": .95},
                    size_hint = (.1,.068)
                )
        self.more_size.bind(on_press=self.more_line)
        ### Less Size
        self.less_size_off = Button(text="Disminuir",
                        pos_hint={"center_x": .25, "center_y": .95},
                        size_hint = (.1,.068),
                        disabled = True
                    )
        self.less_size = Button(text="Disminuir",
                    pos_hint={"center_x": .25, "center_y": .95},
                    size_hint = (.1,.068)
                )
        self.less_size.bind(on_press=self.less_line)
        ## End Size button
        ## BTN Clean
        self.clearbtn = Button(text="Limpiar",
            pos_hint={"center_x": .90, "center_y": .20},
            size_hint = (.1,.068)
        )
        self.clearbtn.bind(on_release=self.clear_canvas)
        # Color button
        ## Red
        self.red_color = Button(text="Rojo",
                    background_color = [1,0,0,1],
                    pos_hint={"center_x": .90, "center_y": .70},
                    size_hint = (.1,.068)
                )
        self.red_color.bind(on_press=self.red_canvas)
        ## Blue
        self.blue_color = Button(text="Azul",
                    background_color = [0,0,1,1],
                    pos_hint={"center_x": .90, "center_y": .60},
                    size_hint = (.1,.068)
                )
        self.blue_color.bind(on_press=self.blue_canvas)
        ## Green
        self.green_color = Button(text="Verde",
                    background_color = [0,1,0,1],
                    pos_hint={"center_x": .90, "center_y": .50},
                    size_hint = (.1,.068)
                )
        self.green_color.bind(on_press=self.green_canvas)
        ## purple
        self.purple_color = Button(text="Purpura",
                    background_color = [1,0,1,1],
                    pos_hint={"center_x": .90, "center_y": .40},
                    size_hint = (.1,.068)
                )
        self.purple_color.bind(on_press=self.purple_canvas)
        ## Random
        self.random_color = Button(text="Aleatorio",
                    background_color = [1,0,0,1],
                    pos_hint={"center_x": .90, "center_y": .30},
                    size_hint = (.1,.068)
                )
        self.random_color.bind(on_press=self.random_canvas)
        # End Color button        
        ## Show Button Widget
        self.show_b = Button(text="Mostrar",
            pos_hint={"center_x": .90, "center_y": .08},
            size_hint = (.15,.068))
        self.show_b.bind(on_press=self.show_bs)
        ## Hidden Button Widget
        self.hidden_b = Button(text="Ocultar",
            pos_hint={"center_x": .90, "center_y": .08},
            size_hint = (.15,.068))
        self.hidden_b.bind(on_press=self.hidden_bs)
        ## Add Widget
        self.add_widget(self.painter)
        self.add_widget(self.show_b)
        self.add_widget(self.title_label)
        self.add_widget(self.more_size)       

    def more_line(self, obj):
        self.painter.set_line()
        self.ver_life = self.painter.wline
        if self.ver_life > 1:
            self.remove_widget(self.less_size)
            self.remove_widget(self.less_size_off)
            self.add_widget(self.less_size)

    def less_line(self, obj):
        self.painter.set_d_line()
        self.ver_life = self.painter.wline
        if self.ver_life == 1:
            self.remove_widget(self.less_size)
            self.remove_widget(self.less_size_off)
            self.add_widget(self.less_size_off)

    def hidden_bs(self, obj):
        ## Buttons
        self.add_widget(self.show_b)
        self.remove_widget(self.hidden_b)
        self.remove_widget(self.red_color)
        self.remove_widget(self.blue_color)
        self.remove_widget(self.green_color)
        self.remove_widget(self.purple_color)
        self.remove_widget(self.random_color)
        self.remove_widget(self.clearbtn)
    
    def show_bs(self, obj):
        ## Buttons
        self.remove_widget(self.show_b)
        self.add_widget(self.hidden_b)
        self.add_widget(self.red_color)
        self.add_widget(self.blue_color)
        self.add_widget(self.green_color)
        self.add_widget(self.purple_color)
        self.add_widget(self.random_color)
        self.add_widget(self.clearbtn)
    
    def clear_canvas(self, obj):
        self.painter.canvas.clear()

    def random_canvas(self, obj):
        self.painter.set_val('none')

    def red_canvas(self, obj):
        self.painter.set_val(v='1',h='1',s='1') ## Red

    def blue_canvas(self, obj):
        self.painter.set_val(v='0.6',h='1',s='1') ## Blue
    
    def green_canvas(self, obj):
        self.painter.set_val(v='0.2',h='1',s='1') ## Green

    def purple_canvas(self, obj):
        self.painter.set_val(v='0.847',h='1',s='1') ## Purple

class ThirdWindow(Screen):
    pass

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

var_vct = resource_path("assets/vct-2.webp")

Builder.load_string("""
WindowManager:
    FirstWindow:
    SecondWindow:
    ThirdWindow:

<FirstWindow>:
    name: "first"
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        FloatLayout:
            Image:
                source: r'"""+var_vct+"""'
                allow_stretch: True
                keep_ratio: True
                size_hint_y: None
                size_hint_x: None
                width: self.parent.width
                height: self.parent.width/self.image_ratio
            Label:
                text: "Inter-Aprende"
                size: '.5','.5'
                pos_hint:{'center_x':.5,'center_y':.7}
                font_size: '50sp'
                bold: True
                italic: True
                outline_color: (16/255.0, 140/255.0, 47/255.0, 1)
                outline_width: 3
            Label:
                text: '"""+n_version+"""'
                size: '.5','.5'
                pos_hint:{'center_x':.7,'center_y':.55}
                font_size: '15sp'
                bold: True
                italic: True
                outline_color: (16/255.0, 140/255.0, 47/255.0, 1)
                outline_width: 2            
            Button:
                text:'Iniciar'
                background_color: 0 , 0 , 1 , 1
                pos_hint: {'x':.33,'y':.31}
                size_hint: '.18', '.12'
                on_release: app.root.current = "second"
            Button:
                text:'Creditos'
                pos_hint: {'x':.53,'y':.31}
                size_hint: '.18', '.12'
                on_release: app.root.current = "third"

<SecondWindow>:
    name: "second"

<ThirdWindow>
    name: "third"
    BoxLayout:
        FloatLayout:
            Label:
                text: "Elaborado por:"
                font_size: '40sp'
                pos_hint:{'center_x':.5,'center_y':.85}
                bold: True
                italic: True
            Label:
                text: "Hernández Luis / V-26.353.427"
                font_size: '32sp'
                pos_hint:{'center_x':.5,'center_y':.68}
            Label:
                text: "Vargas Maibelyn / V-29.876.979"
                font_size: '32sp'
                pos_hint:{'center_x':.5,'center_y':.56}   
            Button:
                text: "Volver Atras"
                pos_hint: {'center_x':.5,'center_y':.3}
                size_hint: '.18', '.12'
                on_release: app.root.current = "first" 

""")

class MainApp(App):
    def build(self):       
        if platform == 'android':
            from jnius import autoclass
            PythonActivity = autoclass("org.kivy.android.PythonActivity")
            ActivityInfo = autoclass("android.content.pm.ActivityInfo")
            activity = PythonActivity.mActivity
            activity.setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_LANDSCAPE)
        sm = WindowManager()

        screens = [FirstWindow(name="first"), SecondWindow(name="second"), ThirdWindow(name="third")]
        for screen in screens:
            sm.add_widget(screen)

        sm.current = "first"
        return sm 

if __name__ == '__main__':
    MainApp().run()
