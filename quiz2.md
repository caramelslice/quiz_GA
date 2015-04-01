#Machine Learning / SKLearn Quiz (Quiz 2)

1. Given the following machine learning matrix, fit each of the following algorithms into their respective places. Some may have multiple.

    .               | continuous          | categorical
    ---------------:|:--------------------|:-----------
    supervised      | regression          | classification
    unsupervised    | dimension reduction | clustering
  
    Algorithms:
    * Ordinary Least Squares (regression,supervised)
    * Logistic Regression (classification,supervised)
    * Naive Bayes (classification,supervised)
    * Decision Trees (classification or regression, supervised)
    * Support Vector Machines (classification,supervised)
    * Nearest Neighbors (classification,supervised)
    * K Means (clustering,unsupervised)
    * Principal Component Analysis (Matrix Decomposition) (clustering,unsupervised,dimension reduction)

2. Given the 4 entities in the matrix above, describe a problem / example we worked on in class for each, and provide one idea on your own.

regression - can be used to predict quantitative target variables. For example, predict housing prices in the Boston dataset.

classification - can use logistic regression decision trees. For example, predict whether a car is lemon or not. Or even the iris dataset, to see what type of flowr it is. 


3. All sklearn prediction objects have functions akin to fit(), transform(), predict(), and fit_transform(). Explain each in their most general terms.

fit() - Fit the model according to the given training data.
transform() - Takes an X -> makes new X. Transform X and y with parameters
score: some metrix given y (original values) and y' (predicted values)
predict: takes an X and returns y (targe values)
fit_transform - fir then return new x. 


3. Two of the above algorithms can use kernels (in their sklearn context)
    a. Explain what a kernel does
    b. Which are the two algorithms that use kernels?

a. A Kernal computes the similarity. 
b. Support Vector machines and PCA


4. One of the above algorithms is most obviously not a linear solution to classification (it does not draw straight decision lines). Which algorithm is it, and how does it decide on decision lines?

PCA.
We can used kernals. 


5. You are working on microarray (DNA) samples where number of observations (n) is 5 and number of observations (m) is > 10,000.
    1. Describe a supervised and unsupervised technique in order to reduce the number of features in the samples to those that are most significant.
    2. Compare the two techniques in their solution.


1. lasso regression (supervised), or pca (unsupervised, cluster)
2. lasso - reduced features
pca - 

6. Below is a table of Gini Importance (Normalized to 1) in predicting rent in New York City.
    1. Which algorithm uses Gini Importance?
    2. Interpret the table.

    Feature           | GiniImportance
    :-----------------|:--------------
    bedrooms          | 0.211
    bathrooms         | 0.005
    sqft              | 0.532
    distance subway   | 0.198
    distance columbus | 0.017
    nearby pizza      | 0.042

    1. Decision Trees
    2. sqft is the most important feature in predicting rent in NYC. The higher the Gini Importance, the higher the predictability. 

7. What is the Receiving Operator Characteristic Curve? What two metrics is it composed of?

ROC curve. Also known as area under the curve. We want it to be as close to 1 as possible. 
We can calculate the AUC from the results of a confusion matrix. Use precision and accuracy. 

9. How does a grid search work? Use an example algorithm from above to help explain it.

10. Three parts:
    1. What's your strongest "takeaway" from machine learning and this segment of the course?
    - Statistics

    2. Given a 2 dimensional figure where y=effort to learn and x=immediate usefulness, and slope = 1, what is one algorithm that felt above the slope (more effort to learn than usefulness) and one algorithm that felt below the slope (more usefulness than effort to learn)?

    svm. we can use a hyperplane to assess that. 

    3. What's one question you still have about machine learning?
    Lots... Maths in particular. I am trying to read and understand some of the Kaggle competition notes - still have problems after this class....