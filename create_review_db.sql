CREATE TABLE reviews (
    article_id int generated always as identity primary key,
    company TEXT,
    product TEXT,
    vendor_code TEXT,
    pros TEXT,
    cons TEXT,
    comment TEXT,
    grade TEXT
);