# Project structure to Run Hundreds of ML Pipelines
In this repository, we want to propose an organized structure for your ML projects to simplify traning and tuning lots of ML pipelines.
This repository is based on (medium article)

(add pipeline image)


## Table of contents

- [Project structure to Run Hundreds of ML Pipelines](#project-structure-to-run-hundreds-of-ml-pipelines)
- [Preview](#preview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
     - [Requirements](#requirements)
- [Usage](#usage)
- [Project structure](#project-structure)
    - [Data flow between directories](#data-flow-between-directories)

## Prerequisites
[(Back to top)](#table-of-contents)

Knowing following concepts give you a great idea what we try to talk about.
‌Basic machine learning concepts.
- Basic python (3 or higher versions)
- Having a little experience with ML libraries such as scikit-learn, XGBoost, Dask, pandas, or etc.
- And some other libraries like imbalanced-learn, category_encoders would help you.

### Installation
[(Back to top)](#table-of-contents)

To use this project, first clone the repo on your device using the command below:

```git init```

```git clone https://github.com/IDAS-Labratory/Project-Structure-to-Run-Hundreds-of-ML-Pipelines.git```

## Requirements
```pip install requirements.txt```

## Usage
[(Back to top)](#table-of-contents)

To run this sample project just go to main_run.ipynb notebook and run all cells.

## Project structure
[(Back to top)](#table-of-contents)
```
.
├── project                       <- project's name
│   ├── configs                   <- Yaml config files correspond to ML models, dimensionality reduction
|   |   |                            algorithms, oversamplers and any other components in your pipeline
│   │   ├── encoder_hp.yaml          that you want to tune it.
│   │   ├── ml_model_hp.yaml
│   │   ├── imputer_hp.yaml
│   │   └── oversampler_hp.yaml
|   |
│   ├── models                    <- Seperating each main component of your pipeline into
|   |   |                             different .py files.
│   │   ├── __init__.py
│   │   ├── _encoders.py
│   │   ├── _fetch_hyperparameter.py
│   │   ├── _imputers.py
│   │   ├── _ml_algorithms.py
│   │   └── _oversamplers.py
|   |
│   ├── pipelines                 <- Putting your pipelines(if you have several) here. 
|   |   |                            Each pipeline is written as a function.
│   │   ├── __init__.py
│   │   └── _make_pipeline.py
|   |
│   ├── results                   
|   |   |                            
│   │   ├── final-models          <- Saving results of training and testing.
│   │   └── outputs               <- Serialized pipelines are stored here.
|   |
│   └── utils
│       ├── __init__.py
│       ├── _handle_results.py
│       ├── _evaluation_metrics.py
│       └── _load_data.py
|
├── analytics                     <- Putting your analytical notebooks here.
|   |
│   ├── hypotesting
│   └── visualization
|
├── requirements.txt
|
├── main_run.ipynb
|
├── api                          
|
├── data
|   |
│   ├── intermediate             <- Intermediate data that has been transformed.
│   ├── processed                <- The final, canonical data sets for modeling.
│   └── raw                      <- The original, immutable data dump.
│       └── H1N1_Flu_Vaccines.csv
|
├── docker                       <- Docker file of your project.
├── experiments                  <- To test new model, lib etc.
├── lib                          <- Libraries that need to be added manually.
│   └── impute                   
│       ├── __init__.py
│       └── _knn.py
├── papers                       <- Papers which are related to your project.
└── scripts                      <- Scripts like scraping etc (if it is needed).

```

## Data flow between directories
[(Back to top)](#table-of-contents)

<!-- This is the place where you give instructions to developers on how to modify the code.

You could give **instructions in depth** of **how the code works** and how everything is put together.

You could also give specific instructions to how they can setup their development environment.

Ideally, you should keep the README simple. If you need to add more complex explanations, use a wiki. Check out [this wiki](https://github.com/navendu-pottekkat/nsfw-filter/wiki) for inspiration. -->

# Contribute
[(Back to top)](#table-of-contents)

<!-- This is where you can let people know how they can **contribute** to your project. Some of the ways are given below.

Also this shows how you can add subsections within a section. -->



<!-- Your project is gaining traction and it is being used by thousands of people(***with this README there will be even more***). Now it would be a good time to look for people or organisations to sponsor your project. This could be because you are not generating any revenue from your project and you require money for keeping the project alive.

You could add how people can sponsor your project in this section. Add your patreon or GitHub sponsor link here for easy access.

A good idea is to also display the sponsors with their organisation logos or badges to show them your love!(*Someday I will get a sponsor and I can show my love*) -->

### Adding new features or fixing bugs
[(Back to top)](#table-of-contents)

<!-- This is to give people an idea how they can raise issues or feature requests in your projects. 

You could also give guidelines for submitting and issue or a pull request to your project.

Personally and by standard, you should use a [issue template](https://github.com/navendu-pottekkat/nsfw-filter/blob/master/ISSUE_TEMPLATE.md) and a [pull request template](https://github.com/navendu-pottekkat/nsfw-filter/blob/master/PULL_REQ_TEMPLATE.md)(click for examples) so that when a user opens a new issue they could easily format it as per your project guidelines.

You could also add contact details for people to get in touch with you regarding your project. -->

