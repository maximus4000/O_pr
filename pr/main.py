import discord
import os
import random
from discord.ext import commands

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет, я {bot.user}!')

@bot.command()
async def heh(ctx, count_heh):
    await ctx.send("he" * int(count_heh))

@bot.command()
async def global_warming(ctx):
    random_gl = random.choice(["Выработка электроэнергии и тепла путем сжигания ископаемых видов топлива, таких как уголь, нефть и природный газ, является причиной значительной части глобальных выбросов. Большая часть электроэнергии по-прежнему производится из ископаемых видов топлива; лишь около четверти приходится на ветер, солнце и другие возобновляемые источники.",
"В производственных и промышленных процессах выбросы образуются в основном в результате сжигания ископаемых видов топлива с целью получения энергии для производства цемента, железа, стали, электронной аппаратуры, одежды, изделий из пластика и других товаров. Добыча полезных ископаемых и другие промышленные процессы также являются источником выбросов.",
"Вырубка лесов под сельскохозяйственные угодья или пастбища или по другим причинам приводит к выбросам, так как вырубленные деревья выделяют накопленный ими углерод. Поскольку леса поглощают углекислый газ, их уничтожение также ограничивает способность природы удерживать выбросы от попадания в атмосферу."])
    await ctx.send(random_gl)

@bot.command()
async def foto_warming(ctx):
    files = os.listdir("images")
    rand_foto = random.choice(files)
    with open(f"images/{rand_foto}", 'rb') as file:
        picture = discord.File(file)
    await ctx.send(file=picture)

@bot.command()
async def tempchange(ctx, quest):
    if quest == "temp":
        await ctx.send("Cредняя температура по планете: 1000 C")
    elif quest == "changetemp":
        await ctx.send("За последние 100 лет температура выросла на 1,2 С")

bot.run("MTE1NTQ0MzI4ODA5NTA4MDQ3OA.GXbcH1.FHK3-JwIiwDGfzjQLLyV8metcaAie8J79WH4Mo")