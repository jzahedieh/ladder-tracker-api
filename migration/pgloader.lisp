# mysql.cnf
# sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION

LOAD DATABASE
FROM mysql://user:password@localhost/tennis2_migrate
INTO postgresql://postgres@localhost/postgres;