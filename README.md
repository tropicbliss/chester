# chester

Machine learning model to detect cases of pneumonia or COVID-19 from chest X-rays

Two separate models are provided. `withoutcovid.pt` only predicts whether a person is healthy or has pneumonia (and does not take COVID-19 into account) such that accuracy can be improved from a lower amount of classes available for it to train on.

## Prediction
![](assets/withcovid/val_batch1_pred.jpg)
## Actual labels
![](assets/withcovid/val_batch1_labels.jpg)
## Training stats
### With Covid
![](assets/withcovid/results.png)
### Without Covid
![](assets/withoutcovid/results.png)

## Is the model open source?
No it is not. There are way better models out there anyway. Notably, this model is trained on low resolution images of 640px in length and breadth, while radiologists will typically examine radiographies of way higher resolution (+2000px). This is merely created for educational purposes.
