DROP TABLE IF EXISTS diagnosis_codes;

CREATE TABLE diagnosis_codes (
	id serial PRIMARY KEY,
	category_code VARCHAR NOT NULL,
	diagnosis_code VARCHAR NOT NULL,
	full_code VARCHAR NOT NULL,
	abbreviated_description VARCHAR NOT NULL,
	full_description VARCHAR NOT NULL,
	category_title VARCHAR NOT NULL,
	version_number INT NOT NULL DEFAULT 10
);

 INSERT INTO diagnosis_codes (category_code, diagnosis_code, full_code, abbreviated_description, full_description, category_title)
		VALUES('A0', '1234', 'A01234', 'Comma-ind anal ret', 'Comma-induced anal retention', 'Malignant neoplasm of anus and anal canal');