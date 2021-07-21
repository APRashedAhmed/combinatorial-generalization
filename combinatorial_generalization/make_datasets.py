"""Script to hold the functions for making combigen datasets."""
import logging

import combinatorial_generalization.default_configuration as config
import combinatorial_generalization.combigen as cg

logger = logging.getLogger(__name__)

def generate_combigen_x_y_dataset(n_samples=config.n_train, *args, **kwargs):
    """Function to generate X and y pairs for the combigen task.

    Convenience function that runs ``cg.generate_labels`` followed by
    ``cg.inverse_transform`` to creat the ``X`` and ``y`` pairs for the data.
    The only change is that now the default number of samples is defined as
    ``n_train`` from ``default_configuration.py``.

    See documentation for ``cg.generate_labels`` for all passable arguments.

    Parameters
    ----------
    n_samples : int, optional
    	Number of samples to produce for X and Y.

    Returns
    -------
    x : np.array
        The ``X`` that would have generated the inputted ``y``.

    y : np.array
    	Labels for the generated ``X`` array.
    """
    y = cg.generate_labels(n_samples=n_samples, *args, **kwargs)
    x = cg.inverse_transform(y)
    return x, y

def generate_combigen_datasets(
        n_samples_train=config.n_train,
        n_lines_train=config.n_lines,
        line_stats_train=config.line_stats,
        n_samples_val=config.n_val,
        n_lines_val=config.n_lines,
        line_stats_val=config.line_stats,
        n_samples_test=config.n_test,
        n_lines_test=config.n_lines,
        line_stats_test=config.line_stats,
        *args,
        **kwargs,
        ):
    """Generate the training, validation, and testing set data.

    Higher level wrapper that organizes the dataset into the expected groups of
    training, validation, and testing sets. Default values are defined in
    ``default_configuration.py``.

    Parameters that should not be varied between the three datasets (slots,
    size, etc.) are included as star args and kwargs, while the rest that can
    be varied are given their own variables.

    Parameters
    ----------
    n_samples_train : int, optional
    	Number of samples to return in the training data.

    n_lines_train : int, optional
    	Total number of lines to have per sample in the training data.

    line_stats_train : list or None, optional
    	Statistics for sampling from the ``size x dims`` elements for the
    	training data.
    
    n_samples_val : int, optional
    	Number of samples to return in the validation data.

    n_lines_val : int, optional
    	Total number of lines to have per sample in the validation data.

    line_stats_val : list or None, optional
    	Statistics for sampling from the ``size x dims`` elements for the
    	validation data.
    
    n_samples_test : int, optional
    	Number of samples to return in the testing data.

    n_lines_test : int, optional
    	Total number of lines to have per sample in the testing data.

    line_stats_test : list or None, optional
    	Statistics for sampling from the ``size x dims`` elements for the
    	testing data.

    Returns
    -------
    train_data : tuple, (X, y)
    	Training data with ``X`` and ``y``.

    val_data : tuple, (X, y)
    	Validation data with ``X`` and ``y``.

    test_data : tuple, (X, y)
    	Testing data with ``X`` and ``y``.
    """
    # Training data
    x_train, y_train = generate_combigen_x_y_dataset(
        n_samples=n_samples_train,
        n_lines=n_lines_train,
        line_stats=line_stats_train,
        *args,
        **kwargs)

    # Validation data
    x_val, y_val = generate_combigen_x_y_dataset(
        n_samples=n_samples_val,
        n_lines=n_lines_val,
        line_stats=line_stats_val,
        *args,
        **kwargs)

    # Testing data
    x_test, y_test = generate_combigen_x_y_dataset(
        n_samples=n_samples_test,
        n_lines=n_lines_test,
        line_stats=line_stats_test,
        *args,
        **kwargs)

    # Return as a set of tuples that can also be unpacked into components
    return (x_train, y_train), (x_val, y_val), (x_test, y_test)
