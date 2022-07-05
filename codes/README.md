# Code

The project was developed in **Python** programming language and had multiple steps:

- Extracting images from a public Facebook page.
- Extracting visual tags from each image.
- Exploratory data analysis on the data obtained to create sample data.
- Application of machine learning methods for regression or classification.

The code presented here is a framework example, showing how it was done at the time throughout the project. The local directories, access tokens and Facebook page name are generic and do not function.

The access tokens used in the project have been inactive for a long time now.

## Image Extraction

Using *Facebook Graph API*. Code within **extract-image-tag.py**.

- About <a href="https://developers.facebook.com/docs/facebook-login/access-tokens/#pagetokens" title="https://developers.facebook.com/docs/facebook-login/access-tokens/#pagetokens">Facebook Access Tokens</a>.<br>
"*To generate a page access token, an admin of the page must grant an extended permission called manage_pages.*"
- About <a href="https://developers.facebook.com/docs/facebook-login/permissions/#reference-manage_pages" title="https://developers.facebook.com/docs/facebook-login/permissions/#reference-manage_pages">Permissions</a>.<br>
"*require that you have Client OAuth Login enabled for your app on the Facebook Login tab of your app dashboard.*"
- About <a href="https://oauth.net/getting-started/" title="https://oauth.net/getting-started/">OAuth Login</a>.
- GraphAPI <a href="https://developers.facebook.com/docs/graph-api/reference/page/" title="https://developers.facebook.com/docs/graph-api/reference/page/">Reference</a>.

The public Facebook page **@ajudeaacd** from which they were extracted granted permission and access at the time and no longer exists on Facebook.

## Tag Extraction

Using *Miscrosoft Azure Computer Vision*. Code within **extract-image-tag.py**.

- Computer Vision <a href="https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/overview-image-analysis" title="https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/overview-image-analysis">Reference</a>.

The tags obtained from the images are inside the **_Extracted_Tags.zip** compressed folder.

## Data Analysis and Dataset Creation

The dataset used is the **dataset/Bivariate_Table.csv** (comma separated). Generated from the code within **data-organizing.py**.

This code also presents an example of boxplot generation for a single tag, for analysis of useful tags in the dataset. Boxplots for all tags inside the **dataset/_Calculated_Boxplots.zip** compressed folder.

Boxplot example:

![Balanced boxplot of the tag food](/images/boxplot-example-food.jpg "Example of balanced boxplot, using the tag 'food'")

Dataset used:

![Sample of dataset used](/images/structured-data.jpg "Sample of dataset used")

In the dataset, each line refers to an image, and each column refers to a tag. All tags are presented, and the value 0 or 1 identifies if that tag is present or not in the image. The final column is the depend variable, the amount of likes the image received.

## Classification

Using *Scikit-Learn* libraries:

- <a href="https://scikit-learn.org/stable/modules/naive_bayes.html" title="https://scikit-learn.org/stable/modules/naive_bayes.html">Naive Bayes</a>.
- <a href="https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html" title="https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html">Decision Tree Classifier</a>.
- <a href="https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html" title="https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html">K Neighbors Classifier</a>.
- <a href="https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html" title="https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html">Support Vector Classifier</a>.

Using the dataset presented, with the *likes* column as the dependent variable (y) and all tags columns as the independent variables (x).

The classes obtained were "many-likes" and "few-likes", using a value obtained from exploratory analysis as the inflection point of amount of likes.
