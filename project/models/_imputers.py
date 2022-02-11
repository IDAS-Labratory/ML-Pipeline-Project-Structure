# Import imputers
from lib.impute import CustomKnnImputer

# Import auxiliary functions
from project.utils import read_columns
from ._fetch_hyperparameter import get_hyperparameters

__all__ = ["get_imputer"]

columns_dict = read_columns()
all_features = columns_dict["all_features"].copy()
categorical_features = columns_dict["categorical_features"].copy()
all_features.remove("h1n1_vaccine")

imputers_dict = {
    "KnnImputer": CustomKnnImputer(
        category_cols=categorical_features, cols=all_features
    ),
}

def get_imputer(names, config_file="project/configs/imputer_hp.yaml"):
    """
    Return imputers with their names

    Args:
        name (list of str) :  imputer names
        config_file (str): hyperparameter config file address.
            Defaults to "project/configs/imputer_hp.yaml"
        
    Returns:
        dict : dictionary of imputers with their names
    """
    ## Raise error if input parameters is not a list
    if type(names) != list:
        raise TypeError("{0} must be list of imputer names.".format(names))

    ## Raise error if input list contains invalid model name
    invalid_names_ = [item for item in names if item not in list(imputers_dict.keys())]
    if len(invalid_names_) != 0:
        raise ValueError(
            "{0} dont exist in input options{1}".format(
                invalid_names_, imputers_dict.keys()
            )
        )
    
    # Load hyperparameters of specified imputers models in input list
    hyper_dict = get_hyperparameters(model_names=names, file=config_file)

    # Create a dictionary of imputers with their hyperparameters
    models_with_hyperparameters = {}
    for name, hyper in hyper_dict.items():

        models_with_hyperparameters[name] = {
            "model": imputers_dict[name],
            "hyperparameters": hyper,
        }

    return models_with_hyperparameters
