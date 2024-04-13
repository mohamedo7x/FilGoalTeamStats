
# FilGoal Team Analyzer

**Description:**
The FilGoal Team Analyzer is a Python script designed to fetch and analyze match data for a specific football team from the FilGoal website. Using web scraping techniques, it retrieves information such as goals scored and conceded in recent matches, providing insights into the team's performance over time. This script offers flexibility to analyze either the last 10 matches or the matches from a specific page, enabling users to track their favorite team's progress throughout the season. Whether you're a football enthusiast or a data analyst, this tool can help you gain valuable insights into team performance and trends.

**Key Features:**
- Fetches match data from the FilGoal website.
- Analyzes goals scored and conceded in recent matches.
- Provides average goals scored and conceded metrics for insights into team performance.
- Offers options to analyze the last 10 matches or matches from a specific page.
- Utilizes web scraping techniques for data extraction.

**Usage:**
1. Instantiate the `Solution` class with the desired parameters (page number and team number).
2. Use the `load_data` method to fetch match data.
3. Utilize methods such as `get_goals_scored_from_list` and `get_goals_conserned_from_list` to analyze goals scored and conceded.
4. Gain insights into the team's performance based on the extracted data.

**Dependencies:**
- `requests`: For making HTTP requests to fetch webpage content.
- `BeautifulSoup`: For parsing HTML content.
- `numpy`: For numerical operations and array manipulation.

**Note:** Ensure compliance with the terms of use of the FilGoal website when utilizing this script for web scraping purposes.
