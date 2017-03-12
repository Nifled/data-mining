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
    count = np.zeros((df.shape[1] - 1, len(values) - 1))

    for val in values:
        map_val = df[df.ix[:, 1:10] == val]
        map_val = clean_dataframe(map_val, val, 1)

        count[val - 1][:] = np.sum(map_val)[1:10]  # Fills count's [val] row with sum of value in each column.

    result = pd.DataFrame(count, index=values)  # Index range 1-10
    return result + 1  # Add one to every element to filter out the 0's


def test(norm_ben, norm_mal, P_ben, P_mal):
    """
    Generate dataframe containing expected output (Expected) and output columns (Result).
    :param norm_ben & norm_mal: Dataframes to be used to test against Test-set.
    :param P_ben: General probability of benign tumors in Train-set.
    :param P_mal: General probability of malignant tumors in Train-set.
    :return: Dataframe
    """
    test = pd.read_csv('data/Test.csv', header=None)

    expected = test[test.shape[1]-1]  # Stores the actual RIGHT answer column (expected output of each row)

    test = test.ix[:, 1:9]  # Gets columns 1-9, which are the attributes to determine output

    results = []
    for test_index, row in test.iterrows():

        # Initialize the product by row with probability of instance in each row within Test.
        prod_ben = P_ben
        prod_mal = P_mal
        for index, num in enumerate(row):
            # Multiply prod every loop by the prob of num in every attribute in normalized tables.
            prod_ben *= norm_ben[index][num]
            prod_mal *= norm_mal[index][num]

        if prod_ben > prod_mal:
            results.append(2)
        else:
            results.append(4)

    # Create a dataframe with two columns: [0]: Expected values, [1]: Machine results
    d = pd.DataFrame({'Result': results, 'Expected': expected})
    return d


def main():
    # Dataframe object containing all train-set data
    df = pd.read_csv('data/Train.csv', header=None)

    ben = df[df[10] == 2].reset_index(drop=True)  # 289 benign
    mal = df[df[10] == 4].reset_index(drop=True)  # 155 malignant

    P_ben = ben.shape[0] / (ben.shape[0] + mal.shape[0])  # General probability of tumor being benign.
    P_mal = mal.shape[0] / (ben.shape[0] + mal.shape[0])  # General probability of tumor being malignant.

    # Values that every atribute can take (range of 1-10)
    values = pd.Series(range(1, 11))

    freq_ben = get_frequency(ben, values)  # Benign tumor's frequency table.
    freq_mal = get_frequency(mal, values)  # Malignan tumor's freq table.

    divisor_ben = np.sum(freq_ben)[0]  # Scalar to be used to normalize frequency tables.
    divisor_mal = np.sum(freq_mal)[0]

    normalized_ben = freq_ben.div(other=divisor_ben)  # Benign tumor's normalized table
    normalized_mal = freq_mal.div(other=divisor_mal)  # Malignant tumor's normalized table

    test_results = test(normalized_ben, normalized_mal, P_ben, P_mal)  # Call test function.

    # Map out all correct machine predictions.
    correct = test_results[test_results['Expected'] == test_results['Result']]

    percentage = correct.shape[0] / test_results.shape[0] * 100
    print('Consistency: {0:.2f} %'.format(percentage))


if __name__ == '__main__':
    main()
