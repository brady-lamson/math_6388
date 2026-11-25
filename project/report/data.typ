= Data

== Regression

== Classification

This dataset contains 8124 mushrooms with one row per mushroom. The response is a boolean representing whether a mushroom is edible or not. There are 22 other variables in the dataset, all of which are categorical. These variables describe physical attributes such as gill attachments, the color of various parts of the mushroom, and other variables such as the environment the mushroom is found in. Due to the large number of categorical variables, any exploratory analysis in this report must be heavily truncated, any cited plots can be found in the appendix.

Starting with the response, it is extremely balanced with a near fifty fifty split. This makes it a little different from most fraud detection problems where the poisonous equivalent is often extremely rare. To make up for this, almost every other variable is extremely unbalanced. A good example of this is `spore_print_color`, which has a ton of color variations with near 0 frequencies as shown in @spore_color. As such, tailored pre-processing is necessary for any variables chosen for the model. 

It is worth noting that despite every variable appearing to be a categorical one, many are not on closer examination. The variable `ring_number`, is an integer ranging between zero and two, `veil_type` is entirely a single value, `bruises` is a boolean, and so on. After closer examination, five variables are booleans, one is an integer, one is a constant, and the other fifteen are categorical. One variable in the set has missing values, `stalk_root`. This variable is missing 2480 rows and, as such, is excluded from the model. 