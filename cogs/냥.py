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

class λ₯(commands.Cog):
    def __init__(self, client):
        self.client = client
    @cog_ext.cog_slash(name="λ₯", 
                description="π λμΉμ΄ λμμ½",
                guild_ids=guild_ids,
                options=[
                    create_option(
                        name="λ΄μ©",
                        description="λ¬΄μ¨ λ΄μ©μΈκ°μ?",
                        option_type=3,
                        required=True,
                        choices=[
                            create_choice(
                                name="κ²½μ",
                                value="λ₯κ²½μ"
                            ),
                            create_choice(
                                name="μ¬ν",
                                value="λ₯μ¬ν"
                            ),
                            create_choice(
                                name="μ κΈ",
                                value="λ₯μ κΈ"
                            ),
                            create_choice(
                                name="μ μ",
                                value="λ₯μ μ"
                            )
                        ]
                    )
                ])
    async def _λ₯(self, ctx, λ΄μ©: str):
        if λ΄μ© == "λ₯κ²½μ":
            embed=discord.Embed(description="λ₯κ²½μ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/gDB9mzd/sidruddkr.gif")
            await ctx.send(embed=embed)
            
        elif λ΄μ© == "λ₯μ¬ν":
            embed=discord.Embed(description="λ₯μ¬ν", color=embed_color)
            embed.set_image(url="https://i.ibb.co/VxZ3g53/sidtmfvma.gif")
            await ctx.send(embed=embed)
            
        elif λ΄μ© == "λ₯μ κΈ":
            embed=discord.Embed(description="λ₯μ κΈ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/fXgGK2s/sidtjsrmf.gif")
            await ctx.send(embed=embed)
            
        elif λ΄μ© == "λ₯μ μ":
            embed=discord.Embed(description="λ₯μ μ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/d43H7m6/sidwjdtor.gif")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(λ₯(client))