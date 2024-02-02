use flask_db;
CREATE TABLE Users (
	id VARCHAR(64) UNIQUE PRIMARY KEY,
    username VARCHAR(30) NOT NULL,
    email VARCHAR(20) NOT NULL UNIQUE,
    login_date DATE NOT NULL
);

SELECT * FROM Users;