= Appendix

== Mushroom

#figure(
  image("../images/mushroom/mushroom_raw_data.png", width: 100%),
  caption: "Snapshot of the raw mushroom dataset."
) <mushroom_raw_data>

#figure(
  block(stroke: 1pt, inset: 10pt)[
  ```py
  7. Attribute Information: (classes: edible=e, poisonous=p)
      1. cap-shape:                bell=b,conical=c,convex=x,flat=f,
                                    knobbed=k,sunken=s
      2. cap-surface:              fibrous=f,grooves=g,scaly=y,smooth=s
      3. cap-color:                brown=n,buff=b,cinnamon=c,gray=g,green=r,
                                    pink=p,purple=u,red=e,white=w,yellow=y
  ```
  ],
  caption: "Snippet of the mushroom data dictionary"
) <data_dictionary>

#figure(
  image("../images/mushroom/spore_print_color_vs_response.png", width: 70%),
  caption: "Plot showing the relationship between spore print color and if its poisonous or not."
) <spore_color>

#figure(
  grid(
    columns: 2,
    [#image("../images/mushroom/reliability_before_nbins15_seed100_train50.png")],
    [#image("../images/mushroom/reliability_nbins15_seed100_train50.png")],
  ),
  caption: "Reliability diagram of the calibration results. Left is BEFORE, right is AFTER. bins=15, seed=100, train_size=0.5"
) <mushroom_reliability>

=== Alternate results when train_size=0.7

#figure(
  grid(
    columns: 2,
    [#image("../images/mushroom/reliability_before_train70.png")],
    [#image("../images/mushroom/reliability_after_train70.png")],
  ),
  caption: "Alternate results. Reliability diagram of the calibration results. Left is BEFORE, right is AFTER. bins=15, seed=100, train_size=0.7"
) <mushroom_reliability_train70>

#figure(
  include "tables/mushroom_results_train70.typ",
  caption: "Alternate results. Classification results summary. Classification threshold = 0.7, train_size=0.7"
) <mushroom_results_train70>

#figure(
  include "tables/mushroom_confusion_train70.typ",
  caption: "Alternate results. Confusion matrix results. Classification threshold = 0.7, train_size=0.7"
) <confusion_matrix_train70>