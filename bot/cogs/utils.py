import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0xc7bef3
    
    # About command
    # TODO: Fill this out later
    @nextcord.slash_command(description="About Astra")
    async def about(self, interaction: Interaction):
        await interaction.response.send_message("TBA")
    
    # Ping command
    # ! This is a temporary command!
    @nextcord.slash_command(description="Replies with bot latency")
    async def ping(self, interaction: Interaction):
        latency = int(self.bot.latency * 1000)
        await interaction.response.send_message(f"Pong! My latency is {latency}ms.")
    
    # Server command
    # TODO: Comeback to this
    @nextcord.slash_command(description="Replies with server information")
    async def server(self, interaction: Interaction):
        guild = interaction.guild
        server = guild.name
        members = guild.member_count
        await interaction.response.send_message(f"The server name is {server}, and has {members} members!")
    
    # User command
    # TODO: Comeback to this
    @nextcord.slash_command(description="Replies with information about the user")
    async def user(self, interaction: Interaction, member: Member = None):
        if member is None:
            member = interaction.user
        name = member.name
        joined = member.joined_at
        timestamp = int(joined.timestamp())
        await interaction.response.send_message(f"The users's name is {name}, and joined <t:{timestamp}:F>!")
    
    # Avatar command
    @nextcord.slash_command(description="Replies with the avatar of the user")
    async def avatar(self, interaction: Interaction, member: Member = None):
        if member is None:
            member = interaction.user
        name = member.name
        url = member.avatar.url
        embed = nextcord.Embed(
            title=f"{name}'s Avatar",
            color=self.color
        )
        embed.set_image(url=url)
        await interaction.response.send_message(embed=embed)
    
    # Support command
    # TODO: Comeback to this
    @nextcord.slash_command(description="Get support")
    async def support(self, interaction: Interaction):
        await interaction.response.send_message("It is okay to need help, please contact 988 if you or a loved one are suicidal. (More resources coming soon!)")
    
    
    
def setup(bot):
    bot.add_cog(Utilities(bot))