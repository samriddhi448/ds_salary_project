# -*- coding: utf-8 -*-
"""
Created on Tue May 18 22:18:32 2021

@author: samriddhi
"""
import glassdoor_scrapper as gs 
import pandas as pd 

path = "C:/Users/samriddhi/Desktop/ds_salary_project/chromedriver"

df = gs.get_jobs('data scientist',15, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)

