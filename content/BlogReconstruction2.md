Title: Blog Reconstruction, Part 2
Date: 2012-12-06
Tags: old, migrated
Category: Blog
Summary: Rebuilding my site and using python


So here we are only 3 days latter and already this page is starting to both bite back at me
and start to look quite nicely.  
  
Over the past couple days I have learned some hard lesons about web development...  
  
  
*Its not easy!*  
  
  
Ok, that might seem more obvious than I seemed to think. But the internet has 
evolved quite a bit since I last worked on a web page. To date this must be *the*
largest HTML/JS project I've ever worked on. But regardless everything is 
moving smoothly.  
  
Nothing has changed too much from last time. I have 3 kinds of pages now instead of 1.
  
*    Normal Pages
*    Extra Pages
*    Blog Posts

## Normal Pages ##
These are the original pages that are created with the left hand sidebar for navigation and
the associated templates for making it look good with the help of Bootstrap.

## Extra Pages ##
These are pages written in markdown that when generated have nothing added to them. 
These pages are then embedded via jQuery to some components. An example of these pages 
in use is the About Me page. In this page the information about my experience with each
programming language is taken from separate HTML pages and loaded into the popups 
via jQuery.  
  
These pages are useful to combat the lack of being able to link multiple 
markdown documents together before turning them into HTML. Simply having all 
that information would have defeated the purpose of using markdown in the first place. The
markdown files have to be readable easily. If the end up a huge mess then... well 
they're not very readable.

## Blog Posts ##
These are similar to extra pages in that they are rendered in the exact same way. The 
only reason why I differentiate them is that they are displayed in a special way. The home
page became a special page that just contains the introduction to the page.
  
So how are you able to read anything from the home page anyways?
  
  
Well jQuery comes back again to help. To make sure only the lattest posts are shown
I deviesed a script that will load all the posts but only show the lattest ones. With the 
help of bootstrap and its nice looking pagination icons. I show and hide each post 
based on the page selection.  
  
While this is a nice trick the more posts I have here the worse performance will get. But
in the mean time this will be the solution while I come up with a more elegant one that 
will also allow me to link back to the posts themselves.

# So how am I keeping track of all this information? #
Well some people will cringe at the thought of reading the following line:
*TEXT FILES*
  
  
Yeah I know, its bad... But at this point my goal was to go databaseless and so far 
the structure of how I store each page, the markdown source and the destination has not
fired back yet. But a future goal would be to make sure to keep track of things in 
some sort of database. Even something as simple as a LightSQL database that is used for 
creation time things would help. But at this point this is not a priority.
  
I really hope my Software Engineering professors don't see those past lines... Otherwise,
they might think they've failed me for making that decision. In my defense it was 2am when
I started...
<div>
<small>P.S. I really need a spellchecker for this</small>
</div>
------------------------------------------------------------------------------------------