## Pitch_Effective

This project analyizes pitches from Major League Baseball Left Handed Pitchers between the 2015 and 2018 seasons in hopes of evaluating the various pitch metrics and predicting an outcome. 

# Data
The data from this project was acquired using the PyBaseball API which pulled statcast data from the 2015-2018 MLB seasons.
Data: https://github.com/jldbc/pybaseball

# Process
After acquiring and cleaning the data, pitching metrics (pitch velocity, movementment measurements, spin rate etc) were feed into the model as depenedent variables and outcomes (strike, ball, foul, Hit-by_pitch, single, double, triple, homerun) were returned as outputs.

The three primary models used were Logistic Regression, Gradient Boosting Classifier, and Support Vector Machine. In testing each model with 10,000 rows, all models performed decenetly well with the GBC giving the best  R squared score and f1 score.

In adjusting the data, after some initial runs and feature importance graphs I decided to eliminate some of the metrics I was feeding the model. The computer was good at putting the pieces together ie hit location. 

However, when the full 750,000 rows were feed to the models, all of the models performed worse. The R squared scores for both the logistic regression and GBC dropped. Their corresponding classification reports also showed worse ratings. The SVM, was unable to complete testing. After some research, SVMs do not function well with more than 200,000 rows of data unfortunatley. 

In closing, both the models generated results, just not to the to the expected level and faultered when handling the full dataset. 

# Model Analysis

Baseball can be  hard game to interpret. For example, a pitch with identical metric could go for a double for one player, but an out for another based on defensive player positioning. The model would have no way of knowing this which could be one reason by the models did not perform as well with the full dataset. 

# Future Work

In continuing to work on this project the next step is to step up a neural network in hopes of generating an accurate model. 




