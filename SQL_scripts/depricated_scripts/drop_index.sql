DESCRIBE `bills_carrier`;
DESCRIBE `bills_product`;
DESCRIBE `bills_bill`;



/* Drops Columns in bills_bill table */
ALTER TABLE `bills_bill`
	DROP INDEX IF EXISTS `bills_bills_carrierID_id_2f41efe3_fk_bills_carriers_carrierId`,
	DROP CONSTRAINT IF EXISTS `bills_bills_carrierID_id_2f41efe3_fk_bills_carriers_carrierId`,
	
	DROP INDEX IF EXISTS `bills_bills_prodID_id_13b1211a_fk_bills_products_prodID`,
	DROP CONSTRAINT IF EXISTS `bills_bills_prodID_id_13b1211a_fk_bills_products_prodID`,
	-- DROP FOREIGN KEY IF EXISTS fk_symbol
	DROP COLUMN IF EXISTS carrierID_id,
	DROP COLUMN IF EXISTS prodID_id;