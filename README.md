Machine Learning project template
==============================
A project template to simplify building and training  models, written in Python 3.

Project Organization
------------

    ├── LICENSE
    ├── .pylintrc          <- Python style guidance
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- any data we consider as being external. E.g dictionaries, constants.
    │    ├── processed      <- data after whole preprocessing.
    │    ├── raw            <- here all raw data exists. This directory should be considered as read only - just leave what we got as it is.
    │    └── transformed    <- intermediate format between raw and processed.
    │
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks.
    │
    ├── references         <- Manuals, references and other additional materials.
    │
    ├── reports            <- Reports and generated graphics and figures to be used in reporting.
    │   └── tensorboard        <- Tensorboard results
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── configs        <- Here's the default args config file.
    │   │   └── defaults.py 
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py 
    │   ├── engines           <- this foler contains models structure 
    │   │   └── compile_model.py  <- This file contains of compilation of model.
    │   ├── tests           <- this foler contains unit test of your project.
    │   │   └── test_config.py  <- Example for testing config
    │   ├── tools          <- here's the train/test model of your project.
    │   │   ├── train_net.py  <- Train model
    │   │   └── test_net.py  <- Test model
    │   └── utils
    │       └── logger.py  <- For logging information in txt
    │
    └── 


------------
