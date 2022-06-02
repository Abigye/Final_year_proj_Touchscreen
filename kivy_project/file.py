# from kivy.app import App
# from math import sin
# from kivy_garden.graph import Graph, MeshLinePlot
# from kivy.uix.boxlayout import BoxLayout

# graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
# x_ticks_major=25, y_ticks_major=1,
# y_grid_label=True, x_grid_label=True, padding=5,
# x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=-1, ymax=1)
# plot = MeshLinePlot(color=[1, 0, 0, 1])
# plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]
# graph.add_plot(plot)


# class GraphExample(BoxLayout):
#     pass


# class SecondKivyApp(App):
#     def build(self):
#         return GraphExample


# if __name__== '__main__':
#    SecondKivyApp().run()


# importing pyplot for graph plotting
from matplotlib import pyplot as plt

# importing numpy
import numpy as np
from kivy.garden.matplotlib import FigureCanvasKivyAgg

# importing kivyapp
from kivy.app import App

# importing kivy builder
from kivy.lang import Builder


# this is the main class which will
# render the whole application
class uiApp(App):
    def build(self):
        self.str = Builder.load_string(
            """ 
  
BoxLayout:
    layout:layout
      
    BoxLayout:
      
        id:layout
      
                                """
        )

        signal = [7, 89.6, 45.0 - 56.34]

        signal = np.array(signal)

        # this will plot the signal on graph
        plt.plot(signal)

        # setting x label
        plt.xlabel("Time(s)")

        # setting y label
        plt.ylabel("signal (norm)")
        plt.grid(True, color="lightgray")
        plt.show()

        # adding plot to kivy boxlayout
        self.str.layout.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        return self.str


# running the application
uiApp().run()
