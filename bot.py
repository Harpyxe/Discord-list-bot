# bot.py - python 3.11.0
# ----------
# WaifuManager V2
#
# A bot to let people write and access other people's lists in text form
# 
# It also has some small random functions
#
# Lists could be favourite characters, bands, movies or whatever
# ----------
# Kjell Unverricht 

import os
from dotenv import load_dotenv
import discord
from discord import app_commands
from discord.ext import tasks, commands
import json
import nekos
import requests
import random
import re
###Custom imports
from modules.pop_up import *
###DotENV
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
OWNER = os.getenv('OWNER')

###Files to load
waifu_file = 'files/waifu_list.json'
var_file = 'files/var.json'
quotes = 'files/quotes.json'
owner_id= 1111111111111111111111

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

command_prefix = "!"
prefix_help = "!help"
prefix_apex = "!apex"

###Startup
@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

    print("Bot is ready!")

    check.start()



#################################################################### List commands

@bot.tree.command(name="list")
async def hello(interaction: discord.interactions):
    try:
        #User id int
        user1 = interaction.user.mention.replace("<@","")
        user = user1.replace(">","")

        list = []
        f = open(waifu_file)

        # returns JSON object as 
        data = json.load(f)
        n = 1
        for x in range(0, 10):
            num = '"' + str(n) + '"'
            value=data["user"][user][str(n)],
            #print(num)
            list.extend(value)
            n += 1

        await interaction.response.send_message(f"{interaction.user.mention}" + " Waifu list: \n \n"
        ###List starts with 0
        "1. "+list[0]+"\n"
        "2. "+list[1]+"\n"
        "3. "+list[2]+"\n"
        "4. "+list[3]+"\n"
        "5. "+list[4]+"\n"
        "6. "+list[5]+"\n"
        "7. "+list[6]+"\n"
        "8. "+list[7]+"\n"
        "9. "+list[8]+"\n"
        "10. "+list[9]+"\n"
        )
    except:
        await interaction.response.send_message("Oops looks like you dont have a list yet.You can create one with the !new command!")

@bot.tree.command(name="listof")
@app_commands.describe(which_user = "Of which user do you want the list?")
async def say(interaction: discord.Interaction, which_user: str):
    try:
        #User id int
        user1 = which_user.replace("<@","")
        user = user1.replace(">","")

        list = []
        f = open(waifu_file)

        # returns JSON object as 
        data = json.load(f)
        n = 1
        for x in range(0, 10):
            num = '"' + str(n) + '"'
            value=data["user"][user][str(n)],
            #print(num)
            list.extend(value)
            n += 1

        await interaction.response.send_message(f"{interaction.user.mention}" + " Waifu list: \n \n"
        ###List starts with 0
        "1. "+list[0]+"\n"
        "2. "+list[1]+"\n"
        "3. "+list[2]+"\n"
        "4. "+list[3]+"\n"
        "5. "+list[4]+"\n"
        "6. "+list[5]+"\n"
        "7. "+list[6]+"\n"
        "8. "+list[7]+"\n"
        "9. "+list[8]+"\n"
        "10. "+list[9]+"\n"
        )
    except:
        await interaction.response.send_message("Oops looks like that user doesn't have a list.")

#################################################################### Apex commands

@bot.tree.command(name="apex_map")
async def say(interaction: discord.Interaction):

        resp = requests.get("ur key")
        data = resp.json()


        embedVar = discord.Embed(title="Apex - map rotation",
        colour = 0xffb6c1
        )
       
        embedVar.add_field(name=data["current"]["map"], 
        value=data["current"]["remainingTimer"]+"\n"+"\n" ,
        inline=False)


        embedVar.add_field(name="Next map", value=data["next"]["map"]+"\n",
        inline=True)
        

        await interaction.response.send_message(embed=embedVar)

