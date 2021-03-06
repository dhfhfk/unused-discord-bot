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

class λλ¦¬(commands.Cog):
    def __init__(self, client):
        self.client = client
    @cog_ext.cog_slash(name="λλ¦¬", 
                description="π λλ¦¬ λμμ½",
                guild_ids=guild_ids,
                options=[
                    create_option(
                        name="λ΄μ©",
                        description="λ¬΄μ¨ λ΄μ©μΈκ°μ?",
                        option_type=3,
                        required=True,
                        choices=[
                            create_choice(
                                name="μ΄λ₯λ ₯",
                                value="λλ¦¬μ΄λ₯λ ₯"
                            ),
                            create_choice(
                                name="μ²μ ",
                                value="λλ¦¬μ²μ "
                            ),
                            create_choice(
                                name="μμ",
                                value="λλ¦¬μμ"
                            ),
                            create_choice(
                                name="νΈμ",
                                value="λλ¦¬νΈμ"
                            ),
                            create_choice(
                                name="νμ°",
                                value="λλ¦¬νμ°"
                            ),
                            create_choice(
                                name="κΌ΄λ°",
                                value="λλ¦¬κΌ΄λ°"
                            ),
                            create_choice(
                                name="λκ°",
                                value="λλ¦¬λκ°"
                            ),
                            create_choice(
                                name="λμ",
                                value="λλ¦¬λμ"
                            ),
                            create_choice(
                                name="μ±λ₯",
                                value="λλ¦¬μ±λ₯"
                            ),
                            create_choice(
                                name="μ λλ€",
                                value="λλ¦¬μ λλ€"
                            ),
                            create_choice(
                                name="μ―ν",
                                value="λλ¦¬μ―ν"
                            ),
                            create_choice(
                                name="μ’μ§",
                                value="λλ¦¬μ’μ§"
                            ),
                            create_choice(
                                name="μ μ ",
                                value="λλ¦¬μ μ "
                            ),
                            create_choice(
                                name="μ£½μ",
                                value="λλ¦¬μ£½μ"
                            )
                        ]
                    )
                ])
    async def _λλ¦¬(self, ctx, λ΄μ©: str):
        if λ΄μ© == "λλ¦¬μ΄λ₯λ ₯":
            embed=discord.Embed(description="λλ¦¬μ΄λ₯λ ₯", color=embed_color)
            embed.set_image(url="https://i.ibb.co/brTzWWr/enfflchsmdfur.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λλ¦¬μ²μ ":
            embed=discord.Embed(description="λλ¦¬μ²μ ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/68bkXKD/enfflcjtls.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λλ¦¬μμ":
            embed=discord.Embed(description="λλ¦¬μμ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/GTzqBwp/enffldntdma.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λλ¦¬νΈμ":
            embed=discord.Embed(description="λλ¦¬νΈμ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/jfPMZ6t/enfflghdlt.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λλ¦¬νμ°":
            embed=discord.Embed(description="λλ¦¬νμ°", color=embed_color)
            embed.set_image(url="https://i.ibb.co/Cwy8nSM/enfflgmrdn.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λλ¦¬κΌ΄λ°":
            embed=discord.Embed(description="λλ¦¬κΌ΄λ°", color=embed_color)
            embed.set_image(url="https://i.ibb.co/ZGNqMdT/enfflRhfqke.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λλ¦¬λκ°":
            embed=discord.Embed(description="λλ¦¬λκ°", color=embed_color)
            embed.set_image(url="https://i.ibb.co/nDTgfsR/enfflskrk.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λλ¦¬λμ":
            embed=discord.Embed(description="λλ¦¬λμ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/LQ6TRk3/enfflsoato.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λλ¦¬μ±λ₯":
            embed=discord.Embed(description="λλ¦¬μ±λ₯", color=embed_color)
            embed.set_image(url="https://i.ibb.co/KxWvjMF/enffltjdsmd.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λλ¦¬μ λλ€":
            embed=discord.Embed(description="λλ¦¬μ λλ€", color=embed_color)
            embed.set_image(url="https://i.ibb.co/2N1PtPW/enffltjssjasp.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λλ¦¬μ―ν":
            embed=discord.Embed(description="λλ¦¬μ―ν", color=embed_color)
            embed.set_image(url="https://i.ibb.co/y6NxGJK/enffltltvkf.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λλ¦¬μ’μ§":
            embed=discord.Embed(description="λλ¦¬μ’μ§", color=embed_color)
            embed.set_image(url="https://i.ibb.co/2vrRB9D/enfflwhgwl.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λλ¦¬μ μ ":
            embed=discord.Embed(description="λλ¦¬μ μ ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/5s9GtMr/enfflwjdtls.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λλ¦¬μ£½μ":
            embed=discord.Embed(description="λλ¦¬μ£½μ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/3vyJf3X/enfflwnrtkd.png")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(λλ¦¬(client))