## Fork considerations

I couldn't manage to run it entirely once Instagram servers' were always blocking me with 429 even using some VPNs.

I added a `docker-compose.yml` with a Selenium container so it can be run using only a CLI, although you can see the browser running it through `http://localhost:4444/ui/`. I used [Gitpod](https://gitpod.io/#/github.com/patrickkmatias/instagram-auto-create-account) to modify, so do I suggest you to use it.

I wonder that domains used by email-fake.com are all blocked by Instagram's server (with a fast server-side verification, making it return 429), but this could only be assured testing.

If you'd like to contribute fixing it, you're welcome.

Run with `python app.py`.

## Instagram Automatic Account Creator Bot

<p>This small piece of code will create an account automatically by randomizing names. You need Selenium library installed. This is an ongoing work. Beware that Instagram has security measures to prevent bot usage. Do not forget to change the Web driver you use from the part of the code in botAccountCreate.py :</p>

```Python
33 browser = webdriver.Chrome("your chrome driver path here")
```
Also, you can use other browsers with tweaking the code.
```Python
#Another browser
26 browser = webdriver.Firefox("your firefox driver path here")
```
<h2>Requirements</h2>
<p> run
<code>
  pip install -r requirements.txt
</code> 
</p>

<h2>New features</h2>

<ul>
  <li>Fake email address</li>
  <li>Getting verification code</li>
</ul> 


<h2>Thank you very much for your support</h2>

<a href='https://github.com/BbChip0103'>BbChip0103</a> <br/>
<a href='https://github.com/haniyadav'>haniyadav</a><br/>
<a href='https://github.com/Gupta-Anubhav12'>Gupta-Anubhav12</a><br/>
<a href='https://github.com/Mxhmovd'>Mxhmovd</a><br/>
<a href='https://github.com/ManWuzi'>ManWuzi</a><br/>
<a href='https://github.com/mikegrep'>mikegrep</a><br/>
<a href='https://github.com/NoNameoN-A'>Alessandro</a><br/>

