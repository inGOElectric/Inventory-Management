BEGIN TRANSACTION;
CREATE TABLE deleted_inwarding (
	id INTEGER NOT NULL, 
	inwarding_id INTEGER, 
	"productId" INTEGER, 
	part_id INTEGER, 
	area INTEGER, 
	cost INTEGER, 
	quantity INTEGER, 
	quantity1 INTEGER, 
	remaining_area INTEGER, 
	vendor_id INTEGER, 
	vendor_address INTEGER, 
	vendor_phn INTEGER, 
	location_id INTEGER, 
	location_area INTEGER, 
	operationperson_id INTEGER, 
	operationperson_phn INTEGER, 
	inwarding_time DATETIME, 
	type VARCHAR(50) NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY("productId") REFERENCES products ("productId"), 
	FOREIGN KEY(part_id) REFERENCES products (part_id), 
	FOREIGN KEY(area) REFERENCES products (area), 
	FOREIGN KEY(vendor_id) REFERENCES vendor (vendor_id), 
	FOREIGN KEY(vendor_address) REFERENCES vendor (vendor_address), 
	FOREIGN KEY(vendor_phn) REFERENCES vendor (vendor_phn), 
	FOREIGN KEY(location_id) REFERENCES location (location_id), 
	FOREIGN KEY(location_area) REFERENCES location (location_area), 
	FOREIGN KEY(operationperson_id) REFERENCES operationperson (operationperson_id), 
	FOREIGN KEY(operationperson_phn) REFERENCES operationperson (operationperson_phn)
);
INSERT INTO "deleted_inwarding" VALUES(1,6,'RH-switch','fdfs343',5,4,45,0,NULL,'minda','delhi',987654321,'essase',4000,'kashi',5645645,'2023-05-04 11:18:10.000000','inward');
INSERT INTO "deleted_inwarding" VALUES(2,7,'indicator','45343rtet',5,10,19,0,NULL,'minda','delhi',987654321,'inGO',6000,'kashi',5645645,'2023-05-04 11:41:36.000000','inward');
INSERT INTO "deleted_inwarding" VALUES(3,8,'jfghfghf',656,6,6,66,0,NULL,'minda','delhi',987654321,'inGO',6000,'kashi',5645645,'2023-05-04 11:46:50.000000','inward');
INSERT INTO "deleted_inwarding" VALUES(4,9,'RH-switch','rh-3433',4,4,5,0,NULL,'minda','delhi',987654321,'inGO',6000,'kashi',5645645,'2023-05-04 11:48:24.000000','inward');
INSERT INTO "deleted_inwarding" VALUES(5,10,'LH-indicator','rewrw33',5,10,9,0,NULL,'minda','delhi',987654321,'inGO',6000,'kashi',5645645,'2023-05-04 11:55:41.000000','inward');
INSERT INTO "deleted_inwarding" VALUES(6,11,'kdjldasd','sdad',34,3,1,0,NULL,'minda','delhi',987654321,'inGO',6000,'kashi',5645645,'2023-05-04 11:58:58.000000','inward');
INSERT INTO "deleted_inwarding" VALUES(7,12,'hjgjh','tytryr',54,4,36,0,NULL,'minda','delhi',987654321,'inGO',6000,'kashi',5645645,'2023-05-04 12:10:28.000000','inward');
INSERT INTO "deleted_inwarding" VALUES(8,13,'stem','yhty5',7,23,18,0,NULL,'minda','delhi',987654321,'inGO',6000,'kashi',5645645,'2023-05-04 12:10:28.000000','inward');
INSERT INTO "deleted_inwarding" VALUES(9,14,'brake-switch','76fdfd',3,10,10,0,NULL,'minda','delhi',987654321,'inGO',6000,'kashi',5645645,'2023-05-04 12:10:28.000000','inward');
INSERT INTO "deleted_inwarding" VALUES(10,17,'indicator-rh','3ghy5',4,10,10,0,NULL,'minda','delhi',987654321,'inGO',6000,'kashi',5645645,'2023-05-04 13:43:05.000000','inward');
INSERT INTO "deleted_inwarding" VALUES(11,15,'brake-switch','76fdfd',3,10,38,0,NULL,'minda','delhi',987654321,'inGO',6000,'kashi',5645645,'2023-05-04 12:10:28.000000','inward');
INSERT INTO "deleted_inwarding" VALUES(12,16,NULL,NULL,NULL,1,1,0,NULL,'minda','delhi',987654321,'inGO',6000,'kashi',5645645,'2023-05-04 13:41:49.000000','inward');
INSERT INTO "deleted_inwarding" VALUES(13,18,'indicator-rh','3ghy5',4,10,0,0,NULL,'minda','delhi',987654321,'sudharshan',3000,'kashi',5645645,'2023-05-04 13:52:44.000000','inward');
INSERT INTO "deleted_inwarding" VALUES(14,19,'indicator-rh','3ghy5',4,100,0,0,NULL,'minda','delhi',987654321,'sudharshan',3000,'kashi',5645645,'2023-05-04 13:54:51.000000','inward');
INSERT INTO "deleted_inwarding" VALUES(15,20,'indicator-rh','3ghy5',4,10,10,0,NULL,'minda','delhi',987654321,'sudharshan',3000,'kashi',5645645,'2023-05-04 13:54:51.000000','inward');
INSERT INTO "deleted_inwarding" VALUES(16,1,'led','reter',3,3,20,0,NULL,'minda','delhi',987654321,'sudharshan',3000,'kashi',5645645,'2023-05-04 14:03:37.000000','inward');
INSERT INTO "deleted_inwarding" VALUES(17,2,'led3','gf45',5,5,5,0,NULL,'minda','delhi',987654321,'sudharshan',3000,'kashi',5645645,'2023-05-04 14:19:59.000000','inward');
INSERT INTO "deleted_inwarding" VALUES(18,4,'rectifiers','ghfg443',5,4,6,0,NULL,'minda','delhi',987654321,'sudharshan',3000,'kashi',5645645,'2023-05-04 14:26:46.000000','inward');
INSERT INTO "deleted_inwarding" VALUES(19,3,'rectifiers','ghfg443',5,1,0,0,NULL,'minda','delhi',987654321,'sudharshan',3000,'kashi',5645645,'2023-05-04 14:26:46.000000','inward');
INSERT INTO "deleted_inwarding" VALUES(20,5,'rectifiers','ghfg443',5,1,3,0,NULL,'minda','delhi',987654321,'sudharshan',3000,'kashi',5645645,'2023-05-04 14:39:24.000000','inward');
CREATE TABLE deleted_location (
	id INTEGER NOT NULL, 
	location_id VARCHAR(200), 
	location_area INTEGER, 
	deleted_date DATETIME, 
	PRIMARY KEY (id)
);
INSERT INTO "deleted_location" VALUES(1,'sudharshan',5000,'2023-05-04 10:53:42.000000');
INSERT INTO "deleted_location" VALUES(2,'essase',4000,'2023-05-04 11:28:42.000000');
INSERT INTO "deleted_location" VALUES(3,'essase',4000,'2023-05-04 11:28:42.000000');
INSERT INTO "deleted_location" VALUES(4,'essae',4000,'2023-05-04 13:46:27.000000');
INSERT INTO "deleted_location" VALUES(5,'inGO',6000,'2023-05-04 13:46:27.000000');
INSERT INTO "deleted_location" VALUES(6,'inGO',6000,'2023-05-04 13:46:27.000000');
CREATE TABLE deleted_movements (
	id INTEGER NOT NULL, 
	movement_id INTEGER, 
	"productId" INTEGER, 
	part_id INTEGER, 
	area INTEGER, 
	operationperson_id INTEGER, 
	operationperson_phn INTEGER, 
	quantity INTEGER, 
	from_location INTEGER, 
	to_location INTEGER, 
	type VARCHAR(50) NOT NULL, 
	deleted_date DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY("productId") REFERENCES inwardings ("productId"), 
	FOREIGN KEY(part_id) REFERENCES inwardings (part_id), 
	FOREIGN KEY(area) REFERENCES inwardings (area), 
	FOREIGN KEY(operationperson_id) REFERENCES inwardings (operationperson_id), 
	FOREIGN KEY(operationperson_phn) REFERENCES inwardings (operationperson_phn), 
	FOREIGN KEY(from_location) REFERENCES location (location_id), 
	FOREIGN KEY(to_location) REFERENCES location (location_id)
);
INSERT INTO "deleted_movements" VALUES(1,5,'kdjldasd','sdad',34,'kashi',5645645,2,'inGO','essae','movements','2023-05-04 11:58:58.000000');
INSERT INTO "deleted_movements" VALUES(2,5,'hjgjh','tytryr',54,'kashi',5645645,3,'inGO','essae','movements','2023-05-04 12:10:28.000000');
INSERT INTO "deleted_movements" VALUES(3,5,'stem','yhty5',7,'kashi',5645645,2,'inGO','essae','movements','2023-05-04 12:10:28.000000');
INSERT INTO "deleted_movements" VALUES(4,1,'indicator','45343rtet',5,'kashi',5645645,1,'inGO','essae','movements','2023-05-04 12:10:28.000000');
INSERT INTO "deleted_movements" VALUES(5,4,'LH-indicator','rewrw33',5,'kashi',5645645,1,'inGO','essae','movements','2023-05-04 12:10:28.000000');
INSERT INTO "deleted_movements" VALUES(6,3,'RH-switch','rh-3433',4,'kashi',5645645,10,'inGO','essae','movements','2023-05-04 12:10:28.000000');
INSERT INTO "deleted_movements" VALUES(7,2,'jfghfghf',656,6,'kashi',5645645,1,'inGO','essae','movements','2023-05-04 12:10:28.000000');
INSERT INTO "deleted_movements" VALUES(8,1,'brake-switch','76fdfd',3,'kashi',5645645,10,'inGO','essae','movements','2023-05-04 13:46:27.000000');
INSERT INTO "deleted_movements" VALUES(9,1,'indicator-rh','3ghy5',4,'kashi',5645645,20,'sudharshan','essae mechatronics','movements','2023-05-04 14:03:37.000000');
CREATE TABLE deleted_outwarding (
	id INTEGER NOT NULL, 
	outward_id INTEGER, 
	"productId" INTEGER, 
	part_id INTEGER, 
	area INTEGER, 
	operationperson_id INTEGER, 
	operationperson_phn INTEGER, 
	quantity INTEGER, 
	to_location INTEGER, 
	type VARCHAR(50) NOT NULL, 
	sales_id INTEGER, 
	deleted_date DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY("productId") REFERENCES productmovements ("productId"), 
	FOREIGN KEY(part_id) REFERENCES productmovements (part_id), 
	FOREIGN KEY(area) REFERENCES productmovements (area), 
	FOREIGN KEY(operationperson_id) REFERENCES productmovements (operationperson_id), 
	FOREIGN KEY(operationperson_phn) REFERENCES productmovements (operationperson_phn), 
	FOREIGN KEY(to_location) REFERENCES productmovements (to_location), 
	FOREIGN KEY(sales_id) REFERENCES sales (sales_id)
);
INSERT INTO "deleted_outwarding" VALUES(1,1,'hjgjh','tytryr',54,'kashi',5645645,1,'essae','outwardings',NULL,'2023-05-04 12:10:28.000000');
CREATE TABLE deleted_person (
	id INTEGER NOT NULL, 
	operationperson_id VARCHAR(200), 
	operationperson_phn INTEGER, 
	deleted_date DATETIME, 
	PRIMARY KEY (id)
);
INSERT INTO "deleted_person" VALUES(1,'kashi',5464565,'2023-05-04 10:58:15.000000');
CREATE TABLE deleted_product (
	id INTEGER NOT NULL, 
	"productId" VARCHAR(200), 
	part_id INTEGER, 
	area INTEGER, 
	deleted_date DATETIME, 
	PRIMARY KEY (id)
);
INSERT INTO "deleted_product" VALUES(1,'flasher','dsfd',4,'2023-05-04 10:31:40.000000');
INSERT INTO "deleted_product" VALUES(2,'flasher','dsfd',4,'2023-05-04 10:31:40.000000');
INSERT INTO "deleted_product" VALUES(3,'flasher','dsfd',4,'2023-05-04 10:31:40.000000');
INSERT INTO "deleted_product" VALUES(4,'battery','rterter',5,'2023-05-04 10:31:40.000000');
INSERT INTO "deleted_product" VALUES(5,'led','ertrte',4,'2023-05-04 10:35:36.000000');
INSERT INTO "deleted_product" VALUES(6,'led','ertrte',4,'2023-05-04 10:35:36.000000');
INSERT INTO "deleted_product" VALUES(7,'circuit breaker','fdf-4545',5,'2023-05-04 10:35:36.000000');
INSERT INTO "deleted_product" VALUES(8,'circuit breaker','fdf-4545',5,'2023-05-04 10:40:19.000000');
INSERT INTO "deleted_product" VALUES(9,'battery','erer',4,'2023-05-04 11:11:30.000000');
INSERT INTO "deleted_product" VALUES(10,'brakeswitch','tfgdfg',4,'2023-05-04 11:11:30.000000');
INSERT INTO "deleted_product" VALUES(11,'brakeswitch','tfgdfg',4,'2023-05-04 11:11:30.000000');
INSERT INTO "deleted_product" VALUES(12,'RH-switch','fdfs343',5,'2023-05-04 11:40:15.000000');
INSERT INTO "deleted_product" VALUES(13,'indicator','45343rtet',5,'2023-05-04 11:41:36.000000');
INSERT INTO "deleted_product" VALUES(14,'jfghfghf',656,6,'2023-05-04 11:46:50.000000');
INSERT INTO "deleted_product" VALUES(15,'RH-switch','rh-3433',4,'2023-05-04 11:48:24.000000');
INSERT INTO "deleted_product" VALUES(16,'LH-indicator','rewrw33',5,'2023-05-04 11:55:41.000000');
INSERT INTO "deleted_product" VALUES(17,'kdjldasd','sdad',34,'2023-05-04 11:58:58.000000');
INSERT INTO "deleted_product" VALUES(18,'kdjldasd','sdad',34,'2023-05-04 11:58:58.000000');
INSERT INTO "deleted_product" VALUES(19,'hjgjh','tytryr',54,'2023-05-04 12:10:28.000000');
INSERT INTO "deleted_product" VALUES(20,'hjgjh','tytryr',54,'2023-05-04 12:10:28.000000');
INSERT INTO "deleted_product" VALUES(21,'stem','yhty5',7,'2023-05-04 12:10:28.000000');
INSERT INTO "deleted_product" VALUES(22,'stem','yhty5',7,'2023-05-04 12:10:28.000000');
INSERT INTO "deleted_product" VALUES(23,'indicator','45343rtet',5,'2023-05-04 12:10:28.000000');
INSERT INTO "deleted_product" VALUES(24,'LH-indicator','rewrw33',5,'2023-05-04 12:10:28.000000');
INSERT INTO "deleted_product" VALUES(25,'RH-switch','rh-3433',4,'2023-05-04 12:10:28.000000');
INSERT INTO "deleted_product" VALUES(26,'jfghfghf',656,6,'2023-05-04 12:10:28.000000');
INSERT INTO "deleted_product" VALUES(27,'brake-switch','76fdfd',3,'2023-05-04 13:46:27.000000');
INSERT INTO "deleted_product" VALUES(28,'indicator-rh','3ghy5',4,'2023-05-04 14:03:37.000000');
INSERT INTO "deleted_product" VALUES(29,'indicator-rh','3ghy5',4,'2023-05-04 14:03:37.000000');
INSERT INTO "deleted_product" VALUES(30,'led','reter',3,'2023-05-04 14:11:56.000000');
INSERT INTO "deleted_product" VALUES(31,'led','reter',3,'2023-05-04 14:11:56.000000');
INSERT INTO "deleted_product" VALUES(32,'led3','gf45',5,'2023-05-04 14:26:46.000000');
INSERT INTO "deleted_product" VALUES(33,'led3','gf45',5,'2023-05-04 14:26:46.000000');
CREATE TABLE deleted_vendor (
	id INTEGER NOT NULL, 
	vendor_id VARCHAR(200), 
	vendor_address INTEGER, 
	vendor_phn INTEGER, 
	deleted_date DATETIME, 
	PRIMARY KEY (id)
);
INSERT INTO "deleted_vendor" VALUES(1,'evolute','bangalore',8767867867,'2023-05-04 10:46:29.000000');
CREATE TABLE "inwardings" (

	"inwarding_id"	INTEGER NOT NULL,

	"productId"	INTEGER,

	"part_id"	INTEGER,

	"area"	INTEGER,

	"cost"	INTEGER,

	"quantity"	NUMERIC,

	"remaining_area"	TEXT,

	"vendor_id"	TEXT,

	"vendor_address"	TEXT,

	"vendor_phn"	TEXT,

	"location_id"	TEXT,

	"location_area"	INTEGER,

	"operationperson_id"	INTEGER,

	"operationperson_phn"	INTEGER,

	"inwarding_time"	DATETIME,

	"type"	VARCHAR(50) NOT NULL,

	"quantity1"	INTEGER DEFAULT 0,

	PRIMARY KEY("inwarding_id" AUTOINCREMENT),

	FOREIGN KEY("operationperson_id") REFERENCES "operationperson"("operationperson_id"),

	FOREIGN KEY("area") REFERENCES "products"("area"),

	FOREIGN KEY("part_id") REFERENCES "products"("part_id"),

	FOREIGN KEY("operationperson_phn") REFERENCES "operationperson"("operationperson_phn"),

	FOREIGN KEY("productId") REFERENCES "products"("productId"),

	FOREIGN KEY("location_area") REFERENCES "location"("location_area"),

	FOREIGN KEY("vendor_address") REFERENCES "vendor"("vendor_address"),

	FOREIGN KEY("location_id") REFERENCES "location"("location_id"),

	FOREIGN KEY("vendor_id") REFERENCES "vendor"("vendor_id"),

	FOREIGN KEY("vendor_phn") REFERENCES "vendor"("vendor_phn")

);
INSERT INTO "inwardings" VALUES(6,'rectifiers','ghfg443',5,1,20,NULL,'minda','delhi','987654321','essae mechatronics',3000,'kashi',5645645,'2023-05-04 14:46:33.000000','inward',20);
CREATE TABLE location (
	location_id VARCHAR(200) NOT NULL, 
	location_area INTEGER, 
	date_created DATETIME, 
	PRIMARY KEY (location_id)
);
INSERT INTO "location" VALUES('sudharshan',3000,'2023-05-04 13:52:44.000000');
INSERT INTO "location" VALUES('essae mechatronics',3000,'2023-05-04 13:52:44.000000');
CREATE TABLE operationperson (
	operationperson_id VARCHAR(200) NOT NULL, 
	operationperson_phn INTEGER, 
	date_created DATETIME, 
	PRIMARY KEY (operationperson_id)
);
INSERT INTO "operationperson" VALUES('kashi',5645645,'2023-05-04 11:09:44.000000');
CREATE TABLE outwards (
	outward_id INTEGER NOT NULL, 
	"productId" INTEGER, 
	part_id INTEGER, 
	area INTEGER, 
	operationperson_id INTEGER, 
	operationperson_phn INTEGER, 
	quantity INTEGER, 
	to_location INTEGER, 
	sales_id INTEGER, 
	outward_time DATETIME, 
	type VARCHAR(50) NOT NULL, 
	PRIMARY KEY (outward_id), 
	FOREIGN KEY("productId") REFERENCES productmovements ("productId"), 
	FOREIGN KEY(part_id) REFERENCES productmovements (part_id), 
	FOREIGN KEY(area) REFERENCES productmovements (area), 
	FOREIGN KEY(operationperson_id) REFERENCES productmovements (operationperson_id), 
	FOREIGN KEY(operationperson_phn) REFERENCES productmovements (operationperson_phn), 
	FOREIGN KEY(to_location) REFERENCES productmovements (to_location), 
	FOREIGN KEY(sales_id) REFERENCES sales (sales_id)
);
CREATE TABLE "overall product balance" (
"index" INTEGER,
  "Part" TEXT,
  "Id" TEXT,
  "Date" TEXT,
  "essae mechatronics" INTEGER,
  "Total" INTEGER
);
INSERT INTO "overall product balance" VALUES(0,'rectifiers','ghfg443','2023-05-04',26,26);
CREATE TABLE "product balance" (
"PartName" INTEGER
);
CREATE TABLE "productmovements" (

	"movement_id"	INTEGER NOT NULL,

	"productId"	INTEGER,

	"part_id"	INTEGER,

	"area"	INTEGER,

	"operationperson_id"	INTEGER,

	"operationperson_phn"	INTEGER,

	"quantity"	INTEGER,

	"from_location"	INTEGER,

	"to_location"	INTEGER,

	"movement_time"	DATETIME,

	"type"	VARCHAR(50) NOT NULL,

	PRIMARY KEY("movement_id"),

	FOREIGN KEY("operationperson_id") REFERENCES "inwardings"("operationperson_id"),

	FOREIGN KEY("productId") REFERENCES "inwardings"("productId"),

	FOREIGN KEY("part_id") REFERENCES "inwardings"("part_id"),

	FOREIGN KEY("to_location") REFERENCES "location"("location_id"),

	FOREIGN KEY("area") REFERENCES "inwardings"("area"),

	FOREIGN KEY("operationperson_phn") REFERENCES "inwardings"("operationperson_phn"),

	FOREIGN KEY("from_location") REFERENCES "location"("location_id")

);
INSERT INTO "productmovements" VALUES(1,'rectifiers','ghfg443',5,'kashi',5645645,6,'sudharshan','essae mechatronics','2023-05-04 14:39:24.000000','movements');
CREATE TABLE products (
	"productId" VARCHAR(200) NOT NULL, 
	part_id INTEGER, 
	area INTEGER, 
	date_created DATETIME, 
	PRIMARY KEY ("productId")
);
INSERT INTO "products" VALUES('rectifiers','ghfg443',5,'2023-05-04 14:26:46.000000');
CREATE TABLE sales (
	sales_id VARCHAR(200) NOT NULL, 
	date_created DATETIME, 
	PRIMARY KEY (sales_id)
);
INSERT INTO "sales" VALUES('customer','2023-04-28 12:35:16.000000');
CREATE TABLE "summary" (
"index" INTEGER,
  "Type" TEXT,
  "Part" TEXT,
  "Id" TEXT,
  "Quantity" INTEGER,
  "from_location" INTEGER,
  "to_location" TEXT,
  "Person" TEXT,
  "Contact" INTEGER,
  "Date" TEXT
);
INSERT INTO "summary" VALUES(0,'inward','led3','gf45',5,0,'sudharshan','kashi',5645645,'2023-05-04');
CREATE TABLE vendor (
	vendor_id VARCHAR(200) NOT NULL, 
	vendor_address INTEGER, 
	vendor_phn INTEGER, 
	date_created DATETIME, 
	PRIMARY KEY (vendor_id)
);
INSERT INTO "vendor" VALUES('minda','delhi',987654321,'2023-04-28 17:07:08.000000');
CREATE INDEX "ix_product balance_PartName"ON "product balance" ("PartName");
CREATE INDEX "ix_summary_index"ON "summary" ("index");
CREATE INDEX "ix_overall product balance_index"ON "overall product balance" ("index");
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('inwardings',6);
COMMIT;
