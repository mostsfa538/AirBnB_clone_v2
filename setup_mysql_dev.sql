CREATE database IF NOT EXISTS hbnb_dev_db;
-- drop user hbnb_dev@localhost;
-- flush privileges;
CREATE user IF NOT EXISTS hbnb_dev@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO hbnb_dev@'localhost';
GRANT SELECT ON performance_schema.* TO hbnb_dev@'localhost';
FLUSH PRIVILEGES;
