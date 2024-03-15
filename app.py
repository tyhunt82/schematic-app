
import streamlit as st
from streamlit.logger import get_logger
from components import sb 

LOGGER = get_logger(__name__)



def run():
    st.set_page_config(
        page_title="Schematic App",
        page_icon=":punch:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    sb.sidebar()

    tb_setup, tb_schem, tb_inst = st.tabs(["Setup", "Schematic", "Instructions"])

   


if __name__ == "__main__":
    run()
