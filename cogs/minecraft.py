from discord.ext import commands
from os import getenv
from mcrcon import MCRcon
from mcstatus import MinecraftServer


class Minecraft(commands.Cog):
    """Minecraft specific commands."""

    def __init__(self, bot):
        self.bot = bot

        # Get our variables
        self.host = getenv('SERVER_IP')
        self.query_port = int(getenv('QUERY_PORT'))
        self.rcon_port = int(getenv('RCON_PORT'))
        self.rcon_pwd = getenv('RCON_PASSWORD')

        # Init our endpoints
        self.query_server = MinecraftServer(self.host, self.query_port)

    @commands.command(name='test_status', brief="Check our Minecraft server status.")
    @commands.has_permissions(administrator=True)
    async def status(self, ctx):
        """ Get server status """
        status = self.query_server.status()
        await ctx.channel.send(f"The server has {status.players.online} players and replied in {status.latency} ms")

    @commands.command(name='msg', brief="Message the server or a player.")
    @commands.has_permissions(administrator=True)
    async def msg(self, ctx, msg=None, player=None):
        """ Message server or a specific player """
        if player is None:
            with MCRcon(host=self.host, password=self.rcon_pwd, port=self.rcon_port) as mcr:
                mcr.command(f"say {msg}")
                await ctx.channel.send(f"Messaged Minecraft server")
        else:
            with MCRcon(host=self.host, password=self.rcon_pwd, port=self.rcon_port) as mcr:
                resp = mcr.command(f"tell {player} {msg}")
                await ctx.channel.send(f"Server response: {resp}")
