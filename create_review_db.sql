CREATE TABLE reviews (
    article_id int generated always as identity primary key,
    product TEXT,
    vendor_code int,
    pros TEXT,
    cons TEXT,
    comment TEXT,
    grade int
);