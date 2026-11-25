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
  [Accuracy], [76.02\%], [71.54\%], [76.07\%],
  [Precision], [97.66\%], [76.36\%], [100.00\%],
  [Recall], [51.28\%], [58.97\%], [50.15\%],
  [F1-Score], [67.25\%], [66.55\%], [66.80\%],
  [NLL], [0.31279], [1.28004], [0.47453],
  [ECE], [0.15431], [0.28245], [0.26484],
)