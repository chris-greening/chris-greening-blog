![GIF showing user clicking an option on AWS RDS database selection screen](https://res.cloudinary.com/practicaldev/image/fetch/s--TcDrRAIR--/c_imagga_scale,f_auto,fl_progressive,h_420,q_66,w_1000/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xk52t1hfhe5wm1dcveyy.gif)
# Deploying a free tier relational database with Amazon RDS
[Link to post on DEV.to](https://dev.to/chrisgreening/deploying-a-free-tier-relational-database-with-amazon-rds-3jd2)

---

Databases can seem _pretty_ scary! :ghost: 
:heart:
But they don't have to be! (_for the most part_)

So let's sit down together and figure out how we can leverage [Amazon Relational Database Service (RDS)](https://aws.amazon.com/rds/) to setup an instance of a remote free tier relational database to tinker with from our local machine.

This blog post is going to be part of a larger series I'm developing on AWS, Python, R, and SQL so keep an eye out for future posts!

#### Table of Contents
* [What is Amazon RDS and why do we use it?](#what-is-amazon-rds-and-why-do-we-use-it)
* [What does the Amazon RDS Free Tier offer?](#what-does-the-amazon-rds-free-tier-offer)
* [Creating an instance of MySQL (full instructions)](#creating-an-instance-of-mysql)
* [Creating an instance of MySQL (tl;dr)](#creating-an-instance-of-mysql-tldr)
* [Connecting to our instance](#connecting-to-our-instance)
* [That's all folks!](#thats-all-folks)
* [Additional resources](#additional-resources)

![GIF of the AWS console and a user clicking the link to RDS](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/mdzoio8c1pvu7je5a8s3.gif)

_:exclamation: IMPORTANT :exclamation:: This tutorial is strictly for practical learning purposes and not an exhaustive guide for setting up a production-ready environment._

_We will work under Amazon's free tier but pay attention to your surroundings as misconfiguration can turn into unintended paid usage at Amazon's pay-as-you-go rates!_ 

_Be sure to monitor your [AWS Cost Management](https://us-east-1.console.aws.amazon.com/cost-management/home?region=us-east-1#/dashboard) and learn [how to control your AWS costs](https://aws.amazon.com/getting-started/hands-on/control-your-costs-free-tier-budgets/) to prevent incurring any unwanted charges!_

---

## What is Amazon RDS and why do we use it? 
<a name="what-is-amazon-rds-and-why-do-we-use-it"></a>

[Amazon RDS](https://aws.amazon.com/rds/) is a collection of managed services offered on AWS for setting up relational databases in the cloud in just a few clicks. 

Remember how I said databases can seem _pretty_ scary? :ghost: 

Migrations, patches, monitoring, backups, physical hardware, scaling, failover, security, storage, etc. 

Lots to keep in mind!  

Wouldn't it be great if there was a [Database-as-a-Service (DBaas)](https://theappsolutions.com/blog/cloud/cloud-service-models/)  that _managed_ all of this tedious work for us and all we had to do was flip a switch and start using a production-ready database in our apps? :bulb:

This is where Amazon RDS shines! And this is why it's become a popular DBaaS. 

With RDS, Amazon takes on the responsibility (_for extra money of course_) of managing the platform our databases are hosted on. All we have to do is provision our database and run with it. 

This frees up our valuable time so we can focus on app development and not on expensive database administration. 

![Diagram showing Amazon RDS managed features such as "security and compliance", "data durability and redundancy", etc.](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/snfdovqnjfu6rzxlkg9x.PNG)

---

## What does the Amazon RDS Free Tier offer?
<a name="what-does-the-amazon-rds-free-tier-offer"></a>

"Did you say free?!"

"Yes, free!" (_at least for a year_ :sweat_smile:)

[Amazon Free Tier](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all) is a collection of AWS' products offered under varying types of limited usage for free. 

In the context of what we're building, the [Amazon RDS Free Tier](https://aws.amazon.com/rds/free/) allows us 1 year of: 
* 750 hours of instance uptime per month (_just enough to run a single DB instance continuously_)
* select instance types (_db.t2.micro, db.t3.micro, db.t4g.micro_)
* select database engines (_MySQL, PostgreSQL, MariaDB_)
* 20 GB of General Purpose (SSD) DB Storage
* 20 GB of backup storage

This free tier should be more than adequate for most of our practice use cases! We can basically run a single instance continuously or multiple instances but with downtime (_as long as the aggregate uptime across your instances is <750 hours per month you're good._)

_:exclamation: IMPORTANT :exclamation:: When the 1 year is up or you exceed free tier usage, you will be charged accordingly at Amazon's pay-as-you-go rates!_

![Explanation from AWS on what is included in the RDS Free Tier](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/nd533dqecqihbqxnrd02.PNG)

---

## Creating an instance of MySQL (full instructions)
<a name="creating-an-instance-of-mysql"></a>

In this section I'm going to detail step-by-step (with pictures/GIFs) how to create our database. If you would rather read the short version... [skip to the next section!](#creating-an-instance-of-mysql-tldr)

For the purpose of this tutorial we're going to create an instance of a [MySQL](https://www.mysql.com/) database for us to connect to remotely via CLI, Python, R, etc. 

Aside from a couple slight tweaks, Amazon's default configurations will suffice for creating our simple database so there isn't much for us to worry about! For the sake of brevity I'm only going to point out the configurations we'll be changing.

Let's get started:

* First navigate to [RDS](https://us-east-1.console.aws.amazon.com/rds/home) on AWS (if you don't already have an account with AWS, check out [this](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/) walkthrough)

### Create database

* Click _Create database_

![User clicking "Create database" on RDS screen](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9hf8sq8m56eul94c6tne.gif)

### Engine options

* Select _MySQL_ 

### Templates

* :exclamation: _IMPORTANT_ :exclamation:: Select _Free tier_. This will give us guardrails on what we can configure.

![User clicking "MySQL" and then scrolling down and clicking "Free tier"](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/dteniykez5oh1f40yavn.gif)

### Settings

* Name your instance, username, and password as you see fit.

### Storage

* :exclamation: _IMPORTANT_ :exclamation:: Deselect _Enable storage autoscaling_!!! Recall from earlier that we only get 20 GB of General Purpose (SSD) DB Storage under the RDS Free Tier - if we approach that limit while practicing we don't want Amazon to automatically scale our storage up as this would bop us out of the free tier.

![User deselecting "Enable storage autoscaling"](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/baijduj4wmloy5i9lb91.gif)

### Connectivity

* Set _Public access_ to _Yes_. This will allow us to remotely access our database. (_side note: this is for setting up a remote database we can connect to from our local machines - for information on private IP, VPC, etc. see [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html)_)
 
* Find _VPC security group_ and select _Create new_. This will assign a [security group](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) to our RDS instance that has an inbound rule that only allows the IP address from which we created the instance to access our database. 

For information on allowing additional IP's, check out this video from the fantastic [Stephane Maarek](https://www.youtube.com/channel/UCGWZY-0pONnKmF98dhZy9CQ): 

{% embed https://www.youtube.com/watch?v=nA3yN76cNxo %} 

![AWS RDS configuration screen with Public access set to yes and a new VPC security group named "sample-security-group"](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/sme44l72oxlb073bk0id.PNG)

### Additional configuration

* :exclamation: _IMPORTANT_ :exclamation:: Deselect _Enable automated backups_!!! Recall from earlier we only get 20 GB of backup storage. Configure this at your own discretion but for now I would recommend just turning this off (_and of course be aware that you now won't have any backups._)

![User deselecting the Enable automated backup option under Additional configuration on the RDS create screen](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/lsc2uah82xvudqeme6qv.gif)

### Create database

* \*drumroll\* :drum: Now let's scroll to the bottom and click _Create database_

![AWS RDS dashboard showing database being created](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/iqn5syzi952t0kn4zdf6.PNG)

Congratulations! :clap: 

We've now successfully created our RDS instance and can start playing around with connecting to our database and using it for learning purposes, simple web apps, non-critical infrastructure, etc.

If you want to get a deeper understanding I highly encourage you to look up what some of those other configurations mean i.e. virtual private clouds, the implications of autoscaling, etc.  

When you're ready to learn about how we can connect to our instance, feel free to [skip to that section!](#connecting-to-our-instance) 

---

## Creating an instance of MySQL (tl;dr)
<a name="creating-an-instance-of-mysql-tldr"></a>

Ah yes, welcome! 

In this section I'm going to quickly detail step-by-step how to create our database. If you would rather read the long version... [skip to the previous section!](#creating-an-instance-of-mysql)

Here's the tl;dr version of setting up the MySQL instance:
1. Navigate to [RDS](https://us-east-1.console.aws.amazon.com/rds/home) on AWS
2. Click _Create database_
3. Select _MySQL_ under _Engine options_
4. :exclamation: _IMPORTANT_ :exclamation:: Select _Free tier_ under _Templates_
5. Under _Settings_ set your instance name, username, and password
6. :exclamation: _IMPORTANT_ :exclamation:: Deselect _Enable storage autoscaling_!!!
7. Set _Public access_ to _Yes_ under _Connectivity_
8. Find _VPC security group_ and select _Create new_ under _Connectivity_
9. :exclamation: _IMPORTANT_ :exclamation:: Deselect _Enable automated backups_ under _Additional configuration_!!!
10. \*drumroll\* :drum: Scroll to the bottom and click _Create database_

Congratulations! Now go to the Winchester, have a nice cold pint, and wait for your database to finish creating.

![Shaun from Shaun of the Dead holding a beer and smiling at the camera](https://media0.giphy.com/media/QsyPRpG6WVR6SYfBVw/giphy.gif)

---

## Connecting to our instance  
<a name="connecting-to-our-instance"></a>

Now that our instance is created, all that's left is to connect to our remote database and start using it! 

To find the relevant endpoint and port for connecting to your instance, click into your newly created instance and take note of the listed endpoint and port under _Connectivity & security_.

![Connectivity and security section of RDS instance showing 
endpoint and port of instance](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/i9ye9b3qbuu9erjjusyd.PNG)

Plug these into the utility of your choice for accessing MySQL and we should be good to go! I'm personally using the [MariaDB CLI](https://mariadb.com/kb/en/mysql-command-line-client/) on Ubuntu.

```bash
$ mysql -h insert-your-database-name.abcdefgh.us-east-1.rds.amazonaws.com  -P 3306 -u admin -p
```

![MySQL client showing the connection to remote database](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4n2nn8uvlni6dhwcdaj3.PNG)

---

## That's all folks!
<a name="thats-all-folks"></a>

Congratulations! 

With this we were able to quickly launch a sample relational database and learn a bit about how we can leverage the cloud to rapidly provision resources just a few clicks away. 

There is a whole world of cloud computing out there just waiting for you to discover and I urge you to go back and explore some of those other configurations we brushed over while creating our instance!

Thanks so much for reading and if you liked my content, be sure to check out some of my other work or connect with me on social media or my [personal website](https://www.christophergreening.com/) :smile: 

Cheers!

_:exclamation: IMPORTANT :exclamation:: Amazon is a business and thus these things will start incurring charges at Amazon's pay-as-you-go rate if you step outside the free tier. If you create any additional instances recall that we only have enough free tier hours for a single instance to be continuously running - make sure you clean up after yourself and delete any extra instances, backups, etc. you're not using or you might incur some charges._  

_I'd also like to remind you to monitor your [AWS Cost Management](https://us-east-1.console.aws.amazon.com/cost-management/home?region=us-east-1#/dashboard) and learn [how to control your AWS costs](https://aws.amazon.com/getting-started/hands-on/control-your-costs-free-tier-budgets/) to prevent incurring any unwanted charges!_

{% embed https://dev.to/chrisgreening/i-built-an-interactive-3d-photo-display-with-javascript-303j %}
{% embed https://twitter.com/ChrisGreening/status/1472670724406005768 %}  

---

## Additional resources
<a name="additional-resources"></a>

* [Understanding Amazon Relational Database Service (Youtube)](https://www.youtube.com/watch?v=eMzCI7S1P9M)
* [AWS Tutorial - Launch a RDS MySQL instance and connect to it using Linux EC2 (Youtube)](https://www.youtube.com/watch?v=xzCgeRxSzy4)
* [AWS RDS – Launching RDS Database Instance for Free](https://www.geeksforgeeks.org/aws-rds-launching-rds-database-instance-for-free/)
* [Amazon RDS Pricing](https://aws.amazon.com/rds/pricing/)
* [AWS EC2 Instance Comparison: T3 vs T3a vs T4g](https://www.learnaws.org/2020/12/19/t3-t3a-t4g/)
* [Overview of Amazon Web Services](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/aws-overview.pdf#introduction)
