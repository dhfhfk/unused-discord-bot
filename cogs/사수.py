from discord_slash.utils.manage_commands import create_option, create_choice
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord_slash import cog_ext, SlashContext, SlashCommand
from discord import DMChannel
import re
import asyncio
import os


guild_ids = [int(os.environ['guild_id'])]
embed_color = 0x4ac8c7

class μ¬μ(commands.Cog):
    def __init__(self, client):
        self.client = client
    @cog_ext.cog_slash(name="μ¬μ", 
                description="π λ¦¬μ¬μ λμμ½",
                guild_ids=guild_ids,
                options=[
                    create_option(
                        name="λ΄μ©",
                        description="λ¬΄μ¨ λ΄μ©μΈκ°μ?",
                        option_type=3,
                        required=True,
                        choices=[
                            create_choice(
                                name="μμ",
                                value="μ¬μμμ"
                            ),
                            create_choice(
                                name="νλ¨",
                                value="μ¬μνλ¨"
                            ),
                            create_choice(
                                name="μλ",
                                value="μ¬μμλ"
                            ),
                            create_choice(
                                name="μ¬κΈ",
                                value="μ¬μμ¬κΈ"
                            ),
                            create_choice(
                                name="ν΄λ½",
                                value="μ¬μν΄λ½"
                            )
                        ]
                    )
                ])
    async def _μ¬μ(self, ctx, λ΄μ©: str):
        if λ΄μ© == "μ¬μμμ":
            embed=discord.Embed(description="μ¬μμμ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/N1rGd22/tktndntdma.gif")
            await ctx.send(embed=embed)
        elif λ΄μ© == "μ¬μνλ¨":
            embed=discord.Embed(description="μ¬μνλ¨", color=embed_color)
            embed.set_image(url="https://i.ibb.co/6WD90vm/tktnghkska.gif")
            await ctx.send(embed=embed)
        elif λ΄μ© == "μ¬μμλ":
            embed=discord.Embed(description="μ¬μμλ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/nncpZXx/tktnwkfkd.gif")
            await ctx.send(embed=embed)
        elif λ΄μ© == "μ¬μμ¬κΈ":
            embed=discord.Embed(description="μ¬μμ¬κΈ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/sP9nZTV/tktn-Tjsrmf.gif")
            await ctx.send(embed=embed)
        elif λ΄μ© == "μ¬μν΄λ½":
            embed=discord.Embed(description="μ¬μν΄λ½", color=embed_color)
            embed.set_image(url="https://i.ibb.co/DwHvbhs/tktnzmffjq.gif")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(μ¬μ(client))