## Instruções para rodar o projeto ##
### Via Docker ###

* Construir a imagem Docker
    
    No diretório raiz do projeto (onde o Dockerfile está localizado), execute:

```sh
docker build -t rec-web . 
```

* Rodar o container

    Após a imagem ser construída, execute:

```sh
docker run -d -p 8000:8000 rec-web
```

* Acessar a API

    O servidor estará acessível em http://localhost:8000.

### Via Docker Compose ###

* Rodar o Docker Compose
    
    No diretório onde o arquivo docker-compose.yml está localizado, execute:

```sh
docker-compose up --build
```

* Acessar a API
    O servidor estará acessível em http://localhost:8000.


## Instruções de uso da API via endpoints. ##

A API tem dois endpoints principais que retornam recomendações de produtos para um determinado user_id.

### Endpoint 1: Recomendações Padrão ###

Este endpoint retorna as recomendações padrão de produtos para o usuário especificado.

  URL:

```text
/recommendations/{user_id}
```

Método:

```text
GET
```

Parâmetro:

```text
user_id: O ID do usuário (inteiro).
```

Resposta:

```text
Retorna um objeto JSON com o user_id e uma lista de recommended_products.
```

Exemplo de Request:

```text
GET /recommendations/123
```

Exemplo de Resposta:

```json
{
    "user_id": 123,
    "recommended_products": [ "Product A", "Product B","Product C" ]
}
```

### Endpoint 2: Obter Recomendações Baseadas no Histórico ###
Este endpoint retorna recomendações de produtos baseadas no histórico de navegação ou compras do usuário.

URL: 

```text
/history_recommendations/{user_id}
```

Método: 

```text
GET
```

Parâmetro:

```text
user_id: O ID do usuário (inteiro).
```

Resposta:

```text
Retorna um objeto JSON com o user_id e uma lista de recommended_products baseadas no histórico.
```

Exemplo de Request:

```text
GET /history_recommendations/123
```

Exemplo de Resposta:

```json
{
    "user_id": 123,
    "recommended_products": [ "Product X", "Product Y","Product Z" ]
}
```