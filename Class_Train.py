
import pandas as pd
import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class To_Train():
    def __init__(self):
        pass
        
    def __call__(self, dataset):
        df = dataset.copy()
        df['subreddit'] = (df['subreddit']=='dating')*1
        df['all_text'] = df['title'] + ' ' + df['self_text']
        df.drop(['self_text', 'title'], axis=1, inplace=True)
        df['text_length'] = df['all_text'].apply(lambda x: len(x))
        df['special_characters'] = df['all_text'].apply(lambda x: sum(not c.isalpha() for c in x ))
        sa = SentimentIntensityAnalyzer()
        df['compounds'] = df['all_text'].apply(lambda r: sa.polarity_scores(r)['compound'])
        df['neg'] = df['all_text'].apply(lambda r: sa.polarity_scores(r)['neg'])
        df['pos'] = df['all_text'].apply(lambda r: sa.polarity_scores(r)['pos'])
        return df

