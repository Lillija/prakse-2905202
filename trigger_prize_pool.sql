CREATE TRIGGER IF NOT EXISTS check_tournament_prize_pool
BEFORE INSERT ON tournaments
FOR EACH ROW
WHEN NEW.prize_pool < 0
BEGIN
    SELECT RAISE(ABORT, 'Prize pool cannot be negative');
END;
