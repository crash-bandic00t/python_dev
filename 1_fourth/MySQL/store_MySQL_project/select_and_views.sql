
-- Запрос, показывающий все товары, которые пользователь когда либо заказывал, вместе с view:
create or replace view view_order_products
as
	select
		firstname,
		email,
		orders.id as order_id,
		products.id as product_id,
		products.name as product_name,
		products.price as product_price
	from users
	join orders on users.id = orders.user_id
	join order_products on order_products.order_id = orders.id
	join products on products.id = order_products.product_id 
	where users.id = 28
	order by order_id;

select * from view_order_products 

-- Запрос, показывающий все заказы пользователя, вместе с view:
create or replace view view_user_orders
as
	select
		firstname,
		email,
		o.id,
		created_at,
		status
	from users u 
	join orders o on o.user_id = u.id 
	where u.id = 28;

select * from view_user_orders 

-- Запрос для определения количества музыкальных файлов в таблице media
select
	count(*),
	media_type_id,
	mt.name
from media m
join media_types mt on mt.id = m.media_type_id 
where media_type_id = 2
group by media_type_id; 

-- Запрос на определение количесва заказов каждого пользователя
select 
	u.id,
	u.firstname,
	count(*) as orders_cnt
from users u 
join orders o on o.user_id = u.id
group by u.id
order by orders_cnt desc;
