import pandas as pd
from utils.descriptor_utils import canonicalize_smiles

def load_and_preprocess_data(file_path):
    # データの読み込み
    df = pd.read_csv(file_path)

    # 前処理
    df["pka_value"] = df["pka_value"].astype(str).str.replace(r'[><~]', '', regex=True).str.strip()
    df["pka_value"] = pd.to_numeric(df["pka_value"], errors='coerce')
    df = df.dropna(subset=["pka_value"])
    df["canonical_SMILES"] = df["SMILES"].apply(canonicalize_smiles)
    
    # 重複削除
    df_unique = df.drop_duplicates(subset="canonical_SMILES", keep="first")
    
    return df_unique
