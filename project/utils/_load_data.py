import dask.dataframe as dd

__all__ = ["read_columns", "custome_read_data"]

columns_name = {"h1n1_vaccine": "label"}

nominal_features = [
    "race",
    "sex",
    "marital_status",
    "rent_or_own",
    "employment_status",
    "behavioral_wash_hands",
    "behavioral_large_gatherings",
    "behavioral_antiviral_meds",
    "behavioral_avoidance",
    "behavioral_face_mask",
    "behavioral_outside_home",
    "behavioral_touch_face",
    "doctor_recc_h1n1",
    "doctor_recc_seasonal",
    "chronic_med_condition",
    "child_under_6_months",
    "health_worker",
    "health_insurance",
    "hhs_geo_region",
    "census_msa",
    "employment_industry",
    "employment_occupation",
]
label = ["h1n1_vaccine"]

ordinal_features = [
    "age_group",
    "education",
    "income_poverty",
    "h1n1_concern",
    "h1n1_knowledge",
    "opinion_h1n1_vacc_effective",
    "opinion_h1n1_risk",
    "opinion_h1n1_sick_from_vacc",
    "opinion_seas_vacc_effective",
    "opinion_seas_risk",
    "opinion_seas_sick_from_vacc",
]

continous_features = [
    "household_adults",
    "household_children",
]

categorical_features = nominal_features + ordinal_features
all_features = nominal_features + ordinal_features + continous_features + label


def read_columns():
    """
    Just return dataset columns names

    Returns:
        dict : dictionary contains all_features, continuous_features
        categorical_features, ordianl_features, nominal_features
    """
    return {
        "all_features": all_features.copy(),
        "continuous_features": continous_features.copy(),
        "categorical_features": categorical_features.copy(),
        "ordianl_features": ordinal_features.copy(),
        "nominal_features": nominal_features.copy(),
    }


def custome_read_data(path="data/raw/H1N1_Flu_Vaccines.csv"):
    """
    Read raw data and process it

    Args:
        path (str, optional):path to csv data. Defaults to "data/raw/H1N1_Flu_Vaccines.csv".

    Returns:
        dict : dict contains processed data, continuous_features, categorical_features
    """
    try:
        h1n1_data = dd.read_csv(
            urlpath=path,
            usecols=all_features,
        )
    except FileNotFoundError:
        print("The {0} file was not found".format(str(path)), "\n")
    except PermissionError:
        print("No permission to access the file {0}".format(str(path)))

    h1n1_data = h1n1_data.rename(columns=columns_name)

    h1n1_data = _preprocess_input_data(h1n1_data)
    # h1n1_data = _drop_column(h1n1_data)

    return {
        "data": h1n1_data,
        "continuous_features": continous_features,
        "categorical_features": categorical_features,
        "ordianl_features": ordinal_features,
        "nominal_features": nominal_features,
    }


def _drop_column(data, missing_value_thresh=0.4):
    """
    Drop columns which have missign values more than threshold

    Args:
        data (dask DataFrame)
        missing_value_thresh (float): Defaults to 0.4.
    """
    # Checking threshold range
    if not 0 <= missing_value_thresh <= 1:
        raise ValueError("{0} is not between 0 and 1.".format(missing_value_thresh))
    # Checking data object type
    if not isinstance(data, dd.DataFrame):
        raise TypeError("data must be a Dask DataFrame.")
    missing_values = data.isnull().sum()
    # Calculate percentage of missing values in each column
    percent_of_missing = missing_values / data.index.size
    # Drop columns which have missign values more than threshold
    for column_name, missing_percnet in percent_of_missing.iteritems():
        if missing_percnet >= missing_value_thresh:
            data = data.drop(labels=column_name, axis=1)

    return data


