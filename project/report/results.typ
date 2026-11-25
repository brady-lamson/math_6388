= Results

== Regression Results

== Classification Results

#figure(
  include "tables/mushroom_results.typ",
  caption: "Classification results summary. Classification threshold = 0.7"
) <mushroom_results>

#figure(
  include "tables/mushroom_confusion.typ",
  caption: "Confusion matrix results."
) <confusion_matrix>

The results from the classification model are shown in @mushroom_results and @confusion_matrix. At a glance, performance of the logistic regression and post-calibration neural network are similar. The classification metrics are nearly identical for the two. All three models however face the same problem, a terrible false-negative rate. Recall is the metric to focus on here. It tells us how many of the truly poisonous mushrooms we categorized as such and all three models only captured around $50%$ of them. Both the logistic regression and calibrated neural network have near perfect precision scores however. What this indicates is that the models are very careful about classifying a mushroom as poisonous. This behavior is consistent even at lower classification thresholds such as $0.5$, surprisingly enough. 

The calibration process in this case was a big performance improvement, bringing the model more in line with the performance of the logistic regression. The learned temperature was $5.8$, which seems very high. This results in a drop in the negative log likelihood, moving from $1.28$ to $0.47$. The ECE barely changes, however, only going from $0.28$ to $0.26$. The logistic regression has the best scores for these two metrics. 

@mushroom_reliability, the reliability plots for the two neural networks, show evidence of both over-confidence and under-confidence. Before calibration the model was almost entirely low confidence. The post calibration plot shows some extreme cases over over-confidence. For the underlying strategy for ECE and reliability plots, empty bins were skipped entirely. The probabilities were split into 15 uniformly wide, evenly spaced bins. The mean probability for those bins was calculated. 

It's important to note that these results are extremely sensitive to the splits. A simple change in the seed or increase in the training size can sometimes result in perfect scores as an example. No investigation was performed into why this is the case, though these alternate results can be found in @mushroom_results_train70, @confusion_matrix_train70, and @mushroom_reliability_train70. They're included in the appendix as I do think they're interesting. 