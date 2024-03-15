import streamlit as st
import pandas as pd
from datetime import datetime 

def well_config():
  return {
      'Well Name': st.column_config.TextColumn(label="Well Name"), 
      'Well Id': st.column_config.TextColumn(label="Well Id"),
      'Date': st.column_config.DatetimeColumn(label="Date Time",format="MM/D/YYYY h:mm a",),
      'Setup By': st.column_config.TextColumn(label="Setup By"),
      'Comments': st.column_config.TextColumn(label="Comments", width='medium')
  }
def well_test_data():
    return pd.DataFrame({
        'Well Name': ['MT7-93'],
        'Well ID': ['ABC-123'],
        'Date': [datetime(2023, 6, 1)],
        'Setup By': ['Tyler Hunt'],
        'Comments': ['This is a test well'],
    })

def section_config():
  return {
      'Name': st.column_config.TextColumn(label="Name"), 
      'Type': st.column_config.SelectboxColumn(
          label="Type",
          options=["Wellbore", "Casing", "Tubing", "Liner", "Drill String", "Bha"]
      ),
      'OD': st.column_config.NumberColumn(format="%.4f"),  
      'ID': st.column_config.NumberColumn(format="%.4f"),
      'Top Md': st.column_config.NumberColumn(format="%.2f"),
      'Btm Md': st.column_config.NumberColumn(format="%.2f"),
  }



def section_test_data():
    return pd.DataFrame({
        'Name': ['Conductor', 'Surface', 'Intermediate'],
        'Type': ['A', 'B', 'A'],
        'OD': [12.34, 6.78, 9.14],
        'ID': [10.16, 5.45, 7.01],
        'Top Md': [1.0, 2.5, 3.0],
        'Btm Md': [4.0, 5.5, 6.0]
    })