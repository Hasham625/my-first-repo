import kagglehub
# Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Download latest version
path = kagglehub.dataset_download("shivamb/netflix-shows")

# Load the Netflix dataset
df = pd.read_csv('netflix_titles.csv')

# Basic EDA - Checking the first few rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Info about the dataset
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing Values in Dataset:")
print(df.isnull().sum())

# Drop rows where the 'title' column is missing
df.dropna(subset=['title'], inplace=True)

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# EDA: Value Counts for 'type' column (Movies vs TV Shows)
print("\nDistribution of Movies and TV Shows:")
print(df['type'].value_counts())

# Visualization 1: Distribution of Movies and TV Shows
plt.figure(figsize=(8, 6))
sns.countplot(x='type', data=df)
plt.title('Distribution of Movies and TV Shows')
plt.show()

# EDA: Value Counts for 'genres' column (Top 10 genres)
print("\nTop 10 genres:")
print(df['genres'].value_counts().head(10))

# Visualization 2: Distribution of Movies and TV Shows by Release Year
plt.figure(figsize=(10, 6))
df['release_year'].value_counts().sort_index().plot(kind='bar')
plt.title('Number of Movies/TV Shows by Release Year')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.show()

# Visualization 3: Boxplot for Ratings by Release Year
plt.figure(figsize=(10, 6))
sns.boxplot(x='release_year', y='rating', data=df)
plt.title('Distribution of Ratings by Release Year')
plt.xticks(rotation=90)
plt.show()

# Additional Visualization (if necessary)
# Example: Distribution of movies/TV shows by country
if 'country' in df.columns:
    plt.figure(figsize=(10, 6))
    df['country'].value_counts().head(10).plot(kind='bar')
    plt.title('Top 10 Countries of Movies/TV Shows')
    plt.xlabel('Country')
    plt.ylabel('Count')
    plt.show()

# Saving visualizations to files (optional)
plt.figure(figsize=(8, 6))
sns.countplot(x='type', data=df)
plt.title('Distribution of Movies and TV Shows')
plt.savefig('distribution_movies_tv_shows.png')

plt.figure(figsize=(10, 6))
df['release_year'].value_counts().sort_index().plot(kind='bar')
plt.title('Number of Movies/TV Shows by Release Year')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.savefig('movies_by_year.png')

# Preparing files for GitHub deployment
import os

# Initialize Git repository and commit changes
os.system('git init')
os.system('git add .')  # Add all changes
os.system('git commit -m "Initial commit with EDA and visualizations"')

# Create a .gitignore file to exclude unnecessary files
with open(".gitignore", "w") as gitignore:
    gitignore.write("__pycache__/\n*.pyc\n*.pyo\n*.csv\n")

# Add the .gitignore file and commit
os.system('git add .gitignore')
os.system('git commit -m "Add .gitignore file"')

# (Optional) You can push to GitHub repository
# Example: Set remote repository (you need to replace with your actual GitHub repo URL)
# os.system('git remote add origin <your_github_repo_url>')

# Push changes to GitHub
# os.system('git push -u origin master')

# To keep a screenshot of commands while deploying, 
# Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Netflix dataset
df = pd.read_csv('netflix_titles.csv')

# Basic EDA - Checking the first few rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Info about the dataset
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing Values in Dataset:")
print(df.isnull().sum())

# Drop rows where the 'title' column is missing
df.dropna(subset=['title'], inplace=True)

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# EDA: Value Counts for 'type' column (Movies vs TV Shows)
print("\nDistribution of Movies and TV Shows:")
print(df['type'].value_counts())

# Visualization 1: Distribution of Movies and TV Shows
plt.figure(figsize=(8, 6))
sns.countplot(x='type', data=df)
plt.title('Distribution of Movies and TV Shows')
plt.show()

# EDA: Value Counts for 'genres' column (Top 10 genres)
print("\nTop 10 genres:")
print(df['genres'].value_counts().head(10))

# Visualization 2: Distribution of Movies and TV Shows by Release Year
plt.figure(figsize=(10, 6))
df['release_year'].value_counts().sort_index().plot(kind='bar')
plt.title('Number of Movies/TV Shows by Release Year')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.show()

# Visualization 3: Boxplot for Ratings by Release Year
plt.figure(figsize=(10, 6))
sns.boxplot(x='release_year', y='rating', data=df)
plt.title('Distribution of Ratings by Release Year')
plt.xticks(rotation=90)
plt.show()

# Additional Visualization (if necessary)
# Example: Distribution of movies/TV shows by country
if 'country' in df.columns:
    plt.figure(figsize=(10, 6))
    df['country'].value_counts().head(10).plot(kind='bar')
    plt.title('Top 10 Countries of Movies/TV Shows')
    plt.xlabel('Country')
    plt.ylabel('Count')
    plt.show()

# Saving visualizations to files (optional)
plt.figure(figsize=(8, 6))
sns.countplot(x='type', data=df)
plt.title('Distribution of Movies and TV Shows')
plt.savefig('distribution_movies_tv_shows.png')

plt.figure(figsize=(10, 6))
df['release_year'].value_counts().sort_index().plot(kind='bar')
plt.title('Number of Movies/TV Shows by Release Year')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.savefig('movies_by_year.png')

# Preparing files for GitHub deployment
import os

# Initialize Git repository and commit changes
os.system('git init')
os.system('git add .')  # Add all changes
os.system('git commit -m "Initial commit with EDA and visualizations"')

# Create a .gitignore file to exclude unnecessary files
with open(".gitignore", "w") as gitignore:
    gitignore.write("__pycache__/\n*.pyc\n*.pyo\n*.csv\n")

# Add the .gitignore file and commit
os.system('git add .gitignore')
os.system('git commit -m "Add .gitignore file"')

# (Optional) You can push to GitHub repository
# Example: Set remote repository (you need to replace with your actual GitHub repo URL)
# os.system('git remote add origin <your_github_repo_url>')

# Push changes to GitHub
# os.system('git push -u origin master')

# To keep a screenshot of commands while deploying, 
# take a screenshot of your terminal after running the following commands in your terminal:
# git init
# git add .
# git commit -m "Initial commit with EDA and visualizations"
# git remote add origin <your_github_repo_url>
# git push -u origin master
# take a screenshot of your terminal after running the following commands in your terminal:
# git init
# git add .
# git commit -m "Initial commit with EDA and visualizations"
# git remote add origin <your_github_repo_url>
# git push -u origin master
<<<<<<< HEAD

=======
>>>>>>> 1de6f7c (Initial commit)
