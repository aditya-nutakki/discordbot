import discord
from discord.ext import commands
import random
import os

client = commands.Bot(command_prefix=".")

emotes = [":100:", ":innocent:", ":laughing:", ":poop:", ":watermelon:", ":weary:", ":tired_face:", ":heart_eyes:",
          ":blush:", ":star_struck:", ":grinning:", ":sweat_smile:", ":joy:", ":rofl:", ":slight_smile:",
          ":partying_face:", ":zany_face:", ":rage:", ":sunglasses:", ":nerd:", ":exploding_head:", ":cold_face:",
          ":scream:", ":liar:", ":hushed:",
          ":dizzy_face:", ":smiling_imp:", ":clap:", ":raised_hands:", ":punch:", ":muscle:", ":kiss:", ":cop:",
          ":high_heel:", ":rainbow:", ":man_in_manual_wheelchair:", ":sweat_drops:", ":peach:", ":eggplant:",
          ":trophy:", ":toilet:", ":tada:", ":wheelchair:",
          ":x:", ":fire:", ":crown:", ":see_no_evil:", ":new_moon_with_face:"]



def rand_emotes(rand_num):
    os = ""
    for i in range(0 , rand_num):
        os = os + random.choice(emotes)

    return os


@client.event
async def on_ready():
    print("Bot is running")


@client.command()
async def myping(ctx):
    user = str(ctx.message.author)
    await ctx.send(f"{user[:-5]}'s ping = {round(client.latency*1000)}ms")

@client.command()
async def clear(ctx , amount = 5):
    await ctx.channel.purge(limit = int(amount+1))

@client.command()
async def echo(ctx,*, message):
    await ctx.send(f"@{ctx.message.author} says '{message}' ")

@client.command()
async def emote(ctx , * , message):

    words = message.split()
    message = ""

    for word in words:
        rand_num = random.randint(0, 3)

        emote_word = rand_emotes(rand_num)
        message = message +" "+ word + " " + emote_word

    await ctx.send(message)


@client.command()
async def playsound(ctx , tune):

    try:
        channel = ctx.author.voice.channel
    except:
        await ctx.send("You must be in a voice channel")

    channel = ctx.author.voice.channel

    tune = tune+".mp3"
    try:
        await channel.connect()
    except:
        pass

    fp = ""

    tunes = os.listdir("audio")

    if tune in tunes:
        fp = "audio/"+tune

    else:
        await ctx.send("Playsound not found")



    audio = discord.FFmpegPCMAudio(fp)
    guild = ctx.guild

    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    voice_client.play(source=audio)




@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


@client.command()
async def helpme(ctx):
    await ctx.send(".emote -> (input is a sentence) makes emotes out of your sentence \n"
                   ".myping -> gives your ping \n"
                   ".clear -> deletes last n sentences , default set to 5 \n"
                   ".echo -> says what you say \n"
                   ".playsound -> input is the name of an audio file and plays it ; for example: .playsound crabrave\n"
                   ".kill @playername -> kicks someone if you have permission\n")


@client.command()
async def kill(ctx , member :discord.Member , * , reason = None):
    try:
        await member.kick(reason=reason)
    except:
        await ctx.send("You dont have permission to kick")




client.run("NzQ4OTAyNTY1MDAxMDM1Nzg3.X0kL3Q.3KC_F8vf2hXCel1O9gGuVWQB0Rg")


