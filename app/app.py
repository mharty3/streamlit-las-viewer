import streamlit as st
import lasio
import plotly_express as px

st.title('Fancy LAS Viewer')
st.write('For Denver Data Drivers')

# set the mode: upload vs read from disk
mode = st.radio(
    "Select an option:",
    ('Upload File', 'Use Preloaded File')
)

# Get a file
if mode == 'Upload File':
    las_file_object = st.file_uploader('Upload a las file:', type=['las', 'LAS'])

if mode == 'Use Preloaded File':
    las_file_object = 'las_data_storage/49-WY/007-Carbon/4900722147_722147B.las'

# Read the file
if las_file_object:
    las = lasio.read(las_file_object)

    # read header data
    well_name = las.header['Well'].WELL.value
    uwi = las.header['Well'].API.value

    st.write(well_name)
    st.write(uwi)

    # read curve data
    df = las.df()
    
    # show curve data table
    show_data_table = st.checkbox('Show Data Table', value=True)
    if show_data_table:
        st.write(las.df())

    # Set up side bar options
    st.write('Look in the sidebar (> in upper left) for some options')
    curve_name = st.sidebar.selectbox('Select a Curve', 
                                      options=las.curves.keys(),
                                      index=1
                                      )
    
    logarithmic = st.sidebar.checkbox("Logarithmic Axis")

    # make the plot
    plotly_curve = px.line(df, 
                        x=curve_name, 
                        y=df.index, 
                        height=1000, 
                        log_x=logarithmic)
    plotly_curve.update_yaxes(autorange='reversed')
    
    # show the plot
    st.write(plotly_curve)