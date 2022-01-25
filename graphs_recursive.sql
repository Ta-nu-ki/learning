WITH RECURSIVE flights (src, path, dest, amount) AS 
(
	SELECT
		src, 
		ARRAY[src], 
		dest,
		price
	FROM flight
	UNION ALL
	SELECT
		fp.src, 
		fp.path || flight.src, -- добавляем пересадку
		flight.dest, 
		(fp.amount + flight.price) AS amount -- считаем расходы
	FROM flight
	JOIN flights AS fp 
	ON flight.src = fp.dest AND flight.src != ANY(fp.path) -- исключаем города, в которых уже были
) 
SELECT 
	src, 
	dest,
	MIN(amount) 
FROM flights 
WHERE src = 'Los Angeles' and dest = 'Montreal' 
GROUP BY (src, dest)
