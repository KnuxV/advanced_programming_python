# Final Project: Building an AI Agent with Tools

Your goal is to create an AI agent that can understand a user's question, use a set of custom tools to work with data, and produce intelligent answers. This project brings together everything you've learned in this course: Python organization, data structures, database interaction, command-line interfaces, and version control.

## Project Overview

**Teams**: Groups of 3 students

**Project Proposal Deadline**: November 10th
- One team member emails Kevin and me with:
  - All team members' names and email addresses
  - Your chosen domain and dataset
  - Brief outline of your agent's capabilities (3-5 bullet points)
  - List of planned tool functions (5-8 tools minimum)

**Final Presentation**: January 12th at 9:00 AM
- Live demo of your agent (10 minutes)
- Code walkthrough (5 minutes)
- Q&A session (5 minutes)

---

## What You're Building

You'll create an AI agent that connects a Large Language Model (LLM) to a custom toolkit you build in Python. The agent takes natural language questions, determines which tools to use, retrieves, and processes data, and returns comprehensive answers.

**Your main task is designing and implementing the tools the LLM can use.** Think of the LLM as the brain that decides what to do, and your tools as the hands that actually do the work.

---

## Agent Capabilities: What Questions Should It Answer?

Your agent should handle multi-step questions that require combining multiple tools. Here are examples across different domains:

### Quick Examples

**E-commerce Analytics:**
- "Show me last month's sales trends by category and compare them to the same period last year."

**Chess Database Analysis:**
- "What's the win rate for players rated above 2000 who open with the King's Indian Defense as Black?"

**Machine Learning Benchmarking:**
- "Benchmark RandomForest, XGBoost, and LightGBM for predicting house prices. Use cross-validation and compare training time and accuracy."

**Financial Report Generation:**
- "Generate a quarterly financial report with revenue by product line, top 10 customers, profit margins, and growth analysis."

**Research Data Analysis:**
- "Analyze the correlation between study hours and exam scores, controlling for prior GPA. Identify outliers."

---

## Understanding AI Agents

Before diving into the example, let's clarify what an **AI agent** is. Unlike a simple chatbot that just answers questions, an agent can:
- **Plan**: Break down complex questions into steps
- **Use tools**: Call functions you've written to get data, compute results, or perform actions
- **Reason**: Decide which tools to use and in what order
- **Iterate**: If one approach doesn't work, try another
- **Synthesize**: Combine results from multiple tools into a coherent answer

Think of it like this: You ask a question → The LLM (brain) decides what to do → It calls your tools (hands) → Tools return results → LLM interprets and responds.

## Detailed Example: Movie Recommendation Agent

Let's walk through a complete example to understand the level of sophistication expected.

### The Scenario

You build a personalized movie recommendation agent. The user has a database of movies they've watched with their ratings and comments. The agent helps them decide what to watch next based on what's currently showing in their city.

### Example Interaction

**User:** "What movies are showing in Strasbourg this weekend? Recommend one based on what I've enjoyed before."

**Agent's Workflow:**

1. **Query Cinema Listings** (API Tool)
   - Call AlloCiné or similar API
   - Filter for Strasbourg, this weekend
   - Extract: titles, directors, genres, actors, showtimes
   - Result: List of 12 currently showing movies

2. **Analyze User's Watch History** (Database Tool)
   - Query user's movie database: `SELECT * FROM watched_movies`
   - Calculate user preferences:
     - Favorite genres (user rated comedies 4.2/5 avg, dramas 3.8/5)
     - Preferred directors (loves Denis Villeneuve, rates 4.5/5 avg)
     - Actor preferences (enjoys movies with Timothée Chalamet)
     - Rating patterns (rarely rates below 3, average is 3.9)

3. **Gather Movie Details** (Multiple API Tools)
   - For each cinema movie, call TMDB/IMDB API
   - Get: full cast, director filmography, critic ratings, synopsis
   - Extract themes and keywords

4. **Compare and Score** (Analysis Tool)
   - Match cinema movies against user preferences:
     - Genre overlap: +2 points
     - Director match: +3 points
     - Actor from favorite movies: +1 point
     - Similar themes to high-rated movies: +1 point
   - Weight by critic ratings and user's rating tendencies

5. **Generate Recommendation** (Report Tool)
   - Rank movies by score
   - Create explanation: "I recommend 'Dune: Part Two' because:
     - Denis Villeneuve directed it (you rated Arrival and Blade Runner 2049 both 5/5)
     - Features Timothée Chalamet (you enjoyed Call Me By Your Name)
     - Sci-fi genre matches 70% of your top-rated films
     - Shows at UGC Ciné Cité at 20:30 and 22:15"

6. **Update Database** (Database Write Tool)
   - After user watches it, tool adds entry: `INSERT INTO watched_movies (title, date, rating, comments) VALUES (...)`
   - User can say: "Add Dune 2, rated 5 stars, comment: 'Visually stunning, best sci-fi in years'"

### The Tools You'd Build

For this movie recommendation agent, here's a example of tools you could create

**1. Database Tools**
These tools interact with your local database of watched movies. You might use SQLite for this, with a simple schema like `watched_movies(id, title, director, genre, rating, date_watched, user_comment)`.

- `get_user_watch_history()` - Query all watched movies, return as DataFrame
- `get_favorite_genres()` - Analyze which genres the user rates highest
- `get_favorite_directors()` - Calculate average ratings per director
- `add_watched_movie(title, rating, comment)` - Insert new viewing record
- `update_movie_rating(title, new_rating)` - Modify existing entry if user changes their mind

**2. API Integration Tools**
These tools make HTTP requests to external services to fetch real-time data. You'll need API keys (store them in `.env`!).

