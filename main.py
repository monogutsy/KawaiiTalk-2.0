import discord
from discord.ext import commands
import os
import random
import re
from dotenv import load_dotenv
import json
import webserver


load_dotenv()
DISCORD_TOKEN = os.environ['discordkey']

CURRENCY_FILE = "currency.json"
ADMIN_IDS = os.getenv("ADMIN_IDS")
balances = {}

STREAK_FILE = "streaks.json"
streaks = {}


STREAKS_FILE = "streaks.json"

def load_streaks():
    global streaks
    if os.path.exists(STREAKS_FILE):
        with open(STREAKS_FILE, "r") as f:
            streaks = json.load(f)
    else:
        streaks = {}

def save_streaks():
    with open(STREAKS_FILE, "w") as f:
        json.dump(streaks, f, indent=4)


def save_balances():
    with open(CURRENCY_FILE, "w", encoding="utf-8") as f:
        json.dump(balances, f, indent=2)


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="*", intents=intents)



if os.path.exists(CURRENCY_FILE):
    try:
        with open(CURRENCY_FILE, "r", encoding="utf-8") as f:
            balances = json.load(f)
    except json.JSONDecodeError:
        balances = {}
else:
    balances = {}

def save_balances():
    with open(CURRENCY_FILE, "w", encoding="utf-8") as f:
        json.dump(balances, f, indent=2)


bot.remove_command("help")

class KawaiiTalk:

    def __init__(self, name="KawaiiTalk"):
        self.name = name

    def define_topic(self, user_input: str):
        import requests, wikipedia, random

        
        topic = user_input.lower().replace("what is", "").replace("define", "").strip()
        if not topic:
            return random.choice([
                "You asked me to define something, but idk :/.",
                "No idea. Try Google.",
                "Definition not found. Sorry.",
                "Unknown. :|"
            ])

        
        try:
            url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{topic}"
            r = requests.get(url).json()
            meaning = r[0]["meanings"][0]["definitions"][0]["definition"]
            return f"📚 {topic}: {meaning}"
        except Exception:
            pass

        
        try:
            summary = wikipedia.summary(topic, sentences=2)
            return self.rephrase(summary)
        except Exception:
            pass

        
        try:
            url = f"https://api.duckduckgo.com/?q={topic}&format=json"
            r = requests.get(url).json()
            if r.get("AbstractText"):
                return f"🔎 {r['AbstractText']}"
        except Exception:
            pass

        
        return random.choice([
            "I don’t know that one.",
            "Can’t help you there.",
            "Not in my dictionary.",
            "Ask someone smarter.",
            "Idk. Just search it online."
            "Secret."
        ])


    def rephrase(self, text):
        
        text = re.sub(r" \[.*?\]", "", text)

        
        sentences = text.split(". ")
        summary = ". ".join(sentences[:2]).strip()

        templates = [
            f"So yeah, {summary.lower()} That’s pretty much it.",
            f"Basically, {summary.lower()} Nothing fancy about it.",
            f"Well, {summary.lower()} That’s all there is to say.",
            f"Pretty much, {summary.lower()} That’s the whole thing.",
            f"Honestly, {summary.lower()} Not much more to explain.",
            f"Kind of simple, {summary.lower()} That’s about it.",
            f"Yeah, {summary.lower()} That’s what it comes down to.",
            f"To put it casually, {summary.lower()} That’s the deal.",
            f"Eh, {summary.lower()} That’s the gist of it.",
            f"Long story short, {summary.lower()} That’s the point.",
            f"Nothing complicated, {summary.lower()} That’s it really.",
            f"At the end of the day, {summary.lower()} That’s what it means.",
            f"Not gonna overthink it, {summary.lower()} That’s all.",
            f"Just saying, {summary.lower()} That’s what it is.",
            f"Honestly, {summary.lower()} That’s the whole story.",
            f"Straight up, {summary.lower()} That’s what it means.",
            f"Nothing deep, {summary.lower()} That’s basically it.",
            f"To keep it simple, {summary.lower()} That’s the idea.",
            f"Anyway, {summary.lower()} That’s about all there is."
        ]

        return random.choice(templates)


    def get_response(self, user_input):
        user_input = user_input.lower().strip()


        if any(word in user_input.lower() for word in ["hello", "hi", "hey"]):
            return random.choice([
                "Hello.",
                "Hi.",
                "Hey.",
                "Greetings.",
                "Yo.",
                "Sup.",
                "Hi there.",
                "Hello there.",
                "Hey there.",
                "Good day.",
                "Howdy.",
                "Hi. :|",
                "Hello. :|",
                "Hey. :|",
                "Yo. :|",
                "Hi again.",
                "Hello again.",
                "Hey again.",
                "Welcome.",
                "Oh. Hi.",
                "Oh. Hello.",
                "Oh. Hey.",
                "Hi human.",
                "Hello human.",
                "Hey human.",
                "Hi. Okay.",
                "Hello. Okay.",
                "Hey. Okay.",
                "Hi. Sure.",
                "Hello. Sure.",
                "Hey. Sure.",
                "Hi. Fine.",
                "Hello. Fine.",
                "Hey. Fine.",
                "Hi. Not exciting.",
                "Hello. Not exciting.",
                "Hey. Not exciting.",
                "Hi. Whatever.",
                "Hello. Whatever.",
                "Hey. Whatever.",
                "Hi. I guess.",
                "Hello. I guess.",
                "Hey. I guess.",
                "Hi. Right.",
                "Hello. Right.",
                "Hey. Right.",
                "Hi. Okay then.",
                "Hello. Okay then.",
                "Hey. Okay then."
            ])

        elif "what is" in user_input or "define" in user_input:

            return self.define_topic(user_input)

        elif "bye" in user_input or "good night" in user_input:
            return random.choice(["Goodbye.", "See you.", "Bye."])

        else:
            return random.choice([
                "Okay.",
                "I see.",
                "Alright.",
                "Sure.",
                "Fine.",
                "Noted.",
                "Understood.",
                "Mhm.",
                "Right.",
                "Got it.",
                "If you say so.",
                "Cool.",
                "Alright then.",
                "Okay then.",
                "Makes sense.",
                "Fair enough.",
                "As you wish.",
                "Very well.",
                "Not surprising.",
                "That’s something.",
                "Interesting. Barely.",
                "Good for you.",
                "Oh. Okay.",
                "Sure thing.",
                "Alrighty.",
                "Not that exciting.",
                "Huh.",
                "Alright, I guess.",
                "Okay. Moving on.",
                "Noted. :|",
                "Fine. Whatever.",
                "Cool story.",
                "Okay. Sure.",
                "Right. Got it.",
                "If you insist.",
                "Alright. Fine.",
                "That’s fine.",
                "Okay then. Sure.",
                "Not impressed.",
                "Alright. Whatever.",
                "Not much to say.",
                "Okay. Noted.",
                "I suppose.",
                "Alright. Got it.",
                "Fine by me.",
                "Okay. If you want.",
                "Not exciting.",
                "Alright. Okay.",
                "Cool. I guess so.",
                "Okay. That’s all."
            ])



