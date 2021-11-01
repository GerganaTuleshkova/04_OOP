from project.player import Player


class Guild:
    all_players = []

    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        if player in Guild.all_players:
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        Guild.all_players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for player_object in self.players:
            if player_object.name == player_name:
                self.players.remove(player_object)
                player_object.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        resulting_string = f"Guild: {self.name}"
        for player_object in self.players:
            resulting_string += f"\n{player_object.player_info()}"
        return resulting_string

