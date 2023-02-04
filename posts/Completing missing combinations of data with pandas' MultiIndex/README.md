# Completing missing combinations of data with pandas' MultiIndex

The pandas.MultiIndex is a powerful tool for handling multi-level indexing in pandas.DataFrames giving us the flexibility to manipulate, prepare, and analyze complex datasets

Let's investigate how we can leverage MultiIndex to complete missing combinations of identifying columns or categories in our datasets!

## Table of Contents

- [Creating a MultiIndex with all possible combinations of categories]()
- [Reindexing our DataFrame to align with the MultiIndex]()
- [Filling missing values in our completed DataFrame]()
- [Conclusion]()
- [Additional resources]()

{% embed https://www.christophergreening.com %}

## Understanding missing combinations of categories

## What is MultiIndex?

As I mentioned above, MultiIndex is a powerful tool for managing DataFrame's that contain multiple layers, categories, or segmentations

Let's take a look at a simple example:

Starting with a simple DataFrame...

```python
import pandas as pd

df = pd.DataFrame({
    'category_1': ['A', 'A', 'B', 'B', 'C', 'C'],
    'category_2': ['D', 'E', 'D', 'E', 'D', 'E']
    'value': [1, 2, 3, 4, 5, 6]
})
```

... we can create a MultiIndex by setting our categories as the indices

```python
df = df.set_index(["category_1", "category_2"])         
```

## Creating a MultiIndex with all possible combinations of categories
## Reindexing our DataFrame to align with the MultiIndex
## Filling missing values in our completed DataFrame
## Conclusion
## Additional resources