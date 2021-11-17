# Slurred-Speech-Recognition-DeepLearning

For Speech-to-Text problems, our training data consists of:<br>
![img](https://user-images.githubusercontent.com/42781233/135642643-0c3c507a-5a10-4ab6-8445-441091bb7e13.png)

 

# Problem Statement
The purpose of this project is to fine tune the the automatic speech recognition model or apply the technique of transfer learning so that it can convert atypical speech (voice of people with speech impairments) into text.
## High level Solution Overview
We will start with the state of the art end to end speech Recognition model with high accuracy. This high quality ASR model will be trained on hundreds of hours of typical or standard speech with no impairements. After we achieve high accuracy for the end to end model, then we will start fine-tuning parts of the model to an individual with speech impairement.<br>
So our main aproach is training a base model on a large dataset of normal speech and then training a personalised model using a much smaller slurred speech dataset. We can use tranfer learning for fine tuning parts of our base model.
# Model Architecture
![Screenshot from 2021-10-01 20-22-07](https://user-images.githubusercontent.com/42781233/135641230-4775970a-479f-4d40-9707-6c50c9b0bb5b.png)

# Base Model Performance
The base ASR model was trained on 100 hours of Librispeech Dataset.
- Final Epoch Average Loss: 0.46
- Final Epoch Average CER: 0.10
- Final Epoch Average WER: 0.11

# Dataset preparation
After we train our ASR model on hundreds of hours of typical speech, we are good to go for fine-tuning our model on impaired speech. We need to collect impaired speech dataset. We build web app using django framework to do the same.

## Link to web APP:
1. http://speech-collection.herokuapp.com/index/
2. https://mmig.github.io/speech-to-flac/
