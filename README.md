# Everywhere better
This work is an analysis for 'Everywhere better', an app that offers emotional and psychological support.
They wanted to understand differences in online behavior between married and single people and be able to predict from which group a person is.

Text data were collected from reddit social platform. Since people go there with questions and concerns, Reddit was chosen as the source of data.
The subreddits chosen to represent both groups were "marriage" and "dating".

# Objective

The objective of this work is to help improve 'Everywhere Better' tools to better support their clients.
Knowing from which group a person is can narrow down strategies used to support clients who come for help.

# How? 
- Using PRAW API to scrape subreddits
- Searching keywords in top 10 most common words
- Applying sentiment analysis in posts
- Using predictive classification models

Characteristics of posts' texts such as number of special characters, uppercase letters, lowercase letter and sentiment analysis scores were calculated.
These variables along posts' texts were used in both models.


# Type of Model

Two models were explored to approach this problem: Random Forests and Logistic Regression.
They are both supervised models of predictive classification. Logistic regression resulted in a higher accuracy on unseen data, of about 92%.
Since married and single people should be treated equal when coming for support, the metric for optimization was accuracy.


# Data Dictionary
|Feature|Type|Dataset|Description|
|---|---|---|---|
|self_text|object|marriage_dating.csv|description of posts texts| 
|title|object|marriage_dating.csv|title of posts texts| 
|subreddit|object|marriage_dating.csv|'marriage' or 'dating' subreddit| 
|special_characters|int|date_marry|number of special characters of posts texts| 
|compounds|object|date_marry|overall score from negative -1 to positive 1| 
|neg|object|date_marry|overall negative words score of post texts| 
|neu|object|date_marry|overall neutral words score of post texts| 
|positive|object|date_marry|overall positive words score of posts texts|
|special_characters|int|date_marry|number of special characters of posts texts| 
|percent_special_characters|float|date_marry|proportion of characters in posts texts|
|compounds|object|date_marry|overall score from negative -1 to positive 1| 
|lower|int|date_marry|number of lowercase letters  in posts texts| 
|upper|int|date_marry|number of uppercase letters in posts texts| 
|up_low|float|date_marry|number of uppercase letters divided by number of lowercase letters in posts texts|



# Conclusions and recommendations
- Marriage keywords: "husband" and "wife" in top 10 most common words in marriage subreddit
- Dating keywords: "dating" in top 10 most common words in dating subreddit
- When removing the keywords found in top 10 most common words of both groups, the accuracy decreased by 3%. Their differences goes beyond that and should be further analyzed, as looking on some more nuanced characteristics in common.
- When a client asks for support with their story, the model can predict from which group a person is from about 92% of times.
