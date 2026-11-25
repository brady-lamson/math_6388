= Question 1

== Context

A student in the course is trying to train a two-layer Multi-Layer Perceptron (MLP) for a regression task using standard gradient descent. They wrote the following training loop:

#set align(center)
#block(stroke: 0.25pt, inset: 20pt)[
```py
for epoch in range(num_epochs):
    # Forward pass
    h = torch.relu(X @ W1 + b1)
    y_pred = h @ W2 + b2

    # Compute MSE loss
    loss = torch.mean((y_pred - y_true) ** 2)

    # Compute gradients
    loss.backwards()

    # Update parameters
    with torch.no_grad():
        W1 -= learning_rate * W1.grad
        b1 -= learning_rate * b1.grad
        W2 -= learning_rate * W2.grad
        b2 -= learning_rate * b2.grad
```
]
#set align(left)

The model's loss initially decreases, but after several epochs it begins to increase and eventually becomes `NaN`.

== Part A

*Problem:* Identify the critical missing line of code in this training loop.

What is missing is the step to reset the gradients of the different parameters. After the update parameters section, you'd put

```py
W1.grad.zero_()
b1.grad.zero_()
W2.grad.zero_()
b2.grad.zero_()
```

== Part B

*Problem:* Explain the exact mathematical consequence of omitting this line on the parameter updates at epoch $t$.

To describe it simply, failing to reset the gradients causes them to accumulate between forward and backward passes. This can cause them to explode in size and this problem compounds across iterations.

When examining the new value for a parameter we do so like:

$
  w_("new") &= w + Delta w\
  Delta w &= -eta (d L)/(d w)
$

where $eta$ is a non-zero value representing the learning rate. $Delta w$ represents the step length, scaled by the learning rate. The issue is, if gradients aren't reset between passes, this definition is no longer accurate. Say we examine epoch $t = 2$. If the gradient isn't reset it becomes:

$
  Delta w_(t=2) &= -eta (d L)/(d w) + Delta w_(t=1)
$

Which causes 

$
  w_("new") &= w + Delta w\ \
  &= w + (-eta (d L)/(d w) + Delta w_(t=1))
$

This impact may not be huge at first, but as we reach an arbitrary $t$, this becomes:

$
  w_t &= w_(t-1) + Delta w_t\ \
  &= w_(t-1) + Delta w_1 + Delta w_2 + dots + Delta w_t \
  &= w_(t-1) + sum_(i=1)^t Delta w_i
$

This can cause parameters to change drastically as the iterations accrue, which causes the loss to grow even more as predictions grow further from the truth, which only further increases the step size. This can, in some cases, result in the loss diverging, which is represented as `NaN`. It's important to note that the real issue here is that the gradients no longer mean what they're supposed to. This situation won't always cause the loss to diverge, but it will cause problems for the optimization process. 