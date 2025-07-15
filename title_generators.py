
def format_clash_royale(stats):
    return (
        f"🌟 PREMIUM {stats.get('trophies', '?')} TROPHY🏆 "
        f"{stats.get('elite_cards', '?')} ELITE CARDS 🚀 "
        f"{stats.get('max_cards', '?')} MAX CARDS ✨️ "
        f"LEVEL {stats.get('level', '?')} 🎯 "
        f"{stats.get('emotes', '?')} EMOTES 🎊 "
        f"{stats.get('gems', '?')} GEMS 💎 "
        f"KING TOWER LVL {stats.get('king_tower', '?')} ☠️ "
        f"INSTANT DELIVERY 🚚"
    )

def format_clash_of_clans(stats):
    return (
        f"🏰 TH{stats.get('townHallLevel', '?')} | {stats.get('trophies', '?')} Trophies 🏆\n"
        f"Clan: {stats.get('clanName', 'No Clan')} 🛡️ | "
        f"Attacks Won: {stats.get('warStars', '?')} ⚔️ | "
        f"Level {stats.get('expLevel', '?')} 🧠"
    )

def format_brawl_stars(stats):
    return (
        f"🌟 {stats.get('brawlersUnlocked', '?')}/{stats.get('totalBrawlers', '?')} Brawlers Unlocked\n"
        f"Trophies: {stats.get('trophies', '?')} 🏆 | "
        f"Highest: {stats.get('highestTrophies', '?')} 🔥\n"
        f"Club: {stats.get('clubName', 'No Club')} 🏴"
    )
