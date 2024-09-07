create table Sales (
    sale_id serial primary key,
    product_id int,
    year VARCHAR(50),
    quantity int,
    price numeric(10, 2)
);