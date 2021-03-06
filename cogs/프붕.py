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

class νλΆ(commands.Cog):
    def __init__(self, client):
        self.client = client
    @cog_ext.cog_slash(name="νλΆ", 
                description="π νλ‘κ·Έλλ° λμμ½",
                guild_ids=guild_ids,
                options=[
                    create_option(
                        name="λ΄μ©",
                        description="λ¬΄μ¨ λ΄μ©μΈκ°μ?",
                        option_type=3,
                        required=True,
                        choices=[
                        create_choice(
                            name="λ§μ½λ",
                            value="νλΆλ§μ½λ"
                        ),
                        create_choice(
                            name="λ©λͺ¨λ¦¬",
                            value="νλΆλ©λͺ¨λ¦¬"
                        ),
                        create_choice(
                            name="λͺλ²",
                            value="νλΆλͺλ²"
                        ),
                        create_choice(
                            name="μ±",
                            value="νλΆμ±"
                        ),
                        create_choice(
                            name="μΈμ΄ν",
                            value="νλΆμΈμ΄ν"
                        ),
                        create_choice(
                            name="λ°λ΄",
                            value="νλΆλ°λ΄"
                        ),
                        create_choice(
                            name="λ°€μ",
                            value="νλΆλ°€μ"
                        ),
                        create_choice(
                            name="λ°λ³΅",
                            value="νλΆλ°λ³΅"
                        ),
                        create_choice(
                            name="μ€νκ²ν°",
                            value="νλΆμ€νκ²ν°"
                        ),
                        create_choice(
                            name="μκ°",
                            value="νλΆμκ°"
                        ),
                        create_choice(
                            name="μ£Όμ",
                            value="νλΆμ£Όμ"
                        ),
                        create_choice(
                            name="μ½λ",
                            value="νλΆμ½λ"
                        ),
                        create_choice(
                            name="μ½λ",
                            value="νλΆμ½λ"
                        ),
                        create_choice(
                            name="λ²κ·Έ",
                            value="νλΆλ²κ·Έ"
                        ),
                        create_choice(
                            name="μ½λ©μ€",
                            value="νλΆμ½λ©μ€"
                        )
                        ]
                    )
                ])
    async def _νλΆ(self, ctx, λ΄μ©: str):
        if λ΄μ© == "νλΆλ§μ½λ":
            embed=discord.Embed(description="νλΆλ§μ½λ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/0F4M7GY/vmqndakdzhem.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "νλΆλ©λͺ¨λ¦¬":
            embed=discord.Embed(description="νλΆλ©λͺ¨λ¦¬", color=embed_color)
            embed.set_image(url="https://i.ibb.co/wMRrmgr/vmqndapahfl.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "νλΆλͺλ²":
            embed=discord.Embed(description="νλΆλͺλ²", color=embed_color)
            embed.set_image(url="https://i.ibb.co/hCRrn4P/vmqndaucqjs.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "νλΆμ±":
            embed=discord.Embed(description="νλΆμ±", color=embed_color)
            embed.set_image(url="https://i.ibb.co/RbG2qVh/vmqndcor.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "νλΆμΈμ΄ν":
            embed=discord.Embed(description="νλΆμΈμ΄ν", color=embed_color)
            embed.set_image(url="https://i.ibb.co/3kK7WxY/vmqnddjsdjxkt.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "νλΆλ°λ΄":
            embed=discord.Embed(description="νλΆλ°λ΄", color=embed_color)
            embed.set_image(url="https://i.ibb.co/j5Z716k/vmqndEkqhd.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "νλΆλ°€μ":
            embed=discord.Embed(description="νλΆλ°€μ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/b1YZGgZ/vmqndqkatoa.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "νλΆλ°λ³΅":
            embed=discord.Embed(description="νλΆλ°λ³΅", color=embed_color)
            embed.set_image(url="https://i.ibb.co/L0Bhxg2/vmqndqksqhr.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "νλΆμ€νκ²ν°":
            embed=discord.Embed(description="νλΆμ€νκ²ν°", color=embed_color)
            embed.set_image(url="https://i.ibb.co/G0hVxBN/vmqndtmvkrpxl.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "νλΆμκ°":
            embed=discord.Embed(description="νλΆμκ°", color=embed_color)
            embed.set_image(url="https://i.ibb.co/3Ytjz7F/vmqndtodrkr.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "νλΆμ£Όμ":
            embed=discord.Embed(description="νλΆμ£Όμ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/HFj0f48/vmqndwntjr.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "νλΆμ½λ":
            embed=discord.Embed(description="νλΆμ½λ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/RT04zxq/vmqndzhej.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "νλΆμ½λ":
            embed=discord.Embed(description="νλΆμ½λ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/PGJHPNz/vmqndzhem.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "νλΆλ²κ·Έ":
            embed=discord.Embed(description="νλΆλ²κ·Έ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/PjnzMv1/vmqndqjrm.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "νλΆμ½λ©μ€":
            embed=discord.Embed(description="νλΆμ½λ©μ€", color=embed_color)
            embed.set_image(url="https://i.ibb.co/D5zF9FN/vmqndzheldwnd.png")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(νλΆ(client))