Title: Blog Reconstruction, Part 3
Date: 2013-03-01
Tags: NewBegginings, Pelican, Python
Category: Blog
Summary: Rebuilding my site and Learning from my mistakes

After letting the site sit for a while I came to the realization that while nice, 
the site was completely unmantainable. So I decided to set out to rebuild it. This time
using proper frameworks.
  
  
#Research#

At first it was clear that the language of choice would have been either python or
ruby for this website. After some research I found [Tornado](http://www.tornadoweb.org/)
and [Pyramid](http://www.plylonsproject.org). These are mature frameworks and python stacks
for serving web pages.


##A turn for the unexpected##

After settling to start researching these frameworks I stumbled upon a small project called 
[Pelican](http://blog.getpelican.com/).
The aim of this project seemed very similar to what I wanted to do originally, build static pages
using python tools. This also made me realize how much of an overkill Pyramid or 
Tornado would have been.


#How Pelican Works#

For those of you that don't know what Pelican is, Pelican is a python tool that allows
you to generate static html pages using reStructuredText or Markdown.
  
It has a nice syntax for adding properties to each page or blog post that you have. It also 
leverages the powerfull [Jinja2](http://jinja.pocoo.org/) template engine. With these things
in mind I decided to rebuild the site, yet again, using Pelican. The result is what you see
here. A beatifull and fully functioning page that also serves as a blog to document
my misadventures in the world of programming.
  
I will be releasing my old code on github soon and explain how to go from the generic default
theme to something more unique.