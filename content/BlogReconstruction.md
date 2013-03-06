Title: Blog Reconstruction
Date: 2012-12-03
Tags: old, migrated
Category: Blog
Summary: Rebuilding my site and how I got hacked

  
# So what happened... #
On December 3, 2012 I encountered a very peculiar surprise. After sending off some co-op
applications for next summer I decided to double check and update my LinkedIn 
profile and website and found a interesting surprise. My website had been a victim of some 
script kiddie.
  
The front page had been switched with this message: <code>Hacked By Newbie_043</code>
  

And well I wasn't very happy about that...
  
What seems to have happened is that I had neglected my old wordpress blog and 
someone used known vunerabilities to change the main page into this other page.
  

After a frantic search through the server, nothing else had been changed so decided
to recover all the files and nuke the server just to be sure.
  
I got a new VM from the hosting provider and decided to take my time and
be more professional about this site and hey why not learn something new in the
mean time.
  
After doing some research there was an interesting minimalistic Javascript framework 
called [Bootstrap](http://twitter.github.com/bootstrap/). This seemed simple 
enough for what I wanted and included some nice features for dealing with 
phones and tablets via the use of fluid layouts and HTML5 features.

# So the rebuilding begins #
  
Since I was a bit angry and frustrated that the old blog had been defaced because
of my own negligence, I decided to start the rebuild inmediately. So off I was 
learning how this Bootstrap framework is supposed to work and I spin off a nice
sidebar / content layout similar to what you see here now. Nice and simple.
  
But there was a lot of duplicate code, specially when I wanted to go ahead and try
to add another page aditional to the two I had: Home and About Me. So after 1 hour of work
I decided to just script the basic parts of the site.

# Python to the Rescue #
  
So one hour learning a new JS framework after not reading or writting JS for a while
seemed good so around 11pm I decided to go ahead and work on scripting the basic 
parts of the site. These where the features that were going to be built into the site: 

+   Each page would consist of the basic sidebar/main content layout
+   Python would parse Markdown files with the content to each page
  

I had almost forgotten how easy it is to use python and in no time I had 
everything scripted. Using a python Markdown-HTML converter most of the bulk was
taken care of. The rest was simple scripting.
  
In the end 4 hours of work turned into what I have right now. Something simple to use and
to write thing to. Next up I need to work on a way to handle multiple posts and how to show
only the latests ones on the main page. Hey maybe if I feel the code is useful enough for 
other I might even open-source what I have here.
-----------------------------------------------------------------------------------------

*[JS]: Javascript