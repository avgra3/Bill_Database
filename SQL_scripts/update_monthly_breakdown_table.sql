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
			SELECT SUM(totalPaid), DATE_FORMAT(paidDate, '%m - %Y')
			FROM bills_billspaid
			GROUP BY DATE_FORMAT(paidDate, '%m - %Y')
			ORDER BY paidDate;
	END//
	
DELIMITER ;