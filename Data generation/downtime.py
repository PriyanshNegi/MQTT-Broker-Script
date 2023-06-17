import pandas as pd
import numpy as np
import random

def create_csv(n):
    data = []

    if n<365:
        months = n//12
        for month in range(1, months):
            for date in range(1, 29):
                uptime = random.randint(5, 20)
                data.append({
                    'day': f"{date}-{month}-{2021}",
                    'uptime': uptime,
                    'downtime': random.randint(0, 24-uptime),
                })
    else :
        years = n//365
        for year in range(years):
            for month in range(1, 13):
                for date in range(1, 29):
                    uptime = random.randint(0, 20)
                    data.append({
                        'day': f"{date}-{month}-{2021+year}",
                        'uptime': uptime,
                        'downtime': random.randint(0, 24-uptime),
                    })

    df = pd.DataFrame(data, columns=['day', 'uptime', 'downtime'])
    
    df.to_csv('Downtime.csv', index=True)

