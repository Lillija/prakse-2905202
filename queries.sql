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