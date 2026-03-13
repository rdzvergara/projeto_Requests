import requests
import base64

class ManipulaRepos:
    def __init__(self, username):
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.access_token = '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' 
        self.headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'X-GitHub-Api-Version': '2022-11-28'
        }
    
    def cria_repo(self, nome_repo):
        data = {
            "name" : nome_repo,
            "description" : "Dados dos repositórios de algumas empresas",
            "private" : False
        }
        #Criando o repositório
        response = requests.post(f"{self.api_base_url}/user/repos", headers=self.headers, json=data)
        if response.status_code == 201:
            print(f"Repositório '{nome_repo}' criado com sucesso!")
        else:
            print(f"Falha ao criar o repositório '{nome_repo}'. Status code: {response.status_code}")

    def add_arquivo(self, nome_repo, nome_arquivo, caminho_arquivo):
        #Codificando o arquivo
        with open(caminho_arquivo, 'rb') as file:
            file_content = file.read()
        
        encoded_content = base64.b64encode(file_content).decode('utf-8')
        # Realizando o upload
        url = f"{self.api_base_url}/repos/{self.username}/{nome_repo}/contents/{nome_arquivo}"
        data = {
            "message" : f"Adicionando o arquivo {nome_arquivo}",
            "content" : encoded_content
        }
        
        response = requests.put(url, headers=self.headers, json=data)
        if response.status_code == 201:
            print(f"Arquivo '{nome_arquivo}' adicionado com sucesso ao repositório '{nome_repo}'!")
        else:
            print(f"Falha ao adicionar o arquivo '{nome_arquivo}' ao repositório '{nome_repo}'. Status code: {response.status_code}")


# Instanciando um objeto
novo_repo = ManipulaRepos('rdzvergara')

# Criando um repositório
nome_repo = 'linguagens_repositorios_empresas'
novo_repo.cria_repo(nome_repo)

# Adicionando os arquivos salvos no repositório criado
novo_repo.add_arquivo(nome_repo, 'linguagens_amazon.csv', 'dados/linguagens_amazon.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_netflix.csv', 'dados/linguagens_netflix.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_spotify.csv', 'dados/linguagens_spotify.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_apple.csv', 'dados/linguagens_apple.csv')
