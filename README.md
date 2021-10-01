# Slurred-Speech-Recognition-DeepLearning
Deep learning has evolved a lot to develop end to end state of the art speech Recognition System.
End to end deep learning model for automatic speech Recognition is much simpler than traditional speech systems which tend to perform poorly in noisy enviroments. Deep learning End to End models doesn't need hand designed components to model background noise and speaker variation.

The well known Automatic Speech Recognition Systems are Alexa, Siri , Google Home etc. This class of applications starts with clip of spoken audio clip in a particular language and extracts the words that were spoken as text. There are also called Speech to Text Algorithms. 

### For Automatic Speech Recognition, our training data consists of the following:
-  `X: Input features i.e audio clips of spoken words`
-  `Y: Target label or text transcript of what was spoken`
 

## Problem Statement
The state of the art Automatic Speech Recognition can greatly improve the lives of those with speech impairements. However , the end to end deep learning Automatic Speech Recognition System trained from 'normal' speech tend to perform poorly for those who have speech impairements either due to accident or disease. 
The purpose is to improve ASR for people who have speech impairements. In other words, we have to develop an ASR model that works on personalised non-standard speech.

## High level Solution Overview
We will start with the state of the art end to end speech Recognition model with high accuracy. This high quality ASR model will be trained on hundreds of hours of typical or standard speech with no impairements. After we achieve high accuracy for the end to end model, then we will start fine-tuning parts of the model to an individual with speech impairement.<br>
So our main aproach is training a base model on a large dataset of normal speech and then training a personalised model using a much smaller slurred speech dataset. We can use tranfer learning for fine tuning parts of our base model.
# Model Architecture
![Screenshot from 2021-10-01 20-22-07](https://user-images.githubusercontent.com/42781233/135641230-4775970a-479f-4d40-9707-6c50c9b0bb5b.png)

# Base Model Performance
The base ASR model was trained on 100 hours of Librispeech Dataset.
- Final Epoch Average Loss: 0.61
- Final Epoch Average CER: 0.11
- Final Epoch Average WER: 0.14
