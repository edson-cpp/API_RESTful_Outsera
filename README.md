# Raspberry Awards API
API RESTful desenvolvida em Python para leitura da lista de indicados e vencedores da categoria **Pior Filme** do Golden Raspberry Awards e cálculo do intervalo entre vitórias consecutivas dos produtores.

## Requisitos
- Python 3.x
- FastAPI
- Pytest
- CSV (fonte de dados em memória)
- Outros (ver requirements.txt)

## Decisões de implementação

- API construída seguindo nível 2 do modelo de maturidade de Richardson
- Arquitetura simples com separação entre:
  - carregamento de dados
  - lógica de negócio
  - camada HTTP
  
## Como executar o projeto

### 1. Clonar o repositório

git clone git@github.com:edson-cpp/API_RESTful_Outsera.git<br>
cd API_RESTful_Outsera

### 2. Criar e ativar ambiente virtual
## Linux/macOS:
python3 -m venv venv<br>
source venv/bin/activate

## Windows:
python -m venv venv<br>
venv\Scripts\activate

### 3. Instalar dependências
pip install -r requirements.txt

### 4. Executar a aplicação
uvicorn app.main:app --reload

## A API estará disponível em:
http://localhost:8000

## Documentação automática (Swagger):
http://localhost:8000/docs

### Endpoint disponível
## GET /producers/intervals
Retorna os produtores com:
- menor intervalo entre vitórias consecutivas
- maior intervalo entre vitórias consecutivas<br>
Exemplo de resposta<br>

```
{
  "min": [
    {
      "producer": "Producer 1",
      "interval": 1,
      "previousWin": 2008,
      "followingWin": 2009
    }
  ],
  "max": [
    {
      "producer": "Producer 2",
      "interval": 99,
      "previousWin": 1900,
      "followingWin": 1999
    }
  ]
}
```

### Testes
## Para executar os testes:
# Linux/macOS:
export PYTHONPATH=.<br>
pytest
# Windows:
set PYTHONPATH=.<br>
pytest<br>

Os testes de integração garantem que os dados retornados pela API estão consistentes com o arquivo CSV fornecido.

### Observações
- O arquivo CSV é carregado automaticamente ao iniciar a aplicação.
- Os dados são mantidos apenas em memória, sem necessidade de banco externo.