## Step 1 - Updated Use BeautifulSoup to scrape the product price
Use BeautifulSoup on the Practice Page
Live websites change A LOT. Let's get the first version of our project working on a clone of Amazon's page before we move onto the real thing. Take a look at: https://appbrewery.github.io/instant_pot/
1.  Use BeautifulSoup to get hold of the price of the item as a floating point number and print it out. 

## Step 2 - Email alert when the price is below preset value
Send an email if the price is below your target
We want to get an email when the price of our product is below a certain value. e.g in the case of the Instant Pot, we'll set the target price as $100.
When the price is below 100 then use the smtp module to send an email to yourself. In the email, include the title of the product, the current price and a link to buy the product.
On our static page, the price is set for $99.99 so you can test the email functionality by setting your target price to $100 or higher.



SOLUTION 2
Hide your email and password in a .env file
We've already covered environment variables. It's good practice to hide sensitive information like passwords, email addresses and API keys. A good way to hide your information is by keeping it separate from the source code in your .py files.
1. Create a .env file.
2.  Your .env file should consist of key value pairs where you store your personal information. It should look something like this.
SMTP_ADDRESS="smtp.gmail.com"
EMAIL_ADDRESS="angela@email.com"
EMAIL_PASSWORD="Use_an_App_Password_from_your_email_provider"
3. In your main.py file use the os and dotenv modules to remove your personal information from the .py file.
The dotenv documentation shows how to go about it: https://pypi.org/project/python-dotenv/

SOLUTION 3
SMTP Server Disconnected Error?
NOTE: If you have issues and keep getting this error:
1. Make sure you've got the correct smtp address for your email provider:
Gmail: smtp.gmail.com
Hotmail: smtp.live.com
Outlook: outlook.office365.com
Yahoo: smtp.mail.yahoo.com
If you use another email provider, just Google for your email provider e.g. "Gmail SMTP address"

Below are steps specific to users sending email from Gmail and Yahoo addresses.
2. Turn on 2-Step Verification for your email under the Security settings for your account. For example, Manage Your Google Account -> Security.
3. Add an App Password under your email settings. Select "Other" from the drop-down settings and choose a password. Use this app password in your Python code.
4. Add a port number by changing your code to this: smtplib.SMTP("smtp.gmail.com", port=587)


## Step 3 - Add headers to your request
What is a Header?
When making a request to Amazon or any website, your browser will send some additional data along with the request. Typically this will be information regarding what browser you are using, what computer you have, and what your preferred language is. This information is included in the headers. By using the headers, Amazon's server can respond with the right website for your region and your language.

1. See the headers that your own browser is sending by going to this website: http://myhttpheader.com/
Try different browsers (e.g., Chrome, Brave, Firefox, Safari) and see how the headers change. 
There you can see my language settings and that I used a Mac computer to make the request.
Add the headers to your code
Why would you want to do this?
If you pass some headers along then Amazon's servers can give you the instant pot page in your language and also in your currency.
Also, it will make your request look (slightly) more human and less like a bot. Why? Headers include data that is sent over by a browser rather than a script. And many web servers like Amazon's may block requests they think originate from bots.

At the moment we are making a request without adding any headers:
response = requests.get("https://www.udemy.com/")

Here's how you can pass some headers alongside your requests: 
response = requests.get("https://www.udemy.com/", headers={"Accept-Language":"en-US"})
Here is more detailed information on how you pass headers with the requests library:
### https://stackoverflow.com/questions/6260457/using-headers-with-the-python-requests-librarys-get-method


2. Add some headers to your request in the main.py. At minimum add the User-Agent and Accept-Language. At most copy the full header from https://httpbin.org/headers (excluding the host and X-Amzn-Trace-id)
