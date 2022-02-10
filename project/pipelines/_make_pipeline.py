# Import Pipeline class from imblearn library
from imblearn.pipeline import Pipeline

# Import auxiliary functions
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import RobustScaler

from project.utils import read_columns

__all__ = [
    "make_main_pipeline",
]

# Read dataset columns
columns_dict = read_columns()
categorical_features = columns_dict["categorical_features"].copy()
continuous_features = columns_dict["continuous_features"].copy()


def make_main_pipeline(
    classifier,
    imputer,
    encoder,
    oversampler,
):
    """
    Create pipeline with ML model, missing value imputer, encoder
    and oversampler.
    Created Pipeline is an instance of Pipeline class from imblearn.pipeline library.
    Created Pipeline include RobustScaler in its steps.

    Args:
        classifier : ML classifier object
        imputer : imputer object
        encoder : encoder object
        oversampler : oversampler object

    Returns:
        Pipeline object
    """
    main_pipeline = Pipeline(
        steps=[
            ("imputing", imputer),
            (
                "preprocessing",
                ColumnTransformer(
                    transformers=[
                        (
                            "categorical",
                            Pipeline(steps=[("encoding", encoder)]),
                            categorical_features,
                        ),
                        (
                            "continuous",
                            Pipeline(steps=[("normalizing", RobustScaler())]),
                            continuous_features,
                        ),
                    ]
                ),
            ),
            ("oversampling", oversampler),
            ("classifying", classifier),
        ]
    )

    return main_pipeline
