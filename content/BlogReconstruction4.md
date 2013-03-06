Title: Blog Reconstruction, Part 4
Date: 2013-03-02
Tags: NewBegginings, Pelican
Category: Blog
Summary: Applying Bootstrap and Making The Site Pretty Again

Finally, the site is halfway there. After all the previously mentioned research
and problems I can finally say the site looks halfway decent, while still being
resonably maintainable.

# Making Pelican Beautiful #

While [Pelican](http://blog.getpelican.com/) is a great tool, the default theme is 
somewhat unappealing. Thankfully it provides theming capabilities through the
[Jinja2](http://jinja.pocoo.org/) template engine. Its been a while since I had
done any template work so I figured to start with a base and work from there.

## My Love for Bootstrap ##
After having worked with Bootstrap for the previous iteration and for the
[American Greetings](http://hack.ag.com/teams/large-hadron-collider) 
[Hack-Day](https://github.com/masterkoppa/ag-hack_day) it was obvious that 
I would want to include this amazing tool into the website. Thankfully someone
 with the experience in using Jinja2 and Bootstrap had done my job for me. There are
2 Bootstrap based themes on the [Pelican Theme Repository](https://github.com/getpelican/pelican-themes).
This page uses bootstrap2 as a base. 
  

The repository is a great resource to see what is posible to do
with Pelican and Jinja2.

# [Bootstrap2](https://github.com/getpelican/pelican-themes/tree/master/bootstrap2) Theme Features #

[Bootstrap2](https://github.com/getpelican/pelican-themes/tree/master/bootstrap2) utilizes the basic twitter
bootstrap libraries and complements them with the use of [Font-Awesome](http://fortawesome.github.com/Font-Awesome/).
The template also features all the Pelican features present in the default theme with added support for
tag clouds and translations.
  
This theme also added comments to each article via the use of Disqus. Setting this feature up 
was relatively easy to do and adds a great deal to the site. It also free's me of any credential
management and allows for a centralized place for managing discussions without building it from scratch.

# Caveats of Bootstrap2 #
While its a great theme, it felt like a very generic Bootstrap theme, then again aren't most pages
built with bootstrap like that? So just like the last time, the site is themed using the 
[Simplex](http://bootswatch.com/simplex) bootstrap theme. There are many more themes available at 
[bootswatch](http://bootswatch.com/). This is a great resource to make any bootstrap site look
unique and not like every other site out there.
  
Now... The site no longer looks like crap and is no longer generic. What's next?
  
The theme was modified futher through editing the template files directly. For example by default
on the index page only the summary is shown and a button is offered to expand the blog further. This made
the front page feel empty. Instead I opted to show the whole post on the fron page. If you click
on the post title you are shown the discussions.
  
Another modification was the addition of my own personal gravatar. This was both a test of how to play with 
templates and how to use the available plugins. Sadly I ended up hard-coding the gravatar URL to the template.
Now in each article a picture of the author, ME, is on the top right of the article. That might dissapear in 
the future, but for now its a great learning tool.
  
There were also some minor fixes with things on the template but overall those were the two major changes
necessary to get where the site is now.

# Future #
While I'm OK with the site, I'm not perfectly happy with it. The next step is to start with a new theme
from scratch and learn the ropes of theming and integrating Bootstrap into the mix. Hopefully by the end
the site will both feel unique and profesional. After all this page represents my professional achievements
and skills.

After the codebase is clean and the new Theme is done, I will be submitting the source code for the page
into github to share with the world.