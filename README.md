# Naming the Pain in Machine Learning
This repository aims at establishing an environment for generating graphical visualizations of the responses provided as part of the Machine Learning in Practice 2022 survey, that was available at https://ww2.unipark.de/uc/seml/. 

Questions D1 to D15 and Q1 to Q17 are explored using Jupyter Notebooks. 

## Presentation

The results, are available in presentation format at
https://docs.google.com/presentation/d/1Zg4EJQ8EYiCTetFqZbHb8bgPUM8DXwif5LntebSKd-c/edit?usp=sharing

## How to Execute

The project is contained in a Python virtual environment using pipenv, all you have to do to execute it follows:

1. pip install --user pipenv (install pipenv on your machine)
2. pipenv install (or python -m pipenv install) (in a command line terminal, in the same folder where the project was cloned) 
3. pipenv shell (or python -m pipenv shell) (initializes the terminal with the already installed dependencies)
4. jupyter notebook (opens Jupyter Notebook in the folder of the project, including all the individual notebook files)

## New Packages

To install or uninstall new packages and dependencies:

- pipenv install pandas (could be any package included in pip)
- pipenv uninstall pandas
