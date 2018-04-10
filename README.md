# Customize a scheduled email report
### A python template to help you get a custom email report up and running.

The repository is set up in a modular fashion so you can easily substitute in your own email address and report contents. I have personally found this to be a fun use for custom web scrapers that grab information off the internet and add it to my report.

## What is in the repository?
`email_me.py` - This is the executable file that will initiate the message composition and send the email.

`message` folder:
- `compose_message.py`- This file calls the message modules and composes the text of the message.
- `game_scores.py`	- Example module: this is a web scraper module. It acquires baseball scores from games played last night. [Look here for more info on the contents.](https://camnugent.wordpress.com/2017/08/09/139/)
- `countdowns.py` 	- Example module: this is a series of simple countdowns. [Look here for more info on the contents.](https://camnugent.wordpress.com/2017/10/29/ttib-a-set-of-countdowns-using-python-datetime-morning-report-pt-4/)


## How do I make it work?
To get the report up and running there are a few steps you need to follow:
### 1. You need an email account to send the email report from
- I recommend signing up for a new gmail account for this purpose. You must allow unsecure access on the account (a no no for your main email!)
- After you get a new gmail, go to the 'sign in and security' page and toggle the 'allow less secure apps' option to ON. This lets the python script send an email through the account.
### 2. Open `email_me.py`
- On line 11 put change the string to the email address you will be sending FROM.
- On line 12 put the password for the sending email address.
- On line 13 put the email address you are sending the message TO.
NOTE: If you didn't use gmail, you must change the server name on line 33 to match your email host. Just google 'hostname smtp server' and you can figure this out easily.
### 3. Figure out what you want in your report!
- Write some modules to scrape data from the web, provide you with links to interesting news articles, or whatever else you would like!
- Write the code in functions so that they can be imported into the `compose_message.py` file and run automatically.
- When you write these modules, place them in the `message` folder.
- I have included two example modules for inspiration. Information on what they do can be found in posts [here](https://camnugent.wordpress.com/2017/08/09/139/) and [here](https://camnugent.wordpress.com/2017/10/29/ttib-a-set-of-countdowns-using-python-datetime-morning-report-pt-4/)
### 4. Link the report functions to the `compose_message.py` file
- This file is called to build the body of the message for the email. It imports the other modules in the message folder and calls the needed functions.
- There are annotations within the file to help you import and run your custom functions.
### 5. Test it out!
- You will likely need to tweak the message contents to get it looking how you want.
- A few test calls of `email_me.py` will show you the output and help with spacing, newlines etc.
- You can add new modules and import them into `compose_message.py` whenever you like, so you can easily change the report over time!
- After setup, all you need to run the program is:
```
python email_me.py
```
### 6. Run it automatically
- you can set the message up to auto send!
- On mac/linux the easiest way to do this is [cron](https://en.wikipedia.org/wiki/Cron)
- from command line type `crontab -e`
- then add a command to schedule execution. For example: to send the email report at 6am on Monday-Friday on my computer I add the command: `0 6 * * 1-5 python /Users/Cam/bin/email_me.py`
- Here is the general syntax for scheduling the job so that you can get it running at the time you want:
```
*     *     *   *    *        python ./email_me.py
-     -     -   -    -
|     |     |   |    |
|     |     |   |    +----- day of week (0 - 6) (Sunday=0)
|     |     |   +------- month (1 - 12)
|     |     +--------- day of        month (1 - 31)
|     +----------- hour (0 - 23)
+------------- min (0 - 59)
```

Thats it! A simple template for a custom email report feel free to take this and use it yourself! I would love to hear about any interesting scrapers or data aggregation modules that you construct and run in this template!

	
