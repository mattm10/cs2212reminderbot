<h1>Discord Reminder Bot</h1>
A Discord bot that automatically sends meeting reminders to a server. <br>
<h2>Features:</h2>
- Uses Python, Discord.py, APScheduler, Railway<br>
- Sends a reminder message at 3 pm every other Tuesday<br>
- Uses APScheduler to manage the scheduling<br>
- Deployed on Railway for 24/7 uptime<br>
<h2>Requirements:</h2>
- Python 3.x<br>
- discord.py<br>
- APScheduler
<h2>Configuration:</h2>
Set the following environment variable in Railway:<br>
DISCORD_TOKEN=your_token_here
<h2>Configuration:</h2>
This bot is deployed on Railway. It read the 'DISCORD_TOKEN' from Railway's environment variables and restarts automatically on crashes.
