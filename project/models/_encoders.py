# Import encoders
from category_encoders.backward_difference import BackwardDifferenceEncoder
from category_encoders.james_stein import JamesSteinEncoder

from ._fetch_hyperparameter import get_hyperparameters

encoders_dict = {
    "BackwardDifferenceEncoder": BackwardDifferenceEncoder(),
    "JamesSteinEncoder": JamesSteinEncoder(),
}

__all__ = ["get_encoders"]

def get_encoders(names, config_file="project/configs/encoder_hp.yaml"):
    """
    Return encoders with their names

    Args:
        name (list of str) :  encoder names
        config_file (str): hyperparameter config file address.
            Defaults to "project/configs/encoder_hp.yaml"

    Returns:
        dict : dictionary of encoders with their names
    """
    # Raise error if input parameters is not a list
    if type(names) != list:
        raise TypeError("{0} must be list of encoder names.".format(names))

    # Raise error if input list contains invalid model name
    invalid_names_ = [item for item in names if item not in list(encoders_dict.keys())]
    if len(invalid_names_) != 0:
        raise ValueError(
            "{0} dont exist in input options{1}".format(
                invalid_names_, encoders_dict.keys()
            )
        )

    # Load hyperparameters of specified encoders in input list
    hyper_dict = get_hyperparameters(model_names=names, file=config_file)

    # Create a dictionary of encoders with their hyperparameters
    models_with_hyperparameters = {}
    for name, hyper in hyper_dict.items():

        models_with_hyperparameters[name] = {
            "model": encoders_dict[name],
            "hyperparameters": hyper,
        }

    return models_with_hyperparameters
