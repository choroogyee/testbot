import discord
import asyncio

client = discord.Client()

token = 'Njc1NTcxMjA1OTAxNzc4OTQ0.Xj5EvQ.7-yh9gNwdfLJFYaoTdz9SM-dNsc'

@clinet.event
async def on_ready():
    print(client.user.name)
    print(clinet.user.id)
    print("============")

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    
    if message.content.startswith('=도움말'):
        embed = discord.Embed(
            title = '테스트용 봇 도움말',
            description = '테스트 봇 전용 도움말을 볼수 있다.',
            colour = 0xffc0cb
        )
        embed.add_field(name='도움말', description = '도움말을 볼수 있습니다.', inline=False)
        embed.set_footer(text='테스트 전용 봇 입니다.')
        await client.send_message(embed=embed)
    
client.run(token)
