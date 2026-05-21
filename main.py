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
@app_commands.allowed_contexts(guild=True, dms=True, private_channels=True)
@app_commands.allowed_installs(guild=True, user=True)
async def spam(interaction: discord.Interaction, text: str):
    await interaction.response.send_message("מתחיל ספאם... חחח", ephemeral=True)
    for i in range(10):
        await interaction.channel.send(text)
        await asyncio.sleep(0.8)

# --- פקודה 2: תיוג המוני של משתמש ---
@bot.tree.command(name="massping", description="מתייג משתמש 10 פעמים ברצף כדי לשגע אותו")
@app_commands.allowed_contexts(guild=True, dms=True, private_channels=True)
@app_commands.allowed_installs(guild=True, user=True)
async def massping(interaction: discord.Interaction, target: discord.User):
    await interaction.response.send_message(f"מתחיל לתייג את {target.mention}...", ephemeral=True)
    for i in range(10):
        await interaction.channel.send(f"{target.mention} נוווו ענה כברררר!!!")
        await asyncio.sleep(0.8)

# --- פקודה 3: רייד (תיוג @everyone) ---
@bot.tree.command(name="raid", description="מציף את הערוץ בתיוגים של כולם")
@app_commands.allowed_contexts(guild=True, dms=True, private_channels=True)
@app_commands.allowed_installs(guild=True, user=True)
async def raid(interaction: discord.Interaction, text: str):
    await interaction.response.send_message("מתחיל רייד מטורף!", ephemeral=True)
    for i in range(10):
        await interaction.channel.send(f"@everyone {text} 🔥🔥🔥")
        await asyncio.sleep(0.8)

# --- פקודה 4: מדריך לפקודות ---
@bot.tree.command(name="tutorial", description="מציג הסבר על כל פקודות הבוט")
@app_commands.allowed_contexts(guild=True, dms=True, private_channels=True)
@app_commands.allowed_installs(guild=True, user=True)
async def tutorial(interaction: discord.Interaction):
    embed = discord.Embed(title="📜 מדריך הפקודות של הבוט", color=discord.Color.red())
    embed.add_field(name="/spam [טקסט]", value="שולח הודעה 10 פעמים ברצף", inline=False)
    embed.add_field(name="/massping [משתמש]", value="מתייג מישהו 10 פעמים ברצף", inline=False)
    embed.add_field(name="/raid [טקסט]", value="מתייג את כולם (@everyone) עם הטקסט 10 פעמים", inline=False)
    await interaction.response.send_message(embed=embed, ephemeral=True)

# הרצה דרך Railway
token = os.getenv('BOT_TOKEN')
bot.run(token)
