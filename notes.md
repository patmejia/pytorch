# Machine Learning

# Terms

1. decision tree is a flowchart-like structure in which each internal node represents a "test" on an attribute, each branch represents the outcome of the test, and each leaf node represents a class label. The paths from root to leaf represent classification rules.
1. sample decision tree
   ![sample decision tree](https://upload.wikimedia.org/wikipedia/commons/f/f3/CART_tree_titanic_survivors.png)
   "The predicted price for any house under consideration is the historical average price of houses in the same category"

"We use data to decide how to break the houses into two groups, and then again to determine the predicted price in each group. This step of capturing patterns from data is called fitting or training the model. The data used to fit the model is called the training data."

1. deeper trees is a tree with more splits.

```copilot
more splits leads to a model that can make more detailed predictions, and thus can capture more patterns in the data. However, it can lead to overfitting.

are more complex and more prone to overfitting. it is a good idea to start with a small tree and then increase the depth of the tree if the model is underfitting the data. then we can use techniques such as pruning to prevent overfitting and improve generalization performance which is the ability of the model to predict new data. it is a good idea to use a validation set to evaluate the model's performance on data it has not seen before.
```

1. leaf is a node that does not have any children. the prediction for a leaf is the average of the target values in the training data that fall into that leaf.

"The point at the bottom where we make a prediction is called a leaf."` The leaves of the tree are the final predictions that the model makes.`

1. Pandas is the primary tool data scientists use for exploring and manipulating data. its abbreviate code ais `pd`. We do this with the command `import pandas as pd`.
