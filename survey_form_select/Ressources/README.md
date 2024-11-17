## SURVEY FORM SELECT

On top of this website we have a <code><nav></code> that contains various elements.</br>
<img src="./imgs/1.png"></br>
If we click the <i>SURVEY</i> text we will end up in another route.</br> 
<img src="./imgs/2.png"></br></br>

The first time you see that there is clearly something off. This <i>wil</i> dude has 4256, <i>Ben</i> has 666 votes and <i>ol</i> has 69, nice, while the rest do not have scores near those.</br>
Even weirder, this <i>wil</i> dude has an average of 4218.19 while the rest's average is less than 10, makes since since the biggest grade you can submit is 10 and how the average is calculated.</br></br>

# Voting Multiple Times

There is no limit in how many times someone visiting the webpage can vote, so anyone can artificially inflate their score.</br>
That's how everyone besides <i>Thor</i> and <i>alex</i> has more than 20 votes.</br>
But there is still one question to ask. What about <i>wil</i>?</br></br>

# Submitting a bigger score

<i>wil</i>'s score shouldn't be obtainable, but he clearly has it, so how can this be. If we were to inspect element we could easily how he achieved this:</br>
<img src="./imgs/3.png"></br></br>
The value submitted can be changed in the <code>html</code> code so values bigger than 10 can be uploaded and the server's endpoint doesn't seem to care about the score being sent so that's how you can have an average bigger than 10.</br>
