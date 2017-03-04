import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def print_stats(ben, mal):
    print("BENIGN: STD DVN: {:.2f} --- AVG: {:.2f}".format(np.std(ben), np.mean(ben)))
    print("MALIGN: STD DVN: {:.2f} --- AVG: {:.2f}".format(np.std(mal), np.mean(mal)))


def compare_plots(ben_df, mal_df, name):
    # ben_df.plot(kind='line', title="{} in Benign Tumors".format(name))
    plt.scatter(ben_df.index, ben_df)
    plt.title("{} in Benign Tumors".format(name))
    plt.figure()

    # mal_df.plot(kind='line', title="{} in Malignant Tumors".format(name))
    plt.scatter(mal_df.index, mal_df)
    plt.title("{} in Malignant Tumors".format(name))
    plt.figure(2)

    print_stats(ben_df, mal_df)
    plt.show()


def main():
    # Dataframe object
    df = pd.read_csv('breastCancerWisconsinCorrected.csv', header=None)

    ben = df[df[10] == 2].reset_index()  # 444 benign
    mal = df[df[10] == 4].reset_index()  # 239 malignant

    # Comparisons between ben and mal tumors
    # =========================================================       ============================
    # compare_plots(ben[1], mal[1], "Clump Thickness")                # Clump Thickness
    # compare_plots(ben[2], mal[2], "Uniformity of Cell Size")        # Uniformity of Cell Size
    # compare_plots(ben[3], mal[3], "Uniformity of Cell Shape")       # Uniformity of Cell Shape
    # compare_plots(ben[4], mal[4], "Marginal Adhesion")              # Marginal Adhesion
    # compare_plots(ben[5], mal[5], "Single Epithelial Cell Size")    # Single Epithelial Cell Size
    # compare_plots(ben[6], mal[6], "Bare Nuclei")                    # Bare Nuclei
    # compare_plots(ben[7], mal[7], "Bland Chromatin")                # Bland Chromatin
    # compare_plots(ben[8], mal[8], "Normal Nucleoli")                # Normal Nucleoli
    compare_plots(ben[9], mal[9], "Mitoses")                        # Mitoses


if __name__ == '__main__':
    main()