@bot.tree.command(name="apex_predator")
async def say(interaction: discord.Interaction):

        resp = requests.get("ur key")
        data = resp.json()


        embedVar = discord.Embed(title="Apex - Predator",
        colour = 0xffb6c1
        )
       
        embedVar.add_field(name="RP", 
        value=data["RP"]["PC"]["val"],
        inline=False)

        await interaction.response.send_message(embed=embedVar)

@bot.tree.command(name="quote")
@app_commands.describe(which_user = "Of which user do you want a quote?")
async def say(interaction: discord.Interaction, which_user: str):

    f = open(quotes)
    data = json.load(f)

    try:
        someone1 = which_user.replace("<@","")
        someone = someone1.replace(">","")

        maxint_old=data["user"][str(someone)],
        maxint_new = str(maxint_old)
        all_int =  re.sub(r"\D+", ",", maxint_new)
        maxint = max(all_int)

        num = random.randint(1, int(maxint))
        value=data["user"][str(someone)][str(num)],

        quote_1 = str(value).replace("(","")
        quote_2 = quote_1.replace("'","")
        quote_3 = quote_2.replace('""','"')
        quote = quote_3.replace(",)","")

        await interaction.response.send_message("<@"+someone+"> said: "'"'+quote+'"')
        f.close
    except:
        await interaction.response.send_message("This user doenst have any quotes.")

@bot.tree.command(name="random_quote")
async def say(interaction: discord.Interaction):

    f = open(quotes)
    data = json.load(f)

    num = random.randint(1, 83)
    value=data["random"][str(num)],
    quote_1 = str(value).replace("(","")
    quote_2 = quote_1.replace("'","")
    quote_3 = quote_2.replace('""','"')
    quote = quote_3.replace(",)","")

    await interaction.response.send_message('"'+quote+'"')
    f.close

#################################################################### Help commands

@bot.tree.command(name="help")
async def say(interaction: discord.Interaction):

        embedVar = discord.Embed(title="Help - Commands", description="What commands are there?",
        colour = 0xffb6c1
        )

        embedVar.add_field(name="Waifu list commands", 
        value="!list \n !listof @user \n !addlist \n !edit number content \n Use - instead of spaces!",
        inline=False)


        embedVar.add_field(name="Pic commands", value="!pic <tag> \n tags can be found under !help pic",
        inline=False)

        embedVar.add_field(name="Apex commands", 
        value="!apex map \n !apex predator",
        inline=False)
        

        await interaction.response.send_message(embed=embedVar)

@bot.tree.command(name="help_pic")
async def say(interaction: discord.Interaction):

        embedVar = discord.Embed(title="!pic - Commands", description="Commands related to the !pic command",
        colour = 0xffb6c1
        )

        embedVar.add_field(name="Images", 
        value="neko \n kitsune \n waifu",
        inline=False)


        embedVar.add_field(name="Gif's", value="highfive \n happy \n sleep handhold \n laugh \n bite \n poke \n tickle \n kiss \n thumbsup \n stare \n cuddle \n smile \n  yeet \n slap \n kick \n hug",
        inline=True)
        embedVar.add_field(name="-", value="baka \n blush \n think \n pout \n facepalm \n wink \n shoot \n smug \n cry \n smile \n pat \n punch \n dance \n feed \n shrug \n bored", inline=True)


        await interaction.response.send_message(embed=embedVar)
















@bot.event
async def on_message(message):
    user_id = message.author.id
    if message.author == bot.user:
        return

