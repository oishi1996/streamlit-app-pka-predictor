import streamlit as st
import py3Dmol
from rdkit import Chem
from rdkit.Chem import AllChem
from stmol import showmol
from streamlit_ketcher import st_ketcher

# 3D分子構造を取得する関数
def get_optimized_3Dmol(smiles, view_style):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None, None  # SMILES のパースに失敗した場合

    mol = Chem.AddHs(mol, addCoords=True)
    try:
        AllChem.EmbedMolecule(mol, AllChem.ETKDG())  # 3D座標生成
        AllChem.MMFFOptimizeMoleculeConfs(mol)  # 力場最適化
    except Exception as e:
        st.error(f"3D構造の最適化に失敗しました: {e}")
        return None, None
    
    target_sdf = Chem.MolToMolBlock(mol)

    view = py3Dmol.view(data=target_sdf)
    view.setStyle({view_style: {}})
    return mol, view

# Streamlit UI
st.title(":material/Science: 3D Molecular Viewer")
st.markdown("""
            - This app allows you to draw chemical structures and generate 3D structure
            - Draw your molecule below...
            """)

# --- SMILES 入力方法の選択 ---
input_mode = st.radio("Choose input method:", ["Text Input", "Draw Molecule"], horizontal=True)

if input_mode == "Text Input":
    smiles = st.text_input("Enter a SMILES string:", 
        "COc3nc(OCc2ccc(C#N)c(c1ccc(C(=O)O)cc1)c2P(=O)(O)O)ccc3C[NH2+]")
else:
    smiles = st_ketcher()


# 表示スタイル選択
view_style = st.selectbox("Select a view style:", ["stick", "line", "sphere"])

if smiles:
    mol, view = get_optimized_3Dmol(smiles, view_style)
    if mol:
        showmol(view, height=500, width=800)
        st.text("3D structure generated successfully.")
    else:
        st.error("3D structure generation failed. Please check the SMILES string.")

