from abc import ABC, abstractmethod
from typing import Sequence, Iterable, Optional

import numpy

from CPDShell.Core.scenario import Scenario


class AbstractScrubber(ABC):
    """A scrubber for dividing data into windows
    and subsequent processing of data windows
    by change point detection algorithms
    """

    def __init__(self) -> None:
        """A scrubber for dividing data into windows
        and subsequent processing of data windows
        by change point detection algorithms

        """
        self._scenario: Optional[Scenario] = None
        self._data: Sequence[float | numpy.float64] = []
        self.is_running = True
        self.change_points: list[int] = []

    @abstractmethod
    def restart(self) -> None:
        """Function for restarting Scrubber"""
        ...

    @abstractmethod
    def get_windows(self) -> Iterable[Sequence[float | numpy.float64]]:
        """Function for dividing data into parts to feed into the change point detection algorithm

        :return: Iterator of data windows for change point detection algorithm
        """
        ...

    @abstractmethod
    def add_change_points(self, window_change_points: list[int]) -> None:
        """Function for mapping window change points to scrubber data part"""
        ...

    def add_data(self, new_data: Sequence[float | numpy.float64]) -> None:
        """Function for adding new data to Scrubber"""
        self._data += new_data  # TODO Sequence __add__?

    @property
    def scenario(self) -> Scenario:
        return self._scenario

    @scenario.setter
    def scenario(self, new_scenario) -> None:
        self._scenario = new_scenario

    @property
    def data(self) -> Sequence[float | numpy.float64]:
        return self._data

    @data.setter
    def data(self, new_data) -> None:
        self._data = new_data
        self.restart()
