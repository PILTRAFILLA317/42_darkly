## PATH TRAVERSAL

When you use the query page=whatever (http://10.13.8.6/?page=whatever) you get an alert saying "Wtf ?"</br>
Once you get this information you can guess that what is going on is that the page being shown in page the file thats in the path written in the "whatever" part</br>
<img src="./imgs/1.png" width="800"></br>
Once you realize this you can start playing with the route. My first tought was to try an look for the passwd file, which is a file in which information about users that have logged in it is stored.</br>
This file is located at "/etc/passwd".</br>
And php files are usually located at "/var/www/html/(public)/(whatever)/(...)
<a href="https://www.reddit.com/r/webdev/comments/knbdol/where_should_indexphp_and_other_php_files_be/"><img src="./imgs/reddit.png" width="700"></a></br>
With this information I started trying to access /etc/passwd with URI's like:</br>
http://10.13.8.6/?page=../../../etc/passwd</br>
with that exact prompt you get a different alert message, which is a clue that we are heading in the right direction.</br>
<img src="./imgs/2.png" width="500"></br>
As you keep digging further down you start getting different alert messages</br>
<img src="./imgs/3.png" width="500"></br>
That keeps happening until you reach:  http://10.13.8.6:2222/?page=../../../../../../../etc/passwd and you finally get the flag :)</br>
<img src="./imgs/4.png" width="800"></br>

