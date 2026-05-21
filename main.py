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

# הפקודה המשודרגת שכוללת גם טקסט חופשי!
@bot.tree.command(name="ping-user", description="לתייג חבר שלא עונה ולשלוח לו הודעות חחח")
async def ping_user(interaction: discord.Interaction, target: discord.User, amount: int, message: str = None):
    # הגבלת כמות ל-10 כדי שלא יחסמו את הבוט על ספאם
    if amount > 10:
        amount = 10
    if amount < 1:
        amount = 1
        
    await interaction.response.send_message(f"מתחיל להציק ל-{target.mention} כ-{amount} פעמים... חחח", ephemeral=True)
    
    # אם לא רשמת הודעה, הוא ישתמש בטקסט הרגיל
    if message is None:
        message = "נוווו ענה כברררר !!!"
        
    for i in range(amount):
        # שולח את המשפט שאתה בחרת ביחד עם התיוג של החבר
        await interaction.channel.send(f"{target.mention} {message}")
        await asyncio.sleep(1)

# הגדרת הגמישות של הפקודה לעבוד בכל מקום בצורה עוקפת שגיאות גרסה
ping_user.contexts = [discord.AppCommandContext(0), discord.AppCommandContext(1), discord.AppCommandContext(2)]
ping_user.integration_types = [discord.IntegrationType(0), discord.IntegrationType(1)]

# הרצה של הבוט דרך הטוקן שישב ב-Railway
token = os.getenv('BOT_TOKEN')
bot.run(token)
