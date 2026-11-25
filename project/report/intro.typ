= Intro

== Regression

== Classification

The classification portion of this project utilizes the `mushroom` dataset from the Audobon Society Field Guide created in 1981, sourced from the UC Irvine Machine Learning Repository @mushroom_73. The goal of this project is reliable prediction of poisonous mushrooms, which is made possible through the large number of categorical variables in this dataset. This topic, though a little niche on its own, is extremely similar to other high-risk classification topics like fraud and cancer detection. With these kind of problems, not every kind of error has equal risk. Falsely identifying a mushroom as poisonous and not eating it is less of a concern than falsely identifying one as non-poisonous. These situations can be very common depending on the industry, where the statistician must decide on which kind of error is most important for the given problem.  This portion of the project will compare two models, a logistic regression and a neural network trained for binary classification. The neural network will have two versions, with the second version having temperature scaled logits. 