from rdkit import Chem
from rdkit.Chem import Descriptors

# 記述子リスト
descriptor_names = [desc[0] for desc in Descriptors.descList]

# カノニカル SMILES に変換
def canonicalize_smiles(smiles):
    mol = Chem.MolFromSmiles(smiles)
    return Chem.MolToSmiles(mol, canonical=True) if mol else None

# 記述子計算
def compute_all_descriptors(smiles):
    mol = Chem.MolFromSmiles(smiles)
    return [getattr(Descriptors, desc)(mol) for desc in descriptor_names] if mol else None
