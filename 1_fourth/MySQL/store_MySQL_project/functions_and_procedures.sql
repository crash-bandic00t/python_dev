-- Процедура выбора рекомендуемых товаров для пользователя

drop procedure if exists recommended_products;

delimiter //
create procedure recommended_products(for_user_id BIGINT UNSIGNED)
	begin
		-- товары когда-либо заказанные пользователем
		select
			product_id,
			products.name as product_name
		from users
		join orders on users.id = orders.user_id
		join order_products on order_products.order_id = orders.id
		join products on products.id = order_products.product_id 
		where users.id = for_user_id
			union 
		-- товары которым пользователь поставил like
		select 
			product_id,
			products.name as product_name
		from
			likes
		join products on products.id = likes.product_id
		where user_id = for_user_id
		order by rand()
		limit 5;
	end//
delimiter ;
		
call recommended_products(28);

-- Процедура выборки бестселлеров по всем исполненым заказам заказам
drop procedure if exists bestsellers;

delimiter //
create procedure bestsellers()
	begin
		select
			op.product_id as product_id,
			p.name,
			count(*) as cnt
		from orders o
		join order_products op on op.order_id = o.id
		join products p on p.id = op.product_id
		where status = 'executed'
		group by product_id
		order by cnt desc
		limit 5;
	end//
delimiter ;


call bestsellers()