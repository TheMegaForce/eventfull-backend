-- settings.sql
CREATE DATABASE event;
CREATE USER eventuser WITH PASSWORD 'event';
GRANT ALL PRIVILEGES ON DATABASE event TO eventuser;

-- Example
-- CREATE DATABASE restaurants;
-- CREATE USER restaurantsuser WITH PASSWORD 'restaurants';
-- GRANT ALL PRIVILEGES ON DATABASE restaurants TO restaurantsuser;