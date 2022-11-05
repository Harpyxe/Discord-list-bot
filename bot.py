# bot.py - python 3.9.13
# ----------
# A bot to let people write and access other people's lists in text form
# 
# It also has some small random functions
#
# Lists could be favourite characters, bands, movies or whatever
# ----------
# Kjell Unverricht 


#Imports
import os
from sys import prefix
from dotenv import load_dotenv
import discord
import nekos
import requests
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.core import command

#Needs a file named .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
OWNER = os.getenv('OWNER')

intents = discord.Intents.all()

prefix = "!"
prefix_help = "!help"
prefix_apex = "!apex"
bot = discord.Client()
client = discord.Client()



#Startup output
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print((OWNER)+"'s bot")





#def what file to open
f = open(r'list.txt', encoding='utf-8')

file = open(r'list.txt', encoding='utf-8')



@client.event
async def on_message(message):
    if message.author == client.user:
        return



#def user_id
    user_id = message.author.id
    


#random answer functions
    if message.content.startswith('wm!owner'):
        await message.channel.send(OWNER)

#Ping yourself
    if message.content.startswith('wm!ping'):
        print(message.author.id)
        await message.channel.send(f"<@{message.author.id}>")



#request your own list
    if message.content.endswith(prefix+"list"):
            with open("list.txt", "r") as list:
                list = list.readlines()
                user_id = str(message.author.id)
                counter = 0
                ausgabe = ""
                for word in list:
                    counter = counter + 1
                    if user_id in word:
                        for zeile in range(counter, counter +10):
                            ausgabe = ausgabe + list[zeile]
                        await message.channel.send((f"<@{message.author.id}>")+"'s list:"+"\n"
                        +"\n"+ausgabe)
                        list.close()
                list.close()



#request someones list
    if message.content.startswith(prefix+"listof"):

            with open("list.txt", "r") as list:


                #split the message to get the keyword
                msg = message.content
                someone_all = message.content.split(prefix+"listof"+" ", 1)
                someone_1 = someone_all[1]
                someone_2 = someone_1.replace("<", "")
                someone_3 = someone_2.replace(">", "")
                someone = someone_3.replace("@", "")


                content_list = list.readlines()
                user_id = someone
                counter = 0
                ausgabe = ""
                for word in content_list:
                    counter = counter + 1
                    if user_id in word:
                        for zeile in range(counter, counter +10):
                            ausgabe = ausgabe + list[zeile]
                        await message.channel.send(someone_1+"'s list:"+"\n"
                        +"\n"+ausgabe)
                        list.close()
                list.close()





#Add a list for yourself
    if message.content.startswith("!addlist"):

            with open('list.txt', 'r') as list:
                list = list.readlines()
                user_id = str(message.author.id)
                check = False
                for word in list:
                    if user_id in word:
                        check = True
                        list.close() 
            if check == True:
                await message.channel.send("Du hast bereits eine Liste")
            else:
                with open("list.txt", "a") as n:
                    n.write("\n" + str(message.author.id))
                    for num in range(1,11):
                        n.write("\n" + str(num) + ". ") 
                    n.close()


