def validate_team(team):
    return (
        team["name"] != ""
        and team["country"] in ["LV", "LT", "EE"]
    )