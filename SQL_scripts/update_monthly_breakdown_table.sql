/* Will updte monthly breakdown based on Bills Paid table */

DROP TRIGGER IF EXISTS update_billbreakdown_tbl;

DELIMITER //
CREATE TRIGGER update_billbreakdown_tbl
	AFTER INSERT ON bills_billpaid
	FOR EACH ROW
	BEGIN
		INSERT INTO bills_monthlybreakdown
			(myPaid, totalPaid)
			-- VALUES -- (NEW.paidDate, NEW.totalPaid)
			SELECT DATE_FORMAT(paidDate, '%m - %Y'), SUM(totalPaid)
			FROM bills_billpaid
            WHERE paidDate IS NOT NULL
			GROUP BY DATE_FORMAT(paidDate, '%m - %Y')
			ORDER BY paidDate;
	END//
	
DELIMITER ;