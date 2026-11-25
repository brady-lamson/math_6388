= Question 4

== Context

You are designing a CNN for image classification. The input to the first convolutional layer is a batch of RGB images of shape $(3, 64, 64)$ representing $("Channels", "Height", "Width")$. The convolutional layer uses 32 filters, a kernel size of $5 times 5$, a stride of $1$, and padding of $2$ on each side. There is a bias term for each filter. 

== Part A

*Problem:* Calculate the spatial dimensions of the output feature map. Show your work. 

Let's start from a *baseline* answer then adjust as we go. If we had no padding, no bias and one channel, we'd use the formula:

$
  "output dim" &= (n_h - k_h + 1) times (n_w - k_w + 1) \
  &= (64 - 5 + 1) times (64 - 5 + 1) \
  &= 60 times 60
$

Where $n$ and $k$ represent the input and kernel, and $h$ and $w$ represent height and width. 

*Padding* adds height and width to our input. We have padding of 2, giving us an updated height and width of 66 for the input. No adjustment needs to be made for the *stride* as it's set to $1$. 

$
  62 times 62
$

As we have $32$ filters, we have a final output feature map shape of 

$
  32 times 62 times 62
$

== Part B

*Problem:* Calculate the total number of learnable parameters (weights and biases) in this specific convolutional layer. 

For this, we have $32$ filters, $3$ channels, a $5 times 5$ kernel size, with each filter having a bias. 

So we have $32$ biases to start.

As for weights, we have $3 times 5 times 5 = 75$ weights per filter. For a final tally of

$
  (75 dot 32) + 32 = 2432
$

total parameters.

== Part C

*Problem:* If this were a fully connected (Dense) layer mapping the flattened input image to a flattened output of the exact same size, how many learnable parameters would be required? Briefly explain why the CNN's parameter sharing is advantageous here. 

It depends on how we define a flattened input image. If we assume by flatten we are taking a 3 channel image and turning it into a 1D vector, it'll have length $n_h times n_w times C_i = 64 dot 64 dot 3 = 12288$. To get an output of the same shape, you would need:

$
  underbrace((1 times 12288), "input vector dimensions") times underbrace((12288 times 12288), "weight matrix dimensions") = underbrace((1 times 12288), "output vector dimensions")
$

What this means, is for just the weights, you would need $12288^2 = 150,994,944$ learnable parameters. I believe, for bias, that each output would get a bias parameter. So that adds another 12288 onto that total. 

This is enormous, obviously. A far cry from the previous $2432$ parameters. This is due to the fact that every single input value across every channel has to function as input for every single output value. This is far more computationally expensive, and there is also the spatial component that gets lost. With the kernel, nearby pixels share information with one another. This allows for pattern recognition amongst local areas of an image, instead of information from specific pixels getting lost in the noise of the entire image resolution. Dense layers have their place, but this is why we don't typically use them for this specific step.