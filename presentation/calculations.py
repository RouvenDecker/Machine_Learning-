from scipy.stats import pearsonr
import pandas as pd


def calc_corr(feats: list[pd.Series], target) -> list:
    correlations: list = []
    for feat in feats:
        correlations.append(pearsonr(feat, target).statistic)
    return correlations
