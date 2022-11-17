from backbone.heat_stored import *
import time
import streamlit as st

st.header('Heat Stored Method')

with st.form("monte_form"):
    col1, col2, col3, col4 = st.columns(4)
    # col 1 (a,h,phi)
    col1.markdown("**Area** (km<sup>2</sup>)", unsafe_allow_html=True)
    a = {}
    a['min'] = col1.text_input(label='min{}'.format(0*' '),value=0)
    a['max'] = col1.text_input(label='max{}'.format(0*' '),value=0)
    a['most'] = col1.text_input(label='most{}'.format(0*' '),value=0)
    col1.markdown("**Thickness** (m)", unsafe_allow_html=True)
    h = {}
    h['min'] = col1.text_input(label='min{}'.format(1*' '),value=0)
    h['max'] = col1.text_input(label='max{}'.format(1*' '),value=0)
    h['most'] = col1.text_input(label='most{}'.format(1*' '),value=0)
    col1.markdown("**Porosity** (0 to 1)", unsafe_allow_html=True)
    phi = {}
    phi['min'] = col1.text_input(label='min{}'.format(2*' '),value=0)
    phi['max'] = col1.text_input(label='max{}'.format(2*' '),value=0)
    phi['most'] = col1.text_input(label='most{}'.format(2*' '),value=0)
    
    # col 2 (rho_r,cr,rf)
    col2.markdown("**ρ<sub>r</sub>** (kg/m<sup>3</sup>)", unsafe_allow_html=True)
    rho_r = {}
    rho_r['min'] = col2.text_input(label='min{}'.format(3*' '),value=0)
    rho_r['max'] = col2.text_input(label='max{}'.format(3*' '),value=0)
    rho_r['most'] = col2.text_input(label='most{}'.format(3*' '),value=0)
    col2.markdown("**C<sub>r</sub>** (kJ/kg<sup>o</sup>C)", unsafe_allow_html=True)
    cr = {}
    cr['min'] = col2.text_input(label='min{}'.format(4*' '),value=0)
    cr['max'] = col2.text_input(label='max{}'.format(4*' '),value=0)
    cr['most'] = col2.text_input(label='most{}'.format(4*' '),value=0)
    col2.markdown("**RF** (0 to 1)", unsafe_allow_html=True)
    rf = {}
    rf['min'] = col2.text_input(label='min{}'.format(5*' '),value=0)
    rf['max'] = col2.text_input(label='max{}'.format(5*' '),value=0)
    rf['most'] = col2.text_input(label='most{}'.format(5*' '),value=0)
    
    
    # col 3 (ti,tf,ec)
    col3.markdown("**T<sub>i</sub>** (<sup>o</sup>C)", unsafe_allow_html=True)
    ti = {}
    ti['min'] = col3.text_input(label='min{}'.format(6*' '),value=0)
    ti['max'] = col3.text_input(label='max{}'.format(6*' '),value=0)
    ti['most'] = col3.text_input(label='most{}'.format(6*' '),value=0)
    col3.markdown("**T<sub>f</sub>** (<sup>o</sup>C)", unsafe_allow_html=True)
    tf = {}
    tf['min'] = col3.text_input(label='min{}'.format(7*' '),value=0)
    tf['max'] = col3.text_input(label='max{}'.format(7*' '),value=0)
    tf['most'] = col3.text_input(label='most{}'.format(7*' '),value=0)
    col3.markdown("**ECF** (0 to 1)", unsafe_allow_html=True)
    ec = {}
    ec['min'] = col3.text_input(label='min{}'.format(10*' '),value=0)
    ec['max'] = col3.text_input(label='max{}'.format(10*' '),value=0)
    ec['most'] = col3.text_input(label='most{}'.format(10*' '),value=0)

    # col 4 (swi,swf,lt)
    col4.markdown("**S<sub>wi</sub>** (0 to 1)", unsafe_allow_html=True)
    swi = {}
    swi['min'] = col4.text_input(label='min{}'.format(8*' '),value=0)
    swi['max'] = col4.text_input(label='max{}'.format(8*' '),value=0)
    swi['most'] = col4.text_input(label='most{}'.format(8*' '),value=0)
    col4.markdown("**S<sub>wf</sub>** (0 to 1)", unsafe_allow_html=True)
    swf = {}
    swf['min'] = col4.text_input(label='min{}'.format(9*' '),value=0)
    swf['max'] = col4.text_input(label='max{}'.format(9*' '),value=0)
    swf['most'] = col4.text_input(label='most{}'.format(9*' '),value=0)
    col4.markdown("**Life Time** (year)", unsafe_allow_html=True)
    t = {}
    t['min'] = col4.text_input(label='min{}'.format(11*' '),value=0)
    t['max'] = col4.text_input(label='max{}'.format(11*' '),value=0)
    t['most'] = col4.text_input(label='most{}'.format(11*' '),value=0)
    
    submitted = col2.form_submit_button("Submit")
    df_done = False
    if submitted:
        with st.spinner('Wait for it...'):
            # try:
                res = Qel(a,h,phi,rho_r,cr,ti,tf,swi,swf,rf,ec,t)
                # st.write(res)
                df, fig1, fig2 = create_freq_table(res)
                col2.success('Succeeded!')
                df_done = True
            # except Exception as e:
            #     col2.error(str(e)) 
col1, col2, col3 = st.columns([1,2,1])     
if df_done:      
    col2.dataframe(df)
    st.plotly_chart(fig1)
    # st.plotly_chart(fig2)
