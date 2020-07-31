class Plants:
    def __init__(self, *args, **kwargs):
        self.root_depth = float()
        self.depth_to_groundwater = float()
        self.habitat_in_germany = float()
        self.species = ""
        self.xy_position = tuple()

    def print_habitat(self):
        print("{0}: average root depth :{1}m minimum depth to groundwater: {2}m habitat:{3}".format(self.species,
                                                                                         str(self.root_depth),
                                                                                         str(self.depth_to_groundwater),
                                                                                         str(
                                                                                             self.habitat_in_germany)))

    def swim_to_position(self, new_position=()):
        self.xy_position = new_position


class Carex(Plants):
    def __init__(self, species, *args, **kwargs):
        Plants.__init__(self)
        self.family = "Carex"
        self.species = species

    def habitat_function(self, depth, groundwater, lebensraum):
        self.root_depth = depth
        self.depth_to_groundwater = groundwater
        self.habitat_in_germany = lebensraum


german_carex = Carex("Carex acuta") #Alle daten/namen bisher nur placeholder
german_carex.habitat_function(depth=0.4, groundwater=0.5, lebensraum='Alpen')
german_carex.print_habitat()

river_carex = Carex("Carex paradoxa")
river_carex.habitat_function(depth=0.6, groundwater=0.8, lebensraum='Italien')
river_carex.print_habitat()