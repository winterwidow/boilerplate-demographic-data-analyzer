import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # 1. How many of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1)

    # 4. Percentage with and without advanced education that earn >50K
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    higher_education_rich = round(
        (higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100, 1
    )
    lower_education_rich = round(
        (lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0]) * 100, 1
    )

    # 5. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # 6. What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours_people = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (min_hours_people[min_hours_people['salary'] == '>50K'].shape[0] / min_hours_people.shape[0]) * 100, 1
    )

    # 7. What country has the highest percentage of people that earn >50K?
    country_income_percentage = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack()['>50K'] * 100
    highest_earning_country = country_income_percentage.idxmax()
    highest_earning_country_percentage = round(country_income_percentage.max(), 1)

    # 8. Identify the most popular occupation for those who earn >50K in India.
    india_high_income = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_high_income['occupation'].mode()[0]

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
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
