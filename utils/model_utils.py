import joblib
import pandas as pd
from utils.descriptor_utils import descriptor_names, canonicalize_smiles, compute_all_descriptors

# 学習済みモデルのロード
def load_model(model_path="model.pkl"):
    return joblib.load(model_path)

# pKa 予測関数
def predict_pka(smiles, model):
    smiles = canonicalize_smiles(smiles)
    descriptors = compute_all_descriptors(smiles)
    if descriptors is None:
        return "Invalid SMILES"
    descriptors_df = pd.DataFrame([descriptors], columns=descriptor_names)
    return model.predict(descriptors_df)[0]
