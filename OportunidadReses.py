import pandas as pd
import streamlit as st
from logicas import calcular_beneficio_integracion
from GuardarResultados import guardar


st.title('Simulación Oportunidad Reses 🐄') # Diseño

st.write('                    ')
st.write('                    ')

st.subheader('Escenario Valorizado 1')

col0,col1,col2,col3,col4 = st.columns(5)

Precio_KG_Res_Gorda_n12= col0.number_input('Precio por Kg Res Gorda',min_value=1000, max_value=20000, value=7683 ,step=100)
Precio_KG_Res_Flaca_n= col0.number_input('Precio por Kg Res Flaca Integrada',min_value=1000, max_value=20000, value=7486 ,step=100)

Peso_Inicial_Res_n= col1.number_input('Peso inicial kg res Flaca',min_value=150, max_value=400, value=250 ,step=20)
Por_Beneficio_Integrado= col1.slider("% Costo Integración", 0., 1., 0.6)

Peso_Final_Res_n12= col2.number_input('Peso final kg res Flaca',min_value=150, max_value=600, value=400 ,step=20)
Gasto_Operativo_Anual= col2.number_input('Gasto Operativo Anual',min_value=0, max_value=1000000000000, value=1200000000 ,step=100000)

Cantidad_Reses= col3.number_input('Cantidad de reses integradas',min_value=0, max_value=80000, value=47000 ,step=1000)
Gasto_Transporte= col3.number_input('Gasto de Transporte',min_value=0, max_value=500000, value=120000 ,step=1000)

Tasa_Costo_Capital= col4.slider("Costo de Capital", 0., 0.3, 0.125)
Cantidad_Reses_Simular= col4.number_input('Cantidad de reses a simular',min_value=0, max_value=500000, value=1 ,step=1)

st.write('                    ')

# st.subheader('Resultados')

resultado = calcular_beneficio_integracion(Precio_KG_Res_Gorda_n12, Precio_KG_Res_Flaca_n,Peso_Inicial_Res_n,Por_Beneficio_Integrado,Peso_Final_Res_n12,Gasto_Operativo_Anual,Cantidad_Reses,Gasto_Transporte,Tasa_Costo_Capital,Cantidad_Reses_Simular,"metricas")
EVA=resultado[6]

columns = st.columns(4)

def mostrar_metricas(calculos, valores,columns):
    j=0
    for i, col in enumerate(columns):
        col.metric(label=calculos[j], value=valores[j])
        col.metric(label=calculos[j+1], value=valores[j+1])
        j +=2
        
calculos = ["Beneficio", "Valor Res Flaca (Inversión)", "UODI", "Valor Res Gorda", 
          "ROIC", "Utilidad Neta", "EVA", f"Costo de Capital: {'{:,.0f}%'.format(Tasa_Costo_Capital*100)}"]
valores = ["{:.0%}".format(resultado[0]), "${:,.0f}".format(resultado[1]), "${:,.0f}".format(resultado[2]), 
          "${:,.0f}".format(resultado[3]), "{:.0%}".format(resultado[4]), "${:,.0f}".format(resultado[5]), 
          "${:,.0f}".format(resultado[6]), "${:,.0f}".format(resultado[7])]
mostrar_metricas(calculos, valores,columns)

csv = guardar(Precio_KG_Res_Gorda_n12, Precio_KG_Res_Flaca_n,Peso_Inicial_Res_n,Por_Beneficio_Integrado,Peso_Final_Res_n12,Gasto_Operativo_Anual,Cantidad_Reses,Gasto_Transporte,Tasa_Costo_Capital,Cantidad_Reses_Simular,"guardar")

st.download_button(
"Presiona para descargar",
csv,
"file.csv",
"text/csv",
key='download-csv')
    
#  --------------------------------------
st.write('                    ')
st.write('                    ')
st.write('                    ')
st.write('                    ')


