import streamlit as st

st.title("README")

st.subheader(":material/info: Overview", divider=True)
st.image("./docs/pred_act_plot.png", use_container_width=True)
st.markdown("""
### Application Features
- Sketch molecules interactively.
- Predict the pKa value of the drawn molecule.

### Model Details
- Uses molecular descriptors from RDKit.
- Implemented with an ExtraTrees Regressor model for pKa prediction.

### Technologies Used
- **Python** for backend processing.
- **RDKit** for molecular descriptor calculations.
- **Streamlit** for building the interactive web app.
- **Scikit-learn** for machine learning model training.
""")

st.markdown("""
### How It Works
- Users can sketch a molecule using an interactive drawing tool.
- The application extracts molecular descriptors from RDKit.
- The trained ExtraTrees Regressor model predicts the pKa value.
""")

st.subheader(":material/database: Data Source", divider=True)
st.markdown("""
- **Data Source**
This application utilizes the **IUPAC Digitized pKa Dataset, v2.2**.
The dataset is provided under the **CC BY-NC 4.0 license** and is reproduced with permission from IUPAC.
- **Citation**
Zheng, J. W., & Lafontant-Joseph, O. (2024). IUPAC Digitized pKa Dataset, v2.2.
Copyright © 2024 IUPAC. [DOI: 10.5281/zenodo.7236453](https://doi.org/10.5281/zenodo.7236453)
""")
