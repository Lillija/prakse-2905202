# Baltic Esports Market Database Structure

## Overview

The project uses an SQLite database for storing information about Baltic esports teams, players and tournaments before synchronizing data with Webflow CMS.

## Tables

### teams

| Field         | Type    | Description          |
| ------------- | ------- | -------------------- |
| id            | INTEGER | Primary Key          |
| name          | TEXT    | Team name            |
| country       | TEXT    | Country (LV, LT, EE) |
| game          | TEXT    | Main game            |
| founding_date | TEXT    | Founding date/year   |
| owner         | TEXT    | Team owner           |
| sponsors      | TEXT    | Team sponsors        |
| logo_url      | TEXT    | Logo URL             |

### players

| Field          | Type    | Description      |
| -------------- | ------- | ---------------- |
| id             | INTEGER | Primary Key      |
| nickname       | TEXT    | Player nickname  |
| real_name      | TEXT    | Player real name |
| country        | TEXT    | Country          |
| game           | TEXT    | Game             |
| active_team_id | INTEGER | Related team ID  |
| total_earnings | REAL    | Total earnings   |
| previous_teams | TEXT    | Previous teams   |

### tournaments

| Field      | Type    | Description       |
| ---------- | ------- | ----------------- |
| id         | INTEGER | Primary Key       |
| name       | TEXT    | Tournament name   |
| season     | TEXT    | Season/year       |
| game       | TEXT    | Game              |
| prize_pool | INTEGER | Prize pool        |
| organizer  | TEXT    | Organizer         |
| status     | TEXT    | Tournament status |

### tournament_placements

| Field          | Type    | Description          |
| -------------- | ------- | -------------------- |
| id             | INTEGER | Primary Key          |
| tournament_id  | INTEGER | Tournament reference |
| team_id        | INTEGER | Team reference       |
| place_achieved | TEXT    | Placement            |
| prize_won      | INTEGER | Prize won            |

## Relationships

teams (id)
← players (active_team_id)

teams (id)
← tournament_placements (team_id)

tournaments (id)
← tournament_placements (tournament_id)

## Additional Database Features

* SQLite indexes created for faster data lookup.
* SQL View created for combined player and team information.
* Trigger created to prevent negative player earnings.
* Database prepared for future API integration and Webflow CMS synchronization.