with st.expander('Escenario Valorizado 2'):
    st.subheader('Escenario Valorizado 2')
    col0,col1,col2,col3,col4 = st.columns(5)

    Precio_KG_Res_Gorda_n12_e2= col0.number_input('Precio por Kg Res Gorda e2',min_value=1000, max_value=20000, value=7683 ,step=100)
    Precio_KG_Res_Flaca_n_e2= col0.number_input('Precio por Kg Res Flaca Integrada e2',min_value=1000, max_value=20000, value=7486 ,step=100)

    Peso_Inicial_Res_n_e2= col1.number_input('Peso inicial kg res Flaca e2',min_value=150, max_value=400, value=250 ,step=20)
    Por_Beneficio_Integrado_e2= col1.slider("% Costo Integración e2", 0., 1., 0.6)

    Peso_Final_Res_n12_e2= col2.number_input('Peso final kg res Flaca e2',min_value=150, max_value=600, value=400 ,step=20)
    Gasto_Operativo_Anual_e2= col2.number_input('Gasto Operativo Anual e2',min_value=0, max_value=1000000000000, value=1200000000 ,step=100000)

    Cantidad_Reses_e2= col3.number_input('Cantidad de reses integradas e2',min_value=0, max_value=80000, value=47000 ,step=1000)
    Gasto_Transporte_e2= col3.number_input('Gasto de Transporte e2',min_value=0, max_value=500000, value=120000 ,step=1000)

    Tasa_Costo_Capital_e2= col4.metric("Costo de Capital","{:,.0f}%".format(round(Tasa_Costo_Capital*100)))
    Cantidad_Reses_Simular_e2= col4.number_input('Cantidad de reses a simular e2',min_value=0, max_value=500000, value=1 ,step=1)

    st.write('                    ')


    # st.subheader('Resultados')

    resultado2 = calcular_beneficio_integracion(Precio_KG_Res_Gorda_n12_e2, Precio_KG_Res_Flaca_n_e2,Peso_Inicial_Res_n_e2,Por_Beneficio_Integrado_e2,Peso_Final_Res_n12_e2,Gasto_Operativo_Anual_e2,Cantidad_Reses_e2,Gasto_Transporte_e2,Tasa_Costo_Capital,Cantidad_Reses_Simular_e2,"metricas")
    EVA_e2=resultado2[6]

    columns = st.columns(4)

    calculos2 = ["Beneficio e2", "Valor Res Flaca (Inversión) e2", "UODI e2", "Valor Res Gorda e2", 
              "ROIC e2", "Utilidad Neta e2", "EVA e2", f"Costo de Capital: {'{:,.0f}%'.format(Tasa_Costo_Capital*100)} e2"]
    valores2 = ["{:.0%}".format(resultado2[0]), "${:,.0f}".format(resultado2[1]), "${:,.0f}".format(resultado2[2]), 
              "${:,.0f}".format(resultado2[3]), "{:.0%}".format(resultado2[4]), "${:,.0f}".format(resultado2[5]), 
              "${:,.0f}".format(resultado2[6]), "${:,.0f}".format(resultado2[7])]

    mostrar_metricas(calculos2, valores2, columns)
    
    csv = guardar(Precio_KG_Res_Gorda_n12_e2, Precio_KG_Res_Flaca_n_e2,Peso_Inicial_Res_n_e2,Por_Beneficio_Integrado_e2,Peso_Final_Res_n12_e2,Gasto_Operativo_Anual_e2,Cantidad_Reses_e2,Gasto_Transporte_e2,Tasa_Costo_Capital,Cantidad_Reses_Simular_e2,"guardar")

    st.download_button(
    "Presiona para descargar",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv2')


    st.write('                    ')
    st.write('                    ')

    st.subheader('Escenario 1 v.s Escenario 2')

    Eva1Eva2 = (EVA-EVA_e2)

    col0,col1,col2= st.columns(3)
    col1.metric(label="Escenario 1 v.s Escenario 2", value="${:,.0f}".format(Eva1Eva2))
