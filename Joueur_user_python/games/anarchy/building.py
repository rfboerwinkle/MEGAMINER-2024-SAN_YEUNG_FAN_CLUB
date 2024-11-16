# Building: A basic building. It does nothing besides burn down. Other Buildings inherit from this class.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import Optional
from games.anarchy.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Building(GameObject):
    """The class representing the Building in the Anarchy game.

    A basic building. It does nothing besides burn down. Other Buildings inherit from this class.
    """

    def __init__(self):
        """Initializes a Building with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._bribed = False
        self._building_east = None
        self._building_north = None
        self._building_south = None
        self._building_west = None
        self._fire = 0
        self._health = 0
        self._is_headquarters = False
        self._owner = None
        self._x = 0
        self._y = 0

    @property
    def bribed(self) -> bool:
        """bool: When True this building has already been bribed this turn and cannot be bribed again this turn.
        """
        return self._bribed

    @property
    def building_east(self) -> Optional['games.anarchy.building.Building']:
        """games.anarchy.building.Building or None: The Building directly to the east of this building, or None if not present.
        """
        return self._building_east

    @property
    def building_north(self) -> Optional['games.anarchy.building.Building']:
        """games.anarchy.building.Building or None: The Building directly to the north of this building, or None if not present.
        """
        return self._building_north

    @property
    def building_south(self) -> Optional['games.anarchy.building.Building']:
        """games.anarchy.building.Building or None: The Building directly to the south of this building, or None if not present.
        """
        return self._building_south

    @property
    def building_west(self) -> Optional['games.anarchy.building.Building']:
        """games.anarchy.building.Building or None: The Building directly to the west of this building, or None if not present.
        """
        return self._building_west

    @property
    def fire(self) -> int:
        """int: How much fire is currently burning the building, and thus how much damage it will take at the end of its owner's turn. 0 means no fire.
        """
        return self._fire

    @property
    def health(self) -> int:
        """int: How much health this building currently has. When this reaches 0 the Building has been burned down.
        """
        return self._health

    @property
    def is_headquarters(self) -> bool:
        """bool: True if this is the Headquarters of the owning player, False otherwise. Burning this down wins the game for the other Player.
        """
        return self._is_headquarters

    @property
    def owner(self) -> 'games.anarchy.player.Player':
        """games.anarchy.player.Player: The player that owns this building. If it burns down (health reaches 0) that player gets an additional bribe(s).
        """
        return self._owner

    @property
    def x(self) -> int:
        """int: The location of the Building along the x-axis.
        """
        return self._x

    @property
    def y(self) -> int:
        """int: The location of the Building along the y-axis.
        """
        return self._y

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
