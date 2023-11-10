
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('life expectancy.csv')
"""
Load life expectancy data from a CSV file into a pandas DataFrame.
"""


def filter_data(data, countries, start_year, end_year):
    """
    Filter the input data based on specified countries and years.

    Parameters:
    - data (pd.DataFrame): The input data containing life expectancy information.
    - countries (list): List of country names to filter the data.
    - start_year (int): The starting year for filtering the data.
    - end_year (int): The ending year for filtering the data.

    Returns:
    - pd.DataFrame: Filtered data based on input criteria.
    """
    # Filter the data based on countries and years
    filtered_data = data[(data['Country'].isin(countries)) & (
        data['Year'] >= start_year) & (data['Year'] <= end_year)]
    return filtered_data


def plot_life_expectancy(data, countries, output_filename):
    """
    Create a line plot of life expectancy over time for specified countries.

    Parameters:
    - data (pd.DataFrame): The filtered data containing life expectancy information.
    - countries (list): List of country names to plot.
    - output_filename (str): The filename to save the generated plot.

    Returns:
    - None
    """
    # Create a line graph for each country
    plt.figure(figsize=(12, 6))  # Set the figure size
    for country in countries:
        country_data = data[data['Country'] == country]
        plt.plot(country_data['Year'],
                 country_data['Life Expectancy'], label=country)

    # Set plot labels and legend
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.title('Life Expectancy Over Time')
    plt.legend()

    # Show the plot
    plt.grid(True)

    # Save the plot to a PNG file
    plt.savefig(output_filename, dpi=300)

    plt.show()


def main():
    """
    Main function to execute the data filtering and plotting process.
    """
    countries = ['India', 'United Kingdom',
                 'United States', 'Brazil', 'Mexico', 'Australia']
    start_year = 1802
    end_year = 2016
    output_filename = 'line_plot.png'

    # Filter the data
    filtered_data = filter_data(data, countries, start_year, end_year)

    # Plot the life expectancy
    plot_life_expectancy(filtered_data, countries, output_filename)


if __name__ == '__main__':
    main()


""" Code for Bar Graph"""


data = pd.read_csv('life expectancy.csv')
"""
 Load life expectancy data from a CSV file into a pandas DataFrame.
"""


def filter_and_process_data(data, countries, start_year, end_year):
    """
    Filter and process life expectancy data.

    Parameters:
    - data (pd.DataFrame): DataFrame containing life expectancy data.
    - countries (list): List of countries to include in the analysis.
    - start_year (int): Start year for filtering the data.
    - end_year (int): End year for filtering the data.

    Returns:
    pd.DataFrame: Processed and grouped data with average life expectancy.
    """
    # Filter the data based on countries and years
    filtered_data = data[(data['Country'].isin(countries)) & (
        data['Year'] >= start_year) & (data['Year'] <= end_year)]

    # Group data by year and country to calculate the average life expectancy
    grouped_data = filtered_data.groupby(['Year', 'Country'])[
        'Life Expectancy'].mean().unstack()
    return grouped_data


def plot_data(grouped_data, title, output_filename):
    """
     Create a bar chart from grouped data and save it to a file.

    Parameters:
    - grouped_data (pd.DataFrame): Processed and grouped data.
    - title (str): Title for the plot.
    - output_filename (str): Filename to save the plot.
    """
    # Create a bar graph for each country
    ax = grouped_data.plot(kind='bar', figsize=(12, 4))

    # Set plot labels and legend
    plt.xlabel('Year')
    plt.ylabel('Average Life Expectancy')
    plt.title('Average Life Expectancy')
    plt.legend(title='Country', loc='upper right')

    # Save the plot to a PNG file
    plt.savefig(output_filename, dpi=300)

    # Show the plot
    plt.grid(axis='y')
    plt.show()


def main():
    """
    Main function to execute the life expectancy analysis and plotting.
    """
    countries = ['India', 'United Kingdom',
                 'United States', 'Brazil', 'Mexico', 'Australia']
    start_year = 2010
    end_year = 2016
    output_filename = 'bar_graph.png'
    plot_title = 'Average Life Expectancy 2010-2016'

    # Filter and process the data
    grouped_data = filter_and_process_data(
        data, countries, start_year, end_year)

    # Plot the data
    plot_data(grouped_data, plot_title, output_filename)


if __name__ == '__main__':
    main()


"""Code for Pie Chart"""

data = pd.read_csv('life expectancy.csv')
"""
Load life expectancy data from a CSV file into a pandas DataFrame.
"""


def filter_data(data, countries, start_year, end_year):
    """
    Filter data based on specified countries and time range.

    Parameters:
    - data: DataFrame, the input data
    - countries: list of str, countries to filter
    - start_year: int, start year of the time range
    - end_year: int, end year of the time range

    Returns:
    - DataFrame, filtered data
    """
    filtered_data = data[(data['Country'].isin(countries)) & (
        data['Year'] >= start_year) & (data['Year'] <= end_year)]
    return filtered_data


def aggregate_data(filtered_data):
    """
    Aggregate filtered data by calculating the mean life expectancy for each country.

    Parameters:
    - filtered_data: DataFrame, filtered life expectancy data

    Returns:
    - Series, aggregated data with mean life expectancy for each country
    """
    grouped_data = filtered_data.groupby('Country')['Life Expectancy'].mean()
    return grouped_data


def create_pie_chart(data, title, save_path):
    """
    Create a pie chart from aggregated data and save it to a specified path.

    Parameters:
    - data: Series, aggregated data for pie chart
    - title: str, title for the pie chart
    - save_path: str, path to save the pie chart image
    """
    plt.figure(figsize=(8, 8))
    plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=140)
    plt.title('Total Life Expectancy by Country 1802-2016')
    # Equal aspect ratio ensures that the pie chart is drawn as a circle.
    plt.axis('equal')
    plt.savefig(save_path, dpi=300)
    plt.show()


def main():
    """
    Main function to read data, filter, aggregate, and create a pie chart.

    Parameters:
    - filename: str, path to the CSV file containing life expectancy data
    """
    filename = 'life_expectancy.csv'
    countries = ['India', 'United Kingdom',
                 'United States', 'Brazil', 'Mexico', 'Australia']
    start_year = 1802
    end_year = 2016

    filtered_data = filter_data(data, countries, start_year, end_year)
    grouped_data = aggregate_data(filtered_data)
    title = 'Total Life Expectancy by Country 1802-2016'
    save_path = 'pie_chart.png'

    create_pie_chart(grouped_data, title, save_path)


if __name__ == '__main__':
    main()
