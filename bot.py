import os
import re
from urllib.parse import urlparse, urlencode, parse_qs, urlunparse

import discord
from dotenv import load_dotenv

load_dotenv()

# Tracking parameters to strip from any URL
TRACKING_PARAMS = {
    "si",           # YouTube session tracking
    "utm_source",
    "utm_medium",
    "utm_campaign",
    "utm_term",
    "utm_content",
    "utm_id",
    "fbclid",       # Facebook
    "gclid",        # Google Ads
    "msclkid",      # Microsoft Ads
    "ref",
    "referrer",
    "mc_cid",       # Mailchimp
    "mc_eid",
}

URL_PATTERN = re.compile(r"https?://[^\s<>\"']+")


def clean_url(url: str) -> str | None:
    parsed = urlparse(url)
    params = parse_qs(parsed.query, keep_blank_values=True)

    cleaned = {k: v for k, v in params.items() if k not in TRACKING_PARAMS}

    if cleaned == params:
        return None  # nothing was removed

    new_query = urlencode(cleaned, doseq=True)
    clean = parsed._replace(query=new_query)
    return urlunparse(clean)


def process_message(content: str) -> list[tuple[str, str]]:
    """Return list of (original_url, clean_url) for each URL that had tracking params."""
    results = []
    for url in URL_PATTERN.findall(content):
        cleaned = clean_url(url)
        if cleaned:
            results.append((url, cleaned))
    return results


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    pairs = process_message(message.content)
    if not pairs:
        return

    content = message.content
    for original, clean in pairs:
        content = content.replace(original, clean)

    await message.delete()
    await message.channel.send(
        f"**{message.author.display_name}** : {content}\n-# 🔗 Liens nettoyés des trackers"
    )


client.run(os.environ["DISCORD_TOKEN"])
