import os
import pandas as pd

# Caminho absoluto para o diretório atual
caminho_atual = os.path.dirname(os.path.abspath(__file__))

# Construindo o caminho completo para o arquivo CSV
caminho_csv = os.path.join(caminho_atual, 'df_acidentes.csv')

# Conversão dos valores da latitude e longitude.
df_acidentes = pd.read_csv(caminho_csv)

class DF_Acidentes():
    def __init__(self) -> None:
        self.df_acidentes = df_acidentes
        self.uf_centerpoint = {'Todo o Brasil': [-10.186558, -48.333780], 'AC': [-8.77, -70.55], 'AL': [-9.62, -36.82], 'AM': [-3.47, -65.10], 'AP': [1.41, -51.77], 'BA': [-13.29, -41.71], 'CE': [-5.20, -39.53], 'ES': [-19.19, -40.34], 'GO': [-15.98, -49.86], 'MA': [-5.42, -45.44], 'MT': [-12.64, -55.42], 'MS': [-20.51, -54.54], 'MG': [-18.10, -44.38], 'PA': [-3.79, -52.48], 'PB': [-7.28, -36.72], 'PR': [-24.89, -51.55], 'PE': [-8.38, -37.86], 'PI': [-6.60, -42.28], 'RJ': [-22.25, -42.66], 'RN': [-5.81, -36.59], 'RO': [-10.83, -63.34], 'RS': [-30.17, -53.50], 'RR': [1.99, -61.33], 'SC': [-27.45, -50.95], 'SE': [-10.57, -37.45], 'SP': [-22.19, -48.79], 'TO': [-9.46, -48.26]}
        self.list_cities_uf_fastdata = {}

        # Processo da criação rápida de listas de cidades por estado.
        for uf in self.uf_centerpoint.keys():
            if uf =='Todo o Brasil':
                self.list_cities_uf_fastdata[uf] = sorted(self.df_acidentes['municipio'].unique())
            else:
                self.list_cities_uf_fastdata[uf] = sorted(self.df_acidentes[self.df_acidentes['uf'] == uf]['municipio'].unique())

    def get_list_uf(self):
        return self.uf_centerpoint.keys()
    
    def get_list_cities(self, UF='Todo o Brasil'):
        return self.list_cities_uf_fastdata[UF]

    def get_uf_centerpoint(self, UF='Todo o Brasil'):
        return self.uf_centerpoint[UF]
        
    def get_dataframe_uf(self, UF=str) -> pd.DataFrame:
        return self.df_acidentes[self.df_acidentes['uf'] == UF]
    
    def get_dataframe_filtered(self, uf, municipio):
        filter = (df_acidentes['uf'] == uf) & (self.df_acidentes['municipio'] == municipio)
        return self.df_acidentes.loc[filter]
    
    def get_dataframe_from_data(self, list_years=None, list_months=None):
        df_filtered = self.df_acidentes

        if list_years is not None:
            df_filtered = df_filtered[df_filtered['ano'].isin(list_years)]
        
        if list_months is not None:
            df_filtered = df_filtered[df_filtered['mes'].isin(list_months)]

        return df_filtered

df_acidentes_transito = DF_Acidentes()