# Toxic Comments Classifier
Discussing things we care about can be difficult. The threat of abuse and harassment online means that many people stop expressing themselves and give up on seeking different opinions. Platforms struggle to effectively facilitate conversations, leading many communities to limit or completely shut down user comments.

![image](https://github.com/tripathiGithub/toxic_comments_classifier/raw/master/Results/toxic.gif)

#### Web App Link : https://share.streamlit.io/tripathigithub/toxic_comments_classifier/app_streamlit.py

This project aims to build a Multi-label Classification model capable of detecting different classes of toxicity for each comment. A comment could belong to more than one or none of the categories - Toxic, Severe_toxic, Obscene, Threat, Insult and Identity_hate

![image](https://github.com/tripathiGithub/toxic_comments_classifier/raw/master/Results/toxicplot.png)

For this Project I have used a Deep Learning model. This project is demonstration of a technique called ULMFit(Universal Language model fine-tuning). This is a transfer learning technique that can be used for text related tasks such as this. This approach has been combined with other modern deep learning practices (discriminative-learning-rates, gradual-unfreezing, etc) to get good results. The target labels were not distributed uniformly and were highly imbalanced, so that was also a challenge to get good results on all class labels

#### The code needed to train the model is detailed in here https://github.com/amancrackpot/ImageClassification_Covid_X_Ray_Scans/blob/main/covid-classification-resnet50.ipynb

#### Dataset available at https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data


### Results on test data:

<p>
  <img alt="Report" src="https://github.com/tripathiGithub/toxic_comments_classifier/blob/master/Results/toxic1.png" width="39%"> <img alt="Report" src="https://github.com/tripathiGithub/toxic_comments_classifier/raw/master/Results/bad_comments.gif" width="59%">
</p>


