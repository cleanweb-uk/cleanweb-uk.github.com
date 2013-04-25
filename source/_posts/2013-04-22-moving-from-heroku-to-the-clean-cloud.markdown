---
layout: post
title: "Moving from Heroku to the clean cloud"
date: 2013-04-21 16:31
comments: true
categories: cloud
author: Jason Neylon
---
Recently I have been building a new website for [Repowering](http://www.repowering.org.uk) - a co-operative focused on radically increasing the number of renewable energy projects in London. Last weekend I migrated the website from [Heroku](http://www.heroku.com) to [GreenQloud](http://www.greenqloud.com).

Whats wrong with Heroku?
========================

When I started building the new Repowering website I initially hosted it on Heroku. I am a big Heroku fan. It makes it super easy to get a Ruby website on the web. However there is a downside to Heroku - it runs on top of Amazon's EC2 cloud computing platform which means it is <strong>powered by dirty CO<sub>2</sub> spurting coal power plants</strong> (check out [MastondonC's dashboard of cloud provider CO<sub>2</sub> emissions](https://www.mastodonc.com/dashboard) to see for yourself). One of Repowering's aims is to reduce carbon emissions, so having a website that produced unnecessary emissions was a big no no. 

Moving to Greenqloud
====================

<div style="margin: 0px 15px; margin-bottom:10px; float: right"><img src="/images/posts/greenqloud-logo-small.png" alt="Greenqloud logo"></div>

There is a greener solution - the Icelandic company Greenqloud offer cloud hosting based in Iceland. As Iceland's electricity system runs on geothermal and hydro power the server emissions are as close to zero carbon as you can get. Cost wise it's comparable too. While Heroku is free for a single dyno, costs escalate rapidly as you start adding workers and features such as SSL. 

Setting up the Virtual Machine for Rails
========================================

<img src="/images/posts/greenqloud-dashboard.png" alt="Greenqloud dashboard">

Greenqloud has an easy to use interface. It's a few clicks to setup a new box and you get a browser based VNC client to do your initial configuration. Unlike Heroku however you need to setup the platform yourself. For something like Wordpress this is [quick and easy](http://support.greenqloud.com/entries/22163871-Getting-started-with-GreenQloud-Part-1), but for the Ruby on Rails application its a bit more involved. I spent 2 or 3 hours installing Ruby, Mongo, Redis, Nginx and configuring Unicorn and SSH. 

I followed these guides setting up the server:

* [How To Easily Build a Fast, Reliable Production Rails 3.2 Web Server with Ubuntu 12.10 / Nginx / Passenger](http://ghosttx.com/2013/02/fast-reliable-production-rails-3-web-server-on-ubuntu-nginx-passenger/)
* [Setting up Unicorn with Nginx](http://sirupsen.com/setting-up-unicorn-with-nginx/)
* [Quick tips on security](http://greenqloud.com/quick-tips-on-security/)

If you are a devops wizard you could use Chef or Puppet to do automate this. The other task you need to handle yourself is backup. I knocked together a little script based on [this to handle backups](https://github.com/billturner/simple-s3-backup). 

Towards a cleaner cloud
=======================

From a price and time perspective it hasn't cost me much to move to a low carbon hosting platform. Its an easy way to reduce your client's or organisation's carbon emissions. To realise cloud computing's green potential we need to make cloud computing low carbon by default. Here are some ways cloud infrastructure can become greener:

* Amazon EC2 could start running their infrastructure on low carbon electricity. Apple, Google, Microsoft and Facebook have recently started to move in this direction.
* Services such as Heroku could have more flexibility over where your applications run
* More Infrastructure as a Service (IaaS) provider need to support green cloud providers
