

{{ config(materialized='table') }}

with x as (
select c.id as customer_id,
	o.due as due,
	c.name as name,
	avg(due) over (partition by c.id) as avg_due,
	rank() over (partition by c.id order by due desc)
from dwh.orders o 
join dwh.customers c on o.customer_id = c.id)
select customer_id, name, due, round(avg_due) as avg_due
from x 
where rank = 1