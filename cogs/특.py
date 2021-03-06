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

class νΉ(commands.Cog):
    def __init__(self, client):
        self.client = client
    @cog_ext.cog_slash(name="νΉ", 
                description="π κ°λ°μνΉ λ°μ¨",
                guild_ids=guild_ids,
                options=[
                    create_option(
                        name="λ΄μ©",
                        description="λ¬΄μ¨ λ΄μ©μΈκ°μ?",
                        option_type=3,
                        required=True,
                        choices=[
                            create_choice(
                                name="λμμ΄λ",
                                value="λμμ΄λνΉ"
                            ),
                            create_choice(
                                name="λμμ΄λ2",
                                value="λμμ΄λνΉ2"
                            ),
                            create_choice(
                                name="CSS",
                                value="CSSνΉ"
                            ),
                            create_choice(
                                name="CSS2",
                                value="CSSνΉ2"
                            )
                        ]
                    )
                ]
        )
    async def _νΉ(self, ctx, λ΄μ©: str):
        if λ΄μ© == "λμμ΄λνΉ":
                embed=discord.Embed(description="λμμ΄λνΉ", color=embed_color)
                embed.set_image(url="https://i.ibb.co/JcncbDj/elwkdlsjxmr.gif")
                await ctx.send(embed=embed)
        elif λ΄μ© == "λμμ΄λνΉ2":
                embed=discord.Embed(description="λμμ΄λνΉ2", color=embed_color)
                embed.set_image(url="https://i.ibb.co/9n6x4hQ/elwkdlsjxmr2.png")
                await ctx.send(embed=embed)
        elif λ΄μ© == "CSSνΉ":
                embed=discord.Embed(description="CSSνΉ", color=embed_color)
                embed.set_image(url="https://i.ibb.co/6Js7Mty/CSSxmr.gif")
                await ctx.send(embed=embed)
        elif λ΄μ© == "CSSνΉ2":
                embed=discord.Embed(description="CSSνΉ2", color=embed_color)
                embed.set_image(url="https://i.ibb.co/gFr6mXx/CSS2.gif")
                await ctx.send(embed=embed)

def setup(client):
    client.add_cog(νΉ(client))