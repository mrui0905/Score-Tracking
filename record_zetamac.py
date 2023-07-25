import pandas as pd
from datetime import date
from datetime import datetime

def init_vars():
    day = date.today().strftime("%m/%d/%y")
    if day[0] == '0':
        day = day[1:]
    time = 'PM' if int(datetime.now().strftime("%H:%M:%S").split(':')[0]) >= 12 else 'AM'
    mode = prompt_mode()

    return day, time, mode

def prompt_mode():
    print("Select 0 for addition, 1 for subtraction, 2 for multiplcation, 3 for division, 4 for combined, 5 for large multiplication, 6 for large divison, 7 for large combined")
    mode = int(input("Mode: "))

    while mode not in [0, 1, 2, 3, 4, 5, 6, 7]:
        mode = int(input('Invalid input. Input mode again: '))

    return mode

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
    d, t, m = init_vars()

    raw_paths = ['data/zetamac/addition_raw.csv', 'data/zetamac/subtraction_raw.csv', 'data/zetamac/multiplication_raw.csv', 'data/zetamac/division_raw.csv', 'data/zetamac/combined_raw.csv', 'data/zetamac/large_multi_raw.csv', 'data/zetamac/large_division_raw.csv', 'data/zetamac/large_combined_raw.csv']
    avg_paths = ['data/zetamac/addition_avg.csv', 'data/zetamac/subtraction_avg.csv', 'data/zetamac/multiplication_avg.csv', 'data/zetamac/division_avg.csv', 'data/zetamac/combined_avg.csv', 'data/zetamac/large_multi_avg.csv', 'data/zetamac/large_division_avg.csv', 'data/zetamac/large_combined_avg.csv']

    # Update raw data csv file
    raw_df = pd.read_csv(raw_paths[m])

    inputs = input_scores()
    for input in inputs:
        raw_df.loc[len(raw_df.index)] = [d, t, input]

    raw_df.to_csv(raw_paths[m], index = False)

    # Update average data csv file
    avg_df = pd.read_csv(avg_paths[m])

    avg = sum(inputs)/(len(inputs)*120)

    avg_df.loc[len(avg_df.index)] = [d, avg]

    avg_df.to_csv(avg_paths[m], index = False)

    
    