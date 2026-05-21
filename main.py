import discord
from discord.ext import commands
from discord import app_commands
import asyncio
import os
import random

# הגדרת הבוט והרשאות
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# רשימת משפטים לפקודת ה-Random Spam
SPAM_PHRASES = [
    "נוווו ענה כברררר !!!",
    "איפה אתה יא נקניק כנס ללובי 😂",
    "אל תסנן אותי יא גנוב",
    "הלוווווו להתעורררר 🔥",
    "שומע? חחחחחחחחחחחחחח",
    "אתה פה או שאתה מפחד?"
]

@bot.event
async def on_ready():
    print(f'Spam Bot מוכן לפעולה בתור: {bot.user.name}')
    try:
        synced = await bot.tree.sync()
        print(f"סונכרנו {len(synced)} פקודות בהצלחה!")
    except Exception as e:
        print(f"שגיאה בסנכרון: {e}")

# --- 1. פקודת Ghost Ping (תיוג נעלם) ---
@bot.tree.command(name="ghostping", description="מתייג חבר ומוחק את זה בשנייה כדי לשגע אותו")
async def ghostping(interaction: discord.Interaction, target: discord.User, amount: int = 5):
    await interaction.response.send_message("מתחיל גוסט-פינג חשאי... 🤫", ephemeral=True)
    if amount > 10: amount = 10
    for i in range(amount):
        msg = await interaction.channel.send(target.mention)
        await msg.delete()  # מוחק מיד את התיוג
        await asyncio.sleep(0.5)

# --- 2. פקודת Random Spam (ספאם משפטים משתנים) ---
@bot.tree.command(name="randomspam", description="מספים משתמש עם משפטים מציקים ורנדומליים")
async def randomspam(interaction: discord.Interaction, target: discord.User, amount: int = 5):
    await interaction.response.send_message(f"מתחיל להציק ל-{target.mention} עם משפטים רנדומליים!", ephemeral=True)
    if amount > 10: amount = 10
    for i in range(amount):
        phrase = random.choice(SPAM_PHRASES)
        await interaction.channel.send(f"{target.mention} {phrase}")
        await asyncio.sleep(0.8)

# --- 3. פקודת Speed Spam (ספאם במהירות שיא) ---
@bot.tree.command(name="speedspam", description="מפציץ את הצ'אט בטקסט במהירות מטורפת בלי הפסקה")
async def speedspam(interaction: discord.Interaction, text: str, amount: int = 10):
    await interaction.response.send_message("משגר ספאם מהיר!! 🔥🔥🔥", ephemeral=True)
    if amount > 15: amount = 15  # הגבלה שלא יחסמו את הבוט מהר מדי
    for i in range(amount):
        await interaction.channel.send(text)
        # בלי asyncio.sleep בכלל - שולח מכה אחת ברצף!

# --- 4. פקודת Mimic (לדבר דרך הבוט) ---
@bot.tree.command(name="mimic", description="שולח הודעה נקייה בשם הבוט בלי שידעו שזה אתה")
async def mimic(interaction: discord.Interaction, text: str):
    # שולח את הודעת האישור בצורה חבויה רק לך
    await interaction.response.send_message("ההודעה נשלחה בהצלחה!", ephemeral=True)
    # הבוט שולח את הטקסט נקי לצ'אט
    await interaction.channel.send(text)


# החלת ההגדרות שיעבדו גם בפרטי (DMs) ובכל מקום
for command in [ghostping, randomspam, speedspam, mimic]:
    command._all_contexts = True
    command._user_install = True

# הרצה דרך Railway
token = os.getenv('BOT_TOKEN')
bot.run(token)
