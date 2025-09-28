<p align="center">
  <img src="https://github.com/user-attachments/assets/c589e4c6-f9c6-410e-a1af-b0d678a38f45" 
       alt="KawaiiTalk Banner" 
       width="800"/>
</p>

# KawaiiTalk Discod Bot Script

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![discord.py](https://img.shields.io/badge/discord.py-2.3.2-blueviolet.svg)](https://github.com/Rapptz/discord.py)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()

Discord bot built with `discord.py`.  
It handles economy, streaks, fun extras, and configurable settings — all wrapped in a dry, understated personality. :|

---

## ✨ What?

- **Economy System**
  - `*mine` → Earn coins.
  - `*daily` → Daily reward with streak bonuses.
  - `*balance` → Check your coins.
  - `*give @user amount` → Transfer coins to user.
  - `*leaderboard` → See top coin holders.
  - `*gamble amount` → Risk coins for a chance to multiply.

- **Streaks**
  - Daily streaks tracked and persisted in `streaks.json`.
  - Bonus coins for consecutive daily claims.

- **Fun Extras**
  - `*flip` → Flip a coin.
  - `*roll [sides]` → Roll a die.
  - `*fact` → Get a boring random fact.
  - `*8ball [question]` → Magic 8‑ball style answer.
  - `*quote` → Get an uninspiring quote.

- **Conversation**
  - Replies to greetings (`hi`, `hello`, `bye`, etc.).
  - Definitions: ask `what is X` or `define Y`.

- **Config System (Owner‑Only)**
  - `*setconfig <key> <value>` → Change a setting.
  - `*viewconfig` → View current settings (grouped by category).
  - `*listconfig` → List all valid keys with descriptions.
  - `*resetconfig` → Reset all to defaults.
  - Self‑documenting with descriptions and 🔧 highlights for changed values.

- **Error Handling**
  - Monotone embeds for cooldowns, missing arguments, and permission errors.
  - Catch‑all fallback: “Something broke. :|”

---
