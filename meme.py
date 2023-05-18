import discord
from discord.ext import commands
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')




def get_duck_image_url():
     url = 'https://random-d.uk/api/random'
     res = requests.get(url)
     data = res.json()
     return data['url']
# def get_fox():
#     url = 'https://randomfox.ca/floof/'
#     res = requests.get(url)
#     data = res.json()
#     return data["image"]

@bot.command("duck")
async def duck(ctx):
#     '''Cada vez que se llama a la solicitud de pato, el programa llama a la función get_duck_image_url'''
     image_url = get_duck_image_url()
     await ctx.send(image_url)

# @bot.command()
# async def mem(ctx):
#     img_name = random.choice(os.listdir('images'))
#     with open(f'images/{img_name}', 'rb') as f:
#         picture = discord.File(f)
 
#     await ctx.send(file=picture)


@bot.command("mem")
async def mem(ctx):
     img_name = random.choice(os.listdir('images'))
     with open(f'images/{img_name}', 'rb') as f:
         picture = discord.File(f)
 
     await ctx.send(file=picture)



@bot.command()
async def consejo(ctx):
    consejos = [
        'Recuerda apagar las luces cuando no las necesites para ahorrar energía.',
        'Utiliza transporte público o comparte coche para reducir la contaminación del aire.',
        'Evita el uso de plásticos de un solo uso y opta por alternativas reutilizables.',
        'Planta árboles en tu comunidad para ayudar a combatir el cambio climático.',
        'Reduce tu consumo de agua cerrando el grifo mientras te cepillas los dientes o lavas los platos.',
        'Recicla tus residuos correctamente para minimizar el impacto ambiental.',
        'Compra productos locales y de temporada para reducir la huella de carbono del transporte.',
        'Ahorra papel imprimiendo solo cuando sea necesario y utiliza papel reciclado.',
        'Participa en actividades de limpieza comunitaria para mantener el medio ambiente limpio.',
        'Informa a otras personas sobre la importancia de cuidar el medio ambiente y cómo pueden contribuir.'
    ]
    consejo_aleatorio = random.choice(consejos)
    await ctx.send(consejo_aleatorio)

@bot.command()
async def articulos(ctx):
    sitios_web = [
        'https://www.ecologiaverde.com/consejos-para-el-buen-uso-de-la-basura-1590.html',
        'https://www.nationalgeographic.es/medio-ambiente/2020/09/como-reducir-residuos-domesticos',
        'https://www.ecoembes.com/es/blog/buenas-practicas-para-tirar-la-basura',
        'https://www.consumer.es/medio-ambiente/los-10-mandamientos-del-reciclaje-en-casa.html',
        'https://www.sostenibilidad.com/que-es-sostenibilidad/gestion-residuos/buenas-practicas-uso-los-contenedores/'
    ]
    sitio_web_aleatorio = random.choice(sitios_web)
    await ctx.send(sitio_web_aleatorio)

bot.run("tu token :)")