#edit your own list
# Will get reworked
    if message.content.startswith("!editlist"):
        with open('list.txt', 'r') as list:
            list = list.readlines()
            user_id = str(message.author.id)
            counter = 0
            for word in list:
                counter = counter + 1
                if user_id in word:
                    list.close()
                    if message.content.startswith("!editlist1"):
                        with open('list.txt', 'r', encoding='utf-8') as file:
                            data = file.readlines()
                        msg = message.content
                        con = msg.split(" " , 1)
                        data[counter] = "1.  "+ str(con[1])+"\n"
                        
                        with open('list.txt', 'w', encoding='utf-8') as file:
                            file.writelines(data)
                            file.close()
                    elif message.content.startswith("!editlist2"):
                        with open('list.txt', 'r', encoding='utf-8') as file:
                            data = file.readlines()
                        msg = message.content
                        con = msg.split(" " , 1)
                        data[counter + 1] = "2.  "+ str(con[1])+"\n"
                        
                        with open('list.txt', 'w', encoding='utf-8') as file:
                            file.writelines(data)
                            file.close()
                    elif message.content.startswith("!editlist3"):
                        with open('list.txt', 'r', encoding='utf-8') as file:
                            data = file.readlines()
                        msg = message.content
                        con = msg.split(" " , 1)
                        data[counter + 2] = "3.  "+ str(con[1])+"\n"
                        
                        with open('list.txt', 'w', encoding='utf-8') as file:
                            file.writelines(data)
                            file.close()
                    elif message.content.startswith("!editlist4"):
                        with open('list.txt', 'r', encoding='utf-8') as file:
                            data = file.readlines()
                        msg = message.content
                        con = msg.split(" " , 1)
                        data[counter + 3] = "4.  "+ str(con[1])+"\n"
                        
                        with open('list.txt', 'w', encoding='utf-8') as file:
                            file.writelines(data)
                            file.close()
                    elif message.content.startswith("!editlist5"):
                        with open('list.txt', 'r', encoding='utf-8') as file:
                            data = file.readlines()
                        msg = message.content
                        con = msg.split(" " , 1)
                        data[counter + 4] = "5.  "+ str(con[1])+"\n"
                        
                        with open('list.txt', 'w', encoding='utf-8') as file:
                            file.writelines(data)
                            file.close()
                    elif message.content.startswith("!editlist6"):
                        with open('list.txt', 'r', encoding='utf-8') as file:
                            data = file.readlines()
                        msg = message.content
                        con = msg.split(" " , 1)
                        data[counter + 5] = "6.  "+ str(con[1])+"\n"
                        
                        with open('list.txt', 'w', encoding='utf-8') as file:
                            file.writelines(data)
                            file.close()
                    elif message.content.startswith("!editlist7"):
                        with open('list.txt', 'r', encoding='utf-8') as file:
                            data = file.readlines()
                        msg = message.content
                        con = msg.split(" " , 1)
                        data[counter + 6] = "7.  "+ str(con[1])+"\n"
                        
                        with open('list.txt', 'w', encoding='utf-8') as file:
                            file.writelines(data)
                            file.close()
                    elif message.content.startswith("!editlist8"):
                        with open('list.txt', 'r', encoding='utf-8') as file:
                            data = file.readlines()
                        msg = message.content
                        con = msg.split(" " , 1)
                        data[counter + 7] = "8.  "+ str(con[1])+"\n"
                        
                        with open('list.txt', 'w', encoding='utf-8') as file:
                            file.writelines(data)
                            file.close()
                    elif message.content.startswith("!editlist9"):
                        with open('list.txt', 'r', encoding='utf-8') as file:
                            data = file.readlines()
                        msg = message.content
                        con = msg.split(" " , 1)
                        data[counter + 8] = "9.  "+ str(con[1])+"\n"
                        
                        with open('list.txt', 'w', encoding='utf-8') as file:
                            file.writelines(data)
                            file.close()
                    elif message.content.startswith("!editlist0"):
                        with open('list.txt', 'r', encoding='utf-8') as file:
                            data = file.readlines()
                        msg = message.content
                        con = msg.split(" " , 1)
                        data[counter + 9] = "10. "+ str(con[1])+"\n"
                        
                        with open('list.txt', 'w', encoding='utf-8') as file:
                            file.writelines(data)
                            file.close()



#If the owner writes message asnwer XXXXXX = Discord_id
    if message.content.startswith(prefix+'hey'):
        if message.author.id == "XXXXXXXXXXXXX":
            await message.channel.send("Yes")
        else:
            await message.channel.send("No")



#Get a Cat picture from API
    if message.content.startswith(prefix+"neko"):
        await message.channel.send(nekos.cat())



#Get an Anime picture (by tag) from API
    if message.content.startswith(prefix+"pic"):

        #split the message to get the keyword
        msg = message.content
        tag = message.content.split(prefix+"pic"+" ", 1)

         #Get response from API
        resp = requests.get("https://nekos.best/api/v2/"+tag[1])
        data = resp.json()
        await message.channel.send(data["results"][0]["url"])




#current Apex Legends map ["current"]["tag"]
    if message.content.startswith(prefix_apex+" "+"map"):

        resp = requests.get("https://api.mozambiquehe.re/maprotation?auth=966aeadd0efd48191f9979c5b419d6c7")
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




#current Apex Legends predator stats ["current"]["tag"]
    if message.content.startswith(prefix_apex+" "+"predator"):

        resp = requests.get("https://api.mozambiquehe.re/predator?auth=966aeadd0efd48191f9979c5b419d6c7")
        data = resp.json()


        embedVar = discord.Embed(title="Apex - Predator",
        colour = 0xffb6c1
        )
       
        embedVar.add_field(name="RP", 
        value=data["RP"]["PC"]["val"],
        inline=False)

        await message.channel.send(embed=embedVar)






#Generall help command
    if message.content.endswith(prefix_help):

        embedVar = discord.Embed(title="Help - Commands", description="What commands are there?",
        colour = 0xffb6c1
        )

        embedVar.add_field(name="list commands", 
        value="!list \n !listof @user \n !addlist (dont) \n !editlistX X=0-9 / 0=10",
        inline=False)


        embedVar.add_field(name="pic commands", value="!pic <tag> \n tags can be found under !help pic",
        inline=False)

        embedVar.add_field(name="Apex commands", 
        value="!apex map \n !apex predator",
        inline=False)
        

        await message.channel.send(embed=embedVar)





#Help command for the pic command
    if message.content.startswith(prefix_help+" "+"pic"):

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




client.run(TOKEN)
