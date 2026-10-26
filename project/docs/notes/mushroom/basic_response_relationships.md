# Overview

Created a ton of plots to examine some relationships with the response. Narrow down candidates. Here are my findings.

## Candidates

### Habitat

Need stratification, but appears promising and neat. 

![](project/images/mushroom/habitat_vs_response.png)

### Odor

Frankly, we can transform this into a "has odor" or not boolean column I think.

![](project/images/mushroom/odor_vs_response.png)

### Stalk Surface Above Ring

This one can likely just be a boolean for silky to be honest. That or its just "smooth, silky, other".

![](project/images/mushroom/stalk_surface_above_ring_vs_response.png)

### Spore print color

This ones interesting...

Think simplify it down to brown, black, white and chocolate. Group the rest into other. 

![](project/images/mushroom/spore_print_color_vs_response.png)

### Booleans

All the booleans look good aside from gill attached

## Columns to Drop

### Veil Color

This one can be ditched. The non-white colors are barely present, and white has no discernable relationship with the response.

![](project/images/mushroom/veil_color_vs_response.png)

### Ring Number

Rows that aren't 1 are too infrequent, only 72 rows for true response on two rings. Would need to be processed into an integer too. 

![](project/images/mushroom/ring_number_vs_response.png)

### Gill Attached

Simply not enough rows for attached gills. Unattached mushrooms are a 50/50 basically, not informative. 

![](project/images/mushroom/gill_attached_vs_response.png)