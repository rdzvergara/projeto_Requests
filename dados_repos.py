from math import ceil
import requests
import pandas as pd

class DadosRepos:
    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = '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'
        self.headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'X-GitHub-Api-Version': '2022-11-28'
        }
    
    def listar_repositorios(self):
        url = f'{self.api_base_url}/users/{self.owner}'
        response = requests.get(url, headers=self.headers)
        num_pages = ceil(response.json()['public_repos'] / 30) 

        repos_list = []

        for page_num in range(1, num_pages + 1):
            try:
                url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url, headers=self.headers)
                repos_list.append(response.json())
            except:
                repos_list.append(None)
            
        return repos_list
    
    def nomes_repos(self,repos_list):
        repos_names = []
        for page in repos_list:
            for repo in page:
                try:
                    if repo['language'] is not None: 
                       repos_names.append(repo['name'])
                except:
                    pass
        return repos_names
    
    def nomes_linguagens(self, repos_list):
        repos_languages = []
        for page in repos_list:
            for repo in page:
                try:
                    if repo['language'] is not None:
                       repos_languages.append(repo['language'])
                except:
                    pass
        return repos_languages
    
    def cria_df_linguagens(self):
        repositorios = self.listar_repositorios()
        nomes = self.nomes_repos(repositorios)
        linguagens = self.nomes_linguagens(repositorios)

        dados = pd.DataFrame({'nome': nomes, 'linguagem': linguagens})
        return dados
    

amazon_rep = DadosRepos('amzn')
lng_mais_usadas_amzn = amazon_rep.cria_df_linguagens()

netflix_rep = DadosRepos('netflix')
lng_mais_usadas_netflix = netflix_rep.cria_df_linguagens()

spotify_rep = DadosRepos('spotify')
lng_mais_usadas_spotify = spotify_rep.cria_df_linguagens()

apple_rep = DadosRepos('apple')
lng_mais_usadas_apple = apple_rep.cria_df_linguagens()

#Salvando os dados em arquivos csv
lng_mais_usadas_amzn.to_csv('dados/linguagens_amazon.csv', index=True, index_label='id')
lng_mais_usadas_netflix.to_csv('dados/linguagens_netflix.csv', index=True, index_label='id')
lng_mais_usadas_spotify.to_csv('dados/linguagens_spotify.csv', index=True, index_label='id')
lng_mais_usadas_apple.to_csv('dados/linguagens_apple.csv', index=True, index_label='id')
