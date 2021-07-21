"""Tests for the visualization function for the combigen task."""
import logging

import pytest

import combinatorial_generalization.combigen as cg
import combinatorial_generalization.visualize as viz

logger = logging.getLogger(__name__)

N = [1, 3, 5]

@pytest.mark.parametrize("length", N)
def test_combigen_heatmap_runs_without_errors_for_different_input_lengths(
        length):
    """Lifted directly from nb0.1 c382."""
    viz.heatmap(cg.generate_labels(length))

@pytest.mark.parametrize("n_pairs", N)
def test_visualize_combigen_runs_without_errors_for_different_numbers_of_pairs(
        n_pairs):
    viz.visualize_combigen(n_pairs)
