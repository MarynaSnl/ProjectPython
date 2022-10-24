import pandas as pd


def calculate_demographic_data(print_data=True):
    df = pd.read_csv("adult.data.csv")
    null_value = pd.isnull(df).sum()
    null_value = null_value[null_value>0]
    if len(null_value) > 0:
        ###  age, fnlwgt, hours-per-week    mean
        ###  education-num   -     min(education-num)
        ###  apital-gain -  0 ,  capital-loss   -  0, salary - 0
        df = df.fillna({'age': df['age'].mean() , 'fnlwgt': int(df["fnlwgt"].mean()), 'hours-per-week': int(df['hours-per-week'].mean()), 'education-num': min(df['education-num']) ,  'capital-gain': 0 , 'capital-loss': 0, 'salary': 0, 'relationship': '-' })
        df = df.fillna(method = 'ffill')
        df = df.fillna(method = 'bfill')
        #  race     sex  native-country    -  delite records !!    salary         
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()   

    # What is the average age of men?
    average_age_men = round(df["age"][df['sex'] == 'Male'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df[df['education'] == 'Bachelors'].groupby('education').size() / len(df))['Bachelors']*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
  

    # percentage with salary >50K
    m_d_bh = len(df[(df.education.isin(['Bachelors','Masters','Doctorate']))])
    higher_education_rich = round(len(df[(df['salary'] == '>50K') & ( df.education.isin(['Bachelors','Masters','Doctorate'])  )])/m_d_bh * 100,1)
    m_d_bh = len(df[(~(df.education.isin(['Bachelors','Masters','Doctorate'])))])
    lower_education_rich = round(len(df[(df['salary'] == '>50K') & (~(df.education.isin(['Bachelors','Masters','Doctorate']) ) )])/m_d_bh * 100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = None

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_work_hours = min(df["hours-per-week"][df['hours-per-week'] != 0])

    rich_percentage = len(df[ (df["hours-per-week"] == min(df["hours-per-week"][df['hours-per-week'] != 0]))  & (df['salary'] == '>50K') ])/len(df[ (df["hours-per-week"] == min(df["hours-per-week"][df['hours-per-week'] != 0]))   ]) * 100

    # What country has the highest percentage of people that earn >50K?
    tmp_df = (df[(df['salary'] == '>50K') ].groupby('native-country').size() / df.groupby('native-country').size()).sort_values() * 100
    highest_earning_country = tmp_df[~tmp_df.isnull()].sort_values(ascending=False).index.values[0]
    highest_earning_country_percentage = round(tmp_df[~tmp_df.isnull()].sort_values(ascending=False)[0],1)

    # Identify the most popular occupation for those who earn >50K in India.
    tmp_df = df[(df['salary'] == '>50K')& (  df['native-country'] == 'India' ) ].groupby('occupation').size().sort_values(ascending=False) 
    top_IN_occupation = tmp_df[~tmp_df.isnull()].sort_values(ascending=False).index.values[0] 

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
