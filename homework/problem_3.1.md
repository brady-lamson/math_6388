## Problem 3.1

Consider the sigmoid function

$$
p=\sigma(a)=\frac{1}{1+e^{-a}},
\qquad a\in\mathbb{R}.
$$

### Part A

**Problem:**

Show that the log-odds satisfy

$$
\log\left(\frac{p}{1-p}\right)=a.
$$

**Solution:**

Before we start, we will simplify the denominator as that will save us a lot of time later.

$$
\begin{align}
    1 - p &= 1 - \frac{1}{1 + e^{-a}} \\
    &= \frac{1 + e^{-a}}{1 + e^{-a}} - \frac{1}{1 + e^{-a}} & \text{(Rewrite 1)} \\
    &= \frac{1 + e^{-a} - 1}{1 + e^{-a}} & \text{(Combine fractions)} \\
    &= \frac{e^{-a}}{1 + e^{-a}} \\
    &= \frac{1}{e^a (1+e^{-a})} \\
    1 - p &= \frac{1}{1+e^a} = (1+e^a)^{-1}
\end{align}
$$

Okay, now we start properly.

$$
\begin{align}
    \ln\left( \frac{p}{1-p} \right) &= \ln\left( \frac{\sigma(a)}{1-p} \right) \\
    &= \ln\left( \frac{(1 + e^{-a})^{-1} }{(1 + e^a)^{-1}}\right) & \text{(From earlier result)} \\
    &= \ln\left( \frac{1 + e^a}{1 + e^{-a}}\right) & \text{(Flip fraction)}
\end{align}
$$

Now we simplify $1 + e^{-a}$

$$
\begin{align}
    1 + e^{-a} &= \frac{e^a}{e^a} + \frac{1}{e^a} & \text{(Rewrite 1)} \\
    &= \frac{e^a + 1}{e^a}
\end{align}
$$

Now we return to where we were before

$$
\begin{align}
    \ln\left( \frac{p}{1-p} \right) &= \ln\left( \frac{1 + e^a}{1 + e^{-a}}\right) \\
    &= \ln\left( \frac{1 + e^a}{\frac{e^a + 1}{e^a}}\right) & \text{(From earlier result)} \\
    &= \ln\left( \frac{e^a (1 + e^a)}{1+e^a} \right) & \text{(Move } e^a \text{ to numerator)} \\
    &= \ln(e^a) & \text{(Simplify)} \\
    &= a & \text{(Log properties)}
\end{align}
$$

Completing the problem for part a.

### Part B

**Problem:**

Show that the derivative of the sigmoid function can be written as

$$
\sigma'(a)=\sigma(a)\bigl[1-\sigma(a)\bigr].
$$

**Solution:**

$$
\begin{align}
    \frac{d}{da} \sigma(a) &= \frac{d}{da} \frac{1}{1+e^{-a}} \\
    &= -(1+e^{-a})^{-2} \cdot \frac{d}{da} 1+e^{-a} \\
    &= -(1+e^{-a})^{-2} \cdot -e^{-a} \\
    &= \frac{1}{e^a(1+e^{-a})^2} \\
    &= \frac{1}{1+e^{-a}} \cdot \frac{1}{1+e^{-a}} \cdot \frac{1}{e^a} & \text{(Split up fraction)} \\
    &= \sigma(a) \cdot \frac{1}{1+e^{-a}} \cdot \frac{1}{e^a} & \text{(Substitution)} \\
    &= \sigma(a) \cdot \frac{1}{e^a(1+e^{-a})} \\
    &= \sigma(a) \cdot \frac{1}{1+e^a} \\
    &= \sigma(a) \cdot (1 - \sigma(a)) & \text{(From part A)}
\end{align}
$$

The final line is justified by the beginning of the work done in **part a** during the simplification of $1 - p$. It saved us time in both parts!

This completes the work for part b. 