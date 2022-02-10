# Import oversamplers
from imblearn.over_sampling import SMOTE
from imblearn.over_sampling import SVMSMOTE

# Import auxiliary functions
from ._fetch_hyperparameter import get_hyperparameters


__all__ = ["get_oversampler"]

oversamplers_dict = {
    "SMOTE": SMOTE(),
    "SVMSMOTE": SVMSMOTE(),
}


def get_oversampler(names, config_file="project/configs/oversampler_hp.yaml"):
    """
    Return oversamplers with their names

    Args:
        name (list of str) :  oversampler names
        config_file (str): hyperparameter config file address.
            Defaults to "project/configs/oversampler_hp.yaml"

    Returns:
        dict : dictionary of oversamplers with their hyperparameters
    """

    # Raise error if input parameters is not a list
    if type(names) != list:
        raise TypeError("{0} must be list of model names.".format(names))

    # Raise error if input list contains invalid name
    invalid_names_ = [
        item for item in names if item not in list(oversamplers_dict.keys())
    ]
    if len(invalid_names_) != 0:
        raise ValueError(
            "{0} dont exist in input options{1}".format(
                invalid_names_, oversamplers_dict.keys()
            )
        )

    # Load hyperparameters of specified oversamplers in input list
    hyper_dict = get_hyperparameters(model_names=names, file=config_file)

    # Create a dictionary of oversamplers with their hyperparameters
    models_with_hyperparameters = {}
    for name, hyper in hyper_dict.items():
        models_with_hyperparameters[name] = {
            "model": oversamplers_dict[name],
            "hyperparameters": hyper,
        }

    return models_with_hyperparameters
