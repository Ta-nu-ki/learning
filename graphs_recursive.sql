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
		fp.path || flight.src, -- adds connection
		flight.dest, 
		(fp.amount + flight.price) AS amount -- calculates expenditures
	FROM flight
	JOIN flights AS fp 
	ON flight.src = fp.dest AND flight.src != ANY(fp.path) -- excluding visited cities
) 
SELECT 
	src, 
	dest,
	MIN(amount) 
FROM flights 
WHERE src = 'Los Angeles' and dest = 'Montreal' 
GROUP BY (src, dest)
