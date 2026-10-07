"""Streamlit entry point (e.g. Streamlit Community Cloud)."""
import streamlit as st

import fielddash

st.set_page_config(page_title="Residuos Bacanga", page_icon="📊", layout="wide")
fielddash.require_access()  # optional PIN: set FIELD_ACCESS_PIN in Streamlit secrets
fielddash.dashboard("project.yaml", configure_page=False)