#################################################################### Misc

    if message.content.startswith('gym'):

        await message.channel.send("Get a life!")

    if message.content.startswith(command_prefix+"quote"):
        f = open(quotes)
        data = json.load(f)
        if "<@" in message.content:
            try:
                old = message.content.split(command_prefix+"quote ",)
                someone_id = old[1]
                someone_1 = someone_id.replace("<@","")
                someone = someone_1.replace(">","")

                maxint_old=data["user"][str(someone)],
                maxint_new = str(maxint_old)
                all_int =  re.sub(r"\D+", ",", maxint_new)
                maxint = max(all_int)

                num = random.randint(1, int(maxint))
                value=data["user"][str(someone)][str(num)],

                quote_1 = str(value).replace("('","")
                quote = quote_1.replace("',)","")

                await message.channel.send("<@"+someone+"> said: "'"'+quote+'"')
                f.close
            except:
                await message.channel.send("This user doenst have any quotes.")  
        else:
            f = open(quotes)
            data = json.load(f)
            num = random.randint(1, 83)
            value=data["random"][str(num)],
            quote_1 = str(value).replace("(","")
            quote_2 = quote_1.replace("'","")
            quote_3 = quote_2.replace('""','"')
            quote = quote_3.replace(",)","")

            await message.channel.send('"'+quote+'"')
            f.close

#################################################################### Gif and pic commands

    if message.content.startswith(command_prefix+"pic"):

        #split the message to get the keyword
        msg = message.content
        tag = message.content.split(command_prefix+"pic"+" ", 1)

        #test tag
        #tag = "waifu"

         #Get response from API
        resp = requests.get("https://nekos.best/api/v2/"+tag[1])
        data = resp.json()
        await message.channel.send(data["results"][0]["url"])

    if message.content.startswith(command_prefix+"neko"):
        await message.channel.send(nekos.cat())

#################################################################### List commands

    if message.content.endswith(command_prefix+"list"):
        try:
                list = []
                f = open(waifu_file)
        
                # returns JSON object as 
                data = json.load(f)
                user = str(message.author.id)
                n = 1
                for x in range(0, 10):
                    num = '"' + str(n) + '"'
                    value=data["user"][user][str(n)],
                    #print(num)
                    list.extend(value)
                    n += 1

                await message.channel.send(f"<@{message.author.id}>" + " Waifu list: \n \n"
                ###List starts with 0
                "1. "+list[0]+"\n"
                "2. "+list[1]+"\n"
                "3. "+list[2]+"\n"
                "4. "+list[3]+"\n"
                "5. "+list[4]+"\n"
                "6. "+list[5]+"\n"
                "7. "+list[6]+"\n"
                "8. "+list[7]+"\n"
                "9. "+list[8]+"\n"
                "10. "+list[9]+"\n"
                )
        except:
            await message.channel.send("Oops looks like you dont have a list.")

    if message.content.startswith(command_prefix+"listof"):
        try:
            msg = message.content
            someone_all = message.content.split(command_prefix+"listof"+" ", 1)
            someone_1 = someone_all[1]
            someone_2 = someone_1.replace("<", "")
            someone_3 = someone_2.replace(">", "")
            someone = someone_3.replace("@", "")

            list = []
            f = open(waifu_file)

            # returns JSON object as 
            # a dictionary
            data = json.load(f)

            n = 1
            for x in range(0, 10):
                num = '"' + str(n) + '"'
                value=data["user"][someone][str(n)],
                #print(num)
                list.extend(value)
                n += 1

            await message.channel.send(f"<@{someone}>" + " Waifu list: \n \n"
            ###List starts with 0
            "1. "+list[0]+"\n"
            "2. "+list[1]+"\n"
            "3. "+list[2]+"\n"
            "4. "+list[3]+"\n"
            "5. "+list[4]+"\n"
            "6. "+list[5]+"\n"
            "7. "+list[6]+"\n"
            "8. "+list[7]+"\n"
            "9. "+list[8]+"\n"
            "10. "+list[9]+"\n"
            )
        except:
            await message.channel.send("Oops looks like that user doesn't have a list.")

    if message.content.startswith(command_prefix+"new"):



            with open(waifu_file, 'r+') as f:
                data = json.load(f)
                content = str(data)

                user = str(message.author.id)
                if user in content:                
                    await message.channel.send("Oops! Looks like you allready have a list.")
                    f.close



                else:
                    with open(waifu_file, 'r+') as f:
                        new_entry = f',"{message.author.id}"'': {"1" : "","2" : "","3" : "","4" : "","5" : "","6" : "","7" : "","8" : "","9" : "","10" : ""}}}'




                        new_content1 = content.replace("}}}","}")

                        ce = new_content1+new_entry

                        cee = ce.replace("'",'"')

                        #print(cee)

                        #json.dump(cee,f)

                        f.truncate()
                        f.write(cee)



                        await message.channel.send("<@"+user+"> has joined the degenerates! Check ur new list with !list or use the slash command.")
