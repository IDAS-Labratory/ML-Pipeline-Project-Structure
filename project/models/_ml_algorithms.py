# Import ML models
from sklearn.svm import SVC
from xgboost import XGBClassifier

# Import auxiliary functions
from ._fetch_hyperparameter import get_hyperparameters

__all__ = ["get_ml_algo"]


classifiers_dict = {
    "XGB": XGBClassifier(),
    "SVC": SVC(),
}


def get_ml_algo(names, config_file="project/configs/ml_algorithm_hp.yaml"):
    """
    Return  ML models with their hyperparameters

    Args:
        name (list of str) :  ML model names
        config_file (str): hyperparameter config file address.
            Defaults to "project/configs/ml_algorithm_hp.yaml"

    Returns:
        dict : dictionary of models with their hyperparameters
    """

    # Raise error if input parameters is not a list
    if type(names) != list:
        raise TypeError("{0} must be list of model names.".format(names))

    # Raise error if input list contains invalid name
    invalid_names_ = [
        item for item in names if item not in list(classifiers_dict.keys())
    ]
    if len(invalid_names_) != 0:
        raise ValueError(
            "{0} dont exist in input options{1}".format(
                invalid_names_, classifiers_dict.keys()
            )
        )

    # Load hyperparameters of specified ML models in input list
    hyper_dict = get_hyperparameters(model_names=names, file=config_file)

    # Create a dictionary of ML models with their hyperparameters
    models_with_hyperparameters = {}
    for name, hyper in hyper_dict.items():

        models_with_hyperparameters[name] = {
            "model": classifiers_dict[name],
            "hyperparameters": hyper,
        }

    return models_with_hyperparameters
