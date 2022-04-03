# Animating 60 years of US energy data with 10 lines of Python
[Link to blog post](https://dev.to/chrisgreening/animating-60-years-of-us-energy-data-with-10-lines-of-python-afi)

---

In this step-by-step tutorial, we're going to cover how to animate a meaningful visualization from a real world dataset with almost 700,000 data points. 

If you would rather clone and follow this tutorial as a Jupyter Notebook, you can do so at this [link](https://github.com/chris-greening/tutorials/blob/master/Python/us-animated-energy-plot/united_states_energy_exploration.ipynb)

{% github chris-greening/tutorials no-readme %}

Otherwise, we'll be animating ~60 years of United States energy consumption data in only 10 lines of Python! 

To prove it to you, here is the code from start to finish: 

```python
import pandas as pd 
import plotly.express as px 

# Importing the dataset
df = pd.read_csv("https://www.eia.gov/state/seds/sep_use/total/csv/use_all_btu.csv")

# Filter out aggregate United States and Washington DC rows
df = df[~df.isin(["US", "DC"])]

# Filter rows that contain total consumption per energy source
total_df = df[df["MSN"].str.match("[A-Z]{2}TC[A-Z]")]

# Melt from wide to long format 
total_df = total_df.melt(id_vars=["Data_Status", "State", "MSN"], var_name="Year", value_name="BTU")

# Sum energy consumption per state per year 
summed_df = total_df.groupby(["State", "Year"], as_index=False).sum()

# Animate the bar plot
fig = px.bar(summed_df, x="State", y="BTU", animation_frame="Year", range_y=(0, summed_df["BTU"].max()), color="State", title="United States total energy consumption (BTU)")
fig.update_xaxes(categoryorder="total ascending")
fig.show()
```

The [.csv](https://www.eia.gov/state/seds/sep_use/total/csv/use_all_btu.csv) we will be working with is publicly available on the [US Energy Information Administration](https://www.eia.gov/) government website. 

**Prerequisite packages:**
- [pandas](https://pandas.pydata.org/)
- [plotly](https://plotly.com/python/)

And now... _time to code!_

# Importing the dataset 

Importing our dataset is relatively straightforward; we're able to pass the URL of a _.csv_ to [pandas.read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) and it will import it into a `pandas.DataFrame`. 

```python
df = pd.read_csv("https://www.eia.gov/state/seds/sep_use/total/csv/use_all_btu.csv")
```

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/na5y7rysi9c7ilupp2dw.gif)

# Removing aggregate US and Washington DC rows

In this case, our dataset contains rows for both aggregate United States (`US`) and Washington DC (`DC`) data. 

Since we are only concerned with energy consumption per state, we're going to filter the `US` and `DC` rows out.

```python
df = df[~df.isin(["US", "DC"])]
```

# Understanding the MSN column

Do NOT worry if you don't fully understand this next section! It has no bearing on the code, we're just going to develop some important domain knowledge before moving forward.

Looking through [documentation](https://www.eia.gov/state/seds/sep_fuel/html/csv/fuel_csv_doc.pdf) provided on the website, we can see that the `"MSN"` column stands for _Mnemonic Series Names_. These are codes that contain information on the type of energy source, the sector, and the unit. 

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/wl3aesjpem7oc64dnvdq.png)

# Understanding MSN by example

In the context of our data, row `0`'s MSN value is _ABICB_.

Let's break it down:
- _AB_: Aviation gasoline blending components 
- _IC_: Industrial sector 
- _B_: British thermal units (BTU)

Thus, that row corresponds to _Aviation gasoline blending components consumed by the industrial sector in british thermal units (BTU)_.

When the 3rd and 4th characters of an  _MSN_ are _TC_, this means the row corresponds to the total energy consumption across all sectors (i.e. residential, industrial, etc.) for that resource.

Looking back at the Aviation gasoline blending components, an _MSN_ of _ABTCB_ would thus be 
- _AB_: Aviation gasoline blending components 
- _TC_: Total of all sectors
- _B_: British thermal units (BTU)

# Filtering rows that contain total consumption per energy source

To get all rows that have _TC_ as the 3rd and 4th characters (and thus the total), we can use a regular expression with the `Series.str.match` method. 

The pattern we will use is `"[A-Z]{2}TC[A-Z]"`. 

Let's break it down: 

- [A-Z]{2}: The 1st and 2nd letter can be any uppercase letters
- TC: The 3rd and 4th letters must be TC 
- [A-Z]: The 5th character can be any uppercase letter

```python
total_df = df[df["MSN"].str.match("[A-Z]{2}TC[A-Z]")]
```

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/1gfe44ba93zofzigw1n7.png)

# Melting years into a Year column

Now that we have the rows we want to visualize, we're going to unpivot our `DataFrame` from wide to long format. This will massage the year columns into rows as two new columns: `"Year"` and `"BTU"`.

This allows us to select and filter our data much easier now as well as pass it through to `plotly.express` which is expecting a long format `DataFrame`.

```python
total_df = total_df.melt(id_vars=["Data_Status", "State", "MSN"], var_name="Year", value_name="BTU")
```

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/0lhyyw4tz8dsy47gk8e2.png)

# Summing all energy sources together

Now that we have the total consumption per energy source, state, and year, we can sum them all together grouped by each state and each year. 

This will leave us with the total energy consumption per state per year which is what we're looking to visualize. 

```python
summed_df = total_df.groupby(["State", "Year"], as_index=False).sum()
```

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/9qosmrd2jzacykrxtjeg.png)

# Creating the animated bar plot

Our data is now ready to be visualized! `plotly.express.bar` has an `animation_frame` argument which allows us to pass what column to animate our data on. 

For this example, we will be animating one frame per `"Year"` of data. 

```python
fig = px.bar(
        summed_df, 
        x="State", 
        y="BTU", 
        color="State",
        animation_frame="Year", 
        title="United States total energy consumption (BTU)",
        range_y=(
            0, 
            summed_df["BTU"].max()
        ), 
).update_xaxes(categoryorder="total ascending")

fig.show()
```

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/oar80z4dlknjk1dnicab.gif)

# Additional exercises 

Great work! Now that we have this data, there is a _ton_ of other insights you can find. I recommend messing around with different _MSN_ codes, groupings, etc. and see what you can learn! 

If you have any questions, feel free to message me or reach out in the comments below! :point_down: