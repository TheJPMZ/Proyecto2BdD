CREATE TABLE	USUARIO
(
	CUSUARIO	VARCHAR			NOT NULL,
	USERNAME	VARCHAR			NOT NULL,
	NOMBRE		VARCHAR			NOT NULL,
	PASSWORD	VARCHAR			NOT NULL,
	EMAIL		VARCHAR			NOT NULL,
	CUENTA		VARCHAR			NOT NULL,
	DATE		DATE			,
	PRIMARY KEY	(CUSUARIO)
);
CREATE INDEX USUARIO_CUSUARIO ON USUARIO(CUSUARIO);
CREATE INDEX USUARIO_EMAIL ON USUARIO(EMAIL);
CREATE INDEX USUARIO_USERNAME ON USUARIO(USERNAME);

CREATE TABLE	PELICULA
(
	CPELICULA		VARCHAR		NOT NULL,
	NOMBRE			VARCHAR		NOT NULL,
	DURACION		FLOAT		NOT NULL,
	CLASIFICACION 	INTEGER		NOT NULL,
	IMAGEN			VARCHAR		NOT NULL,
	LINK			VARCHAR		NOT NULL,
	DIRECTOR		VARCHAR		NOT NULL,
	PRIMARY KEY	(CPELICULA)
);
CREATE INDEX PELICULA_CPELICULA ON PELICULA(CPELICULA);
	
CREATE TABLE	ACTOR
(
	CPELICULA	VARCHAR 	NOT NULL,
	NOMBRE		VARCHAR  	NOT NULL,
	PRIMARY	KEY	(CPELICULA, NOMBRE),
	CONSTRAINT	FK_CCPELICULA	FOREIGN KEY	(CPELICULA)	REFERENCES	PELICULA(CPELICULA)
);
CREATE INDEX ACTOR_CPELICULA ON ACTOR(CPELICULA);

CREATE TABLE	GENERO
(
	CPELICULA	VARCHAR 	NOT NULL,
	GENERO		VARCHAR		NOT NULL,
	PRIMARY KEY	(CPELICULA, GENERO),
	CONSTRAINT	FK_CCPELICULA	FOREIGN KEY	(CPELICULA)	REFERENCES	PELICULA(CPELICULA)
);
CREATE INDEX GENERO_CPELICULA ON GENERO(CPELICULA);

CREATE TABLE 	ANUNCIOS
(
    CANUNCIO  	VARCHAR 	NOT NULL,
    ANUNCIO 	VARCHAR 	NOT NULL,
    ANUNCIANTE  VARCHAR		NOT NULL,
    PRIMARY KEY (CANUNCIO)
);
CREATE INDEX ANUNCIOS_CANUNCIO ON ANUNCIOS(CANUNCIO);

CREATE TABLE	ADBREAK
(
	CPELICULA	VARCHAR 	NOT NULL,
	CANUNCIO	VARCHAR		NOT NULL,
	PRIMARY KEY	(CPELICULA, CANUNCIO),
	CONSTRAINT	FK_CCPELICULA	FOREIGN KEY	(CPELICULA)	REFERENCES	PELICULA(CPELICULA),
	CONSTRAINT	FK_CCANUNCIO	FOREIGN KEY	(CANUNCIO)	REFERENCES	ANUNCIOS(CANUNCIO)
);

CREATE TABLE 	PERFIL
(
	CPERFIL		VARCHAR		NOT NULL,
	CUSUARIO 	VARCHAR		NOT NULL,
	LOGNUMBER	INTEGER		NOT NULL,
	PROFILENAME	VARCHAR 	NOT NULL,
	EDAD	  	INTEGER		NOT NULL,
	
	CONSTRAINT	fk_vcusuario	FOREIGN KEY	(cusuario)	REFERENCES	usuario(cusuario),
	PRIMARY KEY (CPERFIL)
);
CREATE INDEX PERFIL_CPERFIL ON PERFIL(CPERFIL);

