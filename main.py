#!/usr/bin/python3
'''
Showcase of Kivy Features
=========================

This showcases many features of Kivy. You should see a
menu bar across the top with a demonstration area below. The
first demonstration is the accordion layout. You can see, but not
edit, the kv language code for any screen by pressing the bug or
'show source' icon. Scroll through the demonstrations using the
left and right icons in the top right or selecting from the menu
bar.

The file showcase.kv describes the main container, while each demonstration
pane is described in a separate .kv file in the data/screens directory.
The image data/background.png provides the gradient background while the
icons in data/icon directory are used in the control bar. The file
data/faust_github.jpg is used in the Scatter pane. The icons are
from `http://www.gentleface.com/free_icon_set.html` and licensed as
Creative Commons - Attribution and Non-commercial Use Only; they
sell a commercial license.

The file android.txt is used to package the application for use with the
Kivy Launcher Android application. For Android devices, you can
copy/paste this directory into /sdcard/kivy/showcase on your Android device.

'''

from time import time
from kivy.app import App
from os.path import dirname, join
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty, BooleanProperty,\
    ListProperty
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image

import csv
import datetime


""" GARDEN GRAPH """
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


class MyImage(Image):
    fonte = StringProperty()

class ShowcaseScreen(Screen):
    fullscreen = BooleanProperty(False)

    pre_defined_data_values = {'headache': 0, 'spinalneck': 0,
                               'spinalmiddle': 0, 'spinallow': 0,'shoulderleft': 0, 'shoulderright': 0,'hipleft': 0,
                               'hipright': 0,'emotion': 5}

    image = Image()
    image.source = 'data/test2.jpg'


    def add_widget(self, *args):
        if 'content' in self.ids:
            print "Adding content widget: ", self.ids
            return self.ids.content.add_widget(*args)
        print "Adding super showcasescreen: ", super(ShowcaseScreen, self)
        #self.fonte = StringProperty('data/test2.jpg')
        return super(ShowcaseScreen, self).add_widget(*args)

    # Update Data/Stats recived from *.kv
    def update_data(self,datakey,datastat):
        self.pre_defined_data_values[datakey] = datastat
        print "Got it: ", self.pre_defined_data_values[datakey]

    # On Create Graph and Save data/stats
    def change_commit(self):
        print "Data: ", self.pre_defined_data_values
        self.append_cvs_file()

    def append_cvs_file(self):
        today = datetime.date.today()
        cvsdate = today.strftime('%d/%m/%Y')
        cvsrow = []
        #cvsdate = '13/03/1991'
        cvsrow.append(cvsdate)
        #for dkey in self.pre_defined_data_values.keys():
        for dkey in sorted(self.pre_defined_data_values):
            cvsrow.append(self.pre_defined_data_values[dkey])
            print dkey
        print "Print cvsrow: ", cvsrow
        myfile = open('test.csv', 'awb')
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(cvsrow)

    # REMOVE
    def one(self):
        test = "1"
    # REMOVE
    def slidervalue(self,s2value):
        test = "2"
    # REMOVE
    def ask_update(self):
        print "ask uppdate prints NOW"


    """  GARDEN GRAPH """
    def updatecanvas(self):
        incsv='test.csv'
        utcsv='create.csv'
