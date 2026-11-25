= Question 3

== Context

In PyTorch, the standard `nn.CrossEntropyLoss` function expects raw, unnormalized logits ($x = [z_1, ..., z_k]^T$) as its input rather than post-softmax probabilities $(bold(hat(y)))$. For a single observation belonging to a specific true class $c$, the one-hot encoded true label vector has a 1 at index $c$ and $0$ elsewhere. Therefore, the standard categorical cross-entropy loss simplifies to just the negative log probability of the true class:

$
  L = -log(hat(y_c))
$

The softmax probability for this true class is defined as:

$
  hat(y_c) = exp(z_c)/(sum_(j=1)^K exp(z_j))
$

*Problem:* Substitute the softmax definition into the simplified cross-entropy loss function. Use the fundamental properties of logarithms to expand and simplify the expression into a final form that is written entirely in terms of the raw logits ($z_c$ and $z_j$).

== Solution

$
  L &= -log(exp(z_c)/(sum_(j=1)^K exp(z_j))) \
  &= -1 dot (log(exp(z_c)) - log(sum_(j=1)^K exp(z_j))) \
  &= log(sum_(j=1)^K exp(z_j)) - z_c
$

I don't believe this can be simplified any further. 