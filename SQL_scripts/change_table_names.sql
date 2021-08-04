/* Changes the names of the tables if they exist */

RENAME TABLES IF EXISTS
	bills_carriers TO bills_carrier, 
	bills_products TO bills_product,
	bills_bills TO bills_bill,
	bills_billspaid TO bills_billpaid;