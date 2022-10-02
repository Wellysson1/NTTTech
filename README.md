# NTTTech
Para conseguir rodar os processos da forma correta siga estes passos:
1 - Abra o terminal e execute o comando: "pip install fastapi"
2 - No terminal execute o comando: "pip install "uvicorn[standard]""
3 - Para rodar o servidor uvicorn ainda no terminal execute o comando "uvicorn main:app --reload"
4 - Para conseguir se conectar ao seu Banco de Dados não se esqueça de trocar os dados de acesso presentes nas linhas 8 a 12, 29 a 34 e 52 a 57.
5 - Caso deseje criar o schema e as tabelas de forma automática será necessário descomentar o código das linhas 8 até a linha 17;

Para acessar os métodos, com o servidor rodando acesse os endereços pelo Insomnia, Postman, pelo link direto ou pelo Swagger.
GetCifra - http://127.0.0.1:8000/getCifra
ResolveCifra - http://127.0.0.1:8000/resolveCifra  (Necessário inserir a frase que deseja decifrar e a chave que será utiizada em formato JSON.)
GetRaca - http://127.0.0.1:8000/getRaca
GetFacts - http://127.0.0.1:8000/getFacts
Swagger - http://127.0.0.1:8000/docs
Tirando o método ResolveCifra em nenhum outro será necessário inseriir querys ou headers para fazer as requisições;
