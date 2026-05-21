import discord
from discord.ext import commands
from discord import app_commands
import asyncio
import os

# הגדרת הבוט והרשאות
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# אירוע הדלקה וסנכרון פקודות ה-Slash לדיסקורד
@bot.event
async def on_ready():
    print(f'הבוט נדלק בהצלחה בתור: {bot.user.name}')
    try:
        synced = await bot.tree.sync()
        print(f"סונכרנו {len(synced)} פקודות סלאש בהצלחה!")
    except Exception as e:
        print(f"שגיאה בסנכרון פקודות: {e}")

# הפקודה שתשגע את המשתמשים
@bot.tree.command(name="ping-user", description="לתייג חבר שלא עונה כדי להציק לו חחח")
async def ping_user(interaction: discord.Interaction, target: discord.User, amount: int):
    # הגבלת כמות ל-10 כדי שלא יחסמו את הבוט על ספאם
    if amount > 10:
        amount = 10
    if amount < 1:
        amount = 1
        
    await interaction.response.send_message(f"מתחיל לתייג את {target.mention} כ-{amount} פעמים... חחח", ephemeral=True)
    
    for i in range(amount):
        await interaction.channel.send(f"נוווו ענה כברררר {target.mention} !!!")
        await asyncio.sleep(1)

# הרצה של הבוט דרך הטוקן שישב ב-Railway
token = os.getenv('BOT_TOKEN')
bot.run(token)
