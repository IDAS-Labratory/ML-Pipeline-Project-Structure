from sklearn.metrics import (
    balanced_accuracy_score,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    fbeta_score,
    matthews_corrcoef,
    make_scorer,
)

from imblearn.metrics import (
    geometric_mean_score,
    sensitivity_score,
    specificity_score,
)


def make_metrics_for_tuning():
    """
    define different metric to evaluate model.

    Returns:
        dict : metric objects with their names.
    """

    return {
        "balanced_accuracy": make_scorer(balanced_accuracy_score),
        "accuracy": make_scorer(accuracy_score),
        "precision": make_scorer(precision_score),
        "recall": make_scorer(recall_score),
        "f1": make_scorer(f1_score),
        "matthews_corrcoef": make_scorer(matthews_corrcoef),
        "specificity":  make_scorer(specificity_score),
        "sensitivity": make_scorer(sensitivity_score),
        "f_2": make_scorer(fbeta_score, beta=2),
        "f_half": make_scorer(fbeta_score, beta=0.5),
        "gmean": make_scorer(geometric_mean_score),
    }


def evalute_test_data(true_label, pred_label):
    """
    Return dictionary of different calculated metrics

    Args:
        true_label (1d array-like, or label indicator array):
            Ground truth (correct) target values.

        pred_label (1d array-like, or label indicator array):
            Estimated targets as returned by a classifier.

    Returns:
        dict : calculated metrics with their names.
    """

    return {
        "test_balanced_accuracy": balanced_accuracy_score(true_label, pred_label),
        "test_accuracy": accuracy_score(true_label, pred_label),
        "test_precision": precision_score(true_label, pred_label),
        "test_recall": recall_score(true_label, pred_label),
        "test_f1": f1_score(true_label, pred_label),
        "test_matthews_corrcoef": matthews_corrcoef(true_label, pred_label),
        "test_specificity": specificity_score(true_label, pred_label),
        "test_sensitivity": sensitivity_score(true_label, pred_label),
        "test_f_2": fbeta_score(true_label, pred_label, beta=2),
        "test_f_half": fbeta_score(true_label, pred_label, beta=0.5),
        "test_gmean": geometric_mean_score(true_label, pred_label),
    }
