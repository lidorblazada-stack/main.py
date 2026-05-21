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

# --- פקודה 1: ספאם (טקסט רגיל, 10 פעמים) ---
@bot.tree.command(name="spam", description="שולח את ההודעה שתבחר 10 פעמים ברצף")
async def spam(interaction: discord.Interaction, text: str):
    await interaction.response.send_message("מתחיל ספאם... חחח", ephemeral=True)
    for i in range(10):
        await interaction.channel.send(text)
        await asyncio.sleep(0.8)

# --- פקודה 2: תיוג המוני (משתמש ספציפי, 10 פעמים) ---
@bot.tree.command(name="massping", description="מתייג משתמש 10 פעמים ברצף כדי לשגע אותו")
async def massping(interaction: discord.Interaction, target: discord.User):
    await interaction.response.send_message(f"מתחיל לתייג את {target.mention}...", ephemeral=True)
    for i in range(10):
        await interaction.channel.send(f"{target.mention} נוווו ענה כברררר!!!")
        await asyncio.sleep(0.8)
# --- פקודה 3: רייד חופשי ---
@bot.tree.command(name="raid", description="מציף את הערוץ במה שתבחר")
async def raid(interaction: discord.Interaction):
    # הגדרת משתנה קבוע בתוך הקוד במקום קלט מהמשתמש
    target = "הודעה קבועה" 
    
    await interaction.response.send_message(f"מתחיל רייד!", ephemeral=True)
    for i in range(10):
        await interaction.channel.send(f"{target} https://discord.gg/8ShaQ3KDdW")
        await asyncio.sleep(0.8)

# --- 4. פקודת Ghost Ping (תיוג נעלם) ---
@bot.tree.command(name="ghostping", description="מתייג חבר ומוחק את זה בשנייה כדי לשגע אותו")
async def ghostping(interaction: discord.Interaction, target: discord.User, amount: int = 5):
    await interaction.response.send_message("מתחיל גוסט-פינג חשאי... 🤫", ephemeral=True)
    if amount > 10: amount = 10
    for i in range(amount):
        msg = await interaction.channel.send(target.mention)
        await msg.delete()  # מוחק מיד את התיוג
        await asyncio.sleep(0.5)

# --- 5. פקודת Random Spam (ספאם משפטים משתנים) ---
@bot.tree.command(name="randomspam", description="מספים משתמש עם משפטים מציקים ורנדומליים")
async def randomspam(interaction: discord.Interaction, target: discord.User, amount: int = 5):
    await interaction.response.send_message(f"מתחיל להציק ל-{target.mention} עם משפטים רנדומליים!", ephemeral=True)
    if amount > 10: amount = 10
    for i in range(amount):
        phrase = random.choice(SPAM_PHRASES)
        await interaction.channel.send(f"{target.mention} {phrase}")
        await asyncio.sleep(0.8)

# --- 6. פקודת Speed Spam (ספאם במהירות שיא) ---
@bot.tree.command(name="speedspam", description="מפציץ את הצ'אט בטקסט במהירות מטורפת בלי הפסקה")
async def speedspam(interaction: discord.Interaction, text: str, amount: int = 10):
    await interaction.response.send_message("משגר ספאם מהיר!! 🔥🔥🔥", ephemeral=True)
    if amount > 15: amount = 15  # הגבלה שלא יחסמו את הבוט מהר מדי
    for i in range(amount):
        await interaction.channel.send(text)

# --- 7. פקודת Mimic (לדבר דרך הבוט) ---
@bot.tree.command(name="mimic", description="שולח הודעה נקייה בשם הבוט בלי שידעו שזה אתה")
async def mimic(interaction: discord.Interaction, text: str):
    await interaction.response.send_message("ההודעה נשלחה בהצלחה!", ephemeral=True)
    await interaction.channel.send(text)

# --- פקודה 8: מדריך לפקודות (מעודכן לכל הפיצ'רים) ---
@bot.tree.command(name="tutorial", description="מציג הסבר על כל פקודות הבוט")
async def tutorial(interaction: discord.Interaction):
    embed = discord.Embed(title="📜 מדריך הפקודות המלא של הבוט", color=discord.Color.red())
    embed.add_field(name="/spam [טקסט]", value="שולח הודעה 10 פעמים ברצף", inline=False)
    embed.add_field(name="/massping [משתמש]", value="מתייג מישהו 10 פעמים ברצף", inline=False)
    embed.add_field(name="/raid [מה שבאלך]", value="מספים את מה שרשמת עם אמוג'י אש", inline=False)
    embed.add_field(name="/ghostping [משתמש]", value="תיוג נעלם שנמחק מיד", inline=False)
    embed.add_field(name="/randomspam [משתמש]", value="שולח משפטים מציקים משתנים מרשימה", inline=False)
    embed.add_field(name="/speedspam [טקסט]", value="מפציץ טקסט במהירות מקסימלית בלי לחכות", inline=False)
    embed.add_field(name="/mimic [טקסט]", value="שולח הודעה חלקה בשם הבוט", inline=False)
    await interaction.response.send_message(embed=embed, ephemeral=True)


# 👑 הקסם שמחיל את ההגדרות לפרטי (DMs) ולכל מקום על כל הפקודות אוטומטית!
ALL_COMMANDS = [spam, massping, raid, ghostping, randomspam, speedspam, mimic, tutorial]
for command in ALL_COMMANDS:
    command._all_contexts = True  # מאפשר לעבוד בכל מקום (שרת, פרטי, קבוצות)
    command._user_install = True  # מאפשר להתקין ישירות על המשתמש שלך

# הרצה דרך Railway
token = os.getenv('BOT_TOKEN')
bot.run(token)
