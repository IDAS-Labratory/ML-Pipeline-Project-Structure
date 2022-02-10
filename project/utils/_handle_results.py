import pandas as pd
import joblib
from sklearn.utils import estimator_html_repr

def save_results(tuner,
            total_exe_time,
            search_spcace_size,
            model_name,
            over_name,
            imputer_name, 
            encoder_name,
            test_results,
            ):
    """
    This function save results of running each configuration
    into results/output directory, and also save pipeline object 
    as pkl file into results/final-models

    Args:
        tuner (RandomizedSearch object)
        total_exe_time (float): total execution time of tuning
        search_spcace_size (int): hyperparameters search space size
        model_name (str): ML model name
        over_name (str)
        imputer_name (str)
        encoder_name (str)
        test_results (dict): The results of  model evaluation on test data
    """
    
    tuner_cv_results = pd.DataFrame(tuner.cv_results_)
    ## Find best parameters based on refit
    tuner_best_result = tuner_cv_results.loc[[tuner.best_index_]]
    
    model_configs = {}
    model_configs["statistical_model"] = model_name
    model_configs["imputer"] = imputer_name
    model_configs["oversampler"] = over_name
    model_configs["encoder"] = encoder_name
    model_configs["search_space_size"] = search_spcace_size
    model_configs["total_exe_time"] = total_exe_time
    
    model_configs = pd.DataFrame([model_configs])

    test_results = pd.DataFrame([test_results])
    
    frame = pd.DataFrame(
        pd.concat([model_configs.iloc[0],test_results.iloc[0],tuner_best_result.iloc[0]]))
    frame.to_csv("project/results/outputs/"+model_name+"_"+over_name+"_"+imputer_name+"_"+encoder_name+".csv")
    #Saving pipeline
    joblib.dump(tuner.best_estimator_,"project/results/final-models/"+model_name+"_"+over_name+"_"+imputer_name+"_"+encoder_name+".pkl")
    
    with open("project/results/outputs/"+model_name+"_"+over_name+"_"+imputer_name+"_"+encoder_name+".html", 'w') as f:
        f.write(estimator_html_repr(tuner.best_estimator_))
