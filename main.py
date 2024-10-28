# main.py

from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

def test_strategies():
    # Play games against each bot
    bots = [quincy, abbey, kris, mrugesh]
    bot_names = ["Quincy", "Abbey", "Kris", "Mrugesh"]
    results = []

    for i, bot in enumerate(bots):
        print(f"Testing against {bot_names[i]}...")
        result = play(player, bot, 1000, verbose=True)
        results.append(result)

    print("\nResults:")
    for i, result in enumerate(results):
        print(f"{bot_names[i]}: {result}")

if __name__ == "__main__":
    test_strategies()
    # Uncomment the next line to run unit tests automatically
    # import test_module
