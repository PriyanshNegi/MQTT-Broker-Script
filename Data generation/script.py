import pandas as pd
import numpy as np
import random
from sets import Manufacturing, Railway
from downtime import create_csv

sets = [Railway()]
sets_name = ['Railway']

for seti in range(len(sets)):
    obj = sets[seti]

    cols = obj.cols
    data = obj.data
    n = obj.limit

    # create columns
    toinsert = []
    for i in range(n):
        row = {}
        for i in cols:
            row[i] = random.randint(data[i][1], data[i][2])
        toinsert.append(row)

    df = pd.DataFrame(toinsert, columns=cols)

    file_name = './data/fake_'+sets_name[seti]+'.csv'
    df.to_csv(file_name, index=True)

# create_csv(500)