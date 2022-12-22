import discord
import os
import json

m = {}

client = discord.Client()

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
  print('Miranda Notifier Version Python Mode 0.3.0')
  print('(C) 2018 - 2021 Eddie Miranda.')
  print('No part of this program shall be copied, modified, transmitted, reused, or otherwise distributed without permission from either copyright owner.')
  print('This application is currently under development. If you would like to assist in the process: feel free to message us on Discord.')
  print('Our Discord Handles:')
  print('EddieMiranda2000#1959')
  while True:
    try:
      for member in client.get_guild(851474242402385970).members:
        m[str(member.id)]["messageCountdown"] -= 1
    except:
        pass

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

    if message.content.startswith('ms;updatexp') and message.author.id == 732626677947170928:
      with open('users.json' 'w') as f:
        f.write(json.dumps(m))
        f.close()
    elif message.content.startswith('ms;hello'):
      {
        await message.channel.send('Hello there.')
      }
    elif message.content.startswith('ms;level-xp'):
      await message.content.send([str(message.author)], ': you currently at level ', ["level"], ' and need ' [100 - "xp"], ' to advacnce to the next level.')
    elif message.content.startswith('ms;cmds'):
      {
        await message.content.send('Here are the commands: \n''ms;cmds -- Prints this command list.\n' "ms;hello -- Makes Lauren say 'Hello there' back to the member.\n" "ms;level-xp -- Shows the member's level and amount of experience (XP) needed to advance to the next level.\n" "ms;updatexp - Updates the experience of all members of the server (Bot Owner Only)")
      }

client.run(os.environ['TOKEN'])
