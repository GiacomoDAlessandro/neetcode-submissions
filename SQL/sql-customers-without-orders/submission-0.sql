-- Write your query below
-- Customers who have never placed an order,  return names
SELECT name
FROM customers
WHERE id NOT IN (SELECT customer_id FROM orders);