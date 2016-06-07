#!/usr/bin/python3

from kivy.interactive import InteractiveLauncher
from kivy.app import App

import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
from matplotlib.figure import Figure
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas,\
    NavigationToolbar2Kivy
from matplotlib.transforms import Bbox
import matplotlib.pyplot as plt

from kivy.uix.boxlayout import BoxLayout

def press(event):
    print('press released from test', event.x, event.y, event.button)

def release(event):
    print('release released from test', event.x, event.y, event.button)

def keypress(event):
    print('key down', event.key)

def keyup(event):
    print('key up', event.key)

def motionnotify(event):
    print('mouse move to ', event.x, event.y)

def resize(event):
    print('resize from mpl ', event)

def scroll(event):
    print('scroll event from mpl ', event.x, event.y, event.step)

def figure_enter(event):
    print('figure enter mpl')

def figure_leave(event):
    print('figure leaving mpl')

def close(event):
    print('closing figure')

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                '%d' % int(height), ha='center', va='bottom')

def callback(instance):
    autolabel(rects1)
    autolabel(rects2)
    canvas.draw()

class CMplGraph(BoxLayout):

    def __init__(self, **kwargs):
        super(CMplGraph, self).__init__(**kwargs)
        self.create_plot()

    def create_plot(self):

        fig, ax = plt.subplots()

        xCoords = [1,2,3]
        yCoords = [1,4,9]

        # Plot the data
        lineA = ax.plot(xCoords, yCoords, color='blue', marker='o', markerfacecolor='blue', markersize=6)
        ax.set_ylim([0, 10])

        # Connect Matplotlib events to our own callbacks using Matplotlib's mpl_connect method
        fig.canvas.mpl_connect('button_press_event', press)
        fig.canvas.mpl_connect('button_release_event', release)
        fig.canvas.mpl_connect('key_press_event', keypress)
        fig.canvas.mpl_connect('key_release_event', keyup)
        fig.canvas.mpl_connect('motion_notify_event', motionnotify)
        fig.canvas.mpl_connect('resize_event', resize)
        fig.canvas.mpl_connect('scroll_event', scroll)
        fig.canvas.mpl_connect('figure_enter_event', figure_enter)
        fig.canvas.mpl_connect('figure_leave_event', figure_leave)
        fig.canvas.mpl_connect('close_event', close)

        canvas = fig.canvas

        # Add each navigation toolbar and canvas to our BoxLayout
        nav1 = NavigationToolbar2Kivy(canvas)
        self.add_widget(nav1.actionbar)
        self.add_widget(canvas)

class GuiApp(App):
    pass

# Entry point

if __name__ == '__main__':
    INTERACTIVE_MODE = False
    if INTERACTIVE_MODE:
        launcher = InteractiveLauncher(GuiApp())
        launcher.run()
    else:
        GuiApp().run()
