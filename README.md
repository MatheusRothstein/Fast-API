# Fast-API

Este projeto é uma API RestFul contruída em python com framework FastAPI. Para executá-lo, siga as etapas abaixo.

##  Pré-requisitos

Certifique-se de que possui os seguintes itens instalados em sua máquina.

- Docker

## Passos

- Faça o clone do repositório: 
```
git clone https://github.com/MatheusRothstein/Fast-API.git
```
- Acesse a raíz do projeto: 
```
cd Fast-API
```
- Crie e execute o container Docker: 
```
docker-compose up --build
```

## Testes

 Para executar os testes unitários, basta executar o comando:
 ```
 python3 -m unittest discover -s tests -p "*_test.py"
 ``` 