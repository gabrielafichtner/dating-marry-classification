# Everywhere better
Everywhere better hired me to do an analysis of single and married people's concerns

# Subreddits' Marriage and Dating 

The objective of this work is to identify differences in marriage and dating subreddits, specially their sentiment scores, building models to predict from which subreddit the post came from.

# How?

- Using PRAW API to scrape subreddits
- Searching keywords in top 10 most common words
- Applying sentiment analysis in posts
- Executing models considering sentiment analysis
- Comparing models with and without keywords

# Data Dictionary
|Feature|Type|Dataset|Description|
|---|---|---|---|
|self_text|object|marriage_dating|description of post| 
|title|object|marriage_dating|title of post| 
|subreddit|object|marriage_dating|'marriage' or 'dating' subreddit| 
|special_characters|int|marriage_dating|number of special characters of posts| 
|compounds|object|marriage_dating|overall score from negative -1 to positive 1| 
|neg|object|marriage_dating|overall negative words score of post| 
|neu|object|marriage_dating|overall neutral words score of post| 
|positive|object|marriage_dating|overall positive words score of post| 

# Conclusions and recommendations
- When 'dating', 'wife', 'husband' were removed from model, its accuracy decreased more than 5%. The accurary went from approximately 91 to 86%, still showing differences in the words
- Only sentiment analysis wasn't a good predictor of the differences, showing it is not the main difference between subreddits
- Married people generally put more special characters
- Further research in the structure needed
