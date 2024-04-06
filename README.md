# Employee Attrition

## Goal
Learn ML learning sytem development on Industry following the tutorial from [madewithml](https://madewithml.com). 

The tutorial proved to be invaluable resources for bridging academic knowledge with practical applications in the industry.
<br>

Simple ML probelm:

[IBM HR Analytics](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
Uncover the factors that lead to employee attrition and explore important questions such as ‘show me a breakdown of distance from home by job role and attrition’ or ‘compare average monthly income by education and attrition’. 
Note: This is a fictional data set created by IBM data scientists.


### Setup Dev Environment with Docker

```bash
export PYTHONPATH=$PYTHONPATH:$PWD

# Command to compose
docker-compose run --rm emply-attr
#Or, explicitly make it build docker image
#docker-compose run --rm --build emply-attr
```

### Run Test

```bash
make test
```

Source :

@article{madewithml,
    author       = {Goku Mohandas},
    title        = { Home - Made With ML },
    howpublished = {\url{https://madewithml.com/}},
    year         = {2023}
}

Yan, Ziyou. (Jun 2020). How to Set Up a Python Project For Automation and Collaboration. eugeneyan.com. https://eugeneyan.com/writing/setting-up-python-project-for-automation-and-collaboration/