#Replace command
    if message.content.startswith(command_prefix+"replace"):


        try:
            msg = message.content
            split = msg.split(" ")
            num = split[1]

            sp = command_prefix+"replace"+" "+num+" "
            char = msg.replace(sp,"")

        except IndexError: 
            ###Timeout handler
            await message.channel.send("Hey, looks like you haven't given me enough arguments. I need the number and the name of the new character.")

        if int(num) in range(1, 10):

            replaced_list = []
            f = open(waifu_file)

            # returns JSON object as 
            data = json.load(f)
            user = str(message.author.id)

            value=data["user"][user][str(num)]
            #print(value)
            replaced_list.append(value)
            f.close
        
            with open(waifu_file, 'r') as f:

                new_data = json.load(f)
                new_data["user"][user][str(num)] = str(char)

                with open(waifu_file, 'w') as f:
                    f.write(json.dumps(new_data))

            f.close

            await message.channel.send(num +". "+"Replaced "+replaced_list[0]+" with "+char)

        else:
            await message.channel.send("Oops! Looks like you choose a number that isn't between 1-10.")
###Delete an entry from ur list
    if message.content.startswith(command_prefix+"delete"):

        try:
            msg = message.content
            split = msg.split(" ")
            num = split[1]

        except IndexError: 
            ###Timeout handler
            await message.channel.send("Hey, looks like you haven't given me enough arguments. I need the number of the character on your list.")
            return
        #print(char)

        if int(num) in range(1, 10):

            replaced_list = []
            f = open(waifu_file)

            # returns JSON object as 
            data = json.load(f)
            user = str(message.author.id)

            value=data["user"][user][str(num)]
            #print(value)
            replaced_list.append(value)
            print(replaced_list)
            f.close
        
            with open(waifu_file, 'r') as f:

                new_data = json.load(f)
                new_data["user"][user][str(num)]

                with open(waifu_file, 'w') as f:
                    f.write(json.dumps(new_data))

            f.close

            await message.channel.send('You have deleted '+num+'. "'+replaced_list[0]+'" from ur list!')
        else:
            await message.channel.send("Oops! Looks like you choose a number that isn't between 1-10.")

#################################################################### Apex commands

    if message.content.startswith(command_prefix+"apex"+" "+"map"):
        resp = requests.get("ur key")
        data = resp.json()


        embedVar = discord.Embed(title="Apex - map rotation",
        colour = 0xffb6c1
        )
       
        embedVar.add_field(name=data["current"]["map"], 
        value=data["current"]["remainingTimer"]+"\n"+"\n" ,
        inline=False)


        embedVar.add_field(name="Next map", value=data["next"]["map"]+"\n",
        inline=True)
        

        await message.channel.send(embed=embedVar)

    if message.content.startswith(command_prefix+"apex"+" "+"predator"):

        resp = requests.get("ur key")
        data = resp.json()


        embedVar = discord.Embed(title="Apex - Predator",
        colour = 0xffb6c1
        )
       
        embedVar.add_field(name="RP", 
        value=data["RP"]["PC"]["val"],
        inline=False)

        await message.channel.send(embed=embedVar)

