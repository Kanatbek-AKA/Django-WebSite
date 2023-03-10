-- Drop all tables by one go
PRAGMA writable_schema = 1;
DELETE FROM sqlite_master;
PRAGMA writable_schema = 0;
VACUUM;
PRAGMA integrity_check;
-- Checking removal of tables 
select * from sqlite_schema;
