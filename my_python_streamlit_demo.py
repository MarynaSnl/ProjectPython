import streamlit as st
import pandas as pd
#import numpy  as np
import altair as alt

def main():
    #page = st.sidebar.selectbox("Wybierz stronę:", ["Homepage", "Analiza informacji", "Diagramy"])
    try:
        if df.empty:
            df = load_data()
    except:
        df = load_data()
    
    
    title_page = '<p style="font-family:sans-serif; color:DarkBlue; font-weight: bold; font-size: 30px;">Wybierz stronę:</p>'
    st.sidebar.markdown(title_page, unsafe_allow_html=True)
    page = st.sidebar.radio('', ['Dane do eksploracj', 'Eksploracja danych', 'Analiza wizualna'])    
    max_age = 120
    min_age = 0
    if (df is None) | (df.empty):
        file_my = st.file_uploader("Pobiery plik -trane.csv-", accept_multiple_files=False)
        if file_my is not None:
            df = pd.read_csv(file_my)

    if page == "Dane do eksploracj":
        if not ((df is None) | (df.empty)) :
            Print_df_indicators(df)
        else:
            st.write("**Plik 'trane.csv' nie jest załadowany, musisz wgrać plik.**")  

    elif page == "Eksploracja danych":
        if not ((df is None) | (df.empty)) :
            #st.title("Analiza informacji")
            title_df = '<p style="font-family:sans-serif; color:DarkBlue; font-size: 42px;">Eksploracja danych:</p>'
            st.markdown(title_df, unsafe_allow_html=True)
            x_axis = st.selectbox("Choose a variable for the x-axis",  df.columns, index=5)
            y_axis = st.selectbox("Choose a variable for the y-axis",  df.columns, index=6)
            visualize_data(df, x_axis, y_axis)
        else:
            st.write("**Plik 'trane.csv' nie jest załadowany, musisz wgrać plik.**")  
            
            
    elif page == "Analiza wizualna":
        if (df is None) | (df.empty):
            st.write("**Plik 'trane.csv' nie jest załadowany, musisz wgrać plik.**")   
            return
        
        #str_print = '<p style="font-family:Courier; font-style:Italic;  font-weight: bold; color:DarkBlue; font-size: 26px;">Wykresy ocalałych i nieocalonych pasażerów wiedłund płci.</p>'   
        str_print = '<p style="font-family:sans-serif; font-weight: bold; color:DarkGray; font-size: 24px;">Wykresy ocalałych i nieocalonych pasażerów wiedłund płci.</p>'   
        st.markdown(str_print, unsafe_allow_html=True)    
        col1, col2 = st.columns(2)    
        with col1:
            st.header("  ")
            st.write(alt.Chart(df).mark_bar().encode( x='Survived:O',  y=alt.Y('count():Q',  title='łącznie osób'),color='Sex:O').properties(title='Pasażerowie.',    width=350,    height=250).transform_calculate(Survived='datum.Survived == 1 ? "Yes" : "No"'))  

        with col2:
            st.header("  ")
            st.write(alt.Chart(df).mark_bar().encode( x='Sex:O', y=alt.Y('count():Q',  title='łącznie osób'), color=alt.Color('Survived:O' )).properties(title='Pasażerowie.',     width=350,    height=250).transform_calculate(Survived='datum.Survived == 1 ? "Yes" : "No"'))

        
        st.write(alt.Chart(df).mark_bar().encode(y=alt.Y('Survived:N',title="  "),color="Survived:N",x= alt.X('count(Survived):Q',  title='łącznie osób')).transform_calculate(Survived='datum.Survived == 1 ? datum.Sex + " saved" : datum.Sex + " not saved"'))
    
        #str_print = '<p style="font-family:sans-serif; font-weight: bold; color:DarkGray; font-size: 24px;">Według wieku:</p>'   
        #st.markdown(str_print, unsafe_allow_html=True)    

        str_print = '<p style="font-family:sans-serif; font-weight: bold; color:DarkGray; font-size: 24px;">Wykresy z filtrowaniem według wieku.</p>'   
        st.markdown(str_print, unsafe_allow_html=True)    
        str_print = '<p style="font-family:sans-serif;  font-style:Italic; color:DarkGray; font-size: 20px;">Wiersze z pustym wiekiem zostały wykluczone z analizy.</p>'   
        st.markdown(str_print, unsafe_allow_html=True)    
        #str_print = '<p style="font-family:sans-serif; font-style:Italic; color:Green; font-size: 16px;">Wiersze z pustym wiekiem i płcią zostały wykluczone z analizy.</p>'
        #st.markdown(str_print, unsafe_allow_html=True)
        df = df.dropna(subset=['Age'])
  

        max_age = int(df['Age'].max() + 1)
        min_age = 0
        col1, col2 = st.columns(2)    
        with col1:
            str_print = '<p style="font-family:sans-serif; font-weight: bold; color:DarkDarkGray; font-size: 16px;">Wybierz min/max wiek:</p>'   
            st.markdown(str_print, unsafe_allow_html=True)    
            st_number_input = st.number_input('min wiek', 0, int(df['Age'].max() + 1))
        with col2:
            st.header("  ")
       

        if st_number_input:
            min_age = int(st_number_input)    #  number 
            st.write("**Wiek od:** " + '**'+str(min_age)+'**')
            
            st_slider_0_100 = st.slider('max wiek', int(min_age), int(df['Age'].max() + 1), int(max_age))  
            if st_slider_0_100:
                max_age = int(st_slider_0_100)    # return number 0 - 100  int
                st.write(' **Wybrany wiek od** ' + '**'+str(min_age)+'**' + " **do** " +  '**'+str(max_age)+ '**')
                visualize_data2(df, min_age, max_age)
        else:
            visualize_data2(df, 0, int(df['Age'].max() + 1))
        
        
