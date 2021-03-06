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

class μν(commands.Cog):
    def __init__(self, client):
        self.client = client
    @cog_ext.cog_slash(name="μν", 
                description="π μμ΄νμ€λ μ λ λμμ½",
                guild_ids=guild_ids,
                options=[
                    create_option(
                        name="λ΄μ©",
                        description="λ¬΄μ¨ λ΄μ©μΈκ°μ?",
                        option_type=3,
                        required=True,
                        choices=[
                            create_choice(
                                name="λͺ¨μ λΉν¬",
                                value="μνλͺ¨μ λΉν¬"
                            ),
                            create_choice(
                                name="λ¬΄μ­",
                                value="μνλ¬΄μ­"
                            ),
                            create_choice(
                                name="μν¬μ€ν",
                                value="μνμν¬μ€ν"
                            ),
                            create_choice(
                                name="μμλλ°μ",
                                value="μνμμλλ°μ"
                            ),
                            create_choice(
                                name="μλ",
                                value="μνμλ"
                            ),
                            create_choice(
                                name="μ μ€",
                                value="μνμ μ€"
                            ),
                            create_choice(
                                name="νλ³΄ν₯",
                                value="μννλ³΄ν₯"
                            ),
                            create_choice(
                                name="λ±λΆ",
                                value="μνλ±λΆ"
                            ),
                            create_choice(
                                name="κ³ λ±λΆ",
                                value="μνκ³ λ±λΆ"
                            )
                        ]
                    )
                ])
    async def _μν(self, ctx, λ΄μ©: str):
        if λ΄μ© == "μνλͺ¨μ λΉν¬":
            embed=discord.Embed(description="μνλͺ¨μ λΉν¬", color=embed_color)
            embed.set_image(url="https://i.ibb.co/Zz4cNgc/dpvprahwkaqlzm.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "μνλ¬΄μ­":
            embed=discord.Embed(description="μνλ¬΄μ­", color=embed_color)
            embed.set_image(url="https://i.ibb.co/F4vXLqF/dpvprantjq.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "μνμν¬μ€ν":
            embed=discord.Embed(description="μνμν¬μ€ν", color=embed_color)
            embed.set_image(url="https://i.ibb.co/m4h4R5k/dpvprdkzmtmxk.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "μνμμλλ°μ":
            embed=discord.Embed(description="μνμμλλ°μ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/CmZwDHG/dpvprdlTdjTsms.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "μνμλ":
            embed=discord.Embed(description="μνμλ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/z23pdxp/dpvprtleh.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "μνμ μ€":
            embed=discord.Embed(description="μνμ μ€", color=embed_color)
            embed.set_image(url="https://i.ibb.co/3WJTBys/dpvprwjstjf.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "μννλ³΄ν₯":
            embed=discord.Embed(description="μννλ³΄ν₯", color=embed_color)
            embed.set_image(url="https://i.ibb.co/mDc9YKj/dpvprxoqhzlr.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "μνλ±λΆ":
            embed=discord.Embed(description="μνλ±λΆ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/HBbzskp/dpvprqoaqn.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "μνκ³ λ±λΆ":
            embed=discord.Embed(description="μνκ³ λ±λΆ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/pZmBY2F/dpvprrhqoaqn.png")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(μν(client))