INSERT INTO pelicula(
	cpelicula, nombre, duracion, clasificacion, imagen, link)
VALUES (
	'P1',	'Matrix',	136,	18,	'https://m.media-amazon.com/images/M/MV5BYWQxMzg0OGYtNGE3Yi00OGY4LWJjZDktZWZiODE2N2MyODgzXkEyXkFqcGdeQXVyMTYzMDM0NTU@._V1_QL75_UY281_CR13,0,190,281_.jpg','https://www.imdb.com/video/vi1032782617?playlistId=tt0133093&ref_=tt_pr_ov_vi' ) , (
	'P2',	'El señor de los anillos: La comunidad del anillo',	178,	12,	'https://m.media-amazon.com/images/M/MV5BMzgyNjdjOWMtMjAyYy00NzQ4LWIwYTQtZDk2ZDQzYWVlN2IwXkEyXkFqcGdeQXVyMTYzMDM0NTU@._V1_QL75_UY281_CR3,0,190,281_.jpg','https://www.imdb.com/video/vi684573465?playlistId=tt0120737&ref_=tt_pr_ov_vi' ) , (
	'P3',	'El señor de los anillos: Las dos torres',	179,	12,	'https://m.media-amazon.com/images/M/MV5BY2YyYjVlZDgtYTVkNy00MjdmLWFhNjctY2RlYWNhMzMyYTczXkEyXkFqcGdeQXVyODc0OTEyNDU@._V1_QL75_UY*_.jpg','https://www.imdb.com/video/vi701350681?playlistId=tt0167261&ref_=tt_ov_vi' ) , (
	'P4',	'El señor de los anillos: El retorno del rey',	201,	12,	'https://m.media-amazon.com/images/M/MV5BNGJjODMxZGMtOTFlNC00MjI4LThiZWUtZTU3ZGIxYzcxMTBiXkEyXkFqcGdeQXVyODc0OTEyNDU@._V1_QL75_UY*_.jpg','https://www.imdb.com/video/vi718127897?playlistId=tt0167260&ref_=tt_pr_ov_vi' ) , (
	'P5',	'Turning Red',	100,	10,	'https://m.media-amazon.com/images/M/MV5BNjY0MGEzZmQtZWMxNi00MWVhLWI4NWEtYjQ0MDkyYTJhMDU0XkEyXkFqcGdeQXVyODc0OTEyNDU@._V1_QL75_UX*_CR0,0,*_.jpg','https://www.imdb.com/video/vi3974546201?playlistId=tt8097030&ref_=tt_ov_vi' ) , (
	'P6',	'Encanto',	102,	0,	'https://m.media-amazon.com/images/M/MV5BNjE5NzA4ZDctOTJkZi00NzM0LTkwOTYtMDI4MmNkMzIxODhkXkEyXkFqcGdeQXVyNjY1MTg4Mzc@._V1_QL75_UX*_CR0,0,*_.jpg','https://www.imdb.com/video/vi4093755417?playlistId=tt2953050&ref_=tt_ov_vi' ) , (
	'P7',	'Game of Thrones',	57,	18,	'https://m.media-amazon.com/images/M/MV5BOGY1NDQ1MDMtYTY1ZS00MGQ1LTg5ZTgtMDljM2IxY2NhODJhXkEyXkFqcGdeQXVyMTYzMDM0NTU@._V1_QL75_UY*_.jpg','https://www.youtube.com/watch?v=TZE9gVF1QbA' ) , (
	'P8',	'Terminator: Génesis',	126,	12,	'https://m.media-amazon.com/images/M/MV5BMjM1NTc0NzE4OF5BMl5BanBnXkFtZTgwNDkyNjQ1NTE@._V1_QL75_UX*_CR0,*_.jpg','https://www.imdb.com/video/vi1249751321?playlistId=tt1340138&ref_=tt_ov_vi' ) , (
	'P9',	'Death on the Nile',	127,	13,	'https://resizing.flixster.com/ndFvbUyQAZgUf5dXVl1_n2DY3x4=/206x305/v2/https://resizing.flixster.com/T2N9zgvfcLehEt1EkYNrLRaNPXU=/ems.ZW1zLXByZC1hc3NldHMvbW92aWVzLzgzYTg5ODBlLWY5MzMtNGIyYi04MWU0LTMwZTgwYTUyYjIyMS5qcGc=','https://www.youtube.com/watch?v=dZRqB0JLizw' )

