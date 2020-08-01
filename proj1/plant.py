class Plant:
    def __init__(self, species, habitat, groundwater, scourge, root):
        self.root_depth = root
        self.depth_to_groundwater = groundwater
        self.habitat_in_germany = habitat
        self.species = species

    def print_habitat(self):
        print("{0}: average root depth :{1}m minimum depth to groundwater: {2}m habitat:{3}".format(self.species,
                                                                                         str(self.root_depth),
                                                                                         str(self.depth_to_groundwater),
                                                                                         str(
                                                                                             self.habitat_in_germany)))