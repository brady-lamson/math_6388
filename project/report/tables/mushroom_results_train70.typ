#set table(
  fill: (x,y) =>
    if x == 0 or y == 0 {gray.lighten(65%)}
)

#table(
  columns: 4,
  align: (left, center, center, center),
  table.header(
    [*Metric*],
    [*Logistic Regression*],
    [*Neural Net (Before)*],
    [*Neural Net (After)*],
  ),
  [Accuracy], [93.27\%], [99.84\%], [99.92\%],
  [Precision], [98.69\%], [100.00\%], [100.00\%],
  [Recall], [87.54\%], [99.67\%], [99.83\%],
  [F1-Score], [92.78\%], [99.83\%], [99.92\%],
  [NLL], [0.11795], [0.01276], [0.02957],
  [ECE], [0.05595], [0.00960], [0.00082],
)