##################################################
        print "starting"

        rownr = 5
        head = False
        headlist = False
        columns = False
        with open('test.csv') as inf:
            for line in inf:
                parts = line.split(",")
                partlen = len(parts)
                #print "partlen: ",partlen, " parts: ", parts
                if not headlist:
                    headlist = parts
                elif not columns:
                    columns = parts

        print "headlist: ", headlist
        print "columns : ", partlen
        new_cvs_file_list = []
        #new_cvs_file_list.append("empty")
        colum_with_values = []
        colum_with_no_values = []

        replace_append_data = ''

        for colum in range(partlen):
            print "COLUM NAME: ", headlist[colum]
            check_empty_data = True
            countlines = 0
            with open(incsv) as inf:
                for line in inf:
                    parts = line.split(",") # split line into parts
                    if len(parts) > 1:   # if at least 2 parts/columns
                        #print "NEW_CVS_FILE_LIST: ", new_cvs_file_list, " fethcning value: ", colum
                        if not head:
                            head = parts[colum]
                        else:
                            print parts[colum]   # print column 2
                    if parts[colum] == headlist[colum]:
                        print "header TOP"
                    elif parts[colum] != '"0"':
                        print "parts have value: ", parts[colum]
                        check_empty_data = False
                    countlines +=1
            if not check_empty_data:
                print "DATA in: ", headlist[colum]
                colum_with_values.append(headlist[colum])
            else:
                print "EMPTY IN: ", headlist[colum]
                colum_with_no_values.append(headlist[colum])

        print "These columes have legit valuse: ", colum_with_values
        for colum in range(partlen):
            print "COLUM NAME: ", headlist[colum]
            check_empty_data = True
            countlines = 0
            with open(incsv) as inf:
                for line in inf:
                    parts = line.split(",") # split line into parts
                    if len(parts) > 1:   # if at least 2 parts/columns
                        if colum == 0:
                            new_cvs_file_list.append(parts[colum])
                            #print "NEW_CVS_FILE_LIST: ", new_cvs_file_list, " fethcning value: ", colum
                        #elif headlist[colum] != parts[colum] and headlist[colum] in colum_with_values:
                        elif headlist[colum] in colum_with_values:
                            if colum != 0:
                                # reading new file structure
                                read_copy_of_row = new_cvs_file_list[countlines]
                                new_cvs_file_list[countlines] = read_copy_of_row + ',' + parts[colum]
                                countlines +=1

                            print headlist[colum]," -> ", parts[colum]


        myfile = open(utcsv,'w')
        for row in new_cvs_file_list:
            print row
            myfile.write(row + '\n')

        myfile.close()
        fname = open(utcsv)
        plt.plotfile(fname, (colum_with_values), subplots=False)
        plt.xlabel(r'$date$')
        plt.ylabel(r'$levels$')
        # #plt.show()
        plt.savefig('data/test.png')
        #
        # print "column with missing valuse: ", colum_with_no_values
##################################################
        self.image.source  = "data/test.png"

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


