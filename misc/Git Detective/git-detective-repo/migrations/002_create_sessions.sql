CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    token VARCHAR(256) NOT NULL,
    expires_at TIMESTAMP NOT NULL
);
