= Experimental Design & Preprocessing <experimental_design>

== Regression

== Classification

This dataset requires extensive processing from the start. It has no column names, and all values are truncated to a single letter as shown in @mushroom_raw_data. This dataset comes with a data dictionary, shown in @data_dictionary, but applying it to the dataset had to be done manually. Creation of the mapping json file was done using ChatGPT to save on time. 

To determine the candidate variables for the project, plots showing their relationship with the response were created and manually examined. Any promising variables were transformed into booleans if possible. This often required flattening down categorical variables into their most informative level. The variable `spore_print_color`, for example, was modified to only have the levels brown, black, white, chocolate and other. 

The final dataset retained seven variables, six boolean and one categorical. This was done to ease stratification issues and reduce the number of dummy variables required for modeling. These variables are `bruises`, `spore_print_color`, `gill_spacing_crowded`, `gill_size_narrow`, `stalk_shape_tapered`, `has_odor`, and `gill_color_buff`. Three stratified splits of the data were created. One for training $(50%)$, one for testing $(25%)$ and one for calibration $(25%)$. Stratification was done on the `spore_print_color` column. Split indices were saved as a numpy `npz` file. 