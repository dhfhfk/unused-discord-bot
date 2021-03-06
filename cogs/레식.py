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

class λ μ(commands.Cog):
    def __init__(self, client):
        self.client = client
    @cog_ext.cog_slash(name="λ μ", 
                description="π λ μΈλ³΄μ°μμ€μμ¦ λμμ½",
                guild_ids=guild_ids,
                options=[
                    create_option(
                        name="λ΄μ©",
                        description="λ¬΄μ¨ λ΄μ©μΈκ°μ?",
                        option_type=3,
                        required=True,
                        choices=[
                            create_choice(
                                name="λ μ΄μ ",
                                value="λ μλ μ΄μ "
                            ),
                            create_choice(
                                name="μμ¬",
                                value="λ μμμ¬"
                            ),
                            create_choice(
                                name="μλ",
                                value="λ μμλ"
                            ),
                            create_choice(
                                name="μ΄λλ",
                                value="λ μμ΄λλ"
                            ),
                            create_choice(
                                name="μ°μ»΄",
                                value="λ μμ°μ»΄"
                            ),
                            create_choice(
                                name="μ΄",
                                value="λ μμ΄"
                            ),
                            create_choice(
                                name="λλ €μ€",
                                value="λ μλλ €μ€"
                            ),
                            create_choice(
                                name="λλ",
                                value="λ μλλ"
                            ),
                            create_choice(
                                name="λ λ§",
                                value="λ μλ λ§"
                            ),
                            create_choice(
                                name="ν€λ",
                                value="λ μν€λ"
                            ),
                            create_choice(
                                name="λ°κ°",
                                value="λ μλ°κ°"
                            ),
                            create_choice(
                                name="λΈμ",
                                value="λ μλΈμ"
                            ),
                            create_choice(
                                name="λΆλ§",
                                value="λ μλΆλ§"
                            ),
                            create_choice(
                                name="λ°Έλ°μ€",
                                value="λ μλ°Έλ°μ€"
                            ),
                            create_choice(
                                name="κ°μ",
                                value="λ μκ°μ"
                            ),
                            create_choice(
                                name="κ°λΌν₯",
                                value="λ μκ°λΌν₯"
                            ),
                            create_choice(
                                name="γ΄γγ±",
                                value="λ μγ΄γγ±"
                            ),
                            create_choice(
                                name="μ μ΄",
                                value="λ μμ μ΄"
                            ),
                            create_choice(
                                name="μ€ν°ν¬",
                                value="λ μμ€ν°ν¬"
                            ),
                            create_choice(
                                name="νκ΅¬",
                                value="λ μνκ΅¬"
                            ),
                            create_choice(
                                name="νΌμ",
                                value="λ μνΌμ"
                            ),
                            create_choice(
                                name="ν©κΉ‘",
                                value="λ μν©κΉ‘"
                            ),
                            create_choice(
                                name="μ¬ν",
                                value="λ μμ¬ν"
                            )
                        ]
                    )
                ])
    async def _λ μ(self, ctx, λ΄μ©: str):
        if λ΄μ© == "λ μλ μ΄μ ":
            embed=discord.Embed(description="λ μλ μ΄μ ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/6tpggTT/fptlrfpdlwj.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λ μμμ¬":
            embed=discord.Embed(description="λ μμμ¬", color=embed_color)
            embed.set_image(url="https://i.ibb.co/MfNR1Y0/fptlrdidtla.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λ μμλ":
            embed=discord.Embed(description="λ μμλ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/Dz4HfVW/fptlrdkffka.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λ μμ΄λλ":
            embed=discord.Embed(description="λ μμ΄λλ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/mzvdCLC/fptlrdlfoeh.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λ μμ°μ»΄":
            embed=discord.Embed(description="λ μμ°μ»΄", color=embed_color)
            embed.set_image(url="https://i.ibb.co/fQYdC4N/fptlrdnpfzja.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λ μμ΄":
            embed=discord.Embed(description="λ μμ΄", color=embed_color)
            embed.set_image(url="https://i.ibb.co/8XQTXQ3/fptlrdns.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λ μλλ €μ€":
            embed=discord.Embed(description="λ μλλ €μ€", color=embed_color)
            embed.set_image(url="https://i.ibb.co/GQSm2kR/fptlrehffuwnj.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λ μλλ":
            embed=discord.Embed(description="λ μλλ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/yqy46ZB/fptlrenshl.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λ μλ λ§":
            embed=discord.Embed(description="λ μλ λ§", color=embed_color)
            embed.set_image(url="https://i.ibb.co/2ZNNLJH/fptlrfpelt.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λ μν€λ":
            embed=discord.Embed(description="λ μν€λ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/T0Sd3Lq/fptlrgpem.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λ μλ°κ°":
            embed=discord.Embed(description="λ μλ°κ°", color=embed_color)
            embed.set_image(url="https://i.ibb.co/0fDxhXD/fptlrqkfrkr.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λ μλΈμ":
            embed=discord.Embed(description="λ μλΈμ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/GxxQPz5/fptlrqmfdk.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λ μλΆλ§":
            embed=discord.Embed(description="λ μλΆλ§", color=embed_color)
            embed.set_image(url="https://i.ibb.co/Rv5ZNDX/fptlrqnfaks.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λ μλ°Έλ°μ€":
            embed=discord.Embed(description="λ μλ°Έλ°μ€", color=embed_color)
            embed.set_image(url="https://i.ibb.co/FHHf7C6/fptlrqoffjstm.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λ μκ°μ":
            embed=discord.Embed(description="λ μκ°μ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/vP9TfCD/fptlrrkawk.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λ μκ°λΌν₯":
            embed=discord.Embed(description="λ μκ°λΌν₯", color=embed_color)
            embed.set_image(url="https://i.ibb.co/3MhQshn/fptlrrkfkzlr.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λ μγ΄γγ±":
            embed=discord.Embed(description="λ μγ΄γγ±", color=embed_color)
            embed.set_image(url="https://i.ibb.co/t4WKsMZ/fptlrsdr.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λ μμ μ΄":
            embed=discord.Embed(description="λ μμ μ΄", color=embed_color)
            embed.set_image(url="https://i.ibb.co/DbKTndH/fptlrtlschd.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λ μμ€ν°ν¬":
            embed=discord.Embed(description="λ μμ€ν°ν¬", color=embed_color)
            embed.set_image(url="https://i.ibb.co/6RcwndL/fptlrtmvhszlf.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λ μνκ΅¬":
            embed=discord.Embed(description="λ μνκ΅¬", color=embed_color)
            embed.set_image(url="https://i.ibb.co/ZYfCfWx/fptlrvldrn.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λ μνΌμ":
            embed=discord.Embed(description="λ μνΌμ", color=embed_color)
            embed.set_image(url="https://i.ibb.co/pLN052L/fptlrvlwk.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λ μν©κΉ‘":
            embed=discord.Embed(description="λ μν©κΉ‘", color=embed_color)
            embed.set_image(url="https://i.ibb.co/fkbvSzn/fptlrvorRkd.png")
            await ctx.send(embed=embed)
        elif λ΄μ© == "λ μμ¬ν":
            embed=discord.Embed(description="λ μμ¬ν", color=embed_color)
            embed.set_image(url="https://i.ibb.co/zG7prwp/fptlrwoxkd.png")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(λ μ(client))