- `get_cinema_listings(city, date)` - Call AlloCiné or similar API to fetch current showings in the specified city
- `get_movie_details(title)` - Query TMDB/IMDB for comprehensive movie information (cast, crew, plot, ratings)
- `get_director_filmography(director_name)` - Retrieve all movies by a director with their ratings
- `get_critic_reviews(movie_title)` - Fetch professional reviews from Rotten Tomatoes or Metacritic APIs

**3. Analysis Tools**
These tools process data and perform calculations. This is where Polars shines for fast data manipulation.

- `calculate_genre_preferences(watch_history)` - Group by genre, calculate average ratings, return ranked preferences
- `match_movie_to_preferences(movie, user_prefs)` - Scoring algorithm that compares a movie's attributes to user preferences
- `find_similar_movies(movie_title, database)` - Content-based filtering using genre, director, actors to find matches

**4. Report Tools**
These tools format and present results to the user. The output format depends on your project's design.

- `generate_recommendation_text(movie, reasons)` - Create natural language explanation of why a movie was recommended
- `create_comparison_table(movies, scores)` - Format multiple movie options with scores in a readable table

**Why This Structure Works:**
The LLM can chain these tools together. When you ask "What should I watch?", it:
1. Calls `get_cinema_listings()` to see options
2. Calls `get_user_watch_history()` to understand preferences
3. For top cinema options, calls `get_movie_details()` to get full info
4. Calls `match_movie_to_preferences()` to score each option
5. Calls `generate_recommendation_text()` to explain the top choice

Each tool is independent, testable, and reusable in different combinations.

---

## Your Toolbox: What to Build

The core of your project is creating Python functions that serve as tools for the LLM. Your tools should be:
- **Modular**: Each tool does one thing well
- **Composable**: Tools can be combined in different ways


### Essential Tool Categories

#### 1. Database Tools
You need a database to store your data (**mandatory**). The format is your choice:
- **SQL** (SQLite, PostgreSQL, MySQL)
- **NoSQL** (MongoDB, JSON files)
- **File-based** (Parquet, CSV, Pickle, text)

**The format must be justified by your project needs.** For example:
- Relational data with complex queries → SQL
- Nested/flexible structures → NoSQL/JSON
- Large analytical datasets → Parquet
- Simple, small data → CSV

Your database can be:
- **Static**: Pre-populated data that's only read
- **Dynamic**: Updated by your tools as the agent runs

You'll need tools to:
- Query/read from the database
- Optionally: Insert, update, or delete records


#### 2. External API Tools
Fetch data from external sources to enrich your agent's knowledge. Most APIs require registration for a free API key.

**Common use cases:**
- Movie databases (TMDB, IMDB) - Get film information, cast, reviews
- Weather APIs (OpenWeatherMap) - Current conditions, forecasts
- Financial data (Alpha Vantage, Yahoo Finance) - Stock prices, company data
- Geographic data (OpenStreetMap, Google Maps) - Locations, distances, routes
- News APIs (NewsAPI) - Current articles, headlines by topic
- Social media APIs (Twitter, Reddit) - Posts, trends, sentiment
- Domain-specific APIs for your project (sports stats, recipe databases, etc.)

#### 3. Data Processing Tools
Analyze and transform data to extract insights. These tools often work with DataFrames returned by your database or API tools.

**What these tools do:**
- **Statistical calculations** - Mean, median, standard deviation, correlations
- **Aggregations and grouping** - Use Polars to group by categories, time periods, etc.
- **Filtering and ranking** - Top N results, threshold filtering, sorting
- **Machine learning predictions** - Train simple models, make predictions
- **Text analysis** - Sentiment analysis, keyword extraction, summarization
- **Time series analysis** - Trends, seasonality, forecasting

**Example:** A tool that takes sales data and calculates month-over-month growth rates, then identifies which products are trending up or down.

#### 4. Visualization Tools
Create test, tables, charts, and plots to make data easier to understand. 

**Consider your output medium:**
- **Text, tables**: simple python print()
- **Image files**: Generate PNG/JPG plots with matplotlib or plotly, save to disk
- **Interactive**: Create HTML plots with plotly that allow zoom/pan
- **Embedded in reports**: Generate images that get inserted into PDFs or documents

#### 5. Report Generation Tools
Compile results into structured, shareable outputs. Think about how your user wants to consume the final answer.

**Output format options:**
- **Markdown reports** - Easy to read in terminal, convertible to other formats
- **HTML pages** - Rich formatting, can embed images and tables, viewable in browser
- **PDF documents** - Professional reports for sharing/printing (use libraries like reportlab or convert from HTML)
- **JSON/CSV exports** - Structured data for further processing or import into other tools
- **Word documents** - Editable reports using python-docx
- **Email reports** - Send results via email with attachments
---

### Project Structure

Structure your code logically.

```
my_agent_project/
├── src/
│   └── agent_tools/              # Your package
│       ├── __init__.py
│       ├── database.py           # Database tools
│       ├── api_clients.py        # API integration
│       ├── analysis.py           # Data processing
│       ├── visualization.py      # Plotting tools
│       └── reports.py            # Report generation
├── scripts/
│   ├── run_agent.py              # Main CLI script
│   └── setup_database.py         # Initialize database
├── data/
│   ├── raw/                      # Original datasets
│   └── processed/                # Cleaned data
├── config/
│   └── config.yaml               # Configuration files
├── .env                          # API keys (DON'T commit!)
├── .gitignore                    # Ignore patterns
├── requirements.txt              # Dependencies
└── README.md                     # Documentation
```
