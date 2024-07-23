# Discord Email Notification Bot

A Discord bot designed to check for new emails at regular intervals, send notifications about new emails

to a Discord channel,and update a 
Discord thread with a countdown to the next email check. It also supports attachments.

## Features

- **Email Checking:** Periodically checks for new emails.
- **Email Notifications:** Sends notifications about new emails to a specified Discord channel.
- **Thread Countdown:** Updates a Discord thread with a countdown to the next email check.
- **Attachment Support:** Handles and sends email attachments.
![](https://raw.githubusercontent.com/Rfkgaming89/discord-email-notification/main/Example.png )
## Installation

### 1. Clone the Repository

```
git clone https://github.com/rfkgaming89/discord-email-notification.git
cd discord-email-notification
```

### 2. Set Up a Virtual Environment

```
python3 -m venv venv
```

    source venv/bin/activate  # On Windows use `venv\Scripts\activate`


### 3. Install Dependencies

```
pip install discord.py
```

## Configuration

### Edit `email_bot.py`

Open the `email_bot.py` file and update the following settings:

#### Email Settings

```python
IMAP_SERVER = 'imap.example.com'
EMAIL_ACCOUNT = 'your-email@example.com'
PASSWORD = 'YOUR EMAIL PASSWORD'
```

- `IMAP_SERVER`: Your email provider's IMAP server address.
- `EMAIL_ACCOUNT`: Your email address.
- `PASSWORD`: Your email account password.

#### Discord Bot Settings

```python
DISCORD_TOKEN = 'YOUR DISCORD BOT TOKEN'
GUILD_ID = 00000000000000000  # Your guild ID
CHANNEL_ID = 00000000000000000  # Your specified channel ID
```

- `DISCORD_TOKEN`: Your Discord bot token.
- `GUILD_ID`: Your Discord guild (server) ID.
- `CHANNEL_ID`: The ID of the Discord channel where notifications will be sent.

### Adjust Intervals

Customize the bot's behavior by adjusting the following settings:

- **Thread Update Interval:** The frequency of thread name updates with the countdown.

  ```python
  THREAD_UPDATE_INTERVAL = 120  # Update interval in seconds (2 minutes)
  ```

  Change `120` to your desired interval in seconds. For example, to update every minute:

  ```python
  THREAD_UPDATE_INTERVAL = 60  # Update interval in seconds (1 minute)
  ```

- **Email Check Interval:** How often the bot checks for new emails.

  ```python
  EMAIL_CHECK_INTERVAL = 1800  # Check interval in seconds (30 minutes)
  ```

  Change `1800` to your desired interval in seconds. For example, to check every 15 minutes:

  ```python
  EMAIL_CHECK_INTERVAL = 900  # Check interval in seconds (15 minutes)
  ```

- **Initial Check Duration:** Time the bot waits before starting periodic checks after initial startup.

  ```python
  INITIAL_CHECK_DURATION = 30  # Initial wait time in seconds
  ```

  Change `30` to your desired duration in seconds. For example, to wait 1 minute:

  ```python
  INITIAL_CHECK_DURATION = 60  # Initial wait time in seconds (1 minute)
  ```

## Running the Bot

To start the bot, run:

```bash
python email_bot.py
```

The bot will log in and begin checking for new emails based on the configured intervals.

## Notes

- Ensure that your email account allows access from less secure apps if needed.
- Verify that your Discord bot has the necessary permissions to send messages and manage threads in the specified channel.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

