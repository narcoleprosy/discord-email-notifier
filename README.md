# discord-email-notifier
Discord bot that monitors an email address and sends updates to your server.

This repo was forked from [Rfkgaming89's](https://github.com/Rfkgaming89/discord-email-notification) bot. I edited it to remove typos and other inconsistencies, and also to focus on windows as this is how I am running my bot. 


---

# Discord Email Notification Bot

Hey there! This bot checks your email at regular intervals and sends you notifications in a Discord channel. Plus, it updates a Discord thread with a countdown to the next email check and supports attachments. Pretty cool, right?

## Features

- **Email Checking:** Keeps an eye out for new emails.
- **Email Notifications:** Alerts you in a specified Discord channel when new emails arrive.
- **Thread Countdown:** Shows a countdown in a Discord thread for the next email check.
- **Attachment Support:** Can handle and send email attachments.

## Getting Started

### 1. Clone the Repository

First things first, grab the code from GitHub:

```bash
git clone https://github.com/rfkgaming89/discord-email-notification.git
cd discord-email-notification
```

### 2. Set Up a Virtual Environment

Let’s create and activate a virtual environment to keep everything tidy:

```bash
python3 -m venv venv
```

Activate it with:

```bash
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

Install the necessary Python packages, including `python-dotenv` to manage environment variables:

```bash
pip install discord.py python-dotenv
```

### 4. Set Up the `.env` File

Open `env.txt` and add your IMAP server details, email credentials, Discord token, guild ID, and channel IDs.

Rename `env.txt` to `.env`

### 5. Edit `Discord_Email.py`

Open up `Discord_Email.py` and fill in your settings:

#### Email Settings

```python
IMAP_SERVER = 'imap.example.com'
EMAIL_ACCOUNT = 'put@emailaddress.here'
PASSWORD = 'password' # If using gmail, you will need to create an app password.
```

- `IMAP_SERVER`: Your email provider’s IMAP server.
- `EMAIL_ACCOUNT`: Your email address.
- `PASSWORD`: Your email password.

#### Discord Bot Settings

```python
DISCORD_TOKEN = 'YOUR DISCORD BOT TOKEN'
GUILD_ID = 00000000000000000  # Your guild ID
CHANNEL_ID = 0000000000000000000  # Your channel ID
ROLE_ID = 0000000000000000000  # A role that you want to ping when a new email comes in
```

- `DISCORD_TOKEN`: Your bot’s token from Discord.
- `GUILD_ID`: Your Discord server’s ID.
- `CHANNEL_ID`: The ID of the channel where notifications will go.
= `ROLE_ID`: The ID of the role you want to ping with notifications.

### 6. Adjust Intervals

Customize how the bot behaves with these settings:

- **Thread Update Interval:** How often the thread name updates with the countdown.

  ```python
  THREAD_UPDATE_INTERVAL = 120  # Update every 2 minutes
  ```

  Change `120` to your preferred interval in seconds. For instance, to update every minute:

  ```python
  THREAD_UPDATE_INTERVAL = 60  # Update every minute
  ```

- **Email Check Interval:** How frequently the bot checks for new emails.

  ```python
  EMAIL_CHECK_INTERVAL = 1800  # Check every 30 minutes
  ```

  Change `1800` to your desired interval. For example, every 15 minutes:

  ```python
  EMAIL_CHECK_INTERVAL = 900  # Check every 15 minutes
  ```

- **Initial Check Duration:** How long the bot waits before it starts checking emails after you first run it.

  ```python
  INITIAL_CHECK_DURATION = 30  # Wait 30 seconds
  ```

  Adjust `30` to your preferred wait time. For example, to wait a minute:

  ```python
  INITIAL_CHECK_DURATION = 60  # Wait 60 seconds
  ```

### 7. Running the Bot

To start the bot, just run:

```bash
python email_bot.py # If using windows, run the run.ps1 file with powershell instead
```

The bot will log in and start checking your email according to the intervals you set.

### 8. Updating the Setup

If you need to update the setup or make changes to the script, you can simply edit the `.env` file and restart the script. No need to rebuild anything.

### 9. Troubleshooting

If you encounter issues, check the following:

- Ensure all environment variables in the `.env` file are correctly set.
- Verify that your IMAP server and email credentials are correct.
- Ensure your Discord bot token and channel IDs are valid.
- Check the terminal for error messages and consult the [Discord API documentation](https://discord.com/developers/docs/intro) for more information.

Feel free to reach out if you have any questions or run into any issues. Enjoy your setup!

## Docker Setup

Prefer using Docker? No problem! Check out the [Docker setup instructions](https://github.com/Rfkgaming89/discord-email-notification/tree/docker) for a step-by-step guide.

## Notes

- Make sure your email account allows access from less secure apps if needed.
- Ensure your Discord bot has the right permissions to send messages and manage threads in the specified channel.
- In an ideal situation, you use a burner email that only recieves emails from the service you are attempting to monitor. Be *VERY* careful using an email address that is known to server users, as they may be able to send emails to this account to bypass rules / automod, or can use any OTPs that arrive to gain access to accounts you probably don't want them to have access to.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

