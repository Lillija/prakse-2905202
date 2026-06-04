CREATE TRIGGER IF NOT EXISTS check_player_earnings
BEFORE INSERT ON players
FOR EACH ROW
WHEN NEW.total_earnings < 0
BEGIN
    SELECT RAISE(ABORT, 'Total earnings cannot be negative');
END;