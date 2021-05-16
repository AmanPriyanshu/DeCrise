# DeCrisis
## Introduction

<img src="https://github.com/AmanPriyanshu/DeCrise/blob/main/images/Disaster-collage.png" width="500" class="center">

DeCrisis is an online platform that acts as an aggregator for public support/utility services for fast-response during a major crisis or disaster. We utilize the power of social media, which acts as a warehouse for important information during the sudden onset of a natural or manmade disaster. We bring together the concepts of both continual and federated learning to create a volunteer-supported, learning system for the quick response and integral information retrieval. We employed Flask and Heroku to deploy a backend, which incorporates the federated averaging algorithm to learn from models trained across multiple volunteer systems. Which is then deployed on Streamlit with easy to understand UI to allow newcomers to navigate DeCrisis easily. Our model uses continual learning to keep a progressing learning feed so as to learn features from the recent most events. Finally, the tweets are scraped using the Twitter-API and a feed-forward neural network classifies them across 5 different classes.

## What it does

DeCrisis uses both continual and federated learning as a form of distributed learning for model training. One of the most important aspects of crisis management models is their implementation fails beyond similar events, leading to false predictions and mislabelling, therefore we utilize continual learning to keep our model updated across different crisis events. Our volunteer support method expects individuals to train models at their local systems after labelling a small sample space of tweets, our idea is to use the federated averaging algorithm across various users to build a successful aggregate model. We utilise regularisation to alleviate catastrophic forgetting in the target neural networks. At the local/volunteer level we expect the users to train the model using dimensionally compressed GloVe embeddings across 5 classes. 

The classes include:
1. Displaced people and evacuations
2. Infrastructure and utility damage
3. Injured or dead people
4. Missing or found people
5. Unrelated

This can allow public support systems such as police officers, firefighters and rescue operatives to gauge a better understanding of the situation as well as keep track of various public safety records.

## How we built it

We used Streamlit for creating our website. Our goal with the site was to create an easy to understand and navigate website. We used a minimalistic design coupled with a backend hosted on Heroku. Our backend allows volunteers/support systems to push locally trained models for aggregation on the central server at Streamlit. At the central server, the regularization function is used to check for variational changes, from previously trained models. If found, we send the aggregated model for further analysis on a test set, however, if within limits we apply it as the new model.

The aggregation is done using the federated averaging model. At the local training step of the federated methodology, a regularization function taken from `Learning without Forgetting - Li and Hoiem` is used for training the model and to prevent overfitting on recent/new training data. The model was deployed and trained over PyTorch so as to increase transperancy and ease of use between the central host server and the volunteers training the model. 

We used he HumAID Twitter dataset which consists of several thousands of manually annotated tweets that have been collected during 19 major natural disaster events including earthquakes, hurricanes, wildfires, and floods, which happened from 2016 to 2019 across different parts of the World (Alam et al., 2021). 

## Challenges we ran into

Word Embeddings are memory intensive and we used `Effective Dimensionality Reduction for Word Embeddings - Vikas Raunak et al.` to reduce memory demand. In our utilization of the above library, we also contributed to the open-source community by creating an executable Python3 version of it.

## Accomplishments that we're proud of

Creating a continual and federated learning algorithm for crisis management is a novel approach. Although proposed before it utilised sentence encoders which are high computation and memory intensive making it impossible to deploy. Therefore, we used GloVe embeddings and further contracted their effective dimensions following Raunak et al.'s `Effective Dimensionality Reduction for Word Embeddings`.

Deploying an online/life-long learning NLP model for crisis management. The utilization of a volunteer system, further crowdsources the learning capacity of the model, making it more diverse and learn across a lot more samples than individual contributors could ever do.

A project which potentially could save lives or make resource management easier and more efficient during a real crisis or natural/man-made disaster.

A minimalistic easy to navigate UI for crisis management, which does not bog down users with complex theory and alleviates unnecessary stress.

## What we learned

Some of the key take-aways from developing this project underline our newfound love for developing community projects for crisis management. Developing a project which could potentially save lives or make resource management easier. We also learnt a lot about NLP tools for crisis management and how they lose focus as they learn across different disaster events, therefore we employed continual learning. The volunteer system, allowed us to analyze federated learning in crodsourcing light insteead of its traditional privacy based utility. Finally, we learnt about compressing word embeddings from `Effective Dimensionality Reduction for Word Embeddings, Raunak et al.`.

## What's next for DeCrisis
n our developments for this project, we focused on maintaining a scalable nature for our product. We hope to further improve the scalability of the model by introducing concept of sketching - `FetchSGD: Communication-Efficient Federated Learning with Sketching (Rothchild et al.)`. Finally, we would also like to explore architectural continual learning.