@st.cache
def load_data():
    try:
        df = pd.read_csv("train.csv")
        return df
    except:
        return pd.DataFrame()

def visualize_data2(df, min_age, max_age):
    
    #st.write(alt.Chart(df[(df['Age'] >=min_age)&(df['Age'] <=max_age)]).mark_tick().encode(color='count(Survived)',     y='Sex',     x='Age', #).transform_calculate(Survived='datum.Survived == 1 ? "Yes" : "No"'))

    col1, col2 = st.columns(2)    
    with col1:
        st.write(alt.Chart(df[(df['Age'] >=min_age)&(df['Age'] <=max_age)]).mark_bar().encode( x='Sex:O', y=alt.Y('count():Q',  title='łącznie osób'), color=alt.Color('Survived:O' )).properties(title='Pasażerowie.',     width=350,    height=250).transform_calculate(Survived='datum.Survived == 1 ? "Yes" : "No"'))
    with col2:
        st.write(alt.Chart(df[(df['Age'] >=min_age)&(df['Age'] <=max_age)]).mark_bar().encode(y=alt.Y('Survived:N',title="  "),color="Survived:N",x= alt.X('count(Survived):Q',  title='łącznie osób')).properties(title='Pasażerowie.',     width=450,    height=220).transform_calculate(Survived='datum.Survived == 1 ? datum.Sex + " saved" : datum.Sex + " not saved"'))
 
    
    st.write(alt.Chart(df[(df['Sex']== 'female')&(df['Age'] >=min_age)&(df['Age'] <=max_age)]).mark_bar().encode(   alt.Y('count()', title='łącznie osób') ,   x='Age' , color=alt.Color('Survived:N' )  ).properties(title='Wykres ocalałych i nieocalonych pasażerów płci żeńskiej.',  width=800,    height=250).transform_calculate(Survived='datum.Survived == 1 ? "Yes" : "No"').interactive())
 
    st.write(alt.Chart(df[(df['Age'] >=min_age)&(df['Age'] <=max_age)]).mark_bar().encode(alt.Y('count()', title='łącznie osób'),   x='Age' , color=alt.Color('Survived:N' )).properties(title='Wykres ocalałych i nieocalonych pasażerów.', width=800,    height=250).transform_calculate(Survived='datum.Survived == 1 ? "Yes" : "No"').interactive())         
    
    st.write(alt.Chart(df[(df['Sex']== 'male')&(df['Age'] >=min_age)&(df['Age'] <=max_age)]).mark_bar().encode(alt.Y('count()', title='łącznie osób'),   x='Age' , color=alt.Color('Survived:N' )).properties(title='Wykres ocalałych i nieocalonych pasażerów płci męskiej.',
    width=800,    height=250).transform_calculate(Survived='datum.Survived == 1 ? "Yes" : "No"').interactive())   
   
        
    st.write(alt.Chart(df[["Sex", "Survived"]][(df['Age'] >=min_age)&(df['Age'] <=max_age)]).mark_arc().encode(theta=alt.Theta("count()", type="quantitative", ),color=alt.Color("Survived", type="nominal", legend=alt.Legend(title=None, orient='none'))
).transform_calculate(Survived='datum.Survived == 1 ? datum.Sex + " saved" : datum.Sex + " not saved"').interactive())

    st.write(alt.Chart(df.sort_values(['Age'])[["Age", "Survived"]][(df['Age'] >=min_age)&(df['Age'] <=max_age)]).mark_arc().encode(theta=alt.Theta("count()", type="quantitative", ),color=alt.Color("Survived", type="nominal", legend=alt.Legend(title=None, orient='none'))
).transform_calculate(Survived='datum.Survived == 1 ? datum.Age + " saved" : datum.Age + " not saved"').interactive())

