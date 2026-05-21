import discord
from discord.ext import commands
from discord import app_commands
import asyncio
import os
import random

# =========================================
# הגדרות בוט
# =========================================
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

# =========================================
# משפטים רנדומליים
# =========================================
SPAM_PHRASES = [
    "נוווו ענה כברררר !!!",
    "איפה אתה יא נקניק כנס ללובי 😂",
    "אל תסנן אותי יא גנוב",
    "הלוווווו להתעורררר 🔥",
    "שומע? חחחחחחחחחחחחחח",
    "אתה פה או שאתה מפחד?"
]

# =========================================
# כשהבוט נדלק
# =========================================
@bot.event
async def on_ready():

    print(f"✅ מחובר בתור: {bot.user}")

    try:

        synced = await bot.tree.sync()

        print(f"✅ סונכרנו {len(synced)} פקודות")

    except Exception as e:

        print(f"❌ שגיאה: {e}")

# =========================================
# SPAM
# =========================================
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
@app_commands.allowed_installs(
    guilds=True,
    users=True
)
@bot.tree.command(
    name="spam",
    description="שולח הודעה 10 פעמים"
)
async def spam(
    interaction: discord.Interaction,
    text: str
):

    await interaction.response.defer(
        ephemeral=True
    )

    for i in range(10):

        await interaction.channel.send(
            text
        )

        await asyncio.sleep(0.8)

    await interaction.followup.send(
        "✅ הספאם הסתיים",
        ephemeral=True
    )

# =========================================
# MASSPING
# =========================================
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
@app_commands.allowed_installs(
    guilds=True,
    users=True
)
@bot.tree.command(
    name="massping",
    description="מתייג משתמש 10 פעמים"
)
async def massping(
    interaction: discord.Interaction,
    target: discord.User
):

    await interaction.response.defer(
        ephemeral=True
    )

    for i in range(10):

        await interaction.channel.send(
            f"{target.mention} נוווו ענה כברררר!!!"
        )

        await asyncio.sleep(0.8)

    await interaction.followup.send(
        "✅ התיוג הסתיים",
        ephemeral=True
    )

# =========================================
# RAID
# =========================================
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
@app_commands.allowed_installs(
    guilds=True,
    users=True
)
@bot.tree.command(
    name="raid",
    description="מספים לינק אוטומטית"
)
async def raid(
    interaction: discord.Interaction
):

    await interaction.response.defer(
        ephemeral=True
    )

    for i in range(10):

        await interaction.channel.send(
            "https://discord.gg/8qBzSXWY6b 🔥🔥🔥"
        )

        await asyncio.sleep(0.8)

    await interaction.followup.send(
        "✅ הרייד הסתיים",
        ephemeral=True
    )

# =========================================
# GHOSTPING
# =========================================
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
@app_commands.allowed_installs(
    guilds=True,
    users=True
)
@bot.tree.command(
    name="ghostping",
    description="תיוג שנמחק מיד"
)
async def ghostping(
    interaction: discord.Interaction,
    target: discord.User,
    amount: int = 5
):

    await interaction.response.defer(
        ephemeral=True
    )

    if amount > 10:
        amount = 10

    for i in range(amount):

        msg = await interaction.channel.send(
            target.mention
        )

        await msg.delete()

        await asyncio.sleep(0.5)

    await interaction.followup.send(
        "✅ ghostping הסתיים",
        ephemeral=True
    )

# =========================================
# RANDOMSPAM
# =========================================
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
@app_commands.allowed_installs(
    guilds=True,
    users=True
)
@bot.tree.command(
    name="randomspam",
    description="ספאם רנדומלי"
)
async def randomspam(
    interaction: discord.Interaction,
    target: discord.User,
    amount: int = 5
):

    await interaction.response.defer(
        ephemeral=True
    )

    if amount > 10:
        amount = 10

    for i in range(amount):

        phrase = random.choice(
            SPAM_PHRASES
        )

        await interaction.channel.send(
            f"{target.mention} {phrase}"
        )

        await asyncio.sleep(0.8)

    await interaction.followup.send(
        "✅ randomspam הסתיים",
        ephemeral=True
    )

# =========================================
# SPEEDSPAM
# =========================================
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
@app_commands.allowed_installs(
    guilds=True,
    users=True
)
@bot.tree.command(
    name="speedspam",
    description="ספאם במהירות"
)
async def speedspam(
    interaction: discord.Interaction,
    text: str,
    amount: int = 10
):

    await interaction.response.defer(
        ephemeral=True
    )

    if amount > 15:
        amount = 15

    for i in range(amount):

        await interaction.channel.send(
            text
        )

    await interaction.followup.send(
        "✅ speedspam הסתיים",
        ephemeral=True
    )

# =========================================
# MIMIC
# =========================================
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
@app_commands.allowed_installs(
    guilds=True,
    users=True
)
@bot.tree.command(
    name="mimic",
    description="שולח הודעה דרך הבוט"
)
async def mimic(
    interaction: discord.Interaction,
    text: str
):

    await interaction.response.send_message(
        "✅ נשלח",
        ephemeral=True
    )

    await interaction.channel.send(
        text
    )

# =========================================
# TUTORIAL
# =========================================
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
@app_commands.allowed_installs(
    guilds=True,
    users=True
)
@bot.tree.command(
    name="tutorial",
    description="מדריך הפקודות"
)
async def tutorial(
    interaction: discord.Interaction
):

    embed = discord.Embed(
        title="📜 מדריך הפקודות",
        color=discord.Color.red()
    )

    embed.add_field(
        name="/spam [טקסט]",
        value="ספאם רגיל",
        inline=False
    )

    embed.add_field(
        name="/massping [משתמש]",
        value="תיוג 10 פעמים",
        inline=False
    )

    embed.add_field(
        name="/raid",
        value="מספים לינק קבוע",
        inline=False
    )

    embed.add_field(
        name="/ghostping [משתמש]",
        value="תיוג נעלם",
        inline=False
    )

    embed.add_field(
        name="/randomspam [משתמש]",
        value="ספאם רנדומלי",
        inline=False
    )

    embed.add_field(
        name="/speedspam [טקסט]",
        value="ספאם מהיר",
        inline=False
    )

    embed.add_field(
        name="/mimic [טקסט]",
        value="שולח הודעה דרך הבוט",
        inline=False
    )

    await interaction.response.send_message(
        embed=embed,
        ephemeral=True
    )

# =========================================
# מאפשר עבודה בכל מקום
# =========================================
ALL_COMMANDS = [
    spam,
    massping,
    raid,
    ghostping,
    randomspam,
    speedspam,
    mimic,
    tutorial
]

for command in ALL_COMMANDS:

    command._all_contexts = True
    command._user_install = True

# =========================================
# הרצת הבוט
# =========================================
token = os.getenv("BOT_TOKEN")

bot.run(token)