#################################################################### Help commands

    if message.content.endswith(command_prefix+"help"):

        embedVar = discord.Embed(title="Help - Commands", description="What commands are there?",
        colour = 0xffb6c1
        )

        embedVar.add_field(name="Waifu list commands", 
        value="!list \n !listof @user \n !addlist \n !edit number content \n Use - instead of spaces!",
        inline=False)


        embedVar.add_field(name="Pic commands", value="!pic <tag> \n tags can be found under !help pic",
        inline=False)

        embedVar.add_field(name="Apex commands", 
        value="!apex map \n !apex predator",
        inline=False)
        

        await message.channel.send(embed=embedVar)

    if message.content.startswith(command_prefix+"help"+" "+"pic"):

        embedVar = discord.Embed(title="!pic - Commands", description="Commands related to the !pic command",
        colour = 0xffb6c1
        )

        embedVar.add_field(name="Images", 
        value="neko \n kitsune \n waifu",
        inline=False)


        embedVar.add_field(name="Gif's", value="highfive \n happy \n sleep handhold \n laugh \n bite \n poke \n tickle \n kiss \n thumbsup \n stare \n cuddle \n smile \n  yeet \n slap \n kick \n hug",
        inline=True)
        embedVar.add_field(name="-", value="baka \n blush \n think \n pout \n facepalm \n wink \n shoot \n smug \n cry \n smile \n pat \n punch \n dance \n feed \n shrug \n bored", inline=True)

        await message.channel.send(embed=embedVar)

####################################################################################################### Admin Stuff

###God Delete an entry from ANOTHER persons list
    if message.content.startswith(command_prefix+"Gdelete"):
        if message.author.id == 461110190922792960:
            try:
                msg = message.content
                split = msg.split(" ")
                victim_all = split[1]
                num = split[2]

                victim_1 = victim_all.replace("<@", "")
                victim = victim_1.replace(">", "")

            except IndexError: 
                ###Timeout handler
                await message.channel.send("Hey, looks like you haven't given me enough arguments. I need the number of the character on your list.")
                return

            if int(num) in range(1, 10):

                replaced_list = []
                f = open(waifu_file)

                # returns JSON object as 
                data = json.load(f)
                user = str(victim)

                value=data[user][str(num)],
                #print(value)
                replaced_list.extend(value)
                f.close
            
                with open(waifu_file, 'r') as f:

                    new_data = json.load(f)
                    new_data[user][str(num)] = ""

                    with open(waifu_file, 'w') as f:
                        f.write(json.dumps(new_data))

                f.close

                await message.channel.send('You have deleted '+num+'. "'+replaced_list[0]+'" from '+f"<@{victim}>"+' list!')

            else:
                await message.channel.send("Oops! Looks like you choose a number that isn't between 1-10.")

















@tasks.loop(hours=24.0)
async def check():

    get = await compare()
    if get:
        #print("no update")
        ###If True do nothing
        pass
    else:
        #print("update")
        links = []
        links.extend(get_links())

        desc = []
        desc.extend(get_desc())

        url = []
        url.extend(get_url())



        #print(desc[1:5])



        #print(links[1:5])

        channel = bot.get_channel("UR_CHANNEL_ID")

        embed=discord.Embed(title=desc[0], url=url[0], description="")
        embed.set_thumbnail(url=links[0])
        await channel.send(embed=embed)

        embed=discord.Embed(title=desc[1], url=url[1], description="")
        embed.set_thumbnail(url=links[1])
        await channel.send(embed=embed)

        embed=discord.Embed(title=desc[2], url=url[2], description="")
        embed.set_thumbnail(url=links[2])
        await channel.send(embed=embed)

        embed=discord.Embed(title=desc[3], url=url[3], description="")
        embed.set_thumbnail(url=links[3])
        await channel.send(embed=embed)

        embed=discord.Embed(title=desc[4], url=url[4], description="")
        embed.set_thumbnail(url=links[4])
        await channel.send(embed=embed)





























bot.run(TOKEN)