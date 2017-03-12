# Bayesian Model

Making predictions on whether a tumor being benign or malignant depending on 10 different features known to determine cancer-inducing tumors.

Data is taken from [UCI](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)) (<1000 rows total)

#### Features:

* 1) ID number

Ten real-valued features are computed for each cell nucleus:

* 2) radius (mean of distances from center to points on the perimeter)
* 3) texture (standard deviation of gray-scale values)
* 4) perimeter
* 5) area
* 6) smoothness (local variation in radius lengths)
* 7) compactness (perimeter^2 / area - 1.0)
* 8) concavity (severity of concave portions of the contour)
* 9) concave points (number of concave portions of the contour)
* 10) symmetry
* 11) diagnostic (Malignant = 4, Benign = 2)

#### Installation

```
$ pip install - requirements.txt
```