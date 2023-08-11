# python_exercise

## PORTUGUES

### SOBRE

- Este projeto visa solucionar um problema simples de distribuição de empregados para determinadas funções de acordo com algumas premissas. Lembrando que nesse caso estamos utilizando a ideia de motoboys partindo em direção à lojas.

### REQUISITOS

- python 3.10
- pip instalado

### REPOSITORIO

.
└── PYTHON_EXERCISE<br />
├── app<br />
│ ├── **init**.py<br />
│ ├── main<br />
│ ├── **init**.py<br />
│ └── helpers<br />
│ ├── **init**.py<br />
│ └── app_helper.py<br />
│ ├── validation<br />
│ ├── **init**.py<br />
│ └── regex_helper.py<br />
├── tests<br />
│ ├── **init**.py<br />
│ └── tests.py<br />
├── venv<br />
├── .gitignore<br />
├── app.py<br />
├── requirements.txt<br />
└── TESTE TECNOLOGIA - DESENVOLVEDORES.pdf

### PASSOS

- Primeiro, clone o projeto do git na pasta de sua escolha para executa-lo localmente. Execute os comandos dentro da pasta do projeto na ordem abaixo.

```
python3 -m venv venv
```

```
source ./venv/bin/activate
```

```
pip install -r requirements.txt
```

O comando abaixo serve para verificação do coverage de tests

```
python3 -m pytest tests/tests.py -v
```

Para executar o projeto principal, execute o comando abaixo

```
python3 app.py
```

- O problema proposto encontra-se no pdf
- Este app pode executar a separação dos motoboys por quantidade de motoboys e das 3 lojas, podemos colocar quantas encomendas quisermos também. Essas opções estão desabilitadas pelo fato de operar apenas para resolver o problema proposto;
- Exemplo: Loja 1 vai ter agora 5 entregas, logo passamos um array com 5 valores;
- Podemos também alterar a porcentagem recebida pelos motoboys de acordo com a loja. Exemplo loja 3 vai dar 20%, passamos uma variável com share3 = 0.2;
- Estas opções encontram-se comentadas. Caso queira utiliza-las, descomente e siga as premissas explicadas no prompt;
- Digite no nome do motoboy motoboy{numero} ou Motoboy{numero}, não Moto {numero}

## ENGLISH

### ABOUT

- This project has a goal to split employees to the right position following few premises. In this case I'm using motoboy heading to stores.

### REQUIREMENTS

- python 3.10
- pip installed

### REPOSITORY

.
└── PYTHON_EXERCISE<br />
├── app<br />
│ ├── **init**.py<br />
│ ├── main<br />
│ ├── **init**.py<br />
│ └── helpers<br />
│ ├── **init**.py<br />
│ └── app_helper.py<br />
│ ├── validation<br />
│ ├── **init**.py<br />
│ └── regex_helper.py<br />
├── tests<br />
│ ├── **init**.py<br />
│ └── tests.py<br />
├── venv<br />
├── .gitignore<br />
├── app.py<br />
├── requirements.txt<br />
└── TESTE TECNOLOGIA - DESENVOLVEDORES.pdf

### STEPS

- First, clone the repository in the local folder. Second, follow the commands below in the right order.

```
python3 -m venv venv
```

```
source ./venv/bin/activate
```

```
pip install -r requirements.txt
```

The command below has a function to see the test coverage in the app

```
python3 -m pytest tests/tests.py -v
```

To execute the main project, please follow the command below

```
python3 app.py
```

- The proposed problem can be found in pdf file;
- This app can execute rearrangement of motoboys by quantity of three stores, each one can have n orders. This option is disable to use but you can enable it just by uncommenting the code in app.py;
- We can change the quantity of orders of each store by inserting an array of each one passing the values of each order. Example store1 ===> 50,10,150,100,70,30 (The code will understand that it's an array);
- Also we can change the share of each store passing share3 (share of store 3) = 0.5, which corresponds to 50%;
- Type motoboy{number} or Motoboy{number}, not Moto {number}
