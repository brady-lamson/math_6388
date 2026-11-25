= Methods

== Regression

== Classification

The classification portion of this project tightly follows the rubric. Three models were fit. A baseline logistic regression model, a neural network classifier, and lastly a temperature calibrated neural network classifier. For the logistic regression model, there are three key components. First, there is a single linear layer that returns a single logit per observation. It is of the form

$
z = X beta + beta_0
$

From the logits, a sigmoid function is used to convert to the probability space. In other words, we move from $RR arrow [0,1]$. The sigmoid activation function is represented as

$
  f(x) = 1/(1 + e^(-x))
$

The loss function used was binary cross entropy. The pytorch function `BCEWithLogitsLoss()` actually has the sigmoid function built into it. According to the documentation, this is more stable than separating the steps as it can take advantage of the log-sum-exp trick. So during model training the sigmoid function is not called directly. However, conversion from logits to probabilities outside of training does use the sigmoid function. 

For converting from probabilities to actual predictions, a threshold of $0.7$ was utilized. This was selected as it showed an improvement in prediction metrics over a $0.5$ threshold. 

In this project, a true label is poisonous and false is edible.  A learning rate of 0.1 was used across 1500 epochs. 

For the two neural network classifier, almost everything about them is identical. To start with the architecture, there are two hidden layers with 32 neurons and ReLU activation functions.

$
  f(x) = max(0, x)
$

The output layer returns a single logit per observation. This architecture can be represented as

$
  underbrace(I, "Input Features") arrow underbrace(32, "Hidden Layer 1") arrow underbrace(32, "Hidden Layer 2") arrow underbrace(1, "Output Logit")
$

The same loss function, `BCEWithLogitsLoss()`, is used here. The rest of the process is identical to the logistic regression. As for temperature scaling, a separate calibration split was saved that is $15%$ of the total row count. The trained neural network is used to find the positive temperature scalar that optimizes the negative log likelihood against the calibration set. This process does not retrain the model, it simply scales the logit outputs. This is done before conversion to probabilities. 