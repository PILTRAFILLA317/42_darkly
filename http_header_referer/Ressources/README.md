## HTTP HEADER REFERER

Upon inspecting the footer's "© BornToSec" logo you can go to a secret webpage. The url="http://10.13.8.6:2222/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f"
<img src="./imgs/1.png"></br>
</br>
When you inspect the webpage there is are hidden comments. There is one that says:</br> "You must come from : https://www.nsa.gov/"
<img src="./imgs/2.png"></br>
When you see this the first thing you think of is that there has to be an http header that tells the server where you come from. [Referer Header](#https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer)</br>
This header allows a server to indentify where the user comes from</br>
If you try sending a request with this header the response will have another clue</br>
<img src="./imgs/3.png"></br>
If you go to the bottom of the html there is a comment that gives you a clue about the extra header you need
<img src="./imgs/4.png"></br>
The other header we need is User-Agent, to simulate we are using another browser client which might and is needed for the flag.</br>
The User-Agent is ft_bornToSec, which is the name of this project's name
</br>
<img src="./imgs/5.png"></br>