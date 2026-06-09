SELECT * FROM teams
WHERE country = 'LV';

SELECT * FROM players
WHERE game = 'CS2';

SELECT
    p.nickname,
    t.name
FROM players p
JOIN teams t
ON p.active_team_id = t.id;

SELECT *
FROM tournaments
WHERE prize_pool > 10000;

--------------------------------------
-- All Latvian teams

SELECT *
FROM teams
WHERE country = 'LV';

------------------------------------------------

-- All CS2 players

SELECT *
FROM players
WHERE game = 'CS2';

------------------------------------------------

-- Players and their teams

SELECT
    p.nickname,
    p.real_name,
    t.name AS team_name
FROM players p
JOIN teams t
ON p.active_team_id = t.id;

------------------------------------------------

SELECT
    game,
    COUNT(*) AS team_count
FROM teams
GROUP BY game;


SELECT *
FROM tournaments
WHERE prize_pool > 1000;

SELECT
    tp.place_achieved,
    tp.prize_won,
    t.name AS team_name
FROM tournament_placements tp
JOIN teams t
ON tp.team_id = t.id;