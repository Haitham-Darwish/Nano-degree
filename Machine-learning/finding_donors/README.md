# Introduction

CharityML is a fictitious charity organization located in the heart of Silicon Valley that was established to provide financial support for people eager to learn machine learning. After nearly 32,000 letters were sent to people in the community, CharityML determined that every donation they received came from someone that was making more than $50,000 annually. To expand their potential donor base, CharityML has decided to send letters to residents of California, but to only those most likely to donate to the charity. With nearly 15 million working Californians, CharityML has brought us on board to help build an algorithm to best identify potential donors and reduce overhead cost of sending mail. Our goal will be evaluate and optimize several different supervised learners to determine which algorithm will provide the highest donation yield while also reducing the total number of letters being sent.

# Project Highlights
This project is designed to get you acquainted with the many supervised learning algorithms available in sklearn, and to also provide for a method of evaluating just how each model works and performs on a certain type of data. It is important in machine learning to understand exactly when and where a certain algorithm should be used, and when one should be avoided.
Things we will learn by completing this project:
  * How to identify when preprocessing is needed, and how to apply it.
  * How to establish a benchmark for a solution to the problem.
  * What each of several supervised learning algorithms accomplishes given a specific dataset.
  * How to investigate whether a candidate solution model is adequate for the problem.

# Training and Testing
The training data for this competition is the same as what you used to complete the project (census.csv).

However, the test data has a few more data cleaning issues. The 1 values in the test dataset indicate those with incomes greater than 50K, while 0 values indicate that is not the case. Your job is to find a model that performs best on the test data! Use your model to make predictions on the test_census.csv data, then provide the index and predicted income as either a 1 (if more than 50K) or 0 (if less than 50K).

# Reference

[Pandas](https://pandas.pydata.org)
<br>[Numpy](https://numpy.org)
<br>[opengenus](https://iq.opengenus.org/applications-of-random-forest/)
<br>[stackexchange](https://datascience.stackexchange.com/questions/6838/when-to-use-random-forest-over-svm-and-vice-versa)
<br>[Quora](https://www.quora.com/When-is-a-random-forest-a-poor-choice-relative-to-other-algorithms)
<br>[datacamp](https://www.datacamp.com/tutorial/adaboost-classifier-python#adaboost-classifier)
<br>[analyticsvidhya](https://www.analyticsvidhya.com/blog/2017/09/understaing-support-vector-machine-example-code/)
<br>[springer](https://link.springer.com/book/10.1007/978-3-319-02300-7)
<br>[data-flair.training](https://data-flair.training/blogs/applications-of-svm/)
<br>[robertyoung2](https://github.com/robertyoung2/Finding-Donors-for-CharityML/blob/master/finding_donors.ipynb)
<br>[scikit-learn](http://scikit-learn.org/0.17/install.html)
