from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def beru (ctx):
    await ctx.send('☆ベル 木曜日：開始 23:00~ 集結 ~22:45☆日曜日：開始14:00~ 集結 ~13:45☆ｳｨｽ(´・ω・｀)ﾉｳｨｽ☆')
    
    bot.run(token)
