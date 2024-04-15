CREATE database IF NOT EXISTS hbnb_dev_db;
drop user hbnb_dev@localhost;
flush privileges;
CREATE user hbnb_dev@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON database.hbnb_dev_db TO hbnb_dev@'localhost';
