# Alzheimer-MRI-detection

## Webapp Demo

[alzeihmer video.webm](https://github.com/gbiamgaurav/Alzheimer-MRI-detection/assets/81230208/0b64f823-ee2c-417d-a08d-b9bdd2914e5c)

[Checkout the Webapp here](https://alzheimer-mri-detection-94iqb3w8waqhrndawafeua.streamlit.app/)

## Context of Dataset:
Alzheimer's disease (AD) is the most common form of dementia that progressively damages brain cells, resulting in memory and thinking deficits, loss of basic abilities, and ultimately, death. Currently, the annual cost of treating AD is 1 Trillion USD and it is expected that by 2050, 152 Million peope will be affected by AD. While there is no cure for AD, its onset diagnosis can prevent it from becoming too severe thus improving patient’s life. Recent advancements in computer vision have found to be impactful, however the datasets for AD are limited and heavily imbalanced. Due to this severe class imbalance the classifiers are prone to be biased towards the majority class i.e., classifying a person with early symptoms as "Not Impaired" (No Alzheimer's) which is highly undesirable.


## Description:
The data consists of MRI images. The data has four classes of images both in training as well as a testing set:

* Mild Demented
* Moderate Demented
* Non Demented
* Very Mild Demented

The data contains two folders. One of them is augmented ones and the other one is originals.

Data is augmented from an existing dataset. Original images can be seen in Data Explorer.

## Steps to setup the Project

1. Run init_setu.sh file
```
bash init_setup.sh
```

2. Run app.py
```
streamlit run app.py
```



