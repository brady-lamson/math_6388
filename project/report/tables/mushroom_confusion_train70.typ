#set table(
  // gutter: 0.3em,
  fill: (x,y) =>
    if x == 0 or y == 0 {gray.lighten(65%)}
)
#set text(size: 11pt)
#table(
  columns: 5,
  align: (left, center, center, center, center),
  table.header(
    [*Model*],
    [*True Positive*],
    [*True Negative*],
    [*False Positive*],
    [*False Negative*],
  ),
  [Logistic Regression], [527], [610], [7], [75],
  [Neural Net (Before)], [600], [617], [0], [2],
  [Neural Net (After)], [601], [617], [0], [1],
)