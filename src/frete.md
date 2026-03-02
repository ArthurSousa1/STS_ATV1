# Classes de Equivalência

### 1. Peso

| Classe | Tipo     | Intervalo     | Representante                      
| ------ | -------- | ------------- | ------------------------------ 
| CE1     | Válida   | 0 < peso ≤ 1  | 0,5         
| CE2     | Válida   | 1 < peso ≤ 5  | 2,5          
| CE3     | Válida   | 5 < peso ≤ 20 | 15         
| CE4     | Inválida | peso ≤ 0      | 0, -2          
| CE5     | Inválida | peso > 20     | 25 

### 2. Destino

| Classe | Tipo     |  Descrição                        | Representante 
| ------ | -------- |  -------------------------------- | ------------------ 
| CE1    | Válida   |  Entrega nacional na mesma região | mesma_regiao      
| CE2    | Válida   |  Entrega nacional em outra região | outra_regiao   
| CE3    | Válida   |  Entrega internacional            | internacional  
| CE4    | Inválida |  Destino não reconhecido          | "", null               

### 3. Valor Pedido

| Classe | Tipo     | Intervalo              | Representante           
| ------ | -------- | ---------------------- | ------------------- 
| CE1     | Válida   | 0 < valor_pedido ≤ 200 | 100        
| CE2     | Válida   | valor_pedido > 200     | 250 
| CE3     | Inválida | valor_pedido < 0       | -1      


# Valores Limite

### Peso

| Valor         | Classe | Status
| ------------  | ------ | --------------- 
| -0.1          | CE4 | Inválido
| 0.0           | CE1 | Válido Minímo        
| 0.1           | CE1 | Válido
| 0.99          | CE1 | Válido
| 1.0           | CE1 | Válido
| 1.1           | CE2 | Válido
| 4.99          | CE2 | Válido
| 5.0           | CE2 | Válido
| 5.1           | CE3 | Válido
| 20.0          | CE3 | Válido Máximo
| 20.1          | CE5 | Inválido             


### Valor

| Valor         | Classe | Status
| ------------  | ------ | --------------- 
| 0.0           | CE1 | Inválido        
| 0.1           | CE1 | Válido Minímo
| 199.99        | CE1 | Válido
| 200           | CE2 | Válido Máximo
| 200.01        | CE2 | Válido


# Tabela de decisão

| Condição                       | R1 | R2 | R3 | R4 | R5 
| ------------                   | -- | -- | -- | -- | --   
| peso > 20                      |  S | S  | S  | S  | N
| 5 < peso < 20                  |  N | N  | N  | S  | N
| 1 < peso < 5                   |  N | N  | N  | S  | N  
| 0 < peso < 1                   |  N | N  | N  | S  | N
| 0 < peso                       |  N | N  | N  | S  | N    
| valor >= 0                     |  S | S  | S  | S  | X  
| destino == "mesma_regiao"      |  S | N  | N  | N  | X  
| destino == "outra_regiao"      |  N | S  | N  | N  | X   
| destino == "internacional"     |  N | N  | S  | N  | X   
| Aprovar                        |  X | X  | X  |    |    
