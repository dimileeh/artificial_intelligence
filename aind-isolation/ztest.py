""" This module performs Z-test calculations for the difference
    between proportions of two independedent samples.
"""
import scipy
from statsmodels.stats.weightstats import *
from statsmodels.stats.proportion import proportion_confint

def proportions_diff_confint_ind(wins1, wins2, total, alpha = 0.05):
    z = scipy.stats.norm.ppf(1 - alpha / 2.)

    p1 = float(wins1) / total
    p2 = float(wins2) / total

    left_boundary = (p1 - p2) - z * np.sqrt(p1 * (1 - p1)/ total + p2 * (1 - p2)/ total)
    right_boundary = (p1 - p2) + z * np.sqrt(p1 * (1 - p1)/ total + p2 * (1 - p2)/ total)

    return (left_boundary, right_boundary)


def proportions_diff_z_stat_ind(wins1, wins2, total):
    n1 = total
    n2 = total

    p1 = float(wins1) / n1
    p2 = float(wins2) / n2
    P = float(p1*n1 + p2*n2) / (n1 + n2)

    return (p1 - p2) / np.sqrt(P * (1 - P) * (1. / n1 + 1. / n2))


def proportions_diff_z_test(z_stat, alternative = 'two-sided'):
    if alternative not in ('two-sided', 'less', 'greater'):
        raise ValueError("alternative not recognized\n"
                         "should be 'two-sided', 'less' or 'greater'")

    if alternative == 'two-sided':
        return 2 * (1 - scipy.stats.norm.cdf(np.abs(z_stat)))

    if alternative == 'less':
        return scipy.stats.norm.cdf(z_stat)

    if alternative == 'greater':
        return 1 - scipy.stats.norm.cdf(z_stat)
