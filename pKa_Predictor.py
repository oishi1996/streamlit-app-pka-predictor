import streamlit as st
from utils.model_utils import load_model, predict_pka
from streamlit_ketcher import st_ketcher

# モデルのロード
model = load_model()

# Streamlit UI
st.title(":material/Science: pKa Predictor")
st.markdown("""
            - This app allows you to draw chemical structures and predict their pKa values
            - Draw your molecule below...
            """)


with st.container():
    smiles = st_ketcher()

    if smiles:
        predicted_pka = predict_pka(smiles, model)
        st.success(f"**Generated SMILES:** `{smiles}`")
        st.success(f"Predicted pKa: {predicted_pka:.2f}")
    else:
        st.warning("No molecule detected. Please draw a structure.")


# smiles_input = st_ketcher()

# # 予測ボタン
# if st.button("🔍 予測"):
#     predicted_pka = predict_pka(smiles_input, model)
#     st.success(f"Predicted pKa: {predicted_pka:.2f}")
