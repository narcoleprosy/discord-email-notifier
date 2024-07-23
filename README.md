# Discord Email Notification Bot

A Discord bot that checks an email inbox at regular intervals, posts new emails to a specified Discord channel, and includes email details such as sender, subject, and a brief summary of the email body. The bot also handles email attachments and sends them to Discord.

## Features

- Checks for new emails in an inbox every 30 minutes.
- Posts email details (sender, subject, and summary) to a specified Discord channel.
- Handles and sends email attachments (e.g., photos) to Discord.
- Avoids re-posting already processed emails.

## Prerequisites

- Python 3.8 or later
- `discord.py` library
- `imaplib` (standard library)
- `email` (standard library)
- A Discord bot token
- Email account credentials

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/rfkgaming89/discord-email-notification.git
   cd discord-email-notification
