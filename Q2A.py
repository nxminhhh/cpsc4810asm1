#!/usr/bin/env python3
import pandas as pd
import numpy as np
flights = pd.read_csv('flightdelays.csv')
print(flights[flights['Origin']=='SFO'][['ArrDelay','Origin']].head(3))

