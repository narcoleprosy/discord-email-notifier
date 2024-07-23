import discord
import asyncio
import imaplib
import email
import os
from discord.ext import commands

# Email settings
IMAP_SERVER = 'imap.example.com'
EMAIL_ACCOUNT = 'example@example.com'
PASSWORD = 'YOURPASSWORD'

# Discord bot settings
DISCORD_TOKEN = 'DISCORD BOT TOKEN HERE'

# File to store processed email IDs and thread ID
PROCESSED_EMAILS_FILE = 'processed_emails.txt'
THREAD_ID_FILE = 'thread_id.txt'
ATTACHMENTS_DIR = 'attachments/'

# Ensure the attachments directory exists
os.makedirs(ATTACHMENTS_DIR, exist_ok=True)

# Set up Discord client with intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Define your guild and channel IDs
GUILD_ID =   0000000000000000000  #  your guild id 
CHANNEL_ID = 0000000000000000000  # Your specified channel ID

EMAIL_CHECK_INTERVAL = 1800  # Initial email check interval in seconds (30 minutes)

def load_processed_emails():
    if os.path.exists(PROCESSED_EMAILS_FILE):
        with open(PROCESSED_EMAILS_FILE, 'r') as file:
            return set(line.strip() for line in file)
    return set()

def save_processed_email(email_id):
    with open(PROCESSED_EMAILS_FILE, 'a') as file:
        file.write(email_id + '\n')

def load_thread_id():
    if os.path.exists(THREAD_ID_FILE):
        with open(THREAD_ID_FILE, 'r') as file:
            return file.read().strip()
    return None

def save_thread_id(thread_id):
    with open(THREAD_ID_FILE, 'w') as file:
        file.write(str(thread_id))  # Convert the thread ID to a string before writing

def check_email(processed_emails):
    new_emails = []
    try:
        # Connect to the IMAP server
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_ACCOUNT, PASSWORD)
        mail.select('inbox')

        # Search for all emails
        status, data = mail.search(None, 'ALL')
        email_ids = data[0].split()

        for email_id in email_ids:
            email_id_str = email_id.decode()  # Convert byte to string
            if email_id_str in processed_emails:
                continue  # Skip already processed emails

            # Fetch the email by ID
            status, msg_data = mail.fetch(email_id, '(RFC822)')
            msg = email.message_from_bytes(msg_data[0][1])

            # Get email details
            from_ = msg.get('From')
            subject = msg.get('Subject')
            body = get_email_body(msg)
            attachments = get_attachments(msg)

            # Format email details with Markdown
            summary = summarize_body(body)
            email_info = (
                f"**From:** {from_}\n"
                f"**Subject:** {subject}\n\n"
                f"**Summary:**\n{summary}"
            )
            new_emails.append((email_info, attachments))

            # Mark this email as processed
            save_processed_email(email_id_str)

        mail.logout()
    except Exception as e:
        print(f"Error checking email: {e}")
    
    return new_emails

def get_email_body(msg):
    # Extract the email body
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                return part.get_payload(decode=True).decode()
    else:
        return msg.get_payload(decode=True).decode()
    return "No content"

def summarize_body(body):
    # Limit the summary to 40 words
    words = body.split()
    summary = ' '.join(words[:40])
    if len(words) > 40:
        summary += '...'
    return summary

def get_attachments(msg):
    attachments = []
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            filename = part.get_filename()

            if filename:
                filepath = os.path.join(ATTACHMENTS_DIR, filename)
                with open(filepath, 'wb') as file:
                    file.write(part.get_payload(decode=True))
                attachments.append(filepath)
    return attachments

async def send_email_notification(email_info, attachments):
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(email_info)
    for attachment in attachments:
        await channel.send(file=discord.File(attachment))

async def update_thread_name(thread, countdown_time):
    while countdown_time > 0:
        minutes, seconds = divmod(countdown_time, 60)
        await thread.edit(name=f"Next update in: {minutes:02}:{seconds:02}")
        await asyncio.sleep(60)  # Update every 60 seconds
        countdown_time -= 60

async def check_and_notify():
    processed_emails = load_processed_emails()
    channel = bot.get_channel(CHANNEL_ID)
    global EMAIL_CHECK_INTERVAL

    thread_id = load_thread_id()
    if thread_id:
        try:
            # Fetch the existing thread from the channel
            messages = [message async for message in channel.history(limit=1)]
            thread = discord.utils.get(channel.threads, id=int(thread_id))
            if not thread:
                raise discord.NotFound
        except discord.NotFound:
            thread = await channel.create_thread(name="Next update in: 30:00", type=discord.ChannelType.public_thread)
            save_thread_id(thread.id)
    else:
        thread = await channel.create_thread(name="Next update in: 30:00", type=discord.ChannelType.public_thread)
        save_thread_id(thread.id)
    
    while True:
        new_emails = check_email(processed_emails)
        for email_info, attachments in new_emails:
            await send_email_notification(email_info, attachments)
        
        # Start or update the countdown timer
        await update_thread_name(thread, EMAIL_CHECK_INTERVAL)
        await asyncio.sleep(EMAIL_CHECK_INTERVAL)  # Check every countdown_time seconds

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    bot.loop.create_task(check_and_notify())

@bot.tree.command(name="setinterval", description="Set the email check interval")
async def setinterval(interaction: discord.Interaction, interval: int):
    global EMAIL_CHECK_INTERVAL
    EMAIL_CHECK_INTERVAL = interval
    await interaction.response.send_message(f"Email check interval set to {interval} seconds.", ephemeral=True)

async def setup_hook():
    bot.tree.copy_global_to(guild=discord.Object(id=GUILD_ID))
    await bot.tree.sync(guild=discord.Object(id=GUILD_ID))

bot.setup_hook = setup_hook

bot.run(DISCORD_TOKEN)
