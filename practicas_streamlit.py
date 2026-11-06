import streamlit as st
import time

st.success("Todo correcto")
mensaje_error=st.error("No ha ido bien")
time.sleep(3)
mensaje_error.empty()
st.toast("Mensaje flotante", duration="long")
