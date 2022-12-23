import guilded
from guilded.ext import commands
import os
import json

m = {}

bot = commands.Bot(command_prefix='mir;')

@bot.event
async def on_connect(ctx):
  ctx.send("Connecting Miranda to server...")

@bot.event
async def on_ready(ctx):
  global m
  with open('users.json', 'r') as f:
    m = json.load(f)
    f.close()
  if len(m) == 0:
    m = {}
    for user in guilded.Server(id='zE8BVJqR'):
      m[str(user.id)] = {"xp" : 0, "messageCountdown" : 0}

  embed = guilded.Embed(
    title='Miranda Notifier', 
    description='Miranda Notifier 0.1.0 enabled.\n' '(C) 2017 - 2022 Eddie Miranda.\n' '(C) 2019 - 2022 Maria Le.\n' 'No part of this program shall be copied, modified, transmitted, reused, or otherwise distributed without permission from either copyright owner.\n' 'This application is currently under development. If you would like to assist in the process: feel free to message us.\n' 'Our Social Handles:\n' 'Reddit: Moist_Programmer_514\n' 'Guilded: EddieMiranda1640\n' 'Discord: EddieMiranda2000#1959', 
    thumbnail='https://img.guildedcdn.com/ContentMediaGenericFiles/190b5df8c952e21357994348b653db9d-Full.webp?w=288&h=288',
    footer='Miranda Notifier Version 0.1.0')

  await ctx.send(embed=embed)

  print(f'Now logged in as {bot.user} (ID: {bot.user.id})')
  print('Miranda Notifier Version Python Mode 0.1.0')
  print('(C) 2017 - 2022 Eddie Miranda.')
  print('(C) 2019 - 2022 Maria Le.')
  print('No part of this program shall be copied, modified, transmitted, reused, or otherwise distributed without permission from either copyright owner.')
  print('This application is currently under development. If you would like to assist in the process: feel free to message us.')
  print('Our Social Handles:')
  print('Reddit: Moist_Programmer_514')
  print('Guilded: EddieMiranda1640')
  print('Discord: EddieMiranda2000#1959')
  while True:
    try:
      for user in guilded.Server(id='zE8BVJqR'):
        m[str(user.id)]["messageCountdown"] -= 1
    except:
        pass
  
  @bot.event
  async def on_message(message):
    global m
    if message.author != bot.user:
      if m[str(message.author.id)]["messageCountdown"] <= 0:
        m[str(message.author.id)]["xp"] += 1
        m[str(user.id)]["messageCountdown"] = 10
        if m["xp"] > 100:
          m[str(message.author.id)]["level"] += 1
          await message.content.send([str(message.author)], ': you have now reached level ', ["level"])


    if message.author == bot.user:
      return

    @bot.command()
    async def updatexp(ctx):
      if message.author.id == '4vEDkJbA':
        with open('users.json' 'w') as f:
          f.write(json.dumps(m))
          f.close()
          
    @bot.command()
    async def hello(ctx):
      await ctx.send('Hello there.')

    @bot.command()
    async def levelxp(ctx):
      await ctx.send([str(message.author)], ': you are currently at level ', ["level"], ' and need ' [100 - "xp"], ' to advacnce to the next level.')

    @bot.command()
    async def cmdlist(ctx):
        ctx.send('Here are the commands: \n''ms;cmds -- Prints this command list.\n' "ms;hello -- Makes Miranda say 'Hello there' back to the user.\n" "ms;level-xp -- Shows the user's level and amount of experience (XP) needed to advance to the next level.\n" "ms;updatexp - Updates the experience of all members of the server (Bot Owner Only)")

bot.run(os.environ['TOKEN'])
