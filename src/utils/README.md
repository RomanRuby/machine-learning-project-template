Machine Learning project template
==============================


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
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


------------

PyCharm Environment settings
------------
 * Choose File in navigation menu.   
View drop-down list and go down to Settings.
 * Choose Project:[name]  
   -> Project Interpreter 
![image info](/home/rnagibov/Documents/machine-learning-project-template/references/settings.png)
 * On the right area press the icon 'gear' and choose "Show All"
![image info](/home/rnagibov/Documents/machine-learning-project-template/references/project_interpr.png)
 * Press icon 'plus' 
![image info](/home/rnagibov/Documents/machine-learning-project-template/references/interpreters.png)
 * Сheck that the item is selected 'New environment' and press 'Ok'
![image info](/home/rnagibov/Documents/machine-learning-project-template/references/add_interpr.png)
------------

