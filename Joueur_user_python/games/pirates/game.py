# Game: Steal from merchants and become the most infamous pirate.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import Dict, List, Optional
from joueur.base_game import BaseGame

# import game objects
from games.pirates.game_object import GameObject
from games.pirates.player import Player
from games.pirates.port import Port
from games.pirates.tile import Tile
from games.pirates.unit import Unit

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Game(BaseGame):
    """The class representing the Game in the Pirates game.

    Steal from merchants and become the most infamous pirate.
    """

    def __init__(self):
        """Initializes a Game with basic logic as provided by the Creer code generator.
        """
        BaseGame.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._bury_interest_rate = 0
        self._crew_cost = 0
        self._crew_damage = 0
        self._crew_health = 0
        self._crew_moves = 0
        self._crew_range = 0
        self._current_player = None
        self._current_turn = 0
        self._game_objects = {}
        self._heal_factor = 0
        self._map_height = 0
        self._map_width = 0
        self._max_turns = 100
        self._merchant_gold_rate = 0
        self._merchant_interest_rate = 0
        self._min_interest_distance = 0
        self._players = []
        self._ports = []
        self._rest_range = 0
        self._session = ""
        self._ship_cost = 0
        self._ship_damage = 0
        self._ship_health = 0
        self._ship_moves = 0
        self._ship_range = 0
        self._tiles = []
        self._time_added_per_turn = 0
        self._units = []

        self.name = "Pirates"

        self._game_object_classes = {
            'GameObject': GameObject,
            'Player': Player,
            'Port': Port,
            'Tile': Tile,
            'Unit': Unit
        }

    @property
    def bury_interest_rate(self) -> float:
        """float: The rate buried gold increases each turn.
        """
        return self._bury_interest_rate

    @property
    def crew_cost(self) -> int:
        """int: How much gold it costs to construct a single crew.
        """
        return self._crew_cost

    @property
    def crew_damage(self) -> int:
        """int: How much damage crew deal to each other.
        """
        return self._crew_damage

    @property
    def crew_health(self) -> int:
        """int: The maximum amount of health a crew member can have.
        """
        return self._crew_health

    @property
    def crew_moves(self) -> int:
        """int: The number of moves Units with only crew are given each turn.
        """
        return self._crew_moves

    @property
    def crew_range(self) -> float:
        """float: A crew's attack range. Range is circular.
        """
        return self._crew_range

    @property
    def current_player(self) -> 'games.pirates.player.Player':
        """games.pirates.player.Player: The player whose turn it is currently. That player can send commands. Other players cannot.
        """
        return self._current_player

    @property
    def current_turn(self) -> int:
        """int: The current turn number, starting at 0 for the first player's turn.
        """
        return self._current_turn

    @property
    def game_objects(self) -> Dict[str, 'games.pirates.game_object.GameObject']:
        """dict[str, games.pirates.game_object.GameObject]: A mapping of every game object's ID to the actual game object. Primarily used by the server and client to easily refer to the game objects via ID.
        """
        return self._game_objects

    @property
    def heal_factor(self) -> float:
        """float: How much health a Unit recovers when they rest.
        """
        return self._heal_factor

    @property
    def map_height(self) -> int:
        """int: The number of Tiles in the map along the y (vertical) axis.
        """
        return self._map_height

    @property
    def map_width(self) -> int:
        """int: The number of Tiles in the map along the x (horizontal) axis.
        """
        return self._map_width

    @property
    def max_turns(self) -> int:
        """int: The maximum number of turns before the game will automatically end.
        """
        return self._max_turns

    @property
    def merchant_gold_rate(self) -> float:
        """float: How much gold merchant Ports get each turn.
        """
        return self._merchant_gold_rate

    @property
    def merchant_interest_rate(self) -> float:
        """float: When a merchant ship spawns, the amount of additional gold it has relative to the Port's investment.
        """
        return self._merchant_interest_rate

    @property
    def min_interest_distance(self) -> float:
        """float: The Euclidean distance buried gold must be from the Player's Port to accumulate interest.
        """
        return self._min_interest_distance

    @property
    def players(self) -> List['games.pirates.player.Player']:
        """list[games.pirates.player.Player]: List of all the players in the game.
        """
        return self._players

    @property
    def ports(self) -> List['games.pirates.port.Port']:
        """list[games.pirates.port.Port]: Every Port in the game. Merchant ports have owner set to None.
        """
        return self._ports

    @property
    def rest_range(self) -> float:
        """float: How far a Unit can be from a Port to rest. Range is circular.
        """
        return self._rest_range

    @property
    def session(self) -> str:
        """str: A unique identifier for the game instance that is being played.
        """
        return self._session

    @property
    def ship_cost(self) -> int:
        """int: How much gold it costs to construct a ship.
        """
        return self._ship_cost

    @property
    def ship_damage(self) -> int:
        """int: How much damage ships deal to ships and ports.
        """
        return self._ship_damage

    @property
    def ship_health(self) -> int:
        """int: The maximum amount of health a ship can have.
        """
        return self._ship_health

    @property
    def ship_moves(self) -> int:
        """int: The number of moves Units with ships are given each turn.
        """
        return self._ship_moves

    @property
    def ship_range(self) -> float:
        """float: A ship's attack range. Range is circular.
        """
        return self._ship_range

    @property
    def tiles(self) -> List['games.pirates.tile.Tile']:
        """list[games.pirates.tile.Tile]: All the tiles in the map, stored in Row-major order. Use `x + y * mapWidth` to access the correct index.
        """
        return self._tiles

    @property
    def time_added_per_turn(self) -> int:
        """int: The amount of time (in nano-seconds) added after each player performs a turn.
        """
        return self._time_added_per_turn

    @property
    def units(self) -> List['games.pirates.unit.Unit']:
        """list[games.pirates.unit.Unit]: Every Unit in the game. Merchant units have targetPort set to a port.
        """
        return self._units

    def get_tile_at(self, x: int, y: int) -> Optional['games.pirates.tile.Tile']:
        """Gets the Tile at a specified (x, y) position.

        Args:
            x (int): An integer between 0 and the map_width.
            y (int): An integer between 0 and the map_height.

        Returns:
            games.pirates.tile.Tile or None: The Tile at (x, y) or None if out of bounds.
        """
        if x < 0 or y < 0 or x >= self.map_width or y >= self.map_height:
            # out of bounds
            return None

        return self.tiles[x + y * self.map_width]

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
