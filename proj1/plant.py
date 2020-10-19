"""
Spezifikation der Pflanze
"""
class Plant:
    """

    """
    def __init__(self, species, spezifisch, nativ, art, landschaft, habitat):
        """
        Args:
            species: plant species
            spezifisch: specific plant name
            nativ: shows value "1" if the plant is nativ
            art: plant type
            landschaft: Vorkommen in der Aue/am Flussufer
            habitat: Lebensraum
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
        prints the plant parameters as string in console

        Returns:
            Nichts
        """
        print("\nGattung:\n{0}\nName:\n{1}\nNativ?:\n{2}\nKlasse:\n{3}\nVorkommen:\n{4}\nHabitat:\n{5}".format(self.species,
                                                                                         str(self.name_spezifisch),
                                                                                         str(
                                                                                             self.land),
                                                                                         str(self.csl),
                                                                                         #str(self.scour),
                                                                                         str(self.vorkommen),
                                                                                         str(self.habitat_in_germany)))

