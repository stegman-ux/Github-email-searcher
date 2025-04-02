import requests
import colorama
from colorama import Fore
import fade
import clear
import os


def imskid():
    ascii_art = """
                /|  /|  -----------------------------------
                ||__||  |                                 |
               /   O O\__  I am a big hacker !!           |
              /          \ I can find your github email ! |
             /      \     \                               |
            /   _    \     \ ------------------------------
           /    |\____\     \      ||
          /     | | | |\____/      ||
         /       \| | | |/ |     __||
        /  /  \   -------  |_____| ||
       /   |   |           |       --|
       |   |   |           |_____  --|
       |  |_|_|_|          |     \----
       /\                  |
      / /\        |        /
     / /  |       |       | Made by intrable (stegman-ux)
 ___/ /   |       |       | Simple script
|____/    c_c_c_C/ \C_c_c_c
    """
    os.system("title GithubEmail By Intrable")
    clear.clear()
    print(fade.brazil(ascii_art))
    Username = input(Fore.LIGHTYELLOW_EX+"Enter the github username --> ")
    repos = input(Fore.LIGHTYELLOW_EX+"Enter the name of the github repositorie --> ")
    res = requests.get(f"https://api.github.com/repos/{Username}/{repos}/commits")
    data = res.json()
    first_commit = data[0] # ici je récpurere le premier commits car sinon le terminal serais remplis de fou
    author = first_commit.get('commit', {}).get('author', {})  # je n'ai pas pue directement obtenir les infos en faisant un data.get donc j'ai cherché de l'aide sur internet , cette ligne n'a pas étais fais par moi ! 
    Email = author.get('email', 'N/A')
    User = author.get('name', 'N/A')
    print(f"""
+----+------------------+-------------+
| ID | Username         | Email       | 
+----+------------------+-------------+ 
| 1  | {User}           | {Email}     |
+----+-------------+------------------+""") # le "id" c'est pour le style et j'me suis donner pour le print en vraie les mec
    input(Fore.WHITE+"Press enter for exit...")
    
imskid()


