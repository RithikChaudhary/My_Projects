
import discord
from discord.ext import commands
import random
import asyncio

client = commands.Bot(command_prefix='#')

@client.event
async def on_ready():
    print('Bot is Ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Whats Up Boys! {round(client.latency * 1000)}ms ')

@client.command(aliases = ['Magic8Ball', 'test'])
async def _8ball(ctx, *, question):

        responses = ['As I see it, yes.',
                        'Ask again later.',
                        'Better not tell you now.',
                        'Cannot predict now.',
                        'Concentrate and ask again.',
                        'Don’t count on it.',
                        'It is certain.',
                        'It is decidedly so.',
                        'Most likely.',
                        'My reply is no.',
                        'My sources say no.',
                        'Outlook not so good.',
                        'Outlook good.',
                        'Reply hazy, try again.',
                        'Signs point to yes.',
                        'Very doubtful.',
                        'Without a doubt.',
                        'Yes.',
                        'Yes – definitely.',
                        'You may rely on it.']

        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def clc(ctx, amount=21):

    await ctx.channel.purge(limit=amount)


@client.command()
@commands.has_permissions(kick_members=True)
async def gone_girl(ctx, member: discord.Member, mute_time: int):
    guild = ctx.guild
    for role in guild.roles:
        if role.name == "Bye Buddy":
            await member.add_roles(role)
            await ctx.send("{} come back after {} seconds!" .format(member.mention, mute_time))
            await asyncio.sleep(mute_time)
            await member.remove_roles(role)
            await ctx.send("{} come back BB!" .format(member.mention))


@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

client.run('ODA4MTIwNzQzNjgxNTg5Mjk4.YCB7Fw.L4HrsacMaooq5Iw_D6ipAb5Ts1M')
