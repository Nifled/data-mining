import io
import requests
import numpy as np
import pandas as pd


def get_proportion(arr, val):
    filtered_items = list(filter(lambda x: x == val, arr))

    x, y = len(filtered_items), len(arr)
    return (x/y)*100


def logs(mo, me, mi, ma, std, m, fm):
    print('Mode: {}'.format(mo))
    print('Mean: {0:.2f}'.format(me))
    print('Minimum age: {}'.format(mi))
    print('Maximum age: {}'.format(ma))
    print('Standard Deviation: {0:.2f}'.format(std))
    print('Male %: {0:.2f}'.format(m))
    print('Female %: {0:.2f}'.format(fm))


def main():
    req = requests.get('http://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data').content
    data = pd.read_csv(io.StringIO(req.decode('utf-8')), header=None)

    ages = np.array(data[0]).astype(int)
    sexes = np.array(data[1]).astype(int)

    # .bincount - Count number of occurrences of each value by index.
    # .argmax - Returns the indices of the maximum values.
    mode = np.bincount(ages).argmax()
    mean = np.mean(ages)
    min_val = min(ages)
    max_val = max(ages)
    std_dvn = np.std(ages)
    male = get_proportion(sexes, 1)
    female = get_proportion(sexes, 0)

    logs(mode, mean, min_val, max_val, std_dvn, male, female)


if __name__ == '__main__':
    main()
