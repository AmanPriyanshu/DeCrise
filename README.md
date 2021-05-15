# DeCrisis
## Introduction

DeCrisis is an online platform that acts as an aggregator for public support/utility services for fast-response during a major crisis or disaster. We utilize the power of social media, which acts as a warehouse for important information during the sudden onset of a natural or manmade disaster. We bring together the concepts of both continual and federated learning to create a volunteer-supported, learning system for the quick response and integral information retrieval. We employed Flask and Heroku to deploy a backend, which incorporates the federated averaging algorithm to learn from models trained across multiple volunteer systems. Which is then deployed on Streamlit with easy to understand UI to allow newcomers to navigate DeCrisis easily. Our model uses continual learning to keep a progressing learning feed so as to learn features from the recent most events. Finally, the tweets are scraped using the Twitter-API and a feed-forward neural network classifies them across 5 different classes.

## What it does

DeCrisis uses both continual and federated learning as a form of distributed learning for model training. One of the most important aspects of crisis management models is their implementation fails beyond similar events, leading to false predictions and mislabelling, therefore we utilize continual learning to keep our model updated across different crisis events. Our volunteer support method expects individuals to train models at their local systems after labelling a small sample space of tweets, our idea is to use the federated averaging algorithm across various users to build a successful aggregate model. We utilise regularisation to alleviate catastrophic forgetting in the target neural networks. At the local/volunteer level we expect the users to train the model using _______ embeddings across 5 classes. 

The classes include:
1. Displaced people and evacuations
2. Infrastructure and utility damage
3. Injured or dead people
4. Missing or found people
5. Unrelated

This can allow public support systems such as police officers, firefighters and rescue operatives to gauge a better understanding of the situation as well as keep track of various public safety records.

## How we built it

We used Streamlit for creating our website. Our goal with the site was to create an easy to understand and navigate website. We used a minimalistic design coupled with a backend hosted on Heroku. Our backend allows volunteers/support systems to push locally trained models for aggregation on the central server at Streamlit. At the central server, the regularization function is used to check for variational changes, from previously trained models. If found, we send the aggregated model for further analysis on a test set, however, if within limits we apply it as the new model.

The aggregation is done using the federated averaging model. At the local training step of the federated methodology, a regularization function taken from `Learning without Forgetting - Li and Hoiem` is used for training the model. 



## Challenges we ran into

## Accomplishments that we're proud of

## What we learned

## What's next for DeCrisis
