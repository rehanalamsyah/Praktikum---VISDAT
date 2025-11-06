import streamlit as st
import pandas as pd
import numpy as np

st.title("Graphviz")
st.write("Kelompok: 8")
st.markdown("""
- Rehan Alamsyah Putra (0110222168)
- Muhammad Dzaky Dzulfikar Salim (0110222187)
- Ihwanul Fikri Ramadhan (0110222112)
""")

st.graphviz_chart("""
digraph {
    "Training Data" -> "ML Algorithm"
    "ML Algorithm" -> "Model"
    "Model" -> "Results Forecasting"
    "New Data" -> "Model"
}
""")