class ShowcaseApp(App):
    #fonte = StringProperty()
    #source_image = 'data/test.png'
    index = NumericProperty(-1)
    current_title = StringProperty()
    time = NumericProperty(0)
    show_sourcecode = BooleanProperty(False)
    sourcecode = StringProperty()
    screen_names = ListProperty([])
    hierarchy = ListProperty([])

    def build(self):

        self.title = 'Rehab RAW Analyzer - Beta Build'
        Clock.schedule_interval(self._update_clock, 1 / 60.)
        self.screens = {}
        self.available_screens = sorted([
            '1.Pain','2.Drug','3.Activity','4.Training','5.Allergi','6.Food','7.Save','Scatter'])
        self.screen_names = self.available_screens
        curdir = dirname(__file__)
        self.available_screens = [join(curdir, 'data', 'screens',
            '{}.kv'.format(fn)) for fn in self.available_screens]
        self.go_next_screen()

    def on_pause(self):
        return True

    def on_resume(self):
        pass

    def on_current_title(self, instance, value):
        self.root.ids.spnr.text = value

    def go_previous_screen(self):
        self.index = (self.index - 1) % len(self.available_screens)
        screen = self.load_screen(self.index)
        sm = self.root.ids.sm
        sm.switch_to(screen, direction='right')
        self.current_title = screen.name
        self.update_sourcecode()

    def go_next_screen(self):
        self.index = (self.index + 1) % len(self.available_screens)
        screen = self.load_screen(self.index)
        sm = self.root.ids.sm
        sm.switch_to(screen, direction='left')
        self.current_title = screen.name
        self.update_sourcecode()
        print "sm: ", sm
        print "screen: ", screen



    def go_screen(self, idx):
        self.index = idx
        self.root.ids.sm.switch_to(self.load_screen(idx), direction='left')
        self.update_sourcecode()
        print "switch screen: ", self.load_screen(idx)

    def go_hierarchy_previous(self):
        ahr = self.hierarchy
        if len(ahr) == 1:
            return
        if ahr:
            ahr.pop()
        if ahr:
            idx = ahr.pop()
            self.go_screen(idx)

    def load_screen(self, index):
        if index in self.screens:
            return self.screens[index]
        screen = Builder.load_file(self.available_screens[index].lower())
        self.screens[index] = screen
        return screen

    def read_sourcecode(self):
        fn = self.available_screens[self.index].lower() + '.help'
        with open(fn) as fd:
            return fd.read()

    def toggle_source_code(self):
        self.show_sourcecode = not self.show_sourcecode
        if self.show_sourcecode:
            height = self.root.height * .3
        else:
            height = 0

        Animation(height=height, d=.3, t='out_quart').start(
                self.root.ids.sv)

        self.update_sourcecode()

    def update_sourcecode(self):
        if not self.show_sourcecode:
            self.root.ids.sourcecode.focus = False
            return
        self.root.ids.sourcecode.text = self.read_sourcecode()
        self.root.ids.sv.scroll_y = 1

    def showcase_floatlayout(self, layout):

        def add_button(*t):
            if not layout.get_parent_window():
                return
            if len(layout.children) > 5:
                layout.clear_widgets()
            layout.add_widget(Builder.load_string('''
#:import random random.random
Button:
    size_hint: random(), random()
    pos_hint: {'x': random(), 'y': random()}
    text:
        'size_hint x: {} y: {}\\n pos_hint x: {} y: {}'.format(\
            self.size_hint_x, self.size_hint_y, self.pos_hint['x'],\
            self.pos_hint['y'])
'''))
            Clock.schedule_once(add_button, 1)
        Clock.schedule_once(add_button)

    def showcase_boxlayout(self, layout):

        def add_button(*t):
            if not layout.get_parent_window():
                return
            if len(layout.children) > 5:
                layout.orientation = 'vertical'\
                    if layout.orientation == 'horizontal' else 'horizontal'
                layout.clear_widgets()
            layout.add_widget(Builder.load_string('''
Button:
    text: self.parent.orientation if self.parent else ''
'''))
            Clock.schedule_once(add_button, 1)
        Clock.schedule_once(add_button)

    def showcase_gridlayout(self, layout):

        def add_button(*t):
            if not layout.get_parent_window():
                return
            if len(layout.children) > 15:
                layout.rows = 3 if layout.rows is None else None
                layout.cols = None if layout.rows == 3 else 3
                layout.clear_widgets()
            layout.add_widget(Builder.load_string('''
Button:
    text:
        'rows: {}\\ncols: {}'.format(self.parent.rows, self.parent.cols)\
        if self.parent else ''
'''))
            Clock.schedule_once(add_button, 1)
        Clock.schedule_once(add_button)

    def showcase_stacklayout(self, layout):
        orientations = ('lr-tb', 'tb-lr',
                        'rl-tb', 'tb-rl',
                        'lr-bt', 'bt-lr',
                        'rl-bt', 'bt-rl')

        def add_button(*t):
            if not layout.get_parent_window():
                return
            if len(layout.children) > 11:
                layout.clear_widgets()
                cur_orientation = orientations.index(layout.orientation)
                layout.orientation = orientations[cur_orientation - 1]
            layout.add_widget(Builder.load_string('''
Button:
    text: self.parent.orientation if self.parent else ''
    size_hint: .2, .2
'''))
            Clock.schedule_once(add_button, 1)
        Clock.schedule_once(add_button)

    def showcase_anchorlayout(self, layout):

        def change_anchor(self, *l):
            if not layout.get_parent_window():
                return
            anchor_x = ('left', 'center', 'right')
            anchor_y = ('top', 'center', 'bottom')
            if layout.anchor_x == 'left':
                layout.anchor_y = anchor_y[anchor_y.index(layout.anchor_y) - 1]
            layout.anchor_x = anchor_x[anchor_x.index(layout.anchor_x) - 1]

            Clock.schedule_once(change_anchor, 1)
        Clock.schedule_once(change_anchor, 1)

    def _update_clock(self, dt):
        self.time = time()

if __name__ == '__main__':
    ShowcaseApp().run()
