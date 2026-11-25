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
  [Logistic Regression], [500], [1044], [12], [475],
  [Neural Net (Before)], [575], [878], [178], [400],
  [Neural Net (After)], [489], [1056], [0], [486],
)