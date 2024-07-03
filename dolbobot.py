## dolbobot by chapo
TOKEN = 'MTA1Mjg5ODQ4NDI4MzUyMzA5Mg.Gby-Ak.5gumRk8-GypGTKDAzLU-SsaXDXgryP90oimfIo'
import nextcord
from nextcord.ext import commands

bot = commands.Bot()

@bot.slash_command(name='givemefuckingbadgedolbaeb')
async def send(interaction: nextcord.Interaction):
    await interaction.response.send_message('https://media.discordapp.net/attachments/685881366906273792/947944670091153408/emojibest_com_AnimatedSticker.gif', ephemeral=True)

bot.run(TOKEN)