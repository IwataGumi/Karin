# Karin IwataGumi Discord bot

# Requirement
Python 3.8.x
postgresql 15.3
ffmpeg 6.0

# Installing

## Docker
1. Copy the [.env.example](.env.example) file and rename it to .env. Open the `.env` file and replace `YOUR_DISCORD_BOT_TOKEN` with your actual Discord bot token. You can also modify other environment variables if desired.
```bash
$ cp .env.example .env
```
```bash
DISCORD_API_TOKEN=YOUR_DISCORD_BOT_TOKEN
...
```

2. Run the Docker container using the following command:
```bash
docker-compose up
```

All done!

# Other Information
This discord bot utilizes the [VoiceVox Engine](https://github.com/VOICEVOX/voicevox_engine) to read messages.