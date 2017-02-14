%?Cuántos 5s hay en A?
Map5= (A==5)
CountFive= sum(sum(Map5))

%?Cuántos 2s hay en el 2do renglón de B?
Map2B=(B(2,:)==2)
Count2B=sum(sum(Map2B))

%?Cuántos 23s hay en la 2da columna de A?
Map23A= (A(:, 2)==23)
Count23=sum(sum(Map23A))

%Tamaño de la matriz
S=size(A);


S
%S(1) es el num de renglones de A y S(2) es el num de cols
%Ejercicio: Sacar la tabla de frecuencia de los distintos valores de la matriz
%Ejemplo de For:
for c=1:5
c
end