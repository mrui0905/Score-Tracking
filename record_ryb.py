import pandas as pd
from datetime import date
from datetime import datetime

def init_vars():
    day = date.today().strftime("%m/%d/%y")
    if day[0] == '0':
        day = day[1:]
    time = 'PM' if int(datetime.now().strftime("%H:%M:%S").split(':')[0]) >= 12 else 'AM'

    return day, time

def input_scores():
    scores = []

    while True:
        score = input('Score: ')

        if score.lower() == 'end':
            break
        elif score.lower() == 'clear':
            scores.clear()
        elif score.lower() == 'del':
            scores.pop()
        else:
            while True:
                try:
                    score = int(score)
                    scores.append(score)
                    break
                except ValueError:
                    score = input('Invalid input. Input score again: ')

    return scores
                


if __name__ == '__main__':
    # Create date, time, and mode varibles
    d, t = init_vars()

    raw_path = 'data/ryb/ryb_raw.csv'
    avg_path = 'data/ryb/ryb_avg.csv'

    # Update raw data csv file
    raw_df = pd.read_csv(raw_path)

    inputs = input_scores()
    for input in inputs:
        raw_df.loc[len(raw_df.index)] = [d, t, input]

    raw_df.to_csv(raw_path, index = False)

    # Update average data csv file
    avg_df = pd.read_csv(avg_path)

    avg = sum(inputs)/(len(inputs)*120)

    avg_df.loc[len(avg_df.index)] = [d, avg]

    avg_df.to_csv(avg_path, index = False)

    
    