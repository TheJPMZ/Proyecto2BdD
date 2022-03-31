SELECT 		u.username, SUM(v.duracion) AS total
FROM 		usuario u, pelicula p, casting c, actor a, ver v
WHERE 		c.cpelicula = p.codigo AND c.cactor = a.codigo AND p.codigo = v.cpelicula AND u.codigo = v.cusuario AND a.nombre = 'Will' AND a.apellido = 'Smith'
GROUP BY	u.codigo
ORDER BY 	total DESC
LIMIT       1