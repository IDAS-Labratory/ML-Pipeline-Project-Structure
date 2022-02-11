<!-- Add banner here -->

# Project structure to Run Hundreds of ML Pipelines
In this repository, we want to propose an organized structure for your ML projects to simplify traning and tuning lots of ML pipelines.
This repository is based on (medium article)

(add pipeline image)
<!-- Add buttons here -->

<!-- Describe your project in brief -->

<!-- The project title should be self explanotory and try not to make it a mouthful. (Although exceptions exist- **awesome-readme-writing-guide-for-open-source-projects** - would have been a cool name)

Add a cover/banner image for your README. **Why?** Because it easily **grabs people's attention** and it **looks cool**(*duh!obviously!*).

The best dimensions for the banner is **1280x650px**. You could also use this for social preview of your repo.

I personally use [**Canva**](https://www.canva.com/) for creating the banner images. All the basic stuff is **free**(*you won't need the pro version in most cases*).

There are endless badges that you could use in your projects. And they do depend on the project. Some of the ones that I commonly use in every projects are given below. 

I use [**Shields IO**](https://shields.io/) for making badges. It is a simple and easy to use tool that you can use for almost all your badge cravings. -->

<!-- Some badges that you could use -->

<!-- ![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/navendu-pottekkat/awesome-readme?include_prereleases)
: This badge shows the version of the current release.

![GitHub last commit](https://img.shields.io/github/last-commit/navendu-pottekkat/awesome-readme)
: I think it is self-explanatory. This gives people an idea about how the project is being maintained.

![GitHub issues](https://img.shields.io/github/issues-raw/navendu-pottekkat/awesome-readme)
: This is a dynamic badge from [**Shields IO**](https://shields.io/) that tracks issues in your project and gets updated automatically. It gives the user an idea about the issues and they can just click the badge to view the issues.

![GitHub pull requests](https://img.shields.io/github/issues-pr/navendu-pottekkat/awesome-readme)
: This is also a dynamic badge that tracks pull requests. This notifies the maintainers of the project when a new pull request comes.

![GitHub All Releases](https://img.shields.io/github/downloads/navendu-pottekkat/awesome-readme/total): If you are not like me and your project gets a lot of downloads(*I envy you*) then you should have a badge that shows the number of downloads! This lets others know how **Awesome** your project is and is worth contributing to.

![GitHub](https://img.shields.io/github/license/navendu-pottekkat/awesome-readme)
: This shows what kind of open-source license your project uses. This is good idea as it lets people know how they can use your project for themselves.

![Tweet](https://img.shields.io/twitter/url?style=flat-square&logo=twitter&url=https%3A%2F%2Fnavendu.me%2Fnsfw-filter%2Findex.html): This is not essential but it is a cool way to let others know about your project! Clicking this button automatically opens twitter and writes a tweet about your project and link to it. All the user has to do is to click tweet. Isn't that neat? -->

# Demo-Preview

<!-- Add a demo for your project -->

<!-- After you have written about your project, it is a good idea to have a demo/preview(**video/gif/screenshots** are good options) of your project so that people can know what to expect in your project. You could also add the demo in the previous section with the product description.

Here is a random GIF as a placeholder.

![Random GIF](https://media.giphy.com/media/ZVik7pBtu9dNS/giphy.gif) -->

# Table of contents

<!-- After you have introduced your project, it is a good idea to add a **Table of contents** or **TOC** as **cool** people say it. This would make it easier for people to navigate through your README and find exactly what they are looking for.

Here is a sample TOC(*wow! such cool!*) that is actually the TOC for this README. -->

- [Project structure to Run Hundreds of ML Pipelines](#project-structure-to-run-hundreds-of-ml-pipelines)
- [Preview](#preview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
     - [Requirements](#requirements)
- [Usage](#usage)
- [Project structure](#project-structure)
    - [Data flow between directories](#data-flow-between-directories)
- [Contribute](#contribute)
    - [Adding new features or fixing bugs](#adding-new-features-or-fixing-bugs)

- [Footer](#footer)

# Preview
[(Back to top)](#table-of-contents)

# Prerequisites
[(Back to top)](#table-of-contents)

Knowing following concepts give you a great idea what we try to talk about.
‌Basic machine learning concepts.
- Basic python (3 or higher versions)
- Having a little experience with ML libraries such as scikit-learn, XGBoost, Dask, pandas, or etc.
- And some other libraries like imbalanced-learn, category_encoders would help you.

# Installation
[(Back to top)](#table-of-contents)

To use this project, first clone the repo on your device using the command below:

```git init```

```git clone ```

## Requirements
```pip install requirements.txt```
<!-- *You might have noticed the **Back to top** button(if not, please notice, it's right there!). This is a good idea because it makes your README **easy to navigate.*** 

The first one should be how to install(how to generally use your project or set-up for editing in their machine).

This should give the users a concrete idea with instructions on how they can use your project repo with all the steps.

Following this steps, **they should be able to run this in their device.**

A method I use is after completing the README, I go through the instructions from scratch and check if it is working. -->

<!-- Here is a sample instruction:

To use this project, first clone the repo on your device using the command below:

```git init```

```git clone https://github.com/navendu-pottekkat/nsfw-filter.git``` -->

# Usage
[(Back to top)](#table-of-contents)

To run this sample project just go to main_run.ipynb notebook and run all cells.

<!-- This is optional and it is used to give the user info on how to use the project after installation. This could be added in the Installation section also. -->

# Project structure
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
├── Analytics                     <- Putting your analytical notebooks here.
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

