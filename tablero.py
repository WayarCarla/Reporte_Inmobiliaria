

#pip install openpyxl para trabajar con archivos excel
import pandas as pd #pip install pandas
import plotly.express as px #pip install plotly-express
import streamlit as st #pip install streamlit

#Streamlit run tablero.py

st.set_page_config(page_title = 'PROPIEDADES', #Nombre de la pagina, sale arriba cuando se carga streamlit
                   page_icon = 'moneybag:', # https://www.webfx.com/tools/emoji-cheat-sheet/
                   layout="wide")

st.image("https://elementos.entornos.net/clientes/ISPC/ispc.png", width=300)
st.title(':clipboard: REPORTE PROPIEDADES - INMOBILIARIA 2023') #Titulo del tablero
st.subheader('Compañía WAC')
st.markdown('##') #Para separar el titulo de los KPIs, se inserta un paragrafo usando un campo de markdown
                   
archivo_excel = 'Datos.xlsx' #Nombre archivo a importar  xlsx' hace referencia a excel
hoja_excel = 'Sheet1' #la hoja de excel que voy a importar

df = pd.read_excel( 
        archivo_excel,#importo el archivo excel
        sheet_name=hoja_excel,#le digo cual hoja necesito
        usecols = 'B:I', #aqui traigo las columnas que quiero usar
        header =0) #desde que fila debe empezar a tomarme la informacion *Empieza a contar desde 0*
 

#st.dataframe(df)
st.sidebar.header("Opciones:") #sidebar lo que nos va a hacer es crear en la parte izquierda un cuadro para agregar los filtros que queremos tener
Tipo = st.sidebar.multiselect(
    " TIPO DE PROPIEDAD:",
    options = df['Tipo'].unique(),
    default = df['Tipo'].unique() #Aqui podría por default dejar un filtro especifico pero vamos a dejarlos todos puestos por default
)

Estado = st.sidebar.multiselect(
    "ESTADO DE DISPONIBILIDAD",
    options = df['Estado'].unique(),
    default = df['Estado'].unique() #Aqui podría por default dejar un filtro especifico pero vamos a dejarlos todos puestos por default
)

Operacion_comercial = st.sidebar.multiselect(
    "OPERACION COMERCIAL:",
    options = df['Operacion_comercial'].unique(),
    default = df['Operacion_comercial'].unique() #Aqui podría por default dejar un filtro especifico pero vamos a dejarlos todos puestos por default
)
Localidad= st.sidebar.multiselect(
    "LOCALIDAD:",
    options = df['Localidad'].unique(),
    default = df['Localidad'].unique() #Aqui podría por default dejar un filtro especifico pero vamos a dejarlos todos puestos por default
)
df_seleccion = df.query("Tipo==@Tipo  & Estado==@Estado & Operacion_comercial==@Operacion_comercial & Localidad==@Localidad" ) #el primer city es la columna y el segundo es el selector




total_propiedades = int(df_seleccion['Propiedad'].count())

left_column, right_column = st.columns(2)


with left_column:
    st.subheader('TOTAL DE PROPIEDADES:')
    st.subheader(f"{total_propiedades}")

st.markdown("---") 

st.dataframe(df_seleccion)      

#hago un tipo de TABLA DINAMICA para agrupar los datos de una mejor manera, lo que hago aqui es por cada tipo de propiedad , me cuneta la cantidad que hay
df_propiedad_tipo= df.groupby(['Tipo'], as_index = False)['Propiedad'].count() 

#hago un tipo de TABLA DINAMICA para agrupar los datos de una mejor manera, lo que hago aqui es que por cada tipo de propiedad,
#  me cuente la cantidad de propiedades***
df_propiedad_estado= df.groupby(['Estado'], as_index = False)['Propiedad'].count() 

#hago un tipo de TABLA DINAMICA para agrupar los datos de una mejor manera, lo que hago aqui es que por cada tipo de propiedad,
#  me cuente la cantidad de propiedades***
df_propiedad_operacion= df.groupby(['Operacion_comercial'], as_index = False)['Propiedad'].count() 

#Crear un grafico de torta (pie chart)

pie_chart_tipo = px.pie(
    df_propiedad_tipo,
    title = "<b>Tipo de propiedades </b>", #El titulo
    values="Propiedad",
    names = 'Tipo') ## para verlo por EPS --> Colores



st.plotly_chart(pie_chart_tipo) # de esta forma se va a mostrar el dataframe en Streamlit

pie_chart_estado = px.pie(
    df_propiedad_estado,
    title = "<b>Estado de las propiedades </b>", #El titulo
    values="Propiedad",
    names = 'Estado') ## para verlo por EPS --> Colores



st.plotly_chart(pie_chart_estado) # de esta forma se va a mostrar el dataframe en Streamlit

pie_chart_operacion = px.pie(
    df_propiedad_operacion,
    title = "<b>Operacion comercial de propiedades </b>", #El titulo
    values="Propiedad",
    names = 'Operacion_comercial') ## para verlo por EPS --> Colores



st.plotly_chart(pie_chart_operacion) # de esta forma se va a mostrar el dataframe en Streamlit



## QUIERO PONER LAS DOS GRAFICAS A CADA LADO, UNA AL LADO DE LA OTRA

#left_column, right_column = st.columns(2)

#left_column.plotly_chart(fig_propiedades, use_container_width = True) #esta va al lado izquierdo
#right_column.plotly_chart(fig_tipo_propiedad, use_container_width = True)


# Hide Streamlit Style

hide_st_style = """
            <style>
   
            footer {visibility: hidden;}
           
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html= True)