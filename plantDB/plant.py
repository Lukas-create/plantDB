"""
Spezifikation der Pflanze
"""


class Plant:
    """

    """

    def __init__(self, species, name, nativ, type, occurance, habitat, waterdepthmin, waterdepthmax, rootdepth, floodheightmax, floodloss, flooddurationmax):
        """
        Args:
            species: plant species
            spezifisch: specific plant name
            nativ: shows value "1" if the plant is nativ
            art: plant type
            landschaft: Vorkommen in der Aue/am Flussufer
            habitat: Lebensraum
        """
        self.species = species
        self.name_german = name
        self.status = nativ
        self.plant_type = type
        self.occurance_in_floodplain = occurance
        self.habitat_in_germany = habitat
        self.minimum_waterdepth = waterdepthmin
        self.maximum_waterdepth = waterdepthmax
        self.average_root_depth = rootdepth
        self.critical_flood_height = floodheightmax
        self.plant_mortality_during_critial_flooding = floodloss
        self.critical_flood_duration = flooddurationmax

    def print_habitat(self):
        """
        prints the plant parameters as string in console

        Returns:
            Nichts
        """
        print('\nscientific name:\n{0}\ncommon german name:\n{1}\nstatus:\n{2}\noccurance:{4}\nHabitat:\n{5}{6}{7}'.format(self.species,
                                                                                                                     str(self.name_german),
                                                                                                                     str(self.status),
                                                                                                                     str(self.plant_type),
                                                                                                                     str(self.occurance_in_floodplain),
                                                                                                                     str(self.habitat_in_germany),
                                                                                                                     str(self.minimum_waterdepth),
                                                                                                                     str(self.maximum_waterdepth),
                                                                                                                     str(self.average_root_depth),
                                                                                                                     str(self.critical_flood_height),
                                                                                                                     str(self.plant_mortality_during_critial_flooding),
                                                                                                                     str(self.critical_flood_duration)))


'''class aquaticplant
    def __init__(self, species, name, nativ, velocity, waterdepthmin, waterdepthmax):
        self.species = species
        self.name = name
        self.nativ = nativ
        self.flow_velocity = velocity
        self.minimal_required_waterdepth = waterdepthmin
        self.maximum_allowed_waterdepth = waterdepthmax'''

