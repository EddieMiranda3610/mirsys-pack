import guilded
import os
import json
from guilded.ext import commands

m = {}

client = guilded.Client()

@client.event
async def on_ready():
  global m
  with open('users.json', 'r') as f:
    m = json.load(f)
    f.close()
  if len(m) == 0:
    m = {}
    for member in client.get_guild(851474242402385970).members:
      m[str(member.id)] = {"xp" : 0, "messageCountdown" : 0}

  print('Now logged in as {0.user}'.format(client))
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
      for member in client.get_guild(851474242402385970).members:
        m[str(member.id)]["messageCountdown"] -= 1
    except:
        pass
  bot = commands.Bot(command_prefix='mir;')
  @client.event
  async def on_message(message):
    global m
    if message.author != client.user:
      if m[str(message.author.id)]["messageCountdown"] <= 0:
        m[str(message.author.id)]["xp"] += 1
        m[str(member.id)]["messageCountdown"] = 10
        if m["xp"] > 100:
          m[str(message.author.id)]["level"] += 1
          await message.content.send([str(message.author)], ': you have now reached level ', ["level"])


    if message.author == client.user:
      return

    @bot.command()
    async def updatexp(ctx):
      if message.author.id == 732626677947170928:
        with open('users.json' 'w') as f:
          f.write(json.dumps(m))
          f.close()
    @bot.command()
    async def hello(ctx):
      await ctx.send('Hello there.')

    @bot.command()
    async def levelxp(ctx):
      await ctx.send([str(message.author)], ': you currently at level ', ["level"], ' and need ' [100 - "xp"], ' to advacnce to the next level.')

    @bot.command()
    async def cmdlist(ctx):
        ctx.send('Here are the commands: \n''mir;cmds -- Prints this command list.\n' "mir;hello -- Makes Miranda say 'Hello there' back to the member.\n" "mir;levelxp -- Shows the member's level and amount of experience (XP) needed to advance to the next level.\n" "mir;updatexp - Updates the experience of all members of the server (Bot Owner Only).")

client.run(os.environ['TOKEN'])
