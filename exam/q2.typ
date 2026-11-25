= Question 2

== Context

#let xbold = $bold(x)$
#let xboldi = $bold(x)_i$
#let wbold = $bold(w)$
#let wmu = $bold(w)_(mu)$
#let wsigma = $bold(w)_(sigma)$
#let musubi = $#wmu^T #xboldi$
#let varsubi = $exp(#wsigma^T #xboldi)$

In class, we derived the Residual Sum of Squares (RSS) loss function under the assumption of homoscedastic Gaussian noise, where 
$p(y | #xbold, #wbold) = N(y | #wbold^T #xbold, sigma^2)$
and $sigma^2$ is constant. Suppose instead we are dealing with heteroscedastic data where the noise variance depends on the input feature vector $#xbold _i$. We model the mean $mu_i = #musubi$ and the variance as $sigma^2_i = #varsubi$ to ensure positivity.

== Part A

*Problem:* Derive the new Negative Log-Likelihood (NLL) loss function $L(#wmu, #wsigma)$ for a dataset of $N$ independent samples. 

For ease of notation and space I will be using $mu_i$ and $sigma^2_i$ and only substituting in the full values near the end. 

$
  p(y_i | mu_i, sigma_i) = 1/(sqrt(2 pi sigma_i^2)) exp(-(y_i - mu_i)^2/(2sigma^2_i))
$

So the Negative Log-Likelihood can be represented as:

#let NLL = $"NLL"(bold(w)_(mu), bold(w)_(sigma))$

#let mysum = $sum_(i=1)^N$
$
  #NLL &= - #mysum ln(p(y_i|mu_i, sigma_i)) \
  &= - #mysum ln(1/(sqrt(2 pi sigma_i^2)) exp(-(y_i - mu_i)^2/(2 sigma_i^2))) \
  &= - #mysum [ ln((2 pi sigma_i^2)^(-1/2) ) - (y_i - mu_i)^2/(2 sigma_i^2)] \
  &= - #mysum [ -1/2 ln(2 pi sigma_i^2) - (y_i - mu_i)^2/(2 sigma_i^2) ] \
  &= 1/2 #mysum [ ln(2 pi sigma_i^2) + (y_i - mu_i)^2/(sigma_i^2) ] \
  &= 1/2 #mysum [ ln(2 pi) + ln(sigma_i^2) + (y_i - mu_i)^2/(sigma_i^2) ] \
  &= 1/2 #mysum [ (y_i - #musubi )^2/(#varsubi) + ln(#varsubi) + ln(2 pi) ] \
  &= 1/2 #mysum [ (y_i - #musubi )^2/(#varsubi) + #wsigma^T #xboldi + ln(2 pi) ] \
$

Some issues I have with my own results here. I'm really spotty on matrix math nowadays. I'm not convinced the notation of that solution is correct. 

I believe the division is okay because $#varsubi$ should be a scalar after computation. 

#pagebreak()

== Part B

*Problem:* Compute the gradient of this loss function with respect to $#wmu$.

I apologize in advance for this one I am extremely rusty at matrix calculus and matrix math in general.

For the gradient we examine the parts of the NLL that depend on $#wmu$. Because $#varsubi$ does not depend on $#wmu$ I will be substituting back in $sigma^2_i$. 

#let varsubi = $sigma^2_i$

$
  Delta #wmu "NLL"(bold(w)_(mu), bold(w)_(sigma)) &= Delta #wmu
  1/2 #mysum [ 
    (y - #musubi )^2/(#varsubi) 
    + underbrace(#wsigma^T #xboldi, "constant") 
    + underbrace(ln(2 pi), "constant") 
  ] \
  &= 1/2 #mysum Delta #wmu (y_i - #musubi )^2/(#varsubi) + 0 + 0 \
  &= 1/2 #mysum Delta #wmu ((y_i - #musubi)(y_i - #musubi))/(#varsubi) \
  &= 1/2 #mysum Delta #wmu (y_i^2 - y_i#musubi + (#musubi)^2)/(#varsubi) \
  &= 1/2 #mysum Delta #wmu underbrace((y_i^2)/#varsubi, "constant") - (y_i#musubi)/#varsubi + (#musubi)^2/(#varsubi) \
  &= 1/2 #mysum -sigma_i^(-2) ( Delta #wmu (y_i#musubi) - Delta #wmu (#musubi)^2 ) \
  &= 1/2 #mysum -sigma_i^(-2) ( y_i Delta #wmu (#musubi) - Delta #wmu (#musubi#musubi) ) \
$

I'm really shaky on matrix calculus but let me give it a shot. Let's examine $Delta #wmu (#musubi)$.

If we assume that $bold(w)_(mu)$ is of dimension $k times 1$ and $bold(x_i)$ has the same dimensions, then $bold(w)_(mu)^T bold(x_i)$ has dimension $1 times 1$, or just a scalar. 

$
  #musubi &= w_1 x_1 + dots w_k x_k \
  Delta #wmu (#musubi) &= mat(
    delta/(delta w_1) w_1 x_1 + dots w_k x_k;
    delta/(delta w_2) w_2 x_1 + dots w_k x_k;
    dots;
    delta/(delta w_k) w_k x_1 + dots w_k x_k;
  ) = mat(x_1; x_2; dots; x_k) = bold(x)
$

Thankfully the class notes covered this part. 

So we get to:

$
  Delta #wmu "NLL"(bold(w)_(mu), bold(w)_(sigma)) &= 1/2 #mysum -sigma_i^(-2) ( y_i bold(x_i) - Delta #wmu (#musubi#musubi) )
$

For the other part, we get:

$
  #musubi #musubi &= (w_1 x_1 + dots w_k x_k) dot (w_1 x_1 + dots w_k x_k) \
  &= w_1^2 x_1^2 + w_1 x_1 w_2 x_2 + dots + w_1 x_1 w_k x_k + dots + w_k^2 x_k^2
$

The important note here is that only a portion of this final sum will depend on a given $w_i$. That'll be how the derivatives break down. 

$
  Delta #wmu (#musubi) &= mat(
    delta/(delta w_1) w_1^2 x_1^2 + dots + w_1 x_1 w_k x_k + dots + w_k^2 x_k^2;
    delta/(delta w_2) w_1^2 x_1^2 + dots + w_1 x_1 w_k x_k + dots + w_k^2 x_k^2;
    dots;
    delta/(delta w_k) w_1^2 x_1^2 + dots + w_1 x_1 w_k x_k + dots + w_k^2 x_k^2;
  ) \ &= mat(
    2w_1x_1^2 + dots + x_1w_k x_k;
    w_1 x_1 x_2 + 2w_2 x_2^2 + dots + x_2 w_k x_k
    ; dots
  )
$

To be totally honest, not totally sure how to represent this one. I'm not sure how this all simplifies from here either, so I think I need to stop and not finish this problem. 