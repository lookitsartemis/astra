import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0xc7bef3
        
    @nextcord.slash_command(description="About Astra")
    async def about(self, interaction: Interaction):
        bot = self.bot
        ping = int(bot.latency * 1000)
        name = bot.user.mention
        id = bot.user.id
        servers = len(bot.guilds)
        members = sum(guild.member_count for guild in bot.guilds)
        embed = nextcord.Embed(
            title="About",
            color=self.color
        )
        embed.add_field(
            name="About Me",
            value="test",
            inline=False
        )
        embed.add_field(
            name="Statistics",
            value=f"""
            > **Name:** {name}
            > **ID:** {id}
            > **Owner:** <@1241249326844350491>
            > **Ping:** {ping}
            > **Servers:** {servers}
            > **Members:** {members}
            """,
            inline=False
        )
        embed.set_thumbnail(self.bot.user.avatar.url)
        await interaction.response.send_message(embed=embed)
        
    @nextcord.slash_command(description="Replies with bot latency")
    async def ping(self, interaction: Interaction):
        ping = int(self.bot.latency * 1000)
        embed = nextcord.Embed(
            title="Ping",
            color=self.color,
            description=f"""
            ***Bot Latency***
            > * **Latency:** {ping}
            """
        )
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        await interaction.response.send_message(embed=embed)
    
def setup(bot):
    bot.add_cog(Utilities(bot))