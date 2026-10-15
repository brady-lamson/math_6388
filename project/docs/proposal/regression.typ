= Regression

=== Background and Response

For the regression portion of this project I'll be looking at *official building electricity usage records* from Seattle. Non-residental and multi family homes are required to report energy usage to the city of Seattle, and this dataset contains 9 years of data from a ton of buildings. The full dataset contains over $46,000$ records and over $40$ columns of information for each building. I believe the value of this kind of analysis is apparent. Understanding what buildings are more or less efficient than others can help us understand what opportunities we have for improvement. Energy efficiency effects almost every single aspect of our lives. Gains there can put less strain on the power grid and lower usage of fossil fuels that provide this electricity.

For the response, I'll be using a variable called *EUI(kBtu/sf)*. This gives us a measure of electrical intensity per square foot, which allows us to compare the efficiency of buildings of various sizes. This is far better than pure electrical usage, where all I would determine is that bigger properties use more electricity. As well, there is a version of EUI that is weather normalized in this dataset, *EUIWN*, so it controls for bizarre weather that could impact electricity usage and throw off values.

=== Variables

I have a lot to choose from in this dataset. Currently, my interest is on a handful of columns. Below is a table of the response and all of my current candidates.

#set table(
  stroke: none,
  gutter: 0.2em,
  fill: (x, y) =>
    if x == 0 or y == 0 { gray },
  inset: (right: 1.5em),
)

#table(
    columns: (auto, auto, auto, auto),
    table.header([*Variable*], [*Purpose*], [*Data Type*], [*Description*]),
    [EUIWN], [Response], [Numeric], [Weather normalized electricity usage per square foot. Units: (kBtu/sf)],
    [DataYear], [Predictor], [Integer], [Year data was collected, ranges from 2015 - 2025],
    [BuildingType], [Predictor], [Categorical], [7 categories. Multifamily, hospital, nonresidental, etc.],
    [Neighborhood], [Predictor], [Categorical], [14 categories. Describes general location of the building. ],
    [YearBuilt], [Predictor], [Integer], [Age of the building.],
    [NumberofBuildings], [Predictor], [Integer], [Number of buildings on the property.],
    [NumberofFloors], [Predictor], [Integer], [Number of floors]
)



These are all just candidate predictors so I'll have to determine which ones I want to include through analysis later on.

=== Preprocessing and splitting

There isn't a lot to do to pre-process this data as it is quite well behaved. `Neighborhood` has enough categories that I may need to group some together to keep things feasible. `DataYear` will both function as a predictor and as a splitting variable. So I'll likely keep 2025 as the test set. I need to also consider how I will handle the same building showing up multiple times over the years. Basically all of them do, some every single year. One approach is to randomly select a single row to keep for each building. This prevents data leakage and makes interpretation a lot simpler. An alternative solution is to keep one year for training and another for testing, so it becomes more about predicting the next years usage. I personally prefer the former approach as we can also get information on if electrical efficiency is going up or down over time from its coefficient.

=== Modeling and Evaluation

For the models I'll be sticking to the required ones on the rubrick. This is a straightforward dataset, so traditional linear regression, a point prediction NN and a probabilistic neural network should all provide some interesting results.

For metrics, I'll be sticking to the rubrick. RMSE, MAE, gaussian negative log likelihood, prediction interval coverage and average interval width will all be evaluated. I think that's all pretty thorough.

=== Proposed Investigation

I have a clear investigation I want to do on this dataset. I mentioned potentially taking only one row per building to prevent data leakage. What happens to the models if I don't do that? How much, if at all, do the model attributes and predictions change? For this experiment, I would keep a set of buildings as a completely separate hold out set with one row per building. In theory, the models with duplicate buildings may end up overfitting and perform worse on buildings it hasn't been exposed to. Will that end up being true?

For this we can compare the equivalent models with a simple paired hypothesis test. The null hypothesis will be that the point estimates for those locations are the same across both cases. We can do the same for interval widths as well. I'm curious to see what the results of this would be.