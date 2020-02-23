import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june','all']
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input("What city would you like to analyze, Chicago, New York City, or Washington?\n").lower()
        if city.lower() in CITY_DATA.keys():
            print("Let's analyze",city.title())
            break
        else:
            print("That's not a valid city. Please try again.")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input("What month would you like to analyze? January, February, March, April, June, or all?\n").lower()
        if month in months:
            print("Let's analyze",month.title(), 'for', city.title())
            break
        else:
            print("That's not a valid month. Please try again.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("What day of week would you like to analyze? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all?\n").lower()
        if day in days:
            print("Let's analyze",day.title(), 'for' ,month.title(), 'for', city.title())
            break
        else:
            print("That's not a valid day. Please try again.")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most Common Month: ', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most Common Day: ', most_common_day)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('Most Common Hour: ', most_common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print('Most Common Start Station: ', most_common_start)

    # TO DO: display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print('Most Common End Station: ', most_common_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['Combination'] = df['Start Station'] + ' to ' + df['End Station']
    most_common_combo = df['Combination'].mode()[0]
    print('Most Frequent Combination: ', most_common_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time: ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types: \n', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print('Gender Count: \n', gender_count)
    else:
        print('Gender information not available.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        print('Earliest Birth Year: ', earliest_birth_year)
        recent_birth_year = df['Birth Year'].max()
        print('Most Recent Birth Year: ', recent_birth_year)
        common_birth_year = df['Birth Year'].mode()[0]
        print('Most Common Birth Year: ', common_birth_year)
    else:
        print('Birth year information not available.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    i=0
    j=5
    answer = input("Would you like to see the first five lines of raw data?\n").lower()
    while True:
        if answer == 'yes':
            print(df.iloc[i:j])
        elif answer == 'no':
            break
        else:
            answer = input("Invalid answer. Answer yes or no.\n")
            continue
        answer = input("Would you like to see five more lines of raw data?\n").lower()
        i += 5
        j += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
