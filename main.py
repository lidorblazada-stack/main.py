import discord
from discord.ext import commands
from discord import app_commands
import asyncio
import os

# הגדרת הבוט והרשאות
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Spam Bot מוכן לפעולה בתור: {bot.user.name}')
    try:
        synced = await bot.tree.sync()
        print(f"סונכרנו {len(synced)} פקודות בהצלחה!")
    except Exception as e:
        print(f"שגיאה בסנכרון: {e}")

# --- פקודה 1: ספאם ---
@bot.tree.command(name="spam", description="שולח את ההודעה שתבחר 10 פעמים ברצף")
async def spam(interaction: discord.Interaction, text: str):
    await interaction.response.send_message("מתחיל ספאם... חחח", ephemeral=True)
    for i in range(10):
        await interaction.channel.send(text)
        await asyncio.sleep(0.8)

# --- פקודה 2: תיוג המוני ---
@bot.tree.command(name="massping", description="מתייג משתמש 10 פעמים ברצף כדי לשגע אותו")
async def massping(interaction: discord.Interaction, target: discord.User):
    await interaction.response.send_message(f"מתחיל לתייג את {target.mention}...", ephemeral=True)
    for i in range(10):
        await interaction.channel.send(f"{target.mention} נוווו ענה כברררר!!!")
        await asyncio.sleep(0.8)

# --- פקודה 3: רייד חופשי ---
@bot.tree.command(name="raid", description="מציף את הערוץ במה שתבחר (טקסט, תיוג, תפקיד וכו')")
async def raid(interaction: discord.Interaction, target: str):
    await interaction.response.send_message(f"מתחיל רייד על: {target}!", ephemeral=True)
    for i in range(10):
        await interaction.channel.send(f"{target} 🔥🔥🔥")
        await asyncio.sleep(0.8)

# --- פקודה 4: מדריך לפקודות ---
@bot.tree.command(name="tutorial", description="מציג הסבר על כל פקודות הבוט")
async def tutorial(interaction: discord.Interaction):
    embed = discord.Embed(title="📜 מדריך הפקודות של הבוט", color=discord.Color.red())
    embed.add_field(name="/spam [טקסט]", value="שולח הודעה 10 פעמים ברצף", inline=False)
    embed.add_field(name="/massping [משתמש]", value="מתייג מישהו 10 פעמים ברצף", inline=False)
    embed.add_field(name="/raid [מה שבאלך]", value="מספים את מה שרשמת 10 פעמים ברצף", inline=False)
    await interaction.response.send_message(embed=embed, ephemeral=True)

# 👑 הקסם שעוקף את השגיאות ופותח את הפקודות לפרטי בדיסקורד!
for command in [spam, massping, raid, tutorial]:
    command._all_contexts = True  # מאפשר לפקודה לעבוד בכל מקום (שרת, פרטי, קבוצות)
    command._user_install = True  # מאפשר להתקין את הפקודה ישירות על המשתמש שלך

# הרצה דרך Railway
token = os.getenv('BOT_TOKEN')
bot.run(token)
