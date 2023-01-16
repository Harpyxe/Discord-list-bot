import os
from discord.ext import commands
from urllib.request import urlopen
from bs4 import BeautifulSoup


###Timezone


###Beautiful soup setup
url_to_scrape = "https://special.goodsmile.info/popupparade/en/"

request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

soup = BeautifulSoup(page_html, "html.parser")




async def compare():

    ###Temp file for the old list so it will saved even when the bot is turned off
    with open("files\s_temp.txt", "r+") as f:
        old_list = f.readlines()


    ###Bsoup stuff
        a_tags = soup.find_all('a', class_="link", href=True)

    ###Temporary new list
        new_list = []
        new_list.clear()

    ###Use the first id since that one will always change when thereis an update
        for tag in a_tags[:1]:
            links = (tag['href'])
            ids = links.replace('https://www.goodsmile.info/en/product/', '')
            new_list.append(ids)

        
    ###Check if both lists are equal
        if new_list == old_list:
            #print('list1 and list2 are equal.')
            return True

        else:
            #print('lists arent equal')
            f.truncate()
            f.writelines(new_list)
            f.close
            return False




def get_links():
    thumbnail_elements = soup.find_all("img")

    link_list = []
    for element in thumbnail_elements[3:8]:
        link_end = (element['src'])[3:]
        link_start = str('https://special.goodsmile.info/popupparade/')
        link = link_start + link_end

        
        link_list.append(link)
        
    #print(link_list)
    return link_list


def get_desc():
    desc_elements = soup.find_all("img")
    
    desc_list = []
    for element in desc_elements[3:8]:
        desc = (element['alt'])
        
        desc_list.append(desc)
        
    return desc_list

def get_url():
    url_elements = soup.find_all('a', href=True)
    
    url_list = []
    for element in url_elements[6:11]:
        url = (element['href'])
        
        url_list.append(url)
        
    return url_list


