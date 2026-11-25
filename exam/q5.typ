= Question 5

// Definitions
#let x = $mat(2, 1)$
#let w1 = $mat(0.5, -1.0; 1.0, 0.0)$
#let b1 = $mat(0.0, 1.0)$
#let w2 = $mat(0.5; -1.0)$
#let b2 = $-1.0$

== Context

Consider a small Multi-Layer Perceptron (MLP) designed for binary classification. The network consists of an input layer with $2$ features, a single hidden layer with $2$ neurons using a ReLU activation function, and an output layer with 1 neuron using a Sigmoid activation function

$
  sigma(z) = 1/(1 + e^(-z))
$

Let the input vector be defined as a row vector:

$
  bold(x) = #x
$

The weights and biases for the hidden layer are:

$
  bold(W)^((1)) = #w1,quad b^((1)) = #b1 
$

The weights and biases for the output layer are:

$
  bold(W)^((2)) = #w2,quad b^((2)) = #b2
$

== Part A

*Problem:* Calculate the pre-activation vector $bold(z)^((1))$ and the post-activation vector $bold(h)^((1))$ for the hidden layer. Show your step-by-step matrix multiplication. 

So we can calculate $bold(z)^((1))$ as:

#let z1 = $mat(2, -1)$

$
  bold(z)^((1)) &= bold(x) bold(W)^((1)) + bold(b)^((1)) \
  &= #x times #w1 + #b1 \
  &= mat((2 dot 0.5 + 1 dot 1), (2 dot -1 + 1 dot 0)) + #b1 \
  &= mat(2, -2) + #b1 \
  &= #z1
$

With this, we pass each element through the ReLU activation function, which is $max(0, x)$. So the $-2$ element goes to 0. 

#let h1 = $mat(2, 0)$
$
  bold(h)^((1)) = #h1
$

#pagebreak()

== Part B

*Problem:* Calculate the final pre-activation logit $z^((2))$ and the network's final predicted probability $hat(y)$. 

Same setup as before.

$
  bold(z)^((2)) &= bold(h)^((1)) bold(W)^((2)) + bold(b)^((2)) \
  &= #h1 #w2 + #b2 \
  &= 2 dot 0.5 + 0 dot -1.0 - 1.0 \
  &= 1 + 0 - 1 \
  &= 0
$

We pass this through the sigmoid function to get $hat(y)$.

$
  hat(y) &= sigma(bold(z)^((2))) \
  &= 1/(1 + e^(-0)) \
  &= 1/(1 + 1) \
  &= 0.5
$