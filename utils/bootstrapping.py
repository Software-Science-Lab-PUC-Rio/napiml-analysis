"""
Bootstrapping handler.

This module aims to center the process 
and computation of bootstrapping.

Author: Antonio Pedro Santos Alves
Advisor: Marcos Kalinowski
"""

import random
import math
import numpy as np
from scipy.stats import t


class BootstrappingUtils:    
    def __init__(self, answers: list[any], options: list[str], replacements: int = 1000, population_size: int = 1000, confidence: float = 95):
        self.answers = answers
        self.options = options
        self.replacements = replacements
        self.population_size = population_size
        self.confidence = confidence


    def bootstrapping(self, question_type: str):
        """
           Create bootstrapping for 'to-choose-options' questions,
           like both single and multiple choice.
        """

        populations = []
        for _ in range(self.population_size):
            if question_type == 'single':
                population = self.single_option_sampling()

            elif question_type == 'multiple':
                population = self.multiple_option_sampling()

            populations.append(population)

        # compute the percentage of answers in each option for each population/replacement
        population_metrics = {option: 
            {
                'population': [],
                'confidence': ()
            } for option in self.options
        }

        # add population mean total answers
        for population in populations:
            for option in population:
                population_metrics[option]['population'].append(population[option])

        # compute confidence
        for option in population_metrics:
            population_metrics[option]['confidence'] = self.confidence_interval(population_metrics[option]['population'])

        return population_metrics


    def bootstrapping_numerical_fields(self):
        """
            Create bootstrapping for 'set-numerical-value' questions,
            like 'What is your age?', 'What percentage...'.
        """
        populations = []
        for _ in range(self.population_size):
            # get the mean of numerical values informed
            population_mean = self.numerical_field_sampling()
            populations.append(population_mean)

        # compute the percentage of answers for each population
        population_metrics = {
            'population': populations,
            'confidence': self.confidence_interval(populations) # confidence interval for a list of population means
        }

        return population_metrics
        

    def single_option_sampling(self):
        """
            Execute a sampling of answers a 'population_size' times 
            given a previous set of real answers.

            In this case, each answer represents one single option.
        """
        
        # ensure that all options will be filled - with 0 at least
        population_answers = {option: 0 for option in self.options}

        for _ in range(self.replacements):
            rand_idx = random.randrange(len(self.answers))
            random_option = self.answers[rand_idx]
            population_answers[random_option] += 1
            
        for option in population_answers:
            population_answers[option] = population_answers[option] / self.replacements

        return population_answers


    def multiple_option_sampling(self):
        """
            Execute a sampling of answers a 'population_size' times 
            given a previous set of real answers.

            In this case, each answer represents a subset of
            valid options, once we are dealing with multiple 
            option question
        """
        
        # ensure that all options will be filled - with 0 at least
        population_answers = {option: 0 for option in self.options}

        for _ in range(self.replacements):
            random_option_list = []
            while not random_option_list:
                rand_idx = random.randrange(len(self.answers))
                random_option_list = self.answers[rand_idx]

            # increase option total of answers for each one assigned
            for random_option in random_option_list:
                population_answers[random_option] += 1

        for option in population_answers:
            population_answers[option] = population_answers[option] / self.replacements

        return population_answers


    def numerical_field_sampling(self):
        """
            Execute a sampling of answers a 'population_size' times
            given a previous set of answered value.

            In this case, each answer was a numerical value set.
            We choose one that already exists.
        """
        
        population_answers = []

        for _ in range(self.replacements):
            # only choose one value inside of what people have chosen
            rand_idx = random.randrange(len(self.answers))
            random_option = self.answers[rand_idx]
            population_answers.append(random_option)

        return sum(population_answers) / self.replacements


    def confidence_interval(self, data_points):
        """
            Compute the confidence interval for the population answers.

            Based on https://www.indeed.com/career-advice/career-development/how-to-calculate-confidence-interval
        """

        # sampling mean
        m = np.mean(data_points)
        # standard deviation
        s = np.std(data_points) 
        dof = len(data_points) - 1 
        # t-Student distribution
        t_crit = np.abs(t.ppf( (1 - (self.confidence / 100) ) / 2, dof))

        # https://towardsdatascience.com/how-to-calculate-confidence-intervals-in-python-a8625a48e62b
        lower_value = m - s * t_crit / np.sqrt(len(data_points))
        upper_value = m + s * t_crit / np.sqrt(len(data_points))

        return (lower_value, m, upper_value)
