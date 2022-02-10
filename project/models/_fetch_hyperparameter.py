from pyaml import yaml

def get_hyperparameters(model_names, file):
    """
    read hyperparameters from yaml file
    Args:
        model_names (list of str)
        file (str): yaml file address

    Returns:
        dict : dictionary of hyperparameters
    """
    stream = open(file, "r")
    hp_dictionary = yaml.safe_load_all(stream)
    
    model_name_with_hyperparameters = {}
    for doc in hp_dictionary:
        if doc["model"] in model_names:
            model_name_with_hyperparameters[doc["model"]] = doc["hyper"]

    return model_name_with_hyperparameters
