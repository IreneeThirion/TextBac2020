#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 13:59:36 2020

@author: irenee
"""

import sqlite3

conn = sqlite3.connect('/media/irenee/USB-IR/basetext.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS auteur(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     mot TEXT,
     apparitions INTERGER
)
""")
conn.commit()
