% Trabajando con el archivo de HeartDisease (base de datos)

% Agrega ruta para directorio donde esta el archivo de trabajo
addpath 'H:\Erick\Documents\Github\data-mining\Lab3';

% ruta del archivo
filename = 'HeartDisease.csv';
Casos = csvread( filename );

% Elimina la 1er columna, porque solo son ID's (1,2,3,4,...)
Casos(:,1) = [];

% Para ver los distintos valores que contiene columna 58 de Casos 
unique(Casos(:,58))

% Agarrar los que no tienen diagnostico de enfermedad cardiovascular (No
% heart disease)
Map = Casos(:,58) == 0;
Casos_NoHD = Casos(Map, :);

% Renglones que SI tienen heart disease
Map2 = Casos(:,58) > 0;
Casos_SiHD = Casos(Map2, :);

% Graficar num de cigarros que fuman los que NO tienen HD

% Plot graph
figure
plot(Casos_NoHD(:,14)); 

% Bar graph
figure(2)
bar(Casos_NoHD(:,14));

% Pie chart
figure(3)
pie3(Casos_NoHD(:,14));

figure(3)
bar(Casos_SiHD(:,14));