;

INSERT INTO actor(
	cpelicula, nombre)
VALUES (
	'P1','Keanu Reeves') , (
	'P1','Laurence Fishburne') , (
	'P2','Elijah Wood') , (
	'P2','Ian McKellen') , (
	'P2','Viggo Mortensen') , (
	'P3','Elijah Wood') , (
	'P3','Ian McKellen') , (
	'P3','Viggo Mortensen') , (
	'P4','Elijah Wood') , (
	'P4','Ian McKellen') , (
	'P4','Viggo Mortensen') , (
	'P4','Sean Bean') , (
	'P2','Sean Bean') , (
	'P5','Rosalie Chiang') , (
	'P5','Sandra Oh') , (
	'P6','Stephanie Beatriz') , (
	'P6','Maria Cecilia') , ( 
	'P7','Sean Bean') , (
	'P7','Emilia Clarke') , (
	'P7','Kit Harrington') , (
	'P8','Emilia Clarke') , (
	'P8','Arnold Schwarzenegger') , (
	'P8','Jason Clarke') 
;

INSERT INTO genero(
	cpelicula, genero)
VALUES (
	'P1','Ciencia Ficcion') , (
	'P1','Accion') , (
	'P2','Accion') , (
	'P2','Aventura') , (
	'P2','Drama') , (
	'P3','Accion') , (
	'P3','Aventura') , (
	'P3','Drama') , (
	'P4','Accion') , (
	'P4','Aventura') , (
	'P4','Drama') , (
	'P5','Animacion') , (
	'P5','Aventura') , (
	'P5','Comedia') , (
	'P6','Animacion') , (
	'P6','Comedia') , (
	'P6','Familiar') , (
	'P7','Accion') , (
	'P7','Aventura') , (
	'P7','Drama') , (
	'P8','Accion') , (
	'P8','Aventura') , (
	'P8','Ciencia Ficcion')
;

INSERT INTO usuario(
	cusuario, username, nombre, password, email, cuenta)
VALUES (
	'U1','egirl21','Jorge Escopetas','5c7149bf161be854ee758c49aa5b2ad466ad656571dc0527660c07fcf381c493','escopeteando@gmail.com','Avanzada') , (
	'U2','jpmz','Jose Monzon','2f6c46d7790bdad37504095e613b1c852f5888308e2b6ec4bc2d8e9481ee2eff','mon20309@uvg.edu.gt','Admin') , (
	'U3','cayomol','Cayetano Moina','522fa1a6b36eb4500e5cd08aaf8150e50005390c3307940f0c9fc8c4c983fd1e','mol20211@uvg.edu.gt','Admin') 
;

INSERT INTO perfil(
	cperfil, cusuario, lognumber, profilename, edad)
VALUES (
	'Per1','U1',1,'Gerardo [23]',23) , (
	'Per2','U1',2,'Kenny [15]',15) , (
	'Per3','U1',3,'Mabel [10]',10) , (
	'Per4','U1',4,'Anita [6]',6) , (
	'Per5','U1',5,'Deadsoon[99]',99) 
;

INSERT INTO anuncios(
	canuncio, anuncio, anunciante)
VALUES (
	'A1','https://youtu.be/efD3nmwF-IM','Malec') , (
	'A2','https://youtu.be/DAC0t92N8Bc','Galletas Gama') , (
	'A3','https://youtu.be/WHwQeetjLwk','Tesla')
;

INSERT INTO adbreak(
	cpelicula, canuncio)
VALUES (
	'P7','A1') , (
	'P2','A2') , (
	'P3','A2') , (
	'P4','A2') , (
	'P5','A2') , (
	'P6','A2') , (
	'P8','A2') , (
	'P9','A2') , (
	'P6','A3') 
;

INSERT INTO favoritos(
	cperfil, cpelicula)
VALUES (
	'Per1','P7')
;