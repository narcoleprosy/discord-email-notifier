### `README.md`

```markdown
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
```

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/rfkgaming89/discord-email-notification.git
   cd discord-email-notification
   ```

2. **Install Dependencies**

   Ensure you have Python 3.8+ installed. Install the required Python packages using pip:

   ```bash
   pip install discord.py
   ```

3. **Configuration**

   - Update the `Discord_Email.py` script with your email account credentials, Discord bot token, and the channel ID where the notifications will be sent:

     ```python
     # Email settings
     IMAP_SERVER = 'imap.example.com'
     EMAIL_ACCOUNT = 'your-email@example.com'
     PASSWORD = 'your-password'

     # Discord bot settings
     DISCORD_TOKEN = 'your-discord-bot-token'
     CHANNEL_ID = 123456789012345678  # Example channel ID
     ```

   - To change how often the bot checks for emails, modify the `await asyncio.sleep(1800)` line in the `check_and_notify()` function. The value `1800` is the time in seconds (30 minutes). For example, to check every 15 minutes, use `900` seconds:

     ```python
     await asyncio.sleep(900)  # Check every 15 minutes
     ```
 - To adjust the length of the email body summary, modify the summarize_body() function. The default function limits the summary to 40 words. Change the 40 in the following line to your desired word count:

   ```
   words = body.split()
   summary = ' '.join(words[:40])
   ```


   - Ensure that the `attachments/` directory exists or will be created by the script:

     ```bash
     mkdir attachments
     ```

4. **Run the Script**

   Execute the script to start the bot:

   ```bash
   python bot_with_email_checker.py
   ```

## Usage

Once running, the bot will check the email inbox at the specified interval and post any new emails to the specified Discord channel. It will also handle attachments, sending them to the channel along with the email details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the project's style guidelines and includes tests where applicable.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Pull requests

If you make changes to the script and want to open a Pull Request





