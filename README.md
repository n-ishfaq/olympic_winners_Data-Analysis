Olympic Medals Data Visualization Dashboard
This project provides a dashboard to visualize Olympic medal counts using various plots and animations. It allows users to explore historical data on athletes, countries, and medals won (Gold, Silver, and Bronze) with pie charts, animated bar charts, and interactive Dash-based visualizations.

Features
Pie Chart: Visualizes the distribution of Gold medals among athletes.
Animated Bar Graph: Displays the cumulative count of Gold medals for top athletes over time, saved as a GIF animation.
Dash Dashboard: An interactive dashboard where users can select a country from a dropdown and view its medal count (Gold, Silver, Bronze) over time in a stacked bar chart.
Requirements
The following Python packages are required to run this project:

numpy
pandas
seaborn
matplotlib
dash
dash-core-components
dash-html-components
dash-dependencies
plotly
Pillow
To install the dependencies, run:

bash
Copy code
pip install numpy pandas seaborn matplotlib dash plotly Pillow
How to Run
1. Prepare the Data
Make sure you have an Excel file containing the Olympic medal data. The columns should include:

Age: Athlete's age.
Silver: Number of Silver medals.
Bronze: Number of Bronze medals.
Athlete: Name of the athlete.
Date: Date of the event.
Gold: Number of Gold medals.
Sport: Sport type.
Country: Athlete's country.
Modify the filepath in the code to point to your Excel file:

python
filepath = r"your/filepath/to/data.xlsx"
2. Running the Project
After setting up the data, you can run the project in the following steps:

Step 1: Prepare Data and Create Visualizations
Run the script to prepare the data, generate a pie chart, and create the animated bar graph:


python main.py
This will display the pie chart and save the animated bar graph as a GIF to the path specified in output_path. Make sure to update the path if needed:

output_path="C:\\Users\\yourpath\\Desktop\\athletes.gif"
Step 2: Launch the Dash App
After visualizing the data, the Dash dashboard will be launched. The dashboard provides an interactive interface to explore the medal counts for different countries over time.

By default, the Dash app will run on http://127.0.0.1:8050/. You can open this link in your browser to view the dashboard.


python main.py
Project Structure
main.py: The main script that handles data preparation, visualization (pie charts and animated bar graphs), and the Dash app for interactive exploration of medal data.
README.md: This file containing instructions for setting up and running the project.
Visualizations
Pie Chart: Displays the percentage distribution of Gold medals won by athletes.
Animated Bar Graph: A horizontal bar graph showing the top 20 athletes' cumulative Gold medals over time, saved as a GIF.
Dash Dashboard: An interactive plot where users can choose a country from the dropdown and view a bar graph with the medal count per year.
Customization
You can modify the code to:

Change the number of top athletes in the animated bar chart.
Add more visualizations to the Dash dashboard, such as individual athlete performance or comparison between countries.
Extend the functionality by adding more sports or event-related analysis.
Troubleshooting
Excel File Issues: Ensure the Excel file is correctly formatted and contains all required columns.
Dash App Issues: If the app doesn't run, check if all dependencies are installed and whether the port 8050 is free.
License
This project is open-source and available under the MIT License.
