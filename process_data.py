import pandas as pd

file_path = "avocado.csv"  # Assurez-vous que le chemin du fichier est correct

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("Le fichier spécifié est introuvable.")
        return None
    except Exception as e:
        print("Une erreur s'est produite lors du chargement du fichier :", e)
        return None

def handle_missing_values(data):
    if data.isnull().values.any():
        print("Il y a des valeurs manquantes dans le dataset. Voici quelques informations :")
        print(data.isnull().sum())
        data.dropna(inplace=True)
        print("Les valeurs manquantes ont été supprimées.")
    else:
        print("Il n'y a pas de valeurs manquantes dans le dataset.")

def display_header(data):
    print("Entête du dataset :")
    print(data.head())

def display_descriptive_statistics(data):
    print("Statistiques descriptives :")
    print(data.describe())

def main():
    data = load_data(file_path)
    if data is not None:
        handle_missing_values(data)
        display_header(data)
        display_descriptive_statistics(data)

if __name__ == "__main__":
    main()
