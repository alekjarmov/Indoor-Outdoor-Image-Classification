from django.db import models

# Create your models here.

class Prediction(models.Model):
    image = models.ImageField(upload_to="predicted")
    model = models.CharField(max_length=100, choices=[('1', 'Model 1 - ResNetV2 layer, Flatten, Dense 126,64,64,2'),
                                                     ('2', 'Model 2 -  ResNetV2 layer, Flatten, Dense 264, Dropout 0.3, Dense 128, Dropout 0.1, Dense 2'),
                                                     ('3','Model 3 - Xception layer, Flatten, Dense 256,128,64,2'),
                                                     ('4','Model 4 - Xception layer, Flatten, Dense 128, Dropout 0.3, Dense 64, Dropout 0.1, Dense 2'),
                                                     ('5', 'Model 5 - Random Saturation 0.75, Xception layer, Flatten, Dense 256, Dropout 0.4, Dense 128, Dropout 0.2, Dense 64, Dropout 0.1, Dense 2')])
    

    predicted_value = models.CharField(max_length = 10)
    likelihood_indoor = models.FloatField()
    likelihood_outdoor = models.FloatField()
    
