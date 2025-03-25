import streamlit as st
import py3Dmol
import io
import base64
from PIL import Image
from rdkit import Chem
from rdkit.Chem import AllChem
from stmol import showmol

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

# 画像を保存する関数
def save_3Dmol_image(view):
    img_data = view.png()  # py3Dmol の画像を取得
    # img = Image.open(io.BytesIO(img_data))
    
    # 画像を一時保存
    # img_path = "molecule.png"
    # img_data.save(img_path)
    return img_data

# Streamlit アプリの設定
st.title("3D Molecular Viewer")

# 入力欄
smiles = st.text_input("Enter a SMILES string:", 
    "COc3nc(OCc2ccc(C#N)c(c1ccc(C(=O)O)cc1)c2P(=O)(O)O)ccc3C[NH2+]")

# 表示スタイル選択
view_style = st.selectbox("Select a view style:", ["stick", "line", "sphere"])

if smiles:
    mol, view = get_optimized_3Dmol(smiles, view_style)
    if mol:
        showmol(view, height=500, width=800)
        st.text("3D structure generated successfully.")
        # 画像表示
        view.png()

        # 画像保存ボタン
        if st.button("Save 3D Molecule Image"):
            img_data = save_3Dmol_image(view)
            img_data.type()

            # 画像を表示
            # st.image(img_path, caption="Saved 3D Molecule", use_column_width=True)

            # ダウンロードボタン
            # st.download_button(
            #     label="Download Image",
            #     data=img_data,
            #     file_name="molecule.png",
            #     mime="image/png"
            # )
    else:
        st.error("3D structure generation failed. Please check the SMILES string.")

