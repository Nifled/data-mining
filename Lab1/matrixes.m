num_reng = 5;
num_col = 7;

% Iniciando matrices en 0
A = zeros(num_reng, num_col);

% Transpose A
TA = A';

% Acceso a los datos
A(1,5) = 5;

% Asignar 9 al primer elemento del ultimo renglon
A(5, 1) = 9;

% Todo el segundo renglon tenga el valor 2
A(2,:) = 2;

% La columna 3 tenga el valor 23
A(:,3) = 23;

% Sumar un elemento a una matriz
B = A + 2;

% Sumar 2 matrices
C = A + B;

% Para ver los distintos valores que contiene una matriz 
UA = unique(A);
UC = unique(C);
UB = unique(B);

% filter funtction(Python) for MATLAB
MapCeros = (A==2);
MapCeros(2,:);  % Segundo renglon de MapCeros

sum(MapCeros(2,:));  % Cuenta el total de 1's que hay en la matriz de MapCeros


fives = (A==5);
sum(fives(1,:));  % Contar numero de 5's de A 

twos = (B(2,:)==2);  % Contar numero de 2's en 2do renglon de B 
sum(twos);

% Contar numero de 23's en 2da columna de A 
twotrey = sum((A(:,2)==23));