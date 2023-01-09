#Santa Bot V1.00
import discord
from discord.ext import commands
import random
import os
from json import dump, load

game = discord.Game('Santa Simulator')

#inizializza una lista utenti (ho messo due utenti solo per testare che il codice funziona
listaUtenti = []            
#funzione che lista gli utenti
def elencoUtenti(l):                   
    for i in l:
        print(i[0])
        
#guarda se un utente è già nella lista
def trovaUtenteInLista(lista, utente):
    contatore = 0
#se trova l'utente ritorna la sua posiz in lista
    for i in lista:
        if utente == i[0]:
            return contatore                    

        contatore += 1
#se finisce la lista senza trovare utente, ritorna -1.
    return -1                           

os.chdir(r'YOUR_FILE_LOCATION_HERE')
client = commands.Bot(command_prefix = '.')
caramella = 0
fp = open("caramelle.json", "r")
listaUtenti = load(fp)
fp.close()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=game)
    print('Santa Bot è pronto!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.author.bot:
        return
    elif message.content.startswith('.natale'):
        await message.channel.send('Sogna sotto le stelle\ntutte le cose più belle.\nNel cuore del suo sogno,\nsai chi c’è?\nUn regalo tutto per sé.')
    elif message.content.startswith('.regali'):
        indice = trovaUtenteInLista(listaUtenti, str(message.author))
        if indice == -1:
            listaUtenti.append([str(message.author), 0])
            #print(listaUtenti[indice][0],listaUtenti[indice][1])
            await message.channel.send('Benvenuto ' + str(message.author.mention) + ', per ora hai 0 regali')
            fp = open("caramelle.json", "w")
            dump(listaUtenti, fp)
            fp.close()
        else:
            await message.channel.send(str(message.author.mention) + ' hai ' + str(listaUtenti[indice][1]) + ' regali!') #print(listaUtenti[indice][1])
            #print(listaUtenti[indice][0],listaUtenti[indice][1])
    else:
        #print('Caramella')
        caramella = random.randint(1,10)
        #print(caramella)
        if caramella == 1:
            indice = trovaUtenteInLista(listaUtenti, str(message.author))
            if indice == -1:
                listaUtenti.append([str(message.author), 0])
                #print(listaUtenti[indice][0],listaUtenti[indice][1])
                #print('messaggio arrivato')
                await message.channel.send('Oh Oh Oh! Complimenti ' + str(message.author.mention) + ', hai ottenuto un regalo!')
                indice = trovaUtenteInLista(listaUtenti, str(message.author))
                listaUtenti[indice][1] += 1
                #print(listaUtenti[indice][0],listaUtenti[indice][1])
                fp = open("caramelle.json", "w")
                dump(listaUtenti, fp)
                fp.close()
            else:
                #print('messaggio arrivato')
                await message.channel.send('Oh Oh Oh! Complimenti ' + str(message.author.mention) + ', hai ottenuto un regalo!')
                indice = trovaUtenteInLista(listaUtenti, str(message.author))
                listaUtenti[indice][1] += 1
                #print(listaUtenti[indice][0],listaUtenti[indice][1])
                fp = open("caramelle.json", "w")
                dump(listaUtenti, fp)
                fp.close()

client.run('YOUR_TOKEN_HERE')
