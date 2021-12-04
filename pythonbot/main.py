import os
import discord
import datetime
from discord.ext import commands

personal_token = os.environ['personal_token']
total_count = 0
#1 less than number of categories
categories = 17
#client = discord.Client()
client = commands.Bot(command_prefix='!')
awards = ["Record of the Year", "Album of the Year", "Song of the Year", "Best new Artist", "Best Pop Solo Performance", "Best Pop Duo Performance", "Best Traditional Pop Vocal Album", "Best Pop Vocal Album", "Best R&B Performance", "Best Traditional R&B performance", "Best R&B Song", "Best Progressive R&B Album", "Best R&B Album", "Best Rap Performance", "Best Melodic Rap Performance", "Best Rap Song", "Best Rap Album"] 


nominees = [
  
  ["ABBA - I Still Have Faith In You", "Jon Batiste - Freedom", "Tony Bennett & Lady Gaga - I Get A Kick Out Of You", "Justin Bieber Featuring Daniel Caesar & Giveon - Peaches", "Brandi Carlile - Right On Time", "Doja Cat Featuring SZA - Kiss Me More", "Billie Eilish - Happier Than Ever", "Lil Nas X - Montero (Call Me By Your Name)", "Olivia Rodrigo - drivers license", "Silk Sonic - Leave The Door Open"], 

["Jon Batiste - We Are", "Tony Bennett & Lady Gaga - Love For Sale", "Justin Bieber - Justice (Triple Chucks Deluxe)", "Doja Cat - Planet Her(Deluxe)", "Billie Eilish - Happier Than Ever", "H.E.R. - Back of My Mind", "Lil Nas X - Montero", "Olivia Rodrigo - Sour", "Taylor Swift - Evermore", "Kanye West - Donda"], 


["Ed Sheeran - Bad Habits", "Alicia Keys & Brandi Carlile - A Beautiful Noise", "Olivia Rodrigo - drivers license", "H.E.R. - Fight For You", "Billie Eilish - Happier Than Ever", "Doja Cat Featuring SZA - Kiss Me More", "Silk Sonic - Leave The Door Open", "Lil Nas X - Montero", "Justin Bieber Featuring Daniel Caesar & Giveon - Peaches", "Brandi Carlile - Right On Time"], 

["Arooj Aftab", "Jimmie Allen", "Baby Keem", "FINNEAS", "Glass Animals", "Japanese Breakfast", "The Kid LAROI", "Arlo Parks", "Olivia Rodrigo", "Saweetie"], 

["Justin Bieber - Anyone", "Brandi Carlile - Right On Time", "Billie Eilish - Happier Than Ever", "Ariana Grande - Positions", "Olivia Rodrigo - drivers license"], 

["Tony Bennett & Lady Gaga - I Get A Kick Out Of You", "Justin Bieber & benny blanco - Lonely", "BTS - Butter", "Coldplay - Higher Power", "Doja Cat Featuring SZA - Kiss Me More"], 

["Tony Bennett & Lady Gaga - Love For Sale", "Norah Jones - Til We Meet Again (Live)", "Tori Kelly - A Tori Kelly Christmas", "Ledisi - Ledisi Sings Nina", "Willie Nelson - That's Life", "Dolly Parton - A Holly Dolly Christmas"], 

["Justin Bieber - Justice (Triple Chucks Deluxe)", "Doja Cat - Planet Her (Deluxe)", "Billie Eilish - Happier Than Ever", "Ariana Grande - Positions", "Olivia Rodrigo - Sour"], 

["Snoh Aalegra - Lost You", "Justin Bieber Featuring Daniel Caesar & Giveon - Peaches", "H.E.R. - Damage", "Silk Sonic - Leave The Door Open", "Jazmine Sullivan - Pick Up Your Feelings"],

["Jon Batiste - I Need You", "BJ The Chicago Kid, PJ Morton & Kenyon Dixon Featuring Charlie Bereal - Bring It On Home To Me", "Leon Bridges Featuring Robert Glasper - Born Again", "H.E.R. - Fight For You", "Lucky Daye Featuring Yebba - How Much Can A Heart Take"], 

["H.E.R. - Damage", "SZA - Good Days", "Heartbreak Anniversary - Giveon", "Silk Sonic - Leave The Door Open", "Jazmine Sullivan - Pick Up Your Feelings"], 

["Eric Bellinger - New Light", "Cory Henry - Something To Say", "Hiatus Kaiyote - Mood Valiant", "Lucky Daye - Table For Two", "Terrace Martin, Robert Glasper, 9th Wonder & Kamasi Washington - Dinner Party: Dessert", "Masego - Studying Abroad: Extended Stay"], 

["Snoh Aalegra - Temporary Highs In The Violet Skies", "Jon Batiste - We Are", "Leon Bridges - Gold-Diggers Sound", "H.E.R. - Back Of My Mind", "Jazmine Sullivan - Heaux Tales"], 


["Baby Keem Featuring Kendrick Lamar - Family Ties", "Cardi B - Up", "J. Cole Featuring 21 Savage & Morray - M Y . L I F E", "Drake Featuring Future & Young Thug - Way 2 Sexy", "Megan Thee Stallion - Thot S***"], 


["J. Cole Feat. Lil Baby - P R I D E . I S . T H E . D E V I L", "Doja Cat - Need To Know", "Lil Nas X Featuring Jack Harlow - Industry Baby", "Tyler, The Creator Featuring Youngboy Never Broke Again & Ty Dolla $ign - Wusyaname", "Kanye West Featuring The Weeknd & Lil Baby - Hurricane"], 


["DMX Featuring Jay-Z & Nas - Bath Salts", "Saweetie Featuring Doja Cat - Best Friend", "Baby Keem Featuring Kendrick Lamar - Family Ties", "Kanye West Featuring Jay-Z - Jail", "J. Cole Featuring 21 Savage & Morray - M Y . L I F E"], 


["J. Cole - The Off-Season", "Drake - Certified Lover Boy", "Nas - King's Disease II", "Tyler, The Creator - Call Me If You Get Lost", "Kanye West - Donda"]

]


