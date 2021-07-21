<div align="center">

# Combinatorial Generalization and Interactivity

![](images/example_sample.png)

</div>

Code that implements the task described in Randy O'Reily's task in
[Generalization in Interactive Networks: The Benefits of Inhibitory Competition and Hebbian Learning][1].
The package can be installed for general reuse and contains unit tests to ensure
proper functionality.

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
## Table of Contents 

- [Task Description](#task-description)
	- [Desiderata](#desiderata)
- [Getting Started](#getting-started)
	- [Installation](#installation)
	- [Usage](#usage)
- [API](#api)
	- [Generating Datasets](#generating-datasets)
	- [Visualization](#visualization)
- [Example Use-Cases](#example-use-cases)
	- [Different Numbers of Lines](#different-numbers-of-lines)
	- [Nonuniform Line Statistics](#nonuniform-line-statistics)
- [References](#references)

<!-- markdown-toc end -->

<br>

## Task Description

The majority of the text below is taken directly from section **2** of the
paper.

-   Combinatorial structure is implemented by having *four* different input-output
    slots.
-   The output mapping for a given slot depends only on the corresponding input
    pattern for that slot (see [Brousse, 1993][2]; [Noelle & Cottrell, 1996][3],
    for similar tasks).
-   Each slot has a vocabulary of input-output mappings.
-   Input vocabulary consists of all 45 combinations of 5 horizontal and 5
    vertical bars in a 5x5 grid.
-   Output mapping is a localist identification of the two input bars (similar to
    bar tasks used by [Foldiak, 1990][4]; [Saund, 1995][5]; [Zemel, 1993][6]; 
    [Dayan & Zemel, 1995][7]\).
-   Total number of distinct input patterns is approximately 4.1 million.
-   Models are intended only to train on 100 randomly constructed examples, and
    then test on an arbitrarily large testing set (500 in the paper).
-   Error criterion is scored such that each output unit has to be on the right
	side of 0.5 according to the correct target pattern.

### Desiderata

The paper described the task as having several desiderata.

-   It has a simple combinatorial structure that allows for novel inputs to be
    composed from a small vocabulary of features.
-   There is some interesting substructure to the vocabulary mapping at each slot.
-   The structure of the task should be apparent in the weight patterns of the
    models.

<br>

## Getting Started

### Installation

To use the package, first clone it:

```bash
git clone https://github.com/APRashedAhmed/combinatorial-generalization.git
```

Install the requirements:

```bash
# For pip
pip install requirements.txt

# For conda
conda install `cat requirements.txt` -c conda-forge
```

And then install the repo using `pip`:
```bash
# Local install
pip install .
```

### Usage

Once installed, the repo functions similarly to any package installed by `pip`
or `conda` and can be imported:

```python
# Import and alias the whole package
import combinatorial_generalization as cg

# Import a specific module
from combinatorial_generalization import combigen

# Import a specific function
from combinatorial_generalization.make_datasets import generate_combigen_x_y_dataset
```
<br>

## API

### Generating Datasets

The main way to use the package is through the high-level data generation
functions in [`make_datasets.py`](combinatorial_generalization/make_datasets.py). 

1. `generate_combigen_x_y_dataset` - Generates sample (X) and label (y) pairs
according to the desired task structure and statistics.

```python
from combinatorial_generalization.make_datasets import generate_combigen_x_y_dataset

# Outputs the data and labels
X, y = generate_combigen_x_y_dataset() 
```

2. `generate_combigen_datasets` - Wraps the above functoin to return training,
testing, and validation datasets

```python
from combinatorial_generalization.make_datasets import generate_combigen_datasets

# Outputs the data and labels
(x_train, y_train), (x_val, y_val), (x_test, y_test) = generate_combigen_datasets()
```

See the docstrings for each of the functions for more details including their
call signatures.

### Visualization

There are two main ways to visualize the task in 
[`vizualize.py`](combinatorial_generalization/visualize.py):

1. `heatmap` - A wrapper for `sns.heatmap` that plots the inputted y and X as a
heatmap.

```python
import matplotlib.pyplot as plt
from combinatorial_generalization.make_datasets import generate_combigen_x_y_dataset
from combinatorial_generalization.visualize import heatmap

# Generate a two sample dataset of X and y pairings
X, y = generate_combigen_x_y_dataset(n_samples=2)

# Plot the sample
heatmap(y, X)
plt.show()
```
<img src="images/heatmap_2_samples.png" class="center"> 

2. `visualize_combigen` - Plots some number of randomly generated X, y pairs of
the combinatorial generalization task.

```python
import matplotlib.pyplot as plt
from combinatorial_generalization.visualize import visualize_combigen

# Plot two randomly generated sample, label pairs
visualize_combigen(n_pairs=2)
plt.show()
```
<img src="images/visualize_combigen_2_samples.png" class="center"> 

<br>

## Example Use-Cases

### Different Numbers of Lines

The task is set by default to use two lines per sample (as in the paper), but 
this is controllable by the user through the `n_lines` argument:

```python
# Generate with four lines
X, y = generate_combigen_x_y_dataset(n_samples=4, n_lines=4)

# Plot the sample
heatmap(y, X)
plt.show()
```
<img src="images/heatmap_4_lines.png" class="center"> 

### Nonuniform Line Statistics

The statistics governing how likely a particular a line appears on a specific
axis can be fully controlled using the `line_stats` argument:

```python
# First and last elements only
line_stats = [[1,0,0,0,0],[0,0,0,0,1]]

# Pass the line_stats arg
X, y = generate_combigen_x_y_dataset(n_samples=2, line_stats=line_stats)

# Plot the sample
heatmap(y, X)
plt.show()
```

<img src="images/heatmap_first_last_elements.png" class="center"> 

The values in `line_stats` will be normalized, so values can be defined relative
to each other. For example, to define positions that are three times more likely
than others:

```python
# First and last elements are 3 times as likely as other elements
line_stats = [[3,1,1,1,1],[1,1,1,1,3]]

# Pass the line_stats arg
X, y = generate_combigen_x_y_dataset(n_samples=4, line_stats=line_stats)

# Plot the sample
heatmap(y, X)
plt.show()
```
<img src="images/heatmap_varied_statistics.png" class="center"> 

<br>

## References

-   [Brousse, O. (1993). Generativity and systematicity in neural network combinatorial learning][2]
-   [Noelle, D. C., & Cottrell, G. W. (1996). In search of articulated attractors][3]
-   [F¨oldi´ak, P. (1990). Forming sparse representations by local anti-Hebbian learning][4]
-   [Saund, E. (1995). A multiple cause mixture model for unsupervised learning][5]
-   [Zemel, R. S. (1993). A minimum description length framework for unsupervised learning][6]
-   [Dayan, P., & Zemel, R. S. (1995). Competition and multiple cause models][7]

<!-- Markdown References -->

[1]: https://www.mitpressjournals.org/doi/10.1162/08997660152002834
[2]: https://scholar.colorado.edu/csci_techreports/647/
[3]: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.51.2295
[4]: https://link.springer.com/article/10.1007%2FBF02331346
[5]: https://www.mitpressjournals.org/doi/10.1162/neco.1995.7.1.51
[6]: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.53.6050
[7]: http://www.gatsby.ucl.ac.uk/~dayan/papers/cdz95.pdf
