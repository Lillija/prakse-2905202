CREATE VIEW IF NOT EXISTS player_team_view AS
SELECT
    players.nickname,
    players.real_name,
    players.country,
    players.game,
    teams.name AS team_name
FROM players
LEFT JOIN teams
ON players.active_team_id = teams.id;