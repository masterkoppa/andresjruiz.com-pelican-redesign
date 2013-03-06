Title: Theming Pelican with a little Boostrap
Date: 2013-03-03
Tags: Python, Pelican, Jinja2
Category: Projects
Summary: Building a Boostrap Based Theme for Pelican

With the work of rebuilding the site and learning the ropes around Pelican it was
necessary to give the site a unique look and feel. I go into detail of the initial stages
of development [here](|filename|/BlogReconstruction4.md).

# Thememing Pelican Basics #

Pelican makes if very clear from the start that making your own themes is easy enough. Pelican
uses the [Jinja2](http://jinja.pocoo.org/) template engine for all its rendering. Separating 
your data from the look and feel of your data.
  
Pelican offers two themes by default:
  
*     simple
*     notmyidea
  
I personally find both of them to be lackluster and ugly. Here is where Pelican shines,
there is a small repository on github that provides additional themes, 
[Pelican Theme Repository](https://github.com/getpelican/pelican-themes).
  
Both the default included themes and the theme repository proved invaluable to developing
a new theme for pelican. If I had to complain about any part of the exelent documentation 
it would be the lack of documentation for theme creation. A lot of the time it was guess work,
thankfully the themes available had done most of the guess work for me.
  
While you can use a million files to describe your theme, only the following files are
actually required by Pelican to be considered a Theme:
<!-- Hard-Coded in since MD didn't want to play fair -->
<div class="highlight-python"><pre>
├── static
│   ├── css
│   └── images
└── templates
    ├── archives.html    // to display archives
    ├── article.html     // processed for each article
    ├── author.html      // processed for each author
    ├── authors.html     // must list all the authors
    ├── categories.html  // must list all the categories
    ├── category.html    // processed for each category
    ├── index.html       // the index. List all the articles
    ├── page.html        // processed for each page
    ├── tag.html         // processed for each tag
    └── tags.html        // must list all the tags. Can be a tag cloud.</pre>
</div>
<small>Information taken from the 
[Official Pelican Documentation](https://pelican.readthedocs.org/en/3.1.1/themes.html), please
check there for the latests information.
</small>

# Jinja2 Templating Basics #

[Jinja2](http://jinja.pocoo.org/) is a very powerfull template engine. Like most template 
engines it provides both control structures and some flexible logic. While its not the same
as having actual Python code behind the scenes, it works great.
  
For example, the following code allows me to dynamically add categories to the menu bar on
the top of the website.
  
       
       {% for cat, null in categories %}
           <li {% if cat == category %}class="active"{% endif %}>
               <a href="{{ SITEURL }}/{{ cat.url }}">
               <i class="icon-folder-open icon-large"></i> {{ cat }}</a>
           </li>
           <li class="divider-vertical"></li>
       {% endfor %}
  
As you can see the syntax is simple to understand. There is a loop iterating through a list 
of categories. The second element is discarded and the first element is used to generate the 
information for the list item. As per boostrap convetions each element at a navigation bar
is a list item in a unordered list.
  
Most of the information dynamically put into pages is done in the same way, a for loop through
a list. Take the information from that and spit it into the page.

# Using Bootstrap and Jinja2 #

After looking over some examples and understanding the basics of templating the next step was
to integrate the [Bootstrap](http://twitter.github.com/bootstrap/) framework to make the page
seem more modern and usable, not to mention visually apealing.
  
Like many programming languages, the Jinja2 template language allows for extending other elements
or templates. This allows us to have a "Main" template that contains the general structure and
look that we want to achieve. In our case that "Main" template is called 
[base.html](https://github.com/masterkoppa/Pelican-Themes/blob/master/bootstraped/templates/base.html).
  
While the whole file looks a bit daunting there is nothing really special about it. At the very
top you can see the basic header information for HTML. Here the bootstrap CSS and JS are included
since all the templates in the theme extend this "Main" template they will already have Bootstrap
set-up.
  
Ok, first step is done. I have Bootstrap on every page, but that's a bit useless. Here on the 
body page the ground work is layed out to give the whole site a consistent look and feel. In
the body the main top navigation bar is included and generated dynamically based on the site 
name and the available categories.

		<a class="brand" href="{{ SITEURL }}/index.html">
			{{ SITENAME }} 
			{% if SITESUBTITLE %} 
				<small>{{ SITESUBTITLE }}</small>
			{% endif %}
		</a>
		<div class="nav-collapse collapse navbar-responsive-collapse">
			<ul class="nav">
			{% if DISPLAY_PAGES_ON_MENU %}
			{% for page in PAGES %}
				<li>
					<a href="{{ SITEURL }}/{{ page.url }}">
						{{ page.title }}
					</a>
				</li>
				<li class="divider-vertical"></li>
			{% endfor %}
			{% endif %}
			{% for cat, null in categories %}
				<li {% if cat == category %}class="active"{% endif %}>
					<a href="{{ SITEURL }}/{{ cat.url }}">
						<i class="icon-folder-open icon-large"></i> 
						{{ cat }}
					</a>
				</li>
				<li class="divider-vertical"></li>
			{% endfor %}
			{% for title, link in MENUITEMS %}
				<li {% if title == active_page %}class="active"{% endif %}>
					<a href="{{ SITEURL }}/{{ link }}">
						<i class="icon-user"></i> 
						{{ title }}
					</a>
				</li>
				<li class="divider-vertical"></li>
			{% endfor %}
			<li {% if archive_on %}class="active"{% endif %}>
				<a href="{{ SITEURL }}/archives.html">
					<i class="icon-th-list"></i> 
					Archives
				</a>
			</li>
			</ul>
		</div>

As mentioned before, most of the logic will look like this. The thing to note here
is how the variables are being used to interact with the Bootstrap framework and
how the responsive navigation bar is being set up. The sidebar seen next to every blog post is also done in a similar way and will come from 
the base template.
  
The content for each page is done in a different manner. In the base template we include a
empty block called content.
  
		<div class="container-fluid" id="content">
			<div class="row-fluid">
				<div class="span1"></div>
				<div class="span10">
					<div class="row">
						<div class="offset1 span8">
							{% block content %}
							{% endblock content %}
						</div>
						<div class="span3">
							{% include 'sidebar.html' %}
						</div>
					</div>
				</div>
				<div class="span1"></div>
			</div>
		</div>
  
This block will latter be filled up with the content we would like to display. Another 
nice trick worth pointing out is the include statement. This allows me to arbitrarely insert
another template into the section specified. This is great for organizational reasons. The 
sidebar logic can get a little messy at times and it's great to separate all the logic into 
a separate file instead of complicating the base template.
  
Here you can also see how bootstrap and Jinja2 interact with each other. The layout is being
set-up while the information will be filled in latter at compile-time.

## Using the Base Template ##

Now that a good foundation has been layed out, the rest of the template is easy. For example,
this is how the Article template looks like.
  
First we declare that we extend the base template like this
  
		{% extends "base.html" %}
  
Then we declare the content block*
  
		{% block content %}
		<section id="content">
		<article>
			<header>
				<h1>
					<a href="{{ pagename }}">
						{{ article.title}}
					</a>
				</h1>
			</header>
			{{ article.content }}
		</article>
		</section>
		{% endblock %}
  
<small>* Some code has been removed for ease of reading</small>
  
This information then gets inserted into the content block and the result is this page that
you are reading.

# Final Thoughts and More Information #

With these basics in mind creating a Theme for Pelican is extremely easy and in retrospect
a lot easier than what I expected. A little bit of documentation would go a long way, then
again Pelican is an Open-Source project. Maybe on my spare time I'll help the project out
by including more documentation. But for now, this is a great primer on how to work with themes
both for personal use in the future as well as for whomever stumbles upon this site.
  
If you have any questions or want any more help with creating a Theme for pelican drop a comment
bellow and I will try to respond back.
  
Thanks for Reading!
  
The code for the Template I created is available [here](https://github.com/masterkoppa/Pelican-Themes/tree/master/bootstraped).