CREATE INDEX IF NOT EXISTS idx_team_name
ON teams(name);

CREATE INDEX IF NOT EXISTS idx_player_country
ON players(country);

CREATE INDEX IF NOT EXISTS idx_tournament_game
ON tournaments(game);