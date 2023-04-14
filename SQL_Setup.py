#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 19:01:26 2023

@author: pstepien
"""

import pandas as pd
from os import path
import sqlite3

DATA_DIR = '/Users/pstepien/Desktop/The GIST Data'

conn = sqlite3.connect(path.join(DATA_DIR, 'the_gist.sqlite'))

tables = pd.read_sql(
    """
    SELECT name
    FROM sqlite_master where type = "table";
    """, conn)

sub_data = pd.read_sql(
    """
    SELECT *
    FROM sub_data
    """, conn)
    
biz_data1 = pd.read_sql(
    """
    SELECT *
    FROM biz_data1
    """, conn)
    
biz_data2 = pd.read_sql(
    """
    SELECT *
    FROM biz_data2
    """, conn)
    
biz_data3 = pd.read_sql(
    """
    SELECT *
    FROM biz_data3
    """, conn)
    
col_data = pd.read_sql(
    """
    SELECT *
    FROM col_data
    """, conn)

news_data1 = pd.read_sql(
    """
    SELECT *
    FROM news_data1
    """, conn)

news_data2 = pd.read_sql(
    """
    SELECT *
    FROM biz_data2
    """, conn)