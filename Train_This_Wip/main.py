import os
from file_man import File_Man
import requests
import html
from bs4 import BeautifulSoup, SoupStrainer
import re
from urlextract import URLExtract

    



class Trainer():
    def __init__(self, **kw):
        super(Trainer, self).__init__(**kw)
        pass



    def get_codes(self, soup):
        try:
            print("[STACK_SOUP]:\n\n>>",str(soup))
            codes = soup.index("<code>", "</code>")
            print("\n\ncodes: ", str(codes))

            return codes
        except Exception as e:
            print(f"[E]:[GET_CODES]:[>{str(e)}<]")


    def get_links(self, soup):
        try:
            extractor = URLExtract()
            urls = extractor.find_urls(soup)
            return urls
        except Exception as e:
            print(f"[E]:[GET_LINKS]:[>{str(e)}<]")

    def get_stack(self, soup):
        try:
            sof_links = []
            print("[SEARCHING_FOR_STACK_OF]:[SOUP.BODY] ")
            hrefs = soup.split('href="/url?q=')
            for i, h in enumerate(hrefs):
                if "https://stack" not in h:
                    continue
                else:
                    sof_links.append(str(h.split("&")[0]))
                    print("[HREF]: ",str(h.split("&")[0]))
            return sof_links

        except Exception as e:
            print(f"[E]:[print_LINKS]:[>{str(e)}<]")



    def check_flags(self, cmd_in):
        try:
            print("[CMD_IN]:", cmd_in)
        except Exception as e:
            print(f"[E]:[print_LINKS]:[>{str(e)}<]")



    def main(self):
        try:
            mycmd = ""
            my_cmd = []
            stack_link = ""
            stk_r = ""
            to_find = 'https://www.google.com/search?client=firefox-b-e&q=' #str(my_cmd[1:])
            while True:

                mycmd = input(">> ")+" "
                my_cmd = mycmd.split(" ")


                # FIND -> 'WEB_SEARCH'
                if "find" in my_cmd:
                    try:
                        if len(my_cmd) > 1:
                            print("SEARCHING: ", str(my_cmd[1:]))
                            for i, val in enumerate(my_cmd):
                                if i > 0:
                                    to_find+=str(val)+"+"
                            to_find = str(to_find[:-1])
                            print("[TO_FIND]:", to_find)

                            r = requests.get(to_find)
                            print("[GET]:[RESPONSE]:", str(r))

                            html = r.text
                            #print(html.unescape(r.text))

                            soup = BeautifulSoup(html, "html.parser")

                            #print(soup.body.get_text('href').strip())
                            #print(soup.body)


                            self.get_stack(str(soup.body))

                            #links = self.get_links(soup.body.get_text())
                            #for link in links:
                            #    print("[LINK]:",str(link))
                            #    if "stackoverflow" in link:
                            #        print("[CHECKING_STACKOVERFLOW]", str(link))
                            #        stk_r = requests.get(link)
                            #        print("[STK_R]: ",str(stk_r))
                            #        stk_h = stk_r.text
                            #        s_soup = BeautifulSoup(stk_h, "html.parser")
                            #        self.get_codes(s_soup)
#




  
                    except Exception as c:
                        print(f"[E]:[FIND]:[>{str(c)}<]")
        except Exception as e:
            print(f"[E]:[MAIN_LOOP]:[>{str(e)}<]")


if __name__=="__main__":
    T = Trainer()
    T.main()





#r = requests.get(url = URL, params = PARAMS)
#  # extracting data in json format
#data = r.json()
# extracting latitude, longitude and formatted address 
## of the first matching location
#latitude = data['results'][0]['geometry']['location']['lat']
#longitude = data['results'][0]['geometry']['location']['lng']
#formatted_address = data['results'][0]['formatted_address']
  