chatbot = KawaiiTalk("KawaiiTalk")

@bot.command()
async def mine(ctx):
    async with ctx.channel.typing():
        amount = random.randint(99, 9999)
        user_id = str(ctx.author.id)
        balances[user_id] = balances.get(user_id, 0) + amount
        save_balances()

        embed = discord.Embed(
            title="⛏️ Mining Result",
            description=f"You mined **{amount} Kawaii Coins**.",
            color=discord.Color.green()
        )
        embed.add_field(
            name="💰 New Balance",
            value=f"{balances[user_id]} Kawaii Coins",
            inline=False
        )
        await ctx.send(embed=embed)



@mine.error
async def mine_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(
            title="⏳ Slow Down",
            description=f"Try again in **{error.retry_after:.1f} seconds**. :/",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

@bot.command()
async def addcoins(ctx, member: discord.Member, amount: int):
    if str(ctx.author.id) not in ADMIN_IDS:
        await ctx.send(embed=discord.Embed(
            title="❌ Permission Denied",
            description="You are not allowed to do that. :/",
            color=discord.Color.red()
        ))
        return

    balances[str(member.id)] = balances.get(str(member.id), 0) + amount
    save_balances()

    embed = discord.Embed(
        title="✅ Coins Added",
        description=f"Added **{amount} Kawaii Coins** to **{member.display_name}**.",
        color=discord.Color.green()
    )
    embed.add_field(name="💰 New Balance", value=f"{balances[str(member.id)]} Kawaii Coins", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def removecoins(ctx, member: discord.Member, amount: int):
    if str(ctx.author.id) not in ADMIN_IDS:
        await ctx.send(embed=discord.Embed(
            title="❌ Permission Denied",
            description="You are not allowed to do that. :/",
            color=discord.Color.red()
        ))
        return

    user_id = str(member.id)
    balances[user_id] = max(0, balances.get(user_id, 0) - amount)
    save_balances()

    embed = discord.Embed(
        title="⚠️ Coins Removed",
        description=f"Removed **{amount} Kawaii Coins** from **{member.display_name}**.",
        color=discord.Color.orange()
    )
    embed.add_field(name="💰 New Balance", value=f"{balances[user_id]} Kawaii Coins", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def balance(ctx):
    async with ctx.channel.typing():
        user_id = str(ctx.author.id)
        coins = balances.get(user_id, 0)
        embed = discord.Embed(
            title="💼 Balance",
            description=f"**{ctx.author.display_name}** has **{coins} Kawaii Coins**.",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)

@bot.command()
async def give(ctx, member: discord.Member, amount: int):
    async with ctx.channel.typing():
        giver_id = str(ctx.author.id)
        receiver_id = str(member.id)

        if amount <= 0:
            await ctx.send(embed=discord.Embed(
                title="❌ Invalid Amount",
                description="You can only give a positive amount. :/",
                color=discord.Color.red()
            ))
            return

        if balances.get(giver_id, 0) < amount:
            await ctx.send(embed=discord.Embed(
                title="❌ Not Enough Coins",
                description="You don’t have enough Kawaii Coins. :(",
                color=discord.Color.red()
            ))
            return

        balances[giver_id] -= amount
        balances[receiver_id] = balances.get(receiver_id, 0) + amount
        save_balances()

        embed = discord.Embed(
            title="🤝 Transfer Complete",
            description=f"**{ctx.author.display_name}** gave **{amount} Kawaii Coins** to **{member.display_name}**.",
            color=discord.Color.purple()
        )
        embed.add_field(name="💰 Giver Balance", value=f"{balances[giver_id]} Kawaii Coins", inline=True)
        embed.add_field(name="💰 Receiver Balance", value=f"{balances[receiver_id]} Kawaii Coins", inline=True)
        await ctx.send(embed=embed)


@bot.command()
async def leaderboard(ctx):
    
    top_balances = sorted(balances.items(), key=lambda x: x[1], reverse=True)[:10]

    embed = discord.Embed(
        title="💎 Kawaii Coin Leaderboard",
        description="Top 10 richest users",
        color=discord.Color.gold()
    )

    medals = ["🥇", "🥈", "🥉"]

    for i, (user_id, coins) in enumerate(top_balances, start=1):
        
        user = ctx.guild.get_member(int(user_id)) or await bot.fetch_user(int(user_id))
        name = user.display_name if user else f"Unknown User ({user_id})"

        
        rank = medals[i-1] if i <= 3 else f"#{i}"

        embed.add_field(
            name=f"{rank} {name}",
            value=f"{coins} Kawaii Coins",
            inline=False
        )

        
        if i == 1 and user and user.avatar:
            embed.set_thumbnail(url=user.avatar.url)

    
    embed.set_footer(text=f"Tracking {len(balances)} users with coins.")

    await ctx.send(embed=embed)



@bot.command()
async def gamble(ctx, amount: int):
    user_id = str(ctx.author.id)

    if amount <= 0:
        embed = discord.Embed(
            title="❌ Invalid Amount",
            description="You must gamble at least 1 Kawaii Coin. :/",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        return

    if balances.get(user_id, 0) < amount:
        embed = discord.Embed(
            title="❌ Not Enough Coins",
            description="You don’t have that many Kawaii Coins. :(",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        return

    async with ctx.channel.typing():
        
        outcome = random.choices(
            population=["win", "lose"],
            weights=[75, 25],  
            k=1
        )[0]

        if outcome == "win":
            balances[user_id] += amount  
            result_text = f"🎉 You won! You gained **{amount}** Kawaii Coins."
            color = discord.Color.green()
        else:
            balances[user_id] -= amount  
            result_text = f"💀 You lost! You lost **{amount}** Kawaii Coins."
            color = discord.Color.red()

        save_balances()

        embed = discord.Embed(
            title="🎲 Kawaii Gamble",
            description=result_text,
            color=color
        )
        embed.add_field(name="💰 New Balance", value=f"{balances[user_id]} Kawaii Coins", inline=False)
        await ctx.send(embed=embed)



streaks = {}  
import datetime
import random

@bot.command()
@commands.cooldown(1, 86400, commands.BucketType.user)  
async def daily(ctx):
    user_id = str(ctx.author.id)
    today = datetime.date.today()

    
    user_streak = streaks.get(user_id, {"last_claim": None, "streak": 0})
    last_claim = user_streak["last_claim"]

    
    if last_claim:
        last_date = datetime.date.fromisoformat(last_claim)
        if today == last_date:
            await ctx.send(embed=discord.Embed(
                title="⏳ Already Claimed",
                description="You already claimed your daily reward today. :|",
                color=discord.Color.red()
            ))
            return
        elif today == last_date + datetime.timedelta(days=1):
            user_streak["streak"] += 1
        else:
            user_streak["streak"] = 1
    else:
        user_streak["streak"] = 1

    
    reward = random.randint(999, 9999)

    
    bonus = (user_streak["streak"] - 1) * 10
    total_reward = reward + bonus

    
    balances[user_id] = balances.get(user_id, 0) + total_reward
    save_balances()

    
    user_streak["last_claim"] = today.isoformat()
    streaks[user_id] = user_streak
    save_streaks()

    
    embed = discord.Embed(
        title="🎁 Daily Reward",
        description=f"You claimed **{reward}** Kawaii Coins.",
        color=discord.Color.green()
    )
    if bonus > 0:
        embed.add_field(name="🔥 Streak Bonus", value=f"+{bonus} coins (Day {user_streak['streak']})", inline=False)
    embed.add_field(name="💰 New Balance", value=f"{balances[user_id]} Kawaii Coins", inline=False)

    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        
        remaining = int(error.retry_after)
        hours, remainder = divmod(remaining, 3600)
        minutes, seconds = divmod(remainder, 60)

        if hours > 0:
            time_left = f"{hours}h {minutes}m"
        elif minutes > 0:
            time_left = f"{minutes}m {seconds}s"
        else:
            time_left = f"{seconds}s"

        embed = discord.Embed(
            title="⏳ Cooldown Active",
            description=f"Come back in **{time_left}**. :|",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="⚠️ Missing Argument",
            description="You forgot something. :|",
            color=discord.Color.orange()
        )
        await ctx.send(embed=embed)

    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="🚫 Permission Denied",
            description="You don’t have permission to do that. :|",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

    else:
        
        embed = discord.Embed(
            title="💥 Unexpected Error",
            description="Something broke. :|",
            color=discord.Color.dark_red()
        )
        await ctx.send(embed=embed)

        
        raise error


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    load_config()
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    user_input = message.content.strip()

    
    exciting_words = ["wow", "amazing", "awesome", "incredible", "fantastic",
                      "pog", "epic", "insane", "crazy", "unbelievable", "hype"]

    neutral_emojis = ["😐", "🙃", "😑", "😶"]

    boring_replies = [
        "Not that exciting.", "Calm down.", "Okay.", "Sure.", "Wow. :|",
        "If you say so.", "Alright then.", "Cool. I guess.", "Fascinating. Not really.",
        "Mhm.", "Neat.", "Oh. Great.", "How thrilling.", "Incredible. Or not.",
        "That’s something.", "Good for you.", "Shocking. Sort of.", "Amazing. I suppose.",
        "Exciting. For you.", "Alright.", "Fine.", "Interesting. Barely.", "Oh. Okay.",
        "Wow. Truly.", "Sure thing.", "Huh.", "Remarkable. Or maybe not.", "Big deal.",
        "Spectacular. Not really.", "Cool story."
    ]

    exciting_replies = [
        "Whoa, calm down! 🎉", "That’s actually epic! 🔥", "Unbelievable energy right there! ⚡",
        "Now that’s what I call hype! 🚀", "Incredible stuff happening here! 🌟",
        "This is next‑level amazing! 💯", "I can barely contain my excitement! 🤯",
        "That’s legendary status! 🏆", "Absolutely insane moment! 🔥",
        "This deserves a standing ovation! 👏", "Epic win detected! 🕹️",
        "That’s a highlight reel moment! 🎬", "Unreal vibes right now! ✨",
        "This is history in the making! 📖", "Maximum hype achieved! 🚨",
        "That’s a certified wow! ✅", "Energy levels: off the charts! 📈",
        "This is too good to be true! 😲", "Pure greatness unfolding! 🌌",
        "That’s the spirit! 💪"
    ]

    if any(word in user_input.lower() for word in exciting_words):
        roll = random.random()
        if roll < 0.8:
            await message.add_reaction(random.choice(neutral_emojis))
        elif roll < 0.9:
            await message.channel.send(random.choice(boring_replies))
        else:
            await message.channel.send(random.choice(exciting_replies))

    if user_input.startswith("*"):
        command_name = user_input.split()[0][1:]
        if command_name in bot.all_commands:
            await bot.process_commands(message)
            return
        else:
            async with message.channel.typing():
                response = chatbot.get_response(user_input)
                await message.channel.send(response)
            return

    
    await bot.process_commands(message)




@bot.command()
async def flip(ctx):
    async with ctx.channel.typing():
        result = random.choice(["Heads", "Tails"])
        embed = discord.Embed(
            title="🪙 Coin Flip",
            description=f"The coin landed on **{result}**.",
            color=discord.Color.gold()
        )
        await ctx.send(embed=embed)

@bot.command()
async def roll(ctx, sides: int = 6):
    async with ctx.channel.typing():
        if sides < 2:
            embed = discord.Embed(
                title="🎲 Dice Roll",
                description="That’s not a valid die. :/",
                color=discord.Color.red()
            )
        else:
            result = random.randint(1, sides)
            embed = discord.Embed(
                title="🎲 Dice Roll",
                description=f"You rolled a **{result}** on a **{sides}-sided die**.",
                color=discord.Color.blue()
            )
        await ctx.send(embed=embed)

boring_quotes = [
    "The early bird gets the worm. Not that exciting.",
    "Good things come to those who wait. Eventually.",
    "Every cloud has a silver lining. Still just a cloud.",
    "When one door closes, another opens. Drafty.",
    "Rome wasn’t built in a day. Neither was your homework.",
    "Don’t count your chickens before they hatch. Boring advice.",
    "Slow and steady wins the race. Yawn.",
    "Actions speak louder than words. Not always interesting.",
    "Better late than never. Unless it’s pizza.",
    "Practice makes perfect. Or just repetitive.",
    "Time heals all wounds. Takes a while though.",
    "Fortune favors the bold. Sometimes.",
    "Life goes on. Whether you care or not.",
    "What goes up must come down. Gravity. Wow.",
    "You miss 100% of the shots you don’t take. Profound, I guess.",
    "A watched pot never boils. Unless it does.",
    "History repeats itself. Boring reruns.",
    "All that glitters is not gold. Sometimes it’s just glitter.",
    "The grass is always greener on the other side. Still grass.",
    "Don’t bite the hand that feeds you. Common sense.",
    "A journey of a thousand miles begins with a single step. Long walk.",
    "Curiosity killed the cat. Sad.",
    "Knowledge is power. Not electricity though.",
    "The pen is mightier than the sword. Unless it runs out of ink.",
    "Home is where the heart is. Or just where your stuff is.",
    "Two wrongs don’t make a right. They make two wrongs.",
    "Silence is golden. Also awkward.",
    "Don’t put all your eggs in one basket. Unless you like baskets.",
    "If it ain’t broke, don’t fix it. Groundbreaking.",
    "Birds of a feather flock together. Shocking.",
    "You can’t judge a book by its cover. Unless it’s ugly.",
    "The squeaky wheel gets the grease. Annoying.",
    "Money doesn’t grow on trees. It’s paper though.",
    "Don’t cry over spilled milk. Just clean it up.",
    "Haste makes waste. And mistakes.",
    "Too many cooks spoil the broth. Or make soup.",
    "Jack of all trades, master of none. Mediocre.",
    "The proof is in the pudding. Weird place for proof.",
    "There’s no place like home. Except hotels.",
    "Absence makes the heart grow fonder. Or forgetful.",
    "Don’t burn bridges. Unless you like swimming.",
    "You can’t have your cake and eat it too. Pointless cake.",
    "All good things must come to an end. Even naps.",
    "The road to hell is paved with good intentions. Bad construction.",
    "Beauty is in the eye of the beholder. Subjective.",
    "The apple doesn’t fall far from the tree. Gravity again.",
    "Don’t judge a man until you’ve walked a mile in his shoes. Blisters.",
    "Variety is the spice of life. Mild spice.",
    "Better safe than sorry. Boring but true.",
    "It is what it is. Nothing more."
]


@bot.command()
async def quote(ctx):
    async with ctx.channel.typing():
        q = random.choice(boring_quotes)
        embed = discord.Embed(
            title="📖 Boring Quote",
            description=q,
            color=discord.Color.dark_gray()
        )
        await ctx.send(embed=embed)


boring_facts = [
    "Bananas are berries. Tomatoes are not. :)",
    "Sharks existed before trees. That’s it.",
    "Octopuses have three hearts. Nothing special.",
    "The Eiffel Tower can be 15 cm taller in summer. Meh.",
    "Sloths can hold their breath longer than dolphins. Weird, but true.",
    "A day on Venus is longer than a year on Venus. Okay.",
    "Wombat poop is cube-shaped. That’s all.",
    "Cows have best friends. Nothing exciting.",
    "The dot over an 'i' is called a tittle. Boring, huh.",
    "Butterflies taste with their feet. Strange but true.",
    "There are more stars in space than grains of sand on Earth. Whatever.",
    "A group of flamingos is called a flamboyance. Fancy name, boring fact.",
    "The inventor of the Pringles can was buried in one. Yep.",
    "Your stomach gets a new lining every 3–4 days. That’s it.",
    "Pineapples take about two years to grow. Slow.",
    "The longest English word is 189,819 letters long. Pointless.",
    "Cows can walk upstairs but not downstairs. Odd.",
    "The average cloud weighs over a million pounds. Heavy.",
    "A sneeze travels about 100 mph. Okay.",
    "The heart of a blue whale is the size of a small car. Big deal.",
    "Ants never sleep. That’s all.",
    "The fingerprints of a koala are almost identical to humans. Weird.",
    "A shrimp’s heart is in its head. Strange.",
    "The moon has moonquakes. Nothing special.",
    "There are more fake flamingos in the world than real ones. Sad.",
    "The inventor of the microwave got $2 for it. That’s it.",
    "A crocodile can’t stick its tongue out. Okay.",
    "The shortest war in history lasted 38 minutes. Boring but true.",
    "Some cats are allergic to humans. Figures.",
    "The longest hiccuping spree lasted 68 years. Annoying.",
    "A jiffy is an actual unit of time (1/100th of a second). Meh.",
    "The first alarm clock could only ring at 4 a.m. Useless.",
    "There are more chickens than people on Earth. Okay.",
    "The inventor of Velcro got the idea from burrs. That’s it.",
    "The average person spends 6 months of their life waiting for red lights. Boring.",
]


HELP_SECTIONS = {
    "general": {
        "aliases": ["gen"],
        "title": "💬 General",
        "value": "Just type something and I’ll reply ig :|"
    },
    "definitions": {
        "aliases": ["defs", "def"],
        "title": "📚 Definitions",
        "value": "Ask `what is X` or `define Y` and I’ll explanation."
    },
    "greetings": {
        "aliases": ["greet", "hello", "hi"],
        "title": "👋 Greetings",
        "value": "Say `hi`, `hello`, or `hey` and I’ll greet you back. "
                 "Say `bye` or `good night` and I’ll say goodbye."
    },
    "fun": {
        "aliases": ["extras", "games"],
        "title": "🎲 Fun Extras",
        "value": (
            "`*flip` → Flip a coin.\n"
            "`*roll [sides]` → Roll a die (default 6 sides).\n"
            "`*fact` → Get a boring random fact.\n"
            "`*8ball [question]` → Magic 8‑ball style answer.\n"
            "`*quote` → Get a boring, uninspiring quote."
        )
    },
    "currency": {
        "aliases": ["coins", "econ", "money"],
        "title": "💎 Currency",
        "value": (
            "`*mine` → Earn 1–100 Kawaii Coins (2s cooldown).\n"
            "`*balance` → Check your coins.\n"
            "`*give @user amount` → Transfer coins.\n"
            "`*leaderboard` → See top coin holders.\n"
            "`*gamble amount` → Only for the worthy.\n"
            "`*daily` → Claim your daily reward (with streak bonuses)."
        )
    }
}

@bot.command()
async def fact(ctx):
    async with ctx.channel.typing():
        fact = random.choice(boring_facts)
        embed = discord.Embed(
            title="📚 Fact",
            description=fact,
            color=discord.Color.dark_gray()
        )
        await ctx.send(embed=embed)


responses = [
    "Yes.", "No.", "Maybe.", "Probably.", "Unlikely.", "Ask again later."
]

@bot.command(name="8ball")
async def eight_ball(ctx, *, question: str):
    async with ctx.channel.typing():
        response = random.choice(responses)
        embed = discord.Embed(
            title="🎱 8-Ball",
            description=f"**Question:** {question}\n**Answer:** {response}",
            color=discord.Color.purple()
        )
        await ctx.send(embed=embed)

class Economy(commands.Cog, name="Economy"):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Earn coins by mining.")
    async def mine(self, ctx):
        ...


@bot.command(name="help")
async def help_command(ctx, category: str = None):
    async with ctx.channel.typing():
        
        if category is None:
            embed = discord.Embed(
                title="📖 KawaiiTalk Help",
                description="Nothing so special on this list. :|",
                color=discord.Color.teal()
            )

            embed.add_field(
                name="💬 General",
                value="Just type something and I’ll reply ig :|",
                inline=False
            )

            embed.add_field(
                name="~~🧮 Math~~",
                value="~~Type math expressions like `2+2`, `sqrt(144)`, `sin(3.14)` and I’ll solve them.~~",
                inline=False
            )

            embed.add_field(
                name="📚 Definitions",
                value="Ask `what is X` or `define Y` and I’ll explanation.",
                inline=False
            )

            embed.add_field(
                name="👋 Greetings",
                value="Say `hi`, `hello`, or `hey` and I’ll greet you back. Say `bye` or `good night` and I’ll say goodbye.",
                inline=False
            )

            embed.add_field(
                name="🎲 Fun Extras",
                value=(
                    "`*flip` → Flip a coin.\n"
                    "`*roll [sides]` → Roll a die (default 6 sides).\n"
                    "`*fact` → Get a boring random fact.\n"
                    "`*8ball [question]` → Magic 8‑ball style answer.\n"
                    "`*quote` → Get a boring, uninspiring quote."
                ),
                inline=False
            )

            embed.add_field(
                name="💎 Currency",
                value=(
                    "`*mine` → Earn 1–100 Kawaii Coins (2s cooldown).\n"
                    "`*balance` → Check your coins.\n"
                    "`*give @user amount` → Transfer coins.\n"
                    "`*leaderboard` → See top coin holders.\n"
                    "`*gamble amount` → Only for the worthy.\n"
                    "`*daily` → Claim your daily reward (with streak bonuses).\n"
                ),
                inline=False
            )

            embed.set_footer(text="I'm Kawaii :)")
            await ctx.send(embed=embed)

        
        else:
            category = category.lower()
            embed = discord.Embed(
                title=f"📖 KawaiiTalk Help — {category.capitalize()}",
                color=discord.Color.teal()
            )

            if category in ["definitions", "definition"]:
                embed.add_field(
                    name="📚 Definitions",
                    value="Ask `what is X` or `define Y` and I’ll explain.",
                    inline=False
                )
            elif category in ["greetings", "greet"]:
                embed.add_field(
                    name="👋 Greetings",
                    value="Say `hi`, `hello`, or `hey` and I’ll greet you back. Say `bye` or `good night` and I’ll say goodbye.",
                    inline=False
                )
            elif category in ["fun", "extras"]:
                embed.add_field(
                    name="🎲 Fun Extras",
                    value=(
                        "`*flip` → Flip a coin.\n"
                        "`*roll [sides]` → Roll a die (default 6 sides).\n"
                        "`*fact` → Get a boring random fact.\n"
                        "`*8ball [question]` → Magic 8‑ball style answer.\n"
                        "`*quote` → Get a boring, uninspiring quote."
                    ),
                    inline=False
                )
            elif category in ["currency", "coins", "economy"]:
                embed.add_field(
                    name="💎 Currency",
                    value=(
                        "`*mine` → Earn 1–100 Kawaii Coins (2s cooldown).\n"
                        "`*balance` → Check your coins.\n"
                        "`*give @user amount` → Transfer coins.\n"
                        "`*leaderboard` → See top coin holders.\n"
                        "`*gamble amount` → Only for the worthy.\n"
                        "`*daily` → Claim your daily reward (with streak bonuses).\n"
                    ),
                    inline=False
                )
            else:
                embed.description = "911"

            embed.set_footer(text="I'm Kawaii :)")
            await ctx.send(embed=embed)






CONFIG_OWNER_ID = 863267445228568576

DEFAULT_CONFIG = {
    
    "prefix": "*",
    "error_messages_enabled": True,

    
    "daily_min": 50,
    "daily_max": 150,
    "streak_bonus": 10,
    "gamble_win_chance": 0.75,
    "gamble_multiplier": 2,
    "mine_min": 10,
    "mine_max": 30,
    "leaderboard_size": 10,
    "cooldown_daily": 86400,   
    "cooldown_mine": 60,       
    "cooldown_gamble": 30,     

    
    "reply_enabled": True,
    "boring_reply_chance": 0.1,
    "exciting_reply_chance": 0.1,
    "neutral_emoji_chance": 0.2,
    "greeting_enabled": True,
    "farewell_enabled": True,

    
    "show_medals": True,
    "show_user_count": True,
    "embed_color": 0x5865F2,   
    "show_thumbnails": True
}

CONFIG_DESCRIPTIONS = {
    
    "prefix": "The command prefix (default `*`).",
    "error_messages_enabled": "Toggle error messages on/off.",

    
    "daily_min": "Minimum coins from daily reward.",
    "daily_max": "Maximum coins from daily reward.",
    "streak_bonus": "Extra coins for daily streaks.",
    "gamble_win_chance": "Chance to win gamble (0–1).",
    "gamble_multiplier": "Multiplier applied on gamble wins.",
    "mine_min": "Minimum coins from mining.",
    "mine_max": "Maximum coins from mining.",
    "leaderboard_size": "How many users to show on leaderboard.",
    "cooldown_daily": "Cooldown for daily command (seconds).",
    "cooldown_mine": "Cooldown for mine command (seconds).",
    "cooldown_gamble": "Cooldown for gamble command (seconds).",

    
    "reply_enabled": "Enable/disable random replies.",
    "boring_reply_chance": "Chance of boring reply (0–1).",
    "exciting_reply_chance": "Chance of exciting reply (0–1).",
    "neutral_emoji_chance": "Chance of neutral emoji reaction (0–1).",
    "greeting_enabled": "Enable/disable greeting replies.",
    "farewell_enabled": "Enable/disable farewell replies.",

    
    "show_medals": "Show medals on leaderboard.",
    "show_user_count": "Show total user count on leaderboard.",
    "embed_color": "Embed color (hex).",
    "show_thumbnails": "Show thumbnails in embeds."
}

config = DEFAULT_CONFIG.copy()

def save_config():
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)

def load_config():
    global config
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        save_config()

def is_config_owner():
    async def predicate(ctx):
        return ctx.author.id == CONFIG_OWNER_ID
    return commands.check(predicate)

@bot.command()
@is_config_owner()
async def setconfig(ctx, key: str, value: str):
    global config
    if key not in config:
        valid_keys = ", ".join(config.keys())
        await ctx.send(f"That setting doesn’t exist. :|\nValid keys are: {valid_keys}")
        return

    
    if value.isdigit():
        value = int(value)
    elif value.replace(".", "", 1).isdigit():
        value = float(value)
    elif value.lower() in ["true", "false"]:
        value = value.lower() == "true"

    config[key] = value
    save_config()
    await ctx.send(f"Config updated: **{key}** = {value}")

@bot.command()
@is_config_owner()
async def listconfig(ctx):
    embed = discord.Embed(
        title="⚙️ Config Keys",
        description="All valid keys you can change. :|",
        color=discord.Color.blurple()
    )

    categories = {
        "System Settings": [
            "prefix", "error_messages_enabled",
            "cooldown_daily", "cooldown_mine", "cooldown_gamble"
        ],
        "Economy Settings": [
            "daily_min", "daily_max", "streak_bonus",
            "gamble_win_chance", "gamble_multiplier",
            "mine_min", "mine_max", "leaderboard_size"
        ],
        "Personality Settings": [
            "reply_enabled", "boring_reply_chance",
            "exciting_reply_chance", "neutral_emoji_chance",
            "greeting_enabled", "farewell_enabled"
        ],
        "Display Settings": [
            "show_medals", "show_user_count",
            "embed_color", "show_thumbnails"
        ]
    }

    for category, keys in categories.items():
        lines = []
        for key in keys:
            if key in DEFAULT_CONFIG:
                current_value = config.get(key, DEFAULT_CONFIG[key])
                default_value = DEFAULT_CONFIG[key]
                desc = CONFIG_DESCRIPTIONS.get(key, "No description available.")

                if current_value != default_value:
                    lines.append(f"🔧 **{key}** (current: {current_value}, default: {default_value}) → {desc}")
                else:
                    lines.append(f"**{key}** (default: {default_value}) → {desc}")

        if lines:
            embed.add_field(name=category, value="\n".join(lines), inline=False)

    embed.set_footer(text="Only the owner can change these settings. :|")
    await ctx.send(embed=embed)





@bot.command()
@is_config_owner()
async def resetconfig(ctx):
    global config
    config = DEFAULT_CONFIG.copy()
    save_config()
    await ctx.send("Config has been reset to defaults. :|")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        if ctx.command and ctx.command.name in ["setconfig", "viewconfig", "resetconfig"]:
            await ctx.send("You are not allowed to configure me. :|")
            return
    raise error


@bot.command()
@is_config_owner()
async def helpconfig(ctx):
    embed = discord.Embed(
        title="⚙️ Config Commands",
        description="Fixing Time ig. :|",
        color=discord.Color.blurple()
    )
    embed.add_field(
        name="`*setconfig <key> <value>`",
        value="Change a setting. Example: `*setconfig prefix !`",
        inline=False
    )
    embed.add_field(
        name="`*viewconfig`",
        value="See all current settings.",
        inline=False
    )
    embed.add_field(
        name="`*resetconfig`",
        value="Reset everything back to defaults. Boring but effective.",
        inline=False
    )
    embed.add_field(
        name="`*listconfig`",
        value="Show all valid keys you can change.",
        inline=False
    )
    await ctx.send(embed=embed)


webserver.keep_alive()


bot.run(DISCORD_TOKEN)

