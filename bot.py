import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='$', intents=intents)
scheduler = AsyncIOScheduler()
start_date = datetime(2026, 3, 17)

async def send_message():
    weeks_since_start = (datetime.now() - start_date).days // 7
    if weeks_since_start % 2 != 0:
        return
    channel = client.get_channel(1483666728151158907)
    await channel.send("@everyone TA MEETING AT 4:40")

@client.event
async def on_ready():
    print('READY')
    scheduler.add_job(
        send_message,
        CronTrigger(day_of_week='tue', hour=15, minute=0)
    )
    scheduler.start()

with open('token.txt', 'r') as f:
    token = f.read().strip()

client.run(token)