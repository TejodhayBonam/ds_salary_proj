# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 16:39:12 2021

@author: TEJODHAY
"""

import glassdoor_scrapper as gs
import pandas as pd

path = "C:/Users/TEJODHAY/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 172, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)
