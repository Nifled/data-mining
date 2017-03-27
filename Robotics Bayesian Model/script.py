import pandas as pd
import numpy as np


def clean_dataframe(df, to_replace, value):
    """
    Replaces all of given to_replace instances in Dataframe or Series with given value and fills
    NaN values with 0.
    Doesn't directly affect the df.
    :param df: Dataframe
    :param to_replace: See pandas Dataframe.replace()
    :param value: See pandas Dataframe.replace()
    :return: Dataframe or Series with all values replaced.
    """
    df = df.replace(to_replace=to_replace, value=value).fillna(value=0)
    return df


def get_frequency(df, values):
    """
    Generates frequency table depending on given values (row).
    :param df: Dataframe or Series pandas object.
    :param values: Possible values that every attribute can take.
    :return: Dataframe (frequency table).
    """
    count = pd.DataFrame(np.zeros((values.shape[0], df.shape[1])), index=values)

    for val in values:
        map_values = df[df.ix[:, 1:] == val]
        map_values = clean_dataframe(map_values, val, 1)

        count.loc[val][:] = np.sum(map_values)

    return count + 1  # Add one to every element to filter out the 0's


def get_normalized(freq_table):
    """
    Returns a normalized table (Dataframe obj) based on a given frequency table.
    :param freq_table: Table with frequencies of all values based on their features.
    :return:
    """
    divisor = np.sum(freq_table)[1]

    return freq_table.div(other=divisor)


def run_tests(*args):

    for x in args:
        print('arg')
    pass


def main():
    # Dataframe object containing all train-set data
    df = pd.read_csv('data/Robot_Train.csv', header=None)

    # Failure classes
    f1 = df[df[0] == 1].reset_index(drop=True)  # 39 Normal
    f2 = df[df[0] == 2].reset_index(drop=True)  # 24 Bottom Collision
    f3 = df[df[0] == 3].reset_index(drop=True)  # 17 Bottom Obstruction
    f4 = df[df[0] == 4].reset_index(drop=True)  # 42 Collision in Part
    f5 = df[df[0] == 5].reset_index(drop=True)  # 22 Collision in Tool

    total = df.shape[0]
    # Probabilities of failure classes
    P_f1 = f1.shape[0] / total
    P_f2 = f2.shape[0] / total
    P_f3 = f3.shape[0] / total
    P_f4 = f4.shape[0] / total
    P_f5 = f5.shape[0] / total

    # Every value that each feature can possibly take.
    values = pd.read_csv('data/values.csv', header=None)[0]

    # Generate normalized tables for each class based on their frequency table
    norm_f1 = get_normalized(get_frequency(f1, values))
    norm_f2 = get_normalized(get_frequency(f2, values))
    norm_f3 = get_normalized(get_frequency(f3, values))
    norm_f4 = get_normalized(get_frequency(f4, values))
    norm_f5 = get_normalized(get_frequency(f5, values))

    test = pd.read_csv('data/Robot_Test.csv', header=None)

    expected = test[0]

    test = test.ix[:, 1:]

    results = []
    for test_index, row in test.iterrows():

        # Initialize all products by their probability.
        prod_f1, prod_f2, prod_f3, prod_f4, prod_f5 = P_f1, P_f2, P_f3, P_f4, P_f5
        for index, num in enumerate(row):
            prod_f1 *= norm_f1[index][num]
            prod_f2 *= norm_f2[index][num]
            prod_f3 *= norm_f3[index][num]
            prod_f4 *= norm_f4[index][num]
            prod_f5 *= norm_f5[index][num]

        max_prob = max([prod_f1, prod_f2, prod_f3, prod_f4, prod_f5])

        if max_prob == prod_f1:
            results.append(1)
        elif max_prob == prod_f2:
            results.append(2)
        elif max_prob == prod_f3:
            results.append(3)
        elif max_prob == prod_f4:
            results.append(4)
        elif max_prob == prod_f5:
            results.append(5)

    test_results = pd.DataFrame({'Result': results, 'Expected': expected})

    print(test_results)

    # Map out all correct machine predictions.
    correct = test_results[test_results['Expected'] == test_results['Result']]

    percentage = correct.shape[0] / test_results.shape[0] * 100
    print('Consistency: {0:.2f} %'.format(percentage))


if __name__ == '__main__':
    main()