CREATE TABLE	FAVORITOS
(
	CPERFIL		VARCHAR 	NOT NULL,
	CPELICULA	VARCHAR		NOT NULL,
	PRIMARY KEY	(CPERFIL, CPELICULA),
	CONSTRAINT	FK_CCPELICULA	FOREIGN KEY	(CPELICULA)	REFERENCES	PELICULA(CPELICULA),
	CONSTRAINT	FK_CCPERFIL		FOREIGN KEY	(CPERFIL)	REFERENCES	PERFIL(CPERFIL)
);

CREATE TABLE	VER
(
	CPERFIL		VARCHAR 	NOT NULL,
	CPELICULA	VARCHAR		NOT NULL,
	DURACION 	FLOAT		NOT NULL,
	FECHA		DATE 		NOT NULL,
	TIMESTMP    TIME		NOT NULL,
	CONSTRAINT	FK_CCPELICULA	FOREIGN KEY	(CPELICULA)	REFERENCES	PELICULA(CPELICULA),
	CONSTRAINT	FK_CCPERFIL		FOREIGN KEY	(CPERFIL)	REFERENCES	PERFIL(CPERFIL)
);
CREATE INDEX VER_TIMESTMP ON VER(TIMESTMP);

CREATE TABLE	LOGINLOG
(	
	CODIGO		NUMERIC		NOT NULL,
	UIngreso	VARCHAR 	NOT NULL,
	PIngreso	VARCHAR		NOT NULL,
	FECHA		DATE 		NOT NULL,
	PRIMARY KEY	(CODIGO)
);
CREATE INDEX LOGINLOG_CODIGO ON LOGINLOG(CODIGO);

CREATE TABLE BUSQUEDA(
	ID 		 	SERIAL,
	DATO 		TEXT,
	FECHA 		DATE,
	PRIMARY KEY(ID)	
);

CREATE TABLE HISTORY_MOD (
	ID         	SERIAL,
	TSTAMP   	TIMESTAMP	DEFAULT now(),
	SCHEMANAME 	TEXT,
	TABNAME    	TEXT,
	OPERATION	TEXT,
	WHO			TEXT	DEFAULT current_user
);

DROP TABLE if exists d_date;

CREATE TABLE d_date
(
  date_dim_id              INT NOT NULL,
  date_actual              DATE NOT NULL,
  epoch                    BIGINT NOT NULL,
  day_suffix               VARCHAR(4) NOT NULL,
  day_name                 VARCHAR(10) NOT NULL,
  day_of_week              INT NOT NULL,
  day_of_month             INT NOT NULL,
  day_of_quarter           INT NOT NULL,
  day_of_year              INT NOT NULL,
  week_of_month            INT NOT NULL,
  week_of_year             INT NOT NULL,
  week_of_year_iso         CHAR(10) NOT NULL,
  month_actual             INT NOT NULL,
  month_name               VARCHAR(10) NOT NULL,
  month_name_abbreviated   CHAR(3) NOT NULL,
  quarter_actual           INT NOT NULL,
  quarter_name             VARCHAR(10) NOT NULL,
  year_actual              INT NOT NULL,
  first_day_of_week        DATE NOT NULL,
  last_day_of_week         DATE NOT NULL,
  first_day_of_month       DATE NOT NULL,
  last_day_of_month        DATE NOT NULL,
  first_day_of_quarter     DATE NOT NULL,
  last_day_of_quarter      DATE NOT NULL,
  first_day_of_year        DATE NOT NULL,
  last_day_of_year         DATE NOT NULL,
  mmyyyy                   CHAR(6) NOT NULL,
  mmddyyyy                 CHAR(10) NOT NULL,
  weekend_indr             BOOLEAN NOT NULL
);

ALTER TABLE public.d_date ADD CONSTRAINT d_date_date_dim_id_pk PRIMARY KEY (date_dim_id);

CREATE INDEX d_date_date_actual_idx
  ON d_date(date_actual);

COMMIT;