def visualize_data(df, x_axis, y_axis):
    graph = alt.Chart(df).mark_circle(size=60).encode(
        x=x_axis,
        y=y_axis,
        color='Survived',
        tooltip=['Survived', 'Age', 'Sex']
    ).interactive()

    st.write(graph)
    
def print_st_markdown(title_print):  
    st.markdown(title_print, unsafe_allow_html=True)
    
def Print_df_indicators(df):
    str_print = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">Dane do eksploracji, lista pasażerów:</p>'
    st.markdown(str_print, unsafe_allow_html=True)
    st.write('', df, '  ')
            
    str_print = '<p style="font-family:sans-serif; color:Green; font-size: 28px;">♟ General Statistics ♟:</p>'
    st.markdown(str_print, unsafe_allow_html=True)
    #st.markdown("**♟ General Statistics ♟**")
    str_print = "* "+str(round( len(df["Age"][df['Age'].isnull()])/df['PassengerId'].count(),5) * 100) + "%  osób ma nie uzupełnione dane o wieku"
    st.write(str_print)
    str_print = "* "+str(round( len(df["Sex"][df['Sex'].isnull()])/df['PassengerId'].count(),5) * 100) + "%  osób ma nie uzupełnione dane o płci."
    st.write(str_print)
     
    str_print = "* "+str(df[(df['Sex']== 'male')&(df["Survived"]==1)].shape[0]) + " mężczyzn z " + str(df[(df['Sex']== 'male')].shape[0]) + " przeżyło katastrofę."
    st.write(str_print)
 
    str_print = "* "+str(df[(df['Sex']== 'female')&(df["Survived"]==1)].shape[0]) + "  kobiet z  " + str(df[(df['Sex']== 'female')].shape[0]) + " przeżyło katastrofe."
    st.write(str_print)
   
    str_print = '* '+str(round(df['Age'].mean(),3)) + " - średni wiek pasażerów"
    st.write(str_print)
    str_print = '* '+str(round(df['Age'].max(),3)) + " - maksymalny wiek pasażerów"
    st.write(str_print)
    str_print = '* '+str(round(df['Age'].min(),3)) + " - minimalny wiek pasażerów"
    st.write(str_print)
    man_proc = round(100*(df['PassengerId'][df['Sex']== 'male'].count()/df['PassengerId'].count()),3)
    str_print = "* Kobiet - " + str(100 -man_proc) + "%,   mężczyzn - "+ str(man_proc) + "%."
    st.write(str_print)


if __name__ == "__main__":
    #st.set_page_config(page_title='Omdena Envisionit', page_icon="🧊", layout='centered', initial_sidebar_state='auto')
    df = pd.DataFrame()
    main()

