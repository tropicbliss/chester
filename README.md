# chester

Machine learning model to detect cases of pneumonia or COVID-19 from chest X-rays

Two separate models are provided. `withoutcovid.pt` only predicts whether a person is healthy or has pneumonia (and does not take COVID-19 into account) such that accuracy can be improved from a lower amount of classes available for it to train on.

I've added an `mnist.pt` file for digit classification just for fun idk.

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
No it is not, there are way better models out there anyway. Crucially, this model is trained on low resolution images of 1024px in length and breadth while radiologists will typically examine radiographies of much higher resolutions (+2000px). As this is merely created for educational purposes, I do not feel like spending too much time and money on this endeavour.
