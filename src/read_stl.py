import numpy
import pandas
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
from io import StringIO


class ReadStl:
    def __init__(self, input_file):
        self.input_file = input_file

    def read(self):
        """
        Read the stl files using numpy_stl
        :return: mesh object
        """
        your_mesh = mesh.Mesh.from_file(self.input_file)
        return your_mesh

    def plot_stl(self):
        """
        Plot the material picture
        :return: a 3D plot
        """
        # Create a new plot
        figure = pyplot.figure()
        axes = mplot3d.Axes3D(figure)
        axes.add_collection3d(mplot3d.art3d.Poly3DCollection(self.input_file.vectors))
        # Auto scale to the mesh size
        scale = self.input_file.points.flatten()
        axes.auto_scale_xyz(scale, scale, scale)
        imgdata = StringIO()
        figure.savefig(imgdata, format='svg')
        imgdata.seek(0)

        data = imgdata.getvalue()
        pyplot.switch_backend('svg')
        return data
