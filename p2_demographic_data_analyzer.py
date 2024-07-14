import pandas as pd
import math

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()


    # What is the average age of men?
    sub_df = df[(df['sex'] == 'Male')]
    average_age_men = sub_df['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    num_bach = df[df['education']=='Bachelors'].shape[0]
    total = len(df)
    percentage_bachelors = round(((num_bach / total) * 100), 1)
    

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher = len(df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate']) & (df['salary']== '>50K')])
    high_len = len(df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])])
    higher_education = round((higher/high_len) * 100,1)
    
    lower = len(df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate']) & (df['salary']== '>50K')])
    low_len =  len(df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])])
    lower_education = round((lower/low_len) * 100,1)
    
    # percentage with salary >50K
    higher_education_rich = higher_education
    lower_education_rich = lower_education

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')])
    reg_min_workers = len(df[(df['hours-per-week'] == min_work_hours)])
    
    rich_percentage = round((num_min_workers / reg_min_workers) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    max_country = ""
    max_percent=0

    for country in df['native-country'].unique():

        richest = len(df[(df['native-country'] == country) & (df['salary'] == '>50K')])
        len_richest = len(df[(df['native-country'] == country)])
        percent = (richest / len_richest) * 100

        if percent > max_percent:
            max_percent=percent
            max_country = country
            

    highest_earning_country = max_country
    highest_earning_country_percentage = round(max_percent,1)


    # Identify the most popular occupation for those who earn >50K in India.
    rich_india = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    occu_india = rich_india['occupation']
    top_IN_occupation = top_IN_occupation = occu_india.mode().tolist()[0]




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


calculate_demographic_data()