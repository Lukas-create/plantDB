"""
Spezifikation der Pflanze
"""
class Plant:
    """

    """
    def __init__(self, species, spezifisch, nativ, art, landschaft, habitat):
        """

        :param species: Pflanzen Spezies
        :param spezifisch: Pflanzenname
        :param nativ: Native oder invasive Spezies
        :param art: Klasse der Pflanze
        :param landschaft: Vorkommen in der Aue
        :param habitat: Lebensraum
        """
        #self.root_depth = root
        self.name_spezifisch = spezifisch
        self.habitat_in_germany = habitat
        self.species = species
        self.vorkommen = landschaft
        #self.scour = scourge
        self.csl = art
        self.land = nativ

    def print_habitat(self):
        """
        Printet die Pflanzenparameter als Text in der Konsole
        :return:
        """
        print("{0}: Spezifisch : {1} Nativ?: {2} Klasse :{3} Vorkommen :{4} Habitat :{5}".format(self.species,
                                                                                         str(self.name_spezifisch),
                                                                                         str(
                                                                                             self.land),
                                                                                         str(self.csl),
                                                                                         #str(self.scour),
                                                                                         str(self.vorkommen),
                                                                                         str(self.habitat_in_germany)))

