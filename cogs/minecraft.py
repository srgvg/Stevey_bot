from discord.ext import commands


class Minecraft(commands.Cog):
    """Minecraft specific commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='test', brief="Test bot is getting my commands")
    async def test(self, ctx, argument=''):
        await ctx.channel.send(f"You sent me: {argument}")
