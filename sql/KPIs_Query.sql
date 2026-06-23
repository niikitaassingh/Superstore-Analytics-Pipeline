SELECT
    ROUND(SUM(sales),2) AS total_sales
FROM fact_sales;


SELECT
    ROUND(
        (SUM(profit) / SUM(sales))*100,
        2
    ) AS profit_margin_pct
FROM fact_sales;

SELECT
    ROUND(
        (SUM(profit) / SUM(sales))*100,
        2
    ) AS profit_margin_pct
FROM fact_sales;

SELECT
    COUNT(DISTINCT order_id) AS total_orders
FROM fact_sales;

SELECT
    COUNT(DISTINCT customer_id) AS total_customers
FROM fact_sales;

SELECT
    ROUND(
        SUM(sales) /
        COUNT(DISTINCT order_id),
        2
    ) AS avg_order_value
FROM fact_sales;

SELECT
    COUNT(DISTINCT product_id) AS total_products
FROM fact_sales;

SELECT
    p.product_name,
    ROUND(SUM(f.sales),2) AS total_sales
FROM fact_sales f
JOIN dim_product p
ON f.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sales DESC
LIMIT 10;


SELECT
    p.product_name,
    ROUND(SUM(f.profit),2) AS total_profit
FROM fact_sales f
JOIN dim_product p
ON f.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_profit DESC
LIMIT 10;

SELECT
    ROUND(
        SUM(sales) /
        COUNT(DISTINCT customer_id),
        2
    ) AS revenue_per_customer
FROM fact_sales;

SELECT
    ROUND(
        SUM(profit) /
        COUNT(DISTINCT customer_id),
        2
    ) AS profit_per_customer
FROM fact_sales;

SELECT
    ROUND(
        SUM(profit) /
        COUNT(DISTINCT customer_id),
        2
    ) AS profit_per_customer
FROM fact_sales;

SELECT
    region,
    ROUND(SUM(sales),2) AS total_sales
FROM fact_sales
GROUP BY region
ORDER BY total_sales DESC;

SELECT
    region,
    ROUND(SUM(sales),2) AS total_sales
FROM fact_sales
GROUP BY region
ORDER BY total_sales DESC;


SELECT
    region,
    ROUND(SUM(sales),2) AS total_sales
FROM fact_sales
GROUP BY region
ORDER BY total_sales DESC;

SELECT
    ship_mode,
    COUNT(DISTINCT order_id) AS total_orders
FROM fact_sales
GROUP BY ship_mode
ORDER BY total_orders DESC;


SELECT
    ship_mode,
    ROUND(SUM(profit),2) AS total_profit
FROM fact_sales
GROUP BY ship_mode
ORDER BY total_profit DESC;


SELECT
    ROUND(SUM(sales),2) AS total_sales,
    ROUND(SUM(profit),2) AS total_profit,

    ROUND(
        (SUM(profit)/SUM(sales))*100,
        2
    ) AS profit_margin_pct,

    COUNT(DISTINCT order_id) AS total_orders,

    COUNT(DISTINCT customer_id) AS total_customers,

    ROUND(
        SUM(sales)/
        COUNT(DISTINCT order_id),
        2
    ) AS avg_order_value

FROM fact_sales;