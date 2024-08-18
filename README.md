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
- Model Performance: RidgeClassifier demonstrated excellent accuracy, distinguishing between the two groups effectively. RidgeClassifier got more marriage subreddit texts wrong than the other way around, probably because of an unbalanced data. Data had around 60% of dating subreddit posts and 40% of marriage subreddit posts. Besides that, the result does not seem to have a pattern of confusion between classes. Afterall, the accuracy score was more than 99%. Given that classification accuracy for both groups is equally important, accuracy was the primary metric used to select the model.
### Results
- Keywords and words with most predictive power: Most words of the ones with most predictive power between groups are very specific to their respective groups, it did not show valuable context on the issues people want to resolve.
- Sentiment and Text Characteristics: Found nuanced differences in sentiment between the two groups, but not for text characteristics.
- Final Model: RidgeClassifier.
# Conclusions and recommendations
The model was highly effective, achieving excellent accuracy in predicting whether a text belongs to a married or dating individual.
<br><Br>
This classification model is valuable for directing users to the most appropriate support within the "Everywhere Better" app, by allocating them to advisors who specialize in their specific relationship context.  Classifying users based on their relationship status may greatly assist in providing targeted, relevant support, ensuring that users receive the guidance that is most appropriate for their specific needs.
<br><Br>
Additionally, the model has potential for integration into speech-to-text systems to further enhance user experience.
