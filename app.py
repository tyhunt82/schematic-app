
import streamlit as st
from streamlit.logger import get_logger
from utils.col_configs import section_config, section_test_data, well_config, well_test_data

LOGGER = get_logger(__name__)

def run():
    # Page config --------------------------
    st.set_page_config(
        page_title="Schematic App",
        page_icon=":punch:",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Sidebar ------------------------------
    with st.sidebar:
        st.title('Schematic App')


    # Tabs ---------------------------------
    tb_setup, tb_schem, tb_inst = st.tabs(["Setup", "Schematic", "Instructions"])

    with tb_setup:
        col1, col2, col3 = st.columns([0.15,0.7,0.15])
        with col2:
            st.title('Well Information Setup')
            st.data_editor(
                data=well_test_data().reset_index(drop=True),
                column_config=well_config(), 
                use_container_width=True,
                hide_index=True
            )
            st.divider()
            st.title('Well Section Setup')
            st.data_editor(
                data=section_test_data().reset_index(drop=True), 
                column_config=section_config(), 
                use_container_width=True,
                hide_index=True
            )


    with tb_schem:
        pass
    
    with tb_inst:
        pass







if __name__ == "__main__":
    run()
