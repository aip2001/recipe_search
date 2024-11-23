# recipe_search
A Flask-based app to search recipes by ingredients using Elasticsearch. Users input ingredients, and matching recipes are retrieved and displayed. Built with Flask, Elasticsearch, Python, and HTML/CSS. Easy to set up and run locally for efficient recipe searches!
# Features
- Input ingredients to search for recipes containing those ingredients.
- Displays matching recipes with names, ingredients, and cooking instructions.
- Displays number of ingredients matching in search query and suggested recipes.
- Provide alternatives for ingredients required in suggested recipes and not present in the search query.
- Powered by Elasticsearch for fast and efficient full-text search.
# Technologies Used
- Flask: Python web framework for building the application.
- Elasticsearch: Used to index and search recipe data.
- HTML & CSS: Front-end for user interaction.
- Python: Back-end logic.
# How It Works
- Recipe data is stored in an Elasticsearch index.
- Users can enter ingredients in the search bar.
- The app queries Elasticsearch to find recipes matching the ingredients.
- Results are displayed dynamically on the web page.
# Future Work
- Enhanced Search Features - Implement advanced filters (e.g., dietary restrictions, cuisine type, preparation time).
- Add support for fuzzy search and typo tolerance.
- User Authentication and Personalization - Enable user accounts to save favorite recipes.
- Provide personalized recommendations based on user preferences and past searches.
- Improved Recipe Data
- Multilingual Support- Allow users to search recipes and view the interface in different languages.
- Machine Learning Integration - Implement ML algorithms for better ranking and relevance of search results.
- Use recommendation systems to suggest recipes based on user input.
# Setup Instructions
1. Clone the Repository
Open a terminal or command prompt.
Run the following command to clone the repository:
git clone https://github.com/aip2001/recipe_search.git
2. Navigate to the project directory:
cd recipe_search
3. Install Python
Make sure Python (version 3.8 or higher) is installed on your system.
Download Python if not installed.
Install Required Python Libraries
4. Install and Run Elasticsearch
Install Elasticsearch:
Download Elasticsearch from Elastic's website at https://www.elastic.co/downloads/elasticsearch
Follow the instructions to install Elasticsearch on your system.
Run Elasticsearch:
Open the unzipped ElasticSearch folder in command prompt and run bin\elasticsearch.bat to start ElassticSearch.
5. Run the Flask app to add sample data:
Uncomment the add_sample_data() function call in the script.
Run the app:
python app.py
Stop the app, then comment the add_sample_data() line again to prevent duplicate data.
Run the Flask Application
6. Start the Flask server:
python app.py
Access the application at http://127.0.0.1:5000 in your web browser.
7. Search Recipes
Enter ingredients (e.g., chicken, garlic) in the search bar and press Search.
View the matching recipes ranked by relevance.
# Screenshots
<img width="960" alt="image" src="https://github.com/user-attachments/assets/f633eb86-1ce5-4167-aded-a2b6caec23fa">
<img width="960" alt="image" src="https://github.com/user-attachments/assets/5c660ba2-9c3d-42bb-8d16-f10021c357a5">
<img width="960" alt="image" src="https://github.com/user-attachments/assets/c20629f7-180d-4dc5-96d7-bb3c60d54a10">



