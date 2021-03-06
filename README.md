# pdpd-image-classification
Repo for my research project about *A Machine Learning Study to Classify Social Media Images and Extract Information that Identifies Engagement* (translated from portuguese: *Um Estudo de Aprendizado de Máquina para Classificar Imagens de Redes Sociais e Extrair Informações que Identifiquem Engajamento*).

# The Project

PDPD: ***P**esquisando **D**esde o **P**rimeiro **D**ia* - Research Project on the first year of college at *Universidade Federal do ABC* (UFABC), in Brazil. Official paper number 02/2017, with research grant.

Supervisor: Dr. Alexandre Noma.

It is important to note that this project was developed in 2017-2018 and possibly may not be repeated today in the same method.

The full report in portuguese can be found in the repo, along with codes. This is just a simplified explanation.

## Objective

Develop a prediction method for the amount of *likes* an image would receive when posted on *Facebook*, based on information in the image.

## Development

Constructing the training-set of images using *Facebook Graph API* to extract images from the public Facebook page *ajudeaacd* (Assistance Association for Disabled Children).

![Various images displayed in folder](/images/pics.png "Images extracted from Facebook")

Visual tags extracted from images using *Computer Vision API* from *Microsoft Azure*.

![Image with extracted tags](/images/tags.png "Tags extracted from image")

The initial idea was to use regression methods to predict the amount of *likes* the image would receive, however this proved inefective with too much variance and error. Then we tried classification methods to predict if the image would receive many or few likes (binary classification).

## Results

*Naive Bayes*, *Decision Tree*, *Support Vector Machine* and *Nearest Neighbors* were the methods tested, with Support Vector Machine reaching a higher classification accuracy of 70%.

In conclusion, the method for classifiying the amount of likes and image would receive worked, although far from ideal. The Support Vector Classifier presented a better-than-random classification of likes the image would receive, but was lacking due to absence of context between tags, historical context between images, and dependency on the accuracy of the tags extraction process itself.





