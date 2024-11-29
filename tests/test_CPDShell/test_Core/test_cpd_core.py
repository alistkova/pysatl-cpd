import pytest

from CPDShell.Core.algorithms.graph_algorithm import GraphAlgorithm
from CPDShell.Core.cpd_core import CPDCore
from CPDShell.Core.scenario import Scenario
from CPDShell.Core.scrubber.linear_scrubber import LinearScrubber


def custom_comparison(node1, node2):
    arg = 1
    return abs(node1 - node2) <= arg


class TestCPDCore:
    @pytest.mark.parametrize(
        "scenario_param,data,alg_class,alg_param,scrubber_data_size,expected",
        (
                (
                        (1, True),
                        (1, 1, 1, 1, 1, 1, 1, 100, 100, 100, 100, 100, 100, 100),
                        GraphAlgorithm,
                        (custom_comparison, 2),
                        10,
                        [6, 16],
                ),
                (
                        (1, False),
                        (1, 1, 1, 1, 1, 1, 1, 100, 100, 100, 100, 100, 100, 100),
                        GraphAlgorithm,
                        (custom_comparison, 2),
                        10,
                        [0, 10],
                ),
        ),
    )
    def test_run(self, scenario_param, data, alg_class, alg_param, scrubber_data_size, expected):
        scenario = Scenario(*scenario_param)
        scrubber = LinearScrubber()
        algorithm = alg_class(*alg_param)

        core = CPDCore(scenario, data, scrubber, algorithm, scrubber_data_size)
        assert core.run() == expected
