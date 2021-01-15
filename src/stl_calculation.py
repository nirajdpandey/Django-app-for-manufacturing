
class CalculateVolume:

    def __init__(self, your_mesh):
        """
        Initialize your mesh object
        :param your_mesh: provide a mesh file
        """
        self.your_mesh = your_mesh

    def calc_volume(self):
        """
        calculate volume of the mesh
        :return: Mesh volume
        """
        volume = list(self.your_mesh.get_mass_properties())[0]
        return volume

