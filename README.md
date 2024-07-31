# Everywhere better
## Overview
The Everywhere Better project aims to enhance the capabilities of the "Everywhere Better" app, which provides emotional and psychological support. The goal is to analyze online behavior differences between married and single individuals and predict to which group a person belongs based on text data.

Data was collected from Reddit, focusing on the "marriage" and "dating" subreddits, as these are spaces where people commonly share their concerns and questions.

## Objective
The main objective is to refine the support strategies of the "Everywhere Better" app by identifying whether a user is likely married or single. This identification will help tailor the advice and support provided to users.

## Methodology
### Data Collection
- Source: Reddit
- Subreddits: "marriage" and "dating"
- Data Collection Tool: PRAW API
- Data Collected: Titles and texts of posts, subreddit information
### Data Processing
Data Consolidation: Posts from each subreddit were combined into a single dataframe and exported as a CSV file.
### Exploratory Data Analysis (EDA):
- Analyzed the most common words, excluding and including stop words
- Examined the use of special characters, text length, and sentiment analysis
- Identified specific keywords unique to each subreddit group
### Modelling
- Text Vectorization:
Compared CountVectorizer and TfidfVectorizer. Chose TfidfVectorizer for better accuracy.
- Predictive Models:
Tested various models including KNeighbors Classifier and RidgeClassifier
Selected RidgeClassifier for its high accuracy (over 99%)
- Feature Importance: Analyzed coefficients to determine key words for each group
### Results
- Keywords: Identified distinct keywords that correlate with each group.
- Model Performance: RidgeClassifier demonstrated excellent accuracy, distinguishing between the two groups effectively.
Sentiment and Text Characteristics: Found nuanced differences in sentiment and text features between the two groups.

# Conclusions and recommendations
The project successfully developed a model that can predict whether a text belongs to a married or dating person with high accuracy. This capability is expected to significantly enhance the personalization of support provided by the "Everywhere Better" app.

Further research could involve expanding the dataset. The model could also be used for speech in speech to text models.
