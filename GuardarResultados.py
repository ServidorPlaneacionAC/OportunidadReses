from logicas import calcular_beneficio_integracion
import pandas as pd

def guardar(Precio_KG_Res_Gorda_n12, Precio_KG_Res_Flaca_n,Peso_Inicial_Res_n,Por_Beneficio_Integrado,Peso_Final_Res_n12,Gasto_Operativo_Anual,Cantidad_Reses,Gasto_Transporte,Tasa_Costo_Capital,Cantidad_Reses_Simular,caso):

    diccionario_de_calculos = calcular_beneficio_integracion(Precio_KG_Res_Gorda_n12, Precio_KG_Res_Flaca_n,Peso_Inicial_Res_n,Por_Beneficio_Integrado,Peso_Final_Res_n12,Gasto_Operativo_Anual,Cantidad_Reses,Gasto_Transporte,Tasa_Costo_Capital,Cantidad_Reses_Simular,"guardar")
    
    return pd.DataFrame([[key, diccionario_de_calculos[key]] for key in diccionario_de_calculos.keys()], columns=['Variable', 'Cantidad']).to_csv(index=False).encode('utf-8')
