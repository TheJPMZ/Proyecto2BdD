INSERT INTO usuario(
		edad,codigo,username,nombre,apellido,password, email)
VALUES (
		20,'U1','jpmz','Jose','Monzon','pepepepepep','mon20309@uvg.edu.gt'),(
		20,'U2','cayomol','Cayetano','Molina','mememememe','mol20211@uvg.edu.gt'),(
		32,'U3','egirl21','Jorge','Escopetas','1234','escopeteando@gmail.com');

INSERT INTO actor(
	codigo, nombre, apellido, edad)
	VALUES (
		'A1', 'Will', 'Smith', 53),(
		'A2', 'Marlon', 'Brando', 99);

INSERT INTO genero(
	codigo, nombre_genero)
	VALUES 	('G1', 'Accion'),
			('G2', 'Misterio'),
			('G3', 'Ciencia Ficcion');

INSERT INTO pelicula(
	codigo, nombre, genero, duracion)
	VALUES ('P1', 'I, Robot', 'G1', 115);

INSERT INTO casting(
	codigo_rol, cactor, cpelicula, rol)
	VALUES ('CAST1', 'A1', 'P1', 'Protagonista');

INSERT INTO ver(
	cusuario, cpelicula, duracion, fecha, hora)
	VALUES 	('U1', 'P1', '115', '2022-03-16', '16:02'),
			('U2','P1','45','2022-03-16', '16:02');

INSERT INTO perfiles(
	cusuario, profilename, edad, Lognumber)
	VALUES 	('U1', 'perfil1', '20', '1'),
			('U2', 'perfil2', '32', '1');
)