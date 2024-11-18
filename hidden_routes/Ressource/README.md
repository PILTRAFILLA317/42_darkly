# HIDDEN ROUTES

Usually one of the first things people do when trying to break into a page is go to the route /robots.txt.</br>

## What is the robots.txt route???

The [robots.txt](#https://en.wikipedia.org/wiki/Robots.txt) file is a filename implemented for the Robots Exclusion Protocol, a standard used by websites to indicate web crawlers and other web robots which parts of the website are they allowed to visit.</br>
That's why its usefull, because it gives you a list of routes.</br>

## Our robots.txt

If you take a look at this page's robots.txt you will find this:</br>
<img src="./imgs/1.png" width=500></br>
You may think that the routes <code>/whatever</code> and <code>.hidden</code> are Disallowed and you cannot enter them. But the Disallow directive is purely advisory, and so are others.</br>
But you might think otherwise if your VM's ports are forwarded, since the URL <code>10.13.8.6:222/whatever</code> or <code>10.13.8.6:222/.hidden</code> redirect you to <code>10.13.8.6/.hidden/</code> and <code>10.13.8/whatever/</code> respectivily, and you wont be able to see the page.</br>


## .hidden directory

If you go to <code>10.13.8.6:2222/.hidden/</code> you will find this:</br>
<img src="./imgs/2.png" width=500></br>
If you move across directories you will end up in a directory that just has a README.md inside and a french phrase.</br>
I made a python script to search each directory for a README.md file and then see if there is a flag inside. If we let it run for a while we will get this result:</br>
<img src="./imgs/3.png" width=800></br>
