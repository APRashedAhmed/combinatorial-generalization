"""Tests for the combigen dataset generation."""
import logging

import numpy as np

import combinatorial_generalization.default_configuration as config
from combinatorial_generalization.make_datasets import generate_combigen_datasets

def test_combigen_make_datasets_correctly_creates_datasets():
    train, val, test = generate_combigen_datasets()


    for (X, y), name in zip([train, val, test], ["train", "val", "test"]):    
        # Collect the expected shapes
        expected_x_shape = [getattr(config, "n_{}".format(name)),
                            config.slots,
                            config.size,
                            config.size]
        expected_y_shape = [getattr(config, "n_{}".format(name)),
                            config.slots,
                            config.size,
                            config.dims]

        # Assert the shapes match
        assert np.array_equal(X.shape, expected_x_shape)
        assert np.array_equal(y.shape, expected_y_shape)
 