#each element in vote_count is a dictionary with name of nominee and number of votes
votes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#manually fill in message ids instead of using database
message_id = [915119973226143754, 915120096333168680, 915120112317648946, 915120126850920488, 915120141040234506, 915120148162170910, 915120156689174610, 915120165493026826, 915120172459782154, 915120179527155752, 915120186569412639, 915120193565495296, 915120203371790367, 915120210984443916, 915120218282528788, 915120225278648360, 914953581252194357]

upper_values = [10, 10, 10, 10, 5, 5, 6, 5, 5, 5, 5, 6, 5, 5, 5, 5, 5]

nominee_amount = 5

index_list =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

links = ['https://discordapp.com', 'https://discordapp.com', 'https://discordapp.com', 'https://discordapp.com', 'https://discordapp.com', 'https://discordapp.com', 'https://discordapp.com', 'https://discordapp.com', 'https://discordapp.com', 'https://discordapp.com', 'https://discordapp.com', 'https://discordapp.com', 'https://discordapp.com', 'https://discordapp.com', 'https://discordapp.com', 'https://discordapp.com', 'https://discordapp.com',]


channel = client.get_channel(861394194526633984)
number_emojis = ['1️⃣', '2️⃣', '3️⃣','4️⃣','5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))
  launch = datetime.date(2021, 11, 30)
  today = datetime.date.today()
  for i in range(0, categories):
    embed = discord.Embed(title=awards[i], description="Nominees: ", color=0x00ff00, type="rich")
    #upper needs to be 1 less than the number of nominees based on the given ith award category 
    upper = upper_values[i]
    for j in range(0, upper):
      embed.add_field(name=number_emojis[j]+" "+str(nominees[i][j]), value="‎‎‎__", inline=True)
    channel = client.get_channel(861394194526633984)
    new_message = await channel.send(embed=embed)
    temp_message_id = new_message.id
    message_id[i] = temp_message_id
    channel_id_updated = new_message.channel.id
    guild_id = new_message.guild.id
    #522598197986721800
    link = "https://discordapp.com/channels/"+str(guild_id)+"/"+str(channel_id_updated)+"/"+str(temp_message_id)+""
    links[i] = link
    for k in range(0, upper):
      await new_message.add_reaction(emoji = number_emojis[k])

@client.command()
async def vote(ctx):
  embed = discord.Embed(title="Vote", description="Categories Listed Below:", color=0x00ff00, type="rich")
  for i in range(0, categories):
    embed.add_field(name=str(i+1) +". "+awards[i], value=links[i], inline=False)
  await ctx.channel.send(embed=embed)

@client.event
async def on_message(message):
    
  if message.author == client.user:
    return   
  #title of award - name of artist (x votes)
  
  if message.content.startswith('!show'):
    #populate votes list with updated number of votes based on reactions
    #create embed
    channel = client.get_channel(861394194526633984)
    #this process must be quicker
    for i in range(0, categories):
      grammy_msg = await channel.fetch_message(message_id[i])
      reaction_list = grammy_msg.reactions
      new_upper = (upper_values[i])
      temp_count = []
      for j in range(0, new_upper):
        temp_count.append(reaction_list[j].count)
      maximum = max(temp_count)
      index_list[i] = (temp_count.index(maximum))
      votes[i] = maximum
    embed = discord.Embed(title="Leaderboard", color=0x00ff00, type="rich")
    #add fields to embed (signifies # of categories)
    #format everything nicely
    for i in range(0, categories):
      maximum = max(votes)
      embed.add_field(name=awards[i], value =  nominees[i][index_list[i]]+ " | " + "Votes: " + str(votes[i]), inline=True)

    await message.channel.send(embed=embed)
  #when setting up server, just do the below for every single grammy voting option at once, then remove it from the code (copy ID from each of those messages)   
        
  await client.process_commands(message)

client.run(personal_token)
  