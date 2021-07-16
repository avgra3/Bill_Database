/* Will updte the bill paid table when entering data into the bills table */

DROP TRIGGER IF EXISTS update_bills_paid_tbl;

DELIMITER //
CREATE TRIGGER update_bills_paid_tbl
	AFTER INSERT ON bills_bills
	FOR EACH ROW
	BEGIN
		INSERT INTO bills_billspaid
			(paidDate, notes, paidBool, totalPaid, billID_id)
			VALUES(NULL, "N/A", 0, NEW.charge + NEW.anc_fees + NEW.taxes + NEW.credit, NEW.billID);
			
	END//
	
DELIMITER ;