# Structure: A structure on a Tile.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import Optional
from games.catastrophe.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Structure(GameObject):
    """The class representing the Structure in the Catastrophe game.

    A structure on a Tile.
    """

    def __init__(self):
        """Initializes a Structure with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._effect_radius = 0
        self._materials = 0
        self._owner = None
        self._tile = None
        self._type = ""

    @property
    def effect_radius(self) -> int:
        """int: The range of this Structure's effect. For example, a radius of 1 means this Structure affects a 3x3 square centered on this Structure.
        """
        return self._effect_radius

    @property
    def materials(self) -> int:
        """int: The number of materials in this Structure. Once this number reaches 0, this Structure is destroyed.
        """
        return self._materials

    @property
    def owner(self) -> Optional['games.catastrophe.player.Player']:
        """games.catastrophe.player.Player or None: The owner of this Structure if any, otherwise None.
        """
        return self._owner

    @property
    def tile(self) -> Optional['games.catastrophe.tile.Tile']:
        """games.catastrophe.tile.Tile or None: The Tile this Structure is on.
        """
        return self._tile

    @property
    def type(self) -> str:
        """'neutral', 'shelter', 'monument', 'wall', or 'road': The type of Structure this is ('shelter', 'monument', 'wall', 'road', 'neutral').
        """
        return self._type


    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
