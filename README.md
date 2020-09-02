# Ocurl Extensions - Discord Bot

Discord bot to generate short URLs.

## Summon Bot
`!ocurl {your destination url}`

Provide the destination URL and Ocurl will respond with a shortened URL.

## Example

`Rick> !ocurl www.example.com`


`Ocurl Link Bot> https://ocurl.io/owxm2`

## Permissions
Ocurl Link Bot requires the following permissions to work,
- Send Messages

  Ocurl sends a shortened URL after being summoned

- Read Message History

  Ocurl needs to see the message history to process messages that contains links that need to be shortened

## Self Hosting
### Setup
There are only two dependacies to host this bot. Automatically install dependancies using pip by running

`python -m pip install -r requirements.txt`

- Python3+
- discord.py
- requests

Set the Discord API token by exporting the environment variable `DISCORD_BOT_TOKEN`

Windows
`set DISCORD_BOT_TOKEN=YOUR_BOT_TOKEN`

macOS and Linux:
`export DISCORD_BOT_TOKEN=YOUR_BOT_TOKEN`

Start the bot by running with Python

`python bot.py`