def _preprocess_input_data(data):
    """
    Preprocess raw data.
    Changing categorical features to numerical.

    Args:
        data (dask DataFrame) : raw dataset

    Returns:
        DataFrame: processed dataset
    """
    ## Replace age_group values with numbers
    data["age_group"] = data["age_group"].replace(
        {
            "18 - 34 Years": 1,
            "35 - 44 Years": 2,
            "45 - 54 Years": 3,
            "55 - 64 Years": 4,
            "65+ Years": 5,
        }
    )
    ## Replace education values with numbers
    data["education"] = data["education"].replace(
        {
            "< 12 Years": 1,
            "12 Years": 2,
            "College Graduate": 3,
            "Some College": 4,
        }
    )
    ## Replace race values with numbers
    data["race"] = data["race"].replace(
        {
            "White": 1,
            "Black": 2,
            "Other or Multiple": 3,
            "Hispanic": 4,
        }
    )
    ## Replace sex values with numbers
    data["sex"] = data["sex"].replace(
        {
            "Female": 1,
            "Male": 2,
        }
    )
    ## Replace income_poverty values with numbers
    data["income_poverty"] = data["income_poverty"].replace(
        {"Below Poverty": 0, "<= $75,000, Above Poverty": 1, "> $75,000": 2}
    )
    ## Replace marital_status values with numbers
    data["marital_status"] = data["marital_status"].replace(
        {
            "Not Married": 0,
            "Married": 1,
        }
    )
    ## Replace rent_or_own values with numbers
    data["rent_or_own"] = data["rent_or_own"].replace(
        {
            "Own": 0,
            "Rent": 1,
        }
    )
    ## Replace employment_status values with numbers
    data["employment_status"] = data["employment_status"].replace(
        {
            "Not in Labor Force": 0,
            "Employed": 1,
            "Unemployed": 2,
        }
    )
    ## Replace hhs_geo_region values with numbers
    data["hhs_geo_region"] = data["hhs_geo_region"].replace(
        {
            "oxchjgsf": 0,
            "bhuqouqj": 1,
            "qufhixun": 2,
            "lrircsnp": 3,
            "atmpeygn": 4,
            "lzgpxyit": 5,
            "fpwskwrf": 6,
            "mlyzmhmf": 7,
            "dqpwygqj": 8,
            "kbazzjca": 9,
        }
    )
    ## Replace census_msa values with numbers
    data["census_msa"] = data["census_msa"].replace(
        {"Non-MSA": 0, "MSA, Not Principle  City": 1, "MSA, Principle City": 2}
    )
    ## Replace employment_industry values with numbers
    data["employment_industry"] = data["employment_industry"].replace(
        {
            "pxcmvdjn": 0,
            "rucpziij": 1,
            "wxleyezf": 2,
            "saaquncn": 3,
            "xicduogh": 4,
            "ldnlellj": 5,
            "wlfvacwt": 6,
            "nduyfdeo": 7,
            "fcxhlnwr": 8,
            "vjjrobsf": 9,
            "arjwrbjb": 10,
            "atmlpfrs": 11,
            "msuufmds": 12,
            "xqicxuve": 13,
            "phxvnwax": 14,
            "dotnnunm": 15,
            "mfikgejo": 16,
            "cfqqtusy": 17,
            "mcubkhph": 18,
            "haxffmxo": 19,
            "qnlwzans": 20,
        }
    )
    ## Replace employment_occupation values with numbers
    data["employment_occupation"] = data["employment_occupation"].replace(
        {
            "xgwztkwe": 0,
            "xtkaffoo": 1,
            "emcorrxb": 2,
            "vlluhbov": 3,
            "xqwwgdyp": 4,
            "ccgxvspp": 5,
            "qxajmpny": 6,
            "kldqjyjy": 7,
            "mxkfnird": 8,
            "hfxkjkmi": 9,
            "bxpfxfdn": 10,
            "ukymxvdu": 11,
            "cmhcxjea": 12,
            "haliazsg": 13,
            "dlvbwzss": 14,
            "xzmlyyjv": 15,
            "oijqvulv": 16,
            "rcertsgn": 17,
            "hodpvpew": 18,
            "uqqtjvyb": 19,
            "pvmttkik": 20,
            "dcjcmpih": 21,
            "tfqavkke": 22,
        }
    )

    return data
