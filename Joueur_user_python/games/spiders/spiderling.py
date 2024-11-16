# Spiderling: A Spider spawned by the BroodMother.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import Optional
from games.spiders.spider import Spider

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Spiderling(Spider):
    """The class representing the Spiderling in the Spiders game.

    A Spider spawned by the BroodMother.
    """

    def __init__(self):
        """Initializes a Spiderling with basic logic as provided by the Creer code generator.
        """
        Spider.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._busy = ""
        self._moving_on_web = None
        self._moving_to_nest = None
        self._number_of_coworkers = 0
        self._work_remaining = 0

    @property
    def busy(self) -> str:
        """'', 'Moving', 'Attacking', 'Strengthening', 'Weakening', 'Cutting', or 'Spitting': When empty string this Spiderling is not busy, and can act. Otherwise a string representing what it is busy with, e.g. 'Moving', 'Attacking'.
        """
        return self._busy

    @property
    def moving_on_web(self) -> Optional['games.spiders.web.Web']:
        """games.spiders.web.Web or None: The Web this Spiderling is using to move. None if it is not moving.
        """
        return self._moving_on_web

    @property
    def moving_to_nest(self) -> Optional['games.spiders.nest.Nest']:
        """games.spiders.nest.Nest or None: The Nest this Spiderling is moving to. None if it is not moving.
        """
        return self._moving_to_nest

    @property
    def number_of_coworkers(self) -> int:
        """int: The number of Spiderlings busy with the same work this Spiderling is doing, speeding up the task.
        """
        return self._number_of_coworkers

    @property
    def work_remaining(self) -> float:
        """float: How much work needs to be done for this Spiderling to finish being busy. See docs for the Work formula.
        """
        return self._work_remaining

    def attack(self, spiderling: 'games.spiders.spiderling.Spiderling') -> bool:
        """Attacks another Spiderling.

        Args:
            spiderling (games.spiders.spiderling.Spiderling): The Spiderling to attack.

        Returns:
            bool: True if the attack was successful, False otherwise.
        """
        return self._run_on_server('attack', {
            'spiderling': spiderling
        })

    def move(self, web: 'games.spiders.web.Web') -> bool:
        """Starts moving the Spiderling across a Web to another Nest.

        Args:
            web (games.spiders.web.Web): The Web you want to move across to the other Nest.

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        return self._run_on_server('move', {
            'web': web
        })

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
