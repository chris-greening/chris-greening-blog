![GIF scrolling Joe Biden's Instagram page](https://res.cloudinary.com/practicaldev/image/fetch/s--qGMRyeqM--/c_imagga_scale,f_auto,fl_progressive,h_420,q_66,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/wj99ls053d6ox9d9tezu.gif)

# Scraping every post on an Instagram profile with less than 10 lines of Python
[Link to the blog post](https://dev.to/chrisgreening/scraping-every-post-on-an-instagram-profile-with-less-than-10-lines-of-python-1n8b)

---

In this blog post, I'm going to give a quick tutorial on how you can scrape every post on an Instagram profile page using [instascrape](https://github.com/chris-greening/instascrape) with less than 10 lines of Python! 

Specifically, I am going to be scraping every post from Joe Biden's Instagram account ([@joebiden](https://www.instagram.com/joebiden/?hl=en))

{% github chris-greening/instascrape %}

# Prerequisites for those of you following along at home
- an Instagram account  
- [selenium](https://selenium-python.readthedocs.io/)
- [instascrape>=2.0.0](https://github.com/chris-greening/instascrape/releases/tag/v2.0.0)

# Importing from our libraries 

Let's start by importing the tools we'll be using.

```python
from selenium.webdriver import Chrome 
from instascrape import Profile, scrape_posts
```

# Preparing the profile for scraping

As I've mentioned in previous blog posts, Instagram serves most content asynchronously using JavaScript allowing for the seamless infinite scroll effect and decreased load times. 

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/s166cn48bt1441mxlkbe.gif)

To render JavaScript, this is where our webdriver comes in handy. For this tutorial, I will be using [chromedriver](https://chromedriver.chromium.org/) to automate Google Chrome as my browser but feel free to use whatever webdriver you are comfortable with!  

```python 
webdriver = Chrome("path/to/chromedriver.exe")
```

Now a quick aside before we start with this next part; you are going to have to find your Instagram sessionid \*gasp\* Don't worry! Here is a [super short guide](http://valvepress.com/how-to-get-instagram-session-cookie/). Be sure to paste it below in the `headers` dictionary where indicated. 

```python
headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57",
    "cookie": "sessionid=PASTE_YOUR_SESSIONID_HERE;"
}
joe = Profile("joebiden")
joe.scrape(headers=headers)
```

# Dynamically loading all posts 

And now for the part you've all been waiting for! Using the `Profile.get_posts` instance method, there are a variety of arguments we can pass for painlessly loading all the posts on a page. 

In this case, we are going to have to manually login to our Instagram account when the browser opens so we pass `login_first=True`. This will give us 60 seconds to enter our username and password (this wait time can be modified to whatever you want)

```python
posts = joe.get_posts(webdriver=webdriver, login_first=True)
```

Now, to prove to you that it worked, here is a GIF of me scrolling through the scraped URLs of all 1,261 posts :smirk: 

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/kkxgsml7xatpjujza8wq.gif)

# Scraping the data from each post 

Now there is only one thing left to do, and that is scrape every individual post. The `scrape_posts` function takes a variety of arguments that let you configure your scrape however you want! 

The most important argument in this case is `posts` which is a `list` of unscraped `instascrape.Post` objects. 

In this case, I'm going to set a pause of 10 seconds between each scrape so that Instagram doesn't temporarily IP block us. 

```python
scraped_posts, unscraped_posts = scrape_posts(posts, headers=headers, pause=10, silent=False)
```

In the event that there is a problem, we are able to configure `scrape_posts` such that all posts that were not scraped are returned so we don't lose all of the work we did, hence the `unscraped`. 

# In conclusion 
And there we have it! In less than 10 lines of Python, we were able to scrape almost 50,000 data points from @joebiden's Instagram account! 

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/2wfu0doof41pae8avim3.png)

We can now analyze his engagement, how many hashtags he uses, who he tags in photos, etc. In my next blog post, I'll be showing some ways we can analyze this data and glean useful insights! 

In the meantime, here is a related article where I analyze 10,000 data points scraped from Donald Trump's Instagram account. 

{% link https://dev.to/chrisgreening/visualizing-donald-trump-s-instagram-data-with-python-1f01 %}

Click [here](https://github.com/chris-greening/instascrape/tree/master/tutorial/examples/JoeBiden) for the full code, dataset, and file containing all the URLs used in this tutorial. 

If you have any questions, feel free to drop them in the comments below, message me, or email me at chris@christophergreening.com!

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/fxi3v27am3jm2xihyp3j.png)