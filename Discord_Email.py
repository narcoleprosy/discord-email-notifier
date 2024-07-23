import discord
import imaplib
import email
import asyncio
import os

# Email settings
IMAP_SERVER = 'imap.example.com'
EMAIL_ACCOUNT = 'example@rfkgaming.com'
PASSWORD = 'PASSWORD'

# Discord bot settings
DISCORD_TOKEN = 'DISCORD BOT TOKEN'
CHANNEL_ID = 123456789123466789  # Replace with your channel ID

# File to store processed email IDs
PROCESSED_EMAILS_FILE = 'processed_emails.txt'
ATTACHMENTS_DIR = 'attachments/'

# Ensure the attachments directory exists
os.makedirs(ATTACHMENTS_DIR, exist_ok=True)

# Set up Discord client with intents
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def load_processed_emails():
    if os.path.exists(PROCESSED_EMAILS_FILE):
        with open(PROCESSED_EMAILS_FILE, 'r') as file:
            return set(line.strip() for line in file)
    return set()

def save_processed_email(email_id):
    with open(PROCESSED_EMAILS_FILE, 'a') as file:
        file.write(email_id + '\n')

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
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(email_info)
    for attachment in attachments:
        await channel.send(file=discord.File(attachment))

async def check_and_notify():
    processed_emails = load_processed_emails()
    while True:
        new_emails = check_email(processed_emails)
        for email_info, attachments in new_emails:
            await send_email_notification(email_info, attachments)
        await asyncio.sleep(60)  # Check every 30 minutes

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    client.loop.create_task(check_and_notify())

client.run(DISCORD_TOKEN)
