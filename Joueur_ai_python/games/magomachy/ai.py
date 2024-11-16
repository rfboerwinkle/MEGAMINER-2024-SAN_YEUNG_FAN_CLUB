# This is where you build your AI for the Magomachy game.

from typing import List
from joueur.base_ai import BaseAI
import random

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class AI(BaseAI):
    """ The AI you add and improve code inside to play Magomachy. """

    @property
    def game(self) -> 'games.magomachy.game.Game':
        """games.magomachy.game.Game: The reference to the Game instance this AI is playing.
        """
        return self._game # don't directly touch this "private" variable pls

    @property
    def player(self) -> 'games.magomachy.player.Player':
        """games.magomachy.player.Player: The reference to the Player this AI controls in the Game.
        """
        return self._player # don't directly touch this "private" variable pls

    def get_name(self) -> str:
        """This is the name you send to the server so your AI will control the player named this string.

        Returns:
            str: The name of your Player.
        """
        # <<-- Creer-Merge: get-name -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        return "San Yeung Fan Club" # REPLACE THIS WITH YOUR TEAM NAME
        # <<-- /Creer-Merge: get-name -->>

    def start(self) -> None:
        """This is called once the game starts and your AI knows its player and game. You can initialize your AI here.
        """
        # <<-- Creer-Merge: start -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your start logic
        self.player.choose_wizard("map")
        # <<-- /Creer-Merge: start -->>

    def game_updated(self) -> None:
        """This is called every time the game's state updates, so if you are tracking anything you can update it here.
        """
        # <<-- Creer-Merge: game-updated -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your game updated logic
        # <<-- /Creer-Merge: game-updated -->>

    def end(self, won: bool, reason: str) -> None:
        """This is called when the game ends, you can clean up your data and dump files here if need be.

        Args:
            won (bool): True means you won, False means you lost.
            reason (str): The human readable string explaining why your AI won or lost.
        """
        # <<-- Creer-Merge: end -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your end logic
        # <<-- /Creer-Merge: end -->>
    def action(self, wizard: 'games.magomachy.wizard.Wizard') -> int:
        """This is called whenever your wizard selects an action.

        Args:
            wizard (games.magomachy.wizard.Wizard): Wizard performs action.

        Returns:
            int: Three of the choices a Wizard can make as an action.
        """
        # <<-- Creer-Merge: Action -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # Put your game logic here for Action
        return -1
        # <<-- /Creer-Merge: Action -->>
    def move(self, wizard: 'games.magomachy.wizard.Wizard') -> int:
        """This is called whenever your wizard makes a move.

        Args:
            wizard (games.magomachy.wizard.Wizard): Wizard moves.

        Returns:
            int: Eight cardinal directions.
        """
        # <<-- Creer-Merge: Move -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # Put your game logic here for Move
        return -1
        # <<-- /Creer-Merge: Move -->>

    # CREDIT: https://github.com/encukou/bresenham
    def bres(x0, y0, x1, y1):
        """Yield integer coordinates on the line from (x0, y0) to (x1, y1).

        Input coordinates should be integers.

        The result will contain both the start and the end point.
        """
        dx = x1 - x0
        dy = y1 - y0
        xsign = 1 if dx > 0 else -1
        ysign = 1 if dy > 0 else -1
        dx = abs(dx)
        dy = abs(dy)
        if dx > dy:
            xx, xy, yx, yy = xsign, 0, 0, ysign
        else:
            dx, dy = dy, dx
            xx, xy, yx, yy = 0, ysign, xsign, 0
        D = 2*dy - dx
        y = 0
        for x in range(dx + 1):
            yield x0 + x*xx + y*yx, y0 + x*xy + y*yy
            if D >= 0:
                y += 1
                D -= 2*dx
            D += 2*dy

    def can_move_to(self, tile):
        return (tile.type == 'floor') and (tile.object == None or tile.object.form in ("health flask", "aether flask"))

    def determine_move(self):
        optionCW1 = self.ring[(self.current_pos + 1) % len(self.ring)]
        optionCW2 = self.ring[(self.current_pos + 2) % len(self.ring)]
        optionCCW1 = self.ring[(self.current_pos - 1 + len(self.ring)) % len(self.ring)]
        optionCCW2 = self.ring[(self.current_pos - 2 + len(self.ring)) % len(self.ring)]
        tile_cw1 = self.game.get_tile_at(*optionCW1)
        tile_cw2 = self.game.get_tile_at(*optionCW2)
        tile_ccw1 = self.game.get_tile_at(*optionCCW1)
        tile_ccw2 = self.game.get_tile_at(*optionCCW2)
        opposing_wizard_tile = self.player.opponent.wizard.tile

        can_move_cw = self.can_move_to(tile_cw1) and self.can_move_to(tile_cw2)
        can_move_ccw = self.can_move_to(tile_ccw1) and self.can_move_to(tile_ccw2)

        movement_left = self.player.wizard.movement_left


        if not can_move_cw and not can_move_ccw:
            return 0
        
        if can_move_cw and not can_move_ccw:
            self.current_dir = 1
            return movement_left
        
        if can_move_ccw and not can_move_cw:
            self.current_dir = -1
            return movement_left

        dist_cw = abs(tile_cw2.x - opposing_wizard_tile.x) + abs(tile_cw2.y - opposing_wizard_tile.y)
        dist_ccw = abs(tile_ccw2.x - opposing_wizard_tile.x) + abs(tile_ccw2.y - opposing_wizard_tile.y)

        if dist_cw > dist_ccw:
            self.current_dir = 1
        if dist_ccw > dist_cw:
            self.current_dir = -1

        return movement_left

    def check_and_cast(self) -> bool:
      if not self.player.wizard.has_cast:
        return False
      if self.player.wizard.aether <= 3:
        return False
      op_tile = self.player.opponent.wizard.tile
      if self.player.wizard.check_bressenham(op_tile):
        self.cast("Calming Blast", op_tile)
        return True
      return False

    def run_turn(self) -> bool:
        if self.game.current_turn >> 1 == 0:
          self.player.choose_wizard('sustaining')
          self.ring = (
            [(i, 8) for i in range(1,9)] +
            [(8, i) for i in range(7,0,-1)] +
            [(i, 1) for i in range(7,0,-1)] +
            [(1, i) for i in range(2,8)]
          )
          self.current_pos = self.ring.index((8,1) if self.game.current_turn & 1 else (1,8))
          self.current_dir = 1
          return True

        move_count = self.determine_move()
        check_and_cast()
        if move_count > 0:
            self.current_pos = (self.current_pos + self.current_dir) % len(self.ring)
            target_tile = self.game.get_tile_at(*self.ring[self.current_pos])
            self.player.wizard.move(target_tile)
            check_and_cast()
        if move_count > 1:
            self.current_pos = (self.current_pos + self.current_dir) % len(self.ring)
            target_tile = self.game.get_tile_at(*self.ring[self.current_pos])
            self.player.wizard.move(target_tile)
            check_and_cast()
        
        return True

    def find_path(self, start: 'games.magomachy.tile.Tile', goal: 'games.magomachy.tile.Tile') -> List['games.magomachy.tile.Tile']:
        """A very basic path finding algorithm (Breadth First Search) that when given a starting Tile, will return a valid path to the goal Tile.

        Args:
            start (games.magomachy.tile.Tile): The starting Tile to find a path from.
            goal (games.magomachy.tile.Tile): The goal (destination) Tile to find a path to.

        Returns:
            list[games.magomachy.tile.Tile]: A list of Tiles representing the path, the the first element being a valid adjacent Tile to the start, and the last element being the goal.
        """

        if start == goal:
            # no need to make a path to here...
            return []

        # queue of the tiles that will have their neighbors searched for 'goal'
        fringe = []

        # How we got to each tile that went into the fringe.
        came_from = {}

        # Enqueue start as the first tile to have its neighbors searched.
        fringe.append(start)

        # keep exploring neighbors of neighbors... until there are no more.
        while len(fringe) > 0:
            # the tile we are currently exploring.
            inspect = fringe.pop(0)

            # cycle through the tile's neighbors.
            for neighbor in inspect.get_neighbors():
                # if we found the goal, we have the path!
                if neighbor == goal:
                    # Follow the path backward to the start from the goal and
                    # # return it.
                    path = []

                    # Starting at the tile we are currently at, insert them
                    # retracing our steps till we get to the starting tile
                    while inspect != start:
                        path.append(inspect)
                        inspect = came_from[inspect.id]
                    path.reverse()
                    return path
                # else we did not find the goal, so enqueue this tile's
                # neighbors to be inspected

                # if the tile exists, has not been explored or added to the
                # fringe yet, and it is pathable
                if ((neighbor) and
                   (neighbor.id not in came_from) and
                   (neighbor.type == 'floor') and
                   (neighbor.object == None or neighbor.object.form in ("health flask", "aether flask"))
                   ):
                    # add it to the tiles to be explored and add where it came
                    # from for path reconstruction.
                    fringe.append(neighbor)
                    came_from[neighbor.id] = inspect

        # if you're here, that means that there was not a path to get to where
        # you want to go; in that case, we'll just return an empty path.
        return []

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you need additional functions for your AI you can add them here
    # <<-- /Creer-Merge: functions -->>
