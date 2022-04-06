![instascrape logo banner](https://res.cloudinary.com/practicaldev/image/fetch/s--Zua5ht39--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/m2skh86katqgafn3w5f9.png)

# Scrape data from Instagram with instascrape and Python
[Link to the blog post](https://dev.to/chrisgreening/scrape-data-from-instagram-with-instascrape-5e3e)

---

# :question: What the heck is instascrape?
instascrape is a lightweight library designed for scraping data from Instagram using Python! It makes _no_ assumptions about your project and is instead designed for flexibility and productivity so you can get on your way and start exploring Instagram data easily and efficiently. 


Here is a quick glimpse into a scrape that was accomplished using [selenium](https://selenium-python.readthedocs.io/) and instascrape to gather how many likes per post a user got per post in 2020.
![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/viz0cjsfh3tx1ofzzyvm.png)

---

# :floppy_disk: How do I get it?
You can install from [PyPI](https://pypi.org/project/insta-scrape/) with ye old 
```shell
$ pip3 install insta-scrape 
```
or clone from the [official repo](https://github.com/chris-greening/instascrape) with 
```shell
$ git clone https://github.com/chris-greening/instascrape.git
```
The dependencies are light, mostly leveraging [Requests](https://requests.readthedocs.io/en/master/) for requesting the data and [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for parsing it. 

{% github https://github.com/chris-greening/instascrape %}

---

# :computer: Quickstart 
Let's start by scraping some data from a totally random Instagram page that is _definitely_ not mine :wink:
```python
from instascrape import Profile 
profile = Profile('chris_greening')
profile.scrape()
```
And that's it! In those 3 lines, we scraped 52 data points related to @chris_greening's page. We got how many followers, how many posts, whether they have a business profile, whether they're verified, etc. 

Aside from `Profile`, we also have the `Post` and `Hashtag` objects which work with almost the exact same syntax! With methods such 
- `to_dict` 
- `to_json`
- `to_csv`

instascrape integrates nicely with tools like [pandas](https://pandas.pydata.org/) and [matplotlib](https://matplotlib.org/api/pyplot_summary.html) so you can scrape, explore, and analyze your data with just a few lines of code. Integration with [selenium](https://selenium-python.readthedocs.io/) is encouraged so you can get a powerful Instagram scraper going in no time!

We've only just scraped the surface so dig into the [docs](https://pypi.org/project/insta-scrape/) :blue_book: or even better, check out the [source](https://github.com/chris-greening/instascrape) and contribute! Being such a young library (started Hacktoberfest 2020), the sky is the limit and it's only going to get more powerful from here :raised_hands: