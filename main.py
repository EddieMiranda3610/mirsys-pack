import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('Now logged in as {0.user}'.format(client))
  print('Miranda System Bot Version 0.1.0 Update 1')
  print('(C) 2018 - 2021 Eddie Miranda.')
  print('No part of this program shall be copied, modified, transmitted, reused, or otherwise distributed without permission from the copyright owner.')
  print('This application is currently under development. If you would like to assist in the process: feel free to message the developer on Discord:')
  print('EddieMiranda&Keira2000#1959')

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    if message.content.startswith('ms;hello'):
      {
        await message.channel.send('Hello there.')
      }
    elif message.content.startswith('ms;cmds'):
      {
        await message.content.send('Here are the commands: \n''ms;cmds -- Prints this command list.\n' "ms;hello -- Makes Miranda say 'Hello there' back to the member.\n" "ms;level-xp -- Shows the member's level and amount of experience (XP) needed to advance to the next level.")
      }

client.run(os.environ['TOKEN'])    
