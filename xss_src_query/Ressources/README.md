## XSS SRC QUERY

Whenever you inspect the image of the nsa you can see that it has an anchor (\<a>) tag</br>
<img src="./imgs/1.png" width="500"></br></br>
If we click on the anchor we get sent to the ?page=media page and we can see that the image is searched via Query.</br>
<img src="./imgs/2.png" width="500"></br></br>
Having the image being searched via Query is a security risk, if it isn't well sanitized malicious code could be sent there.</br>
If we inspect element we can see that the image being loaded is loaded into a object html tag.</br>
<img src="./imgs/3.png" width="500"></br></br>
This is helpful, we can see where the <i>src</i> is being loaded, so we can prepare code for that.</br>
To test this we could try sending some <code>js</code> code. The code has to be sent in the src parameter. We are gonna send this:</br>
<code>"data:text/html;base64,PHNjcmlwdD5hbGVydCgnVGhpcyBpcyBhbiBhZG1pbmlzdHJhdGlvbiBzY3JpcHQnKTwvc2NyaXB0Pg=="</code></br>
Which is:</br>
<code>\<script>alert('This is an administration script')\</script></code></br>
If we try to load that code in the <code>object</code> html tag we can see that it works.</br>
<img src="./imgs/4.png" width="500"></br></br>
So if we send that code in the src query part we will get the flag:
<img src="./imgs/5.png" width="700"></br></br>

