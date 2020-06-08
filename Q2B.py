#!/usr/bin/env python3
import pandas as pd
import numpy as np
flights = pd.read_csv('flightdelays.csv')
print(flights['Origin'].value_counts()[0:3])

MATTHEW NGUYEN
