CREATE DATABASE pastillero2;

CREATE TABLE "DATOS_PX"(
	"ID_PX" SERIAL NOT NULL PRIMARY KEY,
	"NOMBRE" TEXT NOT NULL,
	"Enfermedad" TEXT NOT NULL,
	"Edad" INTEGER NOT NULL,
	"NoSS" INTEGER NOT NULL,
	"Usuario" TEXT NOT NULL,
	"Contra" TEXT NOT NULL
);

CREATE TABLE "Medicamentos"(
	id_medicamento TEXT NOT NULL PRIMARY KEY,
	nombre_medicamento TEXT NOT NULL
);


CREATE TABLE"TRATAMIENTO"(
	"ID_TRATAMIENTO" SERIAL NOT NULL PRIMARY KEY,
	"ID_PACIENTE" INTEGER NOT NULL REFERENCES "DATOS_PX"("ID_PX"),
	"ID_MED_1" TEXT NOT NULL REFERENCES "Medicamentos"(id_medicamento),
	"ID_MED_2" TEXT NOT NULL REFERENCES "Medicamentos"(id_medicamento),
	"ID_MED_3" TEXT NOT NULL REFERENCES "Medicamentos"(id_medicamento),
	"ID_MED_4" TEXT NOT NULL REFERENCES "Medicamentos"(id_medicamento),
	"ID_MED_5" TEXT NOT NULL REFERENCES "Medicamentos"(id_medicamento)	
);

INSERT INTO "Medicamentos"(id_medicamento, nombre_medicamento) VALUES ('1',' ');

SELECT * FROM "Medicamentos" ORDER BY nombre_medicamento ASC;