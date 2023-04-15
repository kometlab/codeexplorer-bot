import discord
import requests, json

def handle_response(message: str=None, ctx: discord.Message=None, *args) -> (str|None):
    if not message == None:
        message = message.lower()
        if message == 'serverinfo':
            return [f"Server ID - ||`{ctx.guild.id}`||\nCreated On - `{ctx.guild.created_at.strftime('%b %d %Y')}`\nMembers - `{ctx.guild.member_count}`", "Server Info", ctx.guild.icon]
        elif message == 'userinfo':
            return [f'Name - ||`{ctx.author}`||\nDiscord Join Date - `{ctx.author.created_at}`\nServer join Date - `{ctx.author.joined_at}`', f'{ctx.author} info', ctx.author.avatar]
        elif message == 'help':
            return ['Prefixes are responsible for sending messages:\n`!` - send message globally, everyone will see it.\n`?` - local, this will be a private message.\nCommands:\n`!serverinfo` - gives information about the server.\n`!userinfo` - gives information about the person.\n`!responseurl` - you can take information from the link accepts 1 parameters `[url] -> json`\n`!sendbot` - sends information on behalf of the bot accepts 2 parameters `[title], [text]`', 'Help Menu', ctx.guild.icon]
        elif message.split(' ')[0] == 'responseurl':
            try:
                respone = requests.get(message.split(' ')[1]); data = respone.json()
                return ['```json\n'+str(data).replace("'", '"')+'\n```', f'Json response from {message.split(" ")[1]}']
            except Exception as error:
                return ["Function Failed!", error]
        elif message.split(' ')[0] == 'sendbot':
            return [" ".join(message.split(' ')[2:]), message.split(' ')[1]]