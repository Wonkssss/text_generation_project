#PREPROCESS THE SUPERHEROES DATASET
import pandas as pd

class SuperHeroes():
    def __init__(self):
        self.superheroes = pd.read_csv('superheroes_nlp_dataset.csv')
        self.superheroes = self.superheroes.drop(columns=['Unnamed: 0'])
        self.superheroes = self.superheroes.drop(columns=['Unnamed: 0.1'])
        self.superheroes = self.superheroes.drop(columns=['Unnamed: 0.1.1'])

        self.superheroes = self.superheroes.dropna()
        self.superheroes = self.superheroes.reset_index(drop=True)
