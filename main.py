import discord
from discord.ext import commands
from discord import app_commands
import asyncio
import os
import random

# =========================
# הגדרת הבוט והרשאות
# =========================
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

# =========================
# משפטים רנדומליים
# =========================
SPAM_PHRASES = [
    "נוווו ענה כברררר !!!",
    "איפה אתה יא נקניק כנס ללובי 😂",
    "אל תסנן אותי יא גנוב",
    "הלוווווו להתעורררר 🔥",
    "שומע? חחחחחחחחחחחחחח",
    "אתה פה או שאתה מפחד?"
]

# =========================
# כשהבוט נדלק
# =========================
@bot.event
async def on_ready():

    print(f'Spam Bot מוכן לפעולה בתור: {bot.user.name}')

    try:

        synced = await bot.tree.sync()

        print(f"סונכרנו {len(synced)} פקודות בהצלחה!")

    except Exception as e:

        print(f"שגיאה בסנכרון: {e}")

# =========================
# פקודה 1 - Spam
# =========================
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
    description="שולח את ההודעה שתבחר 10 פעמים ברצף"
)
async def spam(
    interaction: discord.Interaction,
    text: str
):

    await interaction.response.send_message(
        "מתחיל ספאם... חחח",
        ephemeral=True
    )

    for i in range(10):

        await interaction.channel.send(text)

        await asyncio.sleep(0.8)

# =========================
# פקודה 2 - Mass Ping
# =========================
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
    description="מתייג משתמש 10 פעמים ברצף"
)
async def massping(
    interaction: discord.Interaction,
    target: discord.User
):

    await interaction.response.send_message(
        f"מתחיל לתייג את {target.mention}...",
        ephemeral=True
    )

    for i in range(10):

        await interaction.channel.send(
            f"{target.mention} נוווו ענה כברררר!!!"
        )

        await asyncio.sleep(0.8)

# =========================
# פקודה 3 - Raid
# =========================
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
    description="מציף את הערוץ אוטומטית"
)
async def raid(interaction: discord.Interaction):

    await interaction.response.send_message(
        "מתחיל רייד!",
        ephemeral=True
    )

    for i in range(10):

        await interaction.channel.send(
            "https://discord.gg/8qBzSXWY6b 🔥🔥🔥"
        )

        await asyncio.sleep(0.8)

# =========================
# פקודה 4 - Ghost Ping
# =========================
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
    description="מתייג חבר ומוחק מיד"
)
async def ghostping(
    interaction: discord.Interaction,
    target: discord.User,
    amount: int = 5
):

    await interaction.response.send_message(
        "מתחיל גוסט-פינג חשאי... 🤫",
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

# =========================
# פקודה 5 - Random Spam
# =========================
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
    description="מספים משפטים רנדומליים"
)
async def randomspam(
    interaction: discord.Interaction,
    target: discord.User,
    amount: int = 5
):

    await interaction.response.send_message(
        f"מתחיל להציק ל-{target.mention}",
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

# =========================
# פקודה 6 - Speed Spam
# =========================
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
    description="מפציץ טקסט במהירות"
)
async def speedspam(
    interaction: discord.Interaction,
    text: str,
    amount: int = 10
):

    await interaction.response.send_message(
        "משגר ספאם מהיר!! 🔥🔥🔥",
        ephemeral=True
    )

    if amount > 15:
        amount = 15

    for i in range(amount):

        await interaction.channel.send(text)

# =========================
# פקודה 7 - Mimic
# =========================
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
        "ההודעה נשלחה בהצלחה!",
        ephemeral=True
    )

    await interaction.channel.send(text)

# =========================
# פקודה 8 - Tutorial
# =========================
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
    description="מציג את כל הפקודות"
)
async def tutorial(interaction: discord.Interaction):

    embed = discord.Embed(
        title="📜 מדריך הפקודות המלא של הבוט",
        color=discord.Color.red()
    )

    embed.add_field(
        name="/spam [טקסט]",
        value="שולח הודעה 10 פעמים",
        inline=False
    )

    embed.add_field(
        name="/massping [משתמש]",
        value="מתייג משתמש 10 פעמים",
        inline=False
    )

    embed.add_field(
        name="/raid",
        value="מספים לינק קבוע אוטומטית",
        inline=False
    )

    embed.add_field(
        name="/ghostping [משתמש]",
        value="תיוג שנמחק מיד",
        inline=False
    )

    embed.add_field(
        name="/randomspam [משתמש]",
        value="משפטים רנדומליים",
        inline=False
    )

    embed.add_field(
        name="/speedspam [טקסט]",
        value="ספאם במהירות מטורפת",
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

# =========================
# מאפשר עבודה ב-DM
# =========================
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

# =========================
# הרצה דרך Railway
# =========================
token = os.getenv('BOT_TOKEN')

bot.run(token)
