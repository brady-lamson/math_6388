#import "@preview/grape-suite:4.0.0": exercise
#import exercise: project, task, subtask
#show selector(heading.where(level: 1)): set heading(numbering: none)
#show selector(heading.where(level: 2)): set heading(numbering: none)
#show selector(heading.where(level: 3)): set heading(numbering: none)
#show selector(heading.where(level: 4)): set heading(numbering: none)
#set par(
    leading:1.0em,
    spacing:2em
)

#show: project.with(
    title: "Project Proposal",

    university: [University of Colorado, Denver],
    semester: [Fall 2026],
    seminar: [MATH 6388 - Statistical and Machine Learning],

    show-outline: false,

    author: "Brady Lamson",

    show-solutions: false,
    show-lines: false,
    type: "Homework Sheet"
)

= Classification
=== Background and Response
For the classification portion of this project I will be examining the *mushroom* dataset from the *Audobon Society Field Guide*, sourced from the *UC Irvine Machine Learning Repository*. This dataset contains a ton of categorical information about 8124 mushrooms with one observation per mushroom. The response of interest is whether a given mushroom is poisonous or not. As such, this topic follows the classic style of fraud detection problems. Though the topic of mushroom edibility doesn't matter a lot on its own, the top of things being safe to consume has gotten far more relevance recently. Lately we have seen a staggering amount of FDA food recalls, and the current administration is consistency gutting and declawing various agencies that ensure what we put in our bodies is safe. So I feel this is topical in its own way as we can imagine various experts using similar models to detect dangerous food and drugs. I like using mushrooms here as it's tangentially related but not nearly as depressing.

=== Variables

Alongside the response are 22 other features, all categorical in nature. These describe aspects of the mushroom such as the coloring of the gills, whether there is any bruising on the mushroom, and the habitat it was found in. This aspect of the dataset I find extremely interesting as categorical columns have to be treated with an additional level of care to numeric ones. A categorical column may be a multi-level factor, an ordinal column, or one that can be treated as a simple boolean. This dataset has all of the above, so I have to be careful during the modeling setup to ensure I'm appropriately handling the final columns I choose.

=== Preprocessing and Splitting

This also leads into the topic of splitting the data. The response of this data is quite balanced, with $48%$ of the rows being poisonous and $52%$ being edible. This cannot be said for many of the categorical columns, with some particularly rare levels of them only showing up about 4 times. Almost every single column is extremely unbalanced. This leads to a risk of levels only being present in one of the splits, and with some categories being so infrequent not even stratification is a perfect solution. I will likely need to combine certain infrequent categories into an "other" level or omit them entirely to prevent breaking issues.

My plan to tackle this is to go through each multi level candidate variable and look for any obvious relationships with the response. For anything that seems promising, I'll decide on a case-by-case basis what feature engineering will be most appropriate. The simplest case are variables with only 2 levels, as they can be easily converted into boolean columns. The only ordinal column present in this dataset, `ring_number`, seems to be a simple integer column that was saved as text which is an easy fix. Lastly, any multi level categorical columns will use dummy variables. As for missing values, only the column `stalk_root` has any. Over a quarter of the rows $(2480/8124)$ are missing data for this column. As such, it will not be a candidate for this project. It's possible I will have to drop some rows depending on my columns of choice. Take `cap_surface`. It has 4 categories, and 3 are very balanced each having about 2 to 3 thousand rows. One category though, `grooves`, only has 4 rows. There is no reasonable way to include that one in the other categories, so I may need to simply drop those 4 rows entirely if I want to use that variable.

=== Modeling and Evaluation

For modeling, I'll be sticking with the required models from section 5.1. So that is logistic regression and a neural network classifier. For metrics I'll be focusing primarily on precision, recall and f-1 score. Recall is huge here in particular as this is a fraud-detection problem. False positives are less of a concern as there isn't a consequence to not eating a mushroom. False negatives however are extremely bad so we want to minimize the number of those.

=== Proposed Investigation

For classification problems we of course care about probability thresholds. For this project I want to pay careful attention to the *true poisonous* mushrooms that end up with low predicted probabilities or those that are borderline. Will they even exist? Is there a clear separation between the response or are certain ones ambiguous? What categories are driving that ambiguity if it is a problem? I want to try and find some tricky to categorize mushrooms and see how the models perform.

= Regression

=== Background and Response

For the regression portion of this project I'll be looking at official building electricity usage records from Seattle. Non-residental and multi family homes are required to report energy usage to the city of Seattle, and this dataset contains 9 years of data from a ton of buildings. The full dataset contains over $46,000$ records and over $40$ columns of information for each building. For the response, I'll be using a variable called *EUI(kBtu/sf)*. This gives us a measure of electrical intensity per square foot, which allows us to compare the efficiency of buildings of various sizes. This is far better than pure electrical usage, where all I would determine is that bigger properties use more electricity. 

=== Variables

I have a lot to choose from in this dataset. Currently, my interest is on a handful of columns. *BuildingType* is a categorical column that tells us if a property is multi family home, a school, hospital, etc. It has 7 categories total and all of the categories have enough frequency to be safe to use. 

// TODO: MAKE THE VARIABLES A MARKDOWN TABLE 