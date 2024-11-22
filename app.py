from flask import Flask, render_template, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)

es = Elasticsearch("http://localhost:9200")

INDEX_NAME = "recipes"


ingredient_alternatives = {
    "butter": ["ghee", "mustard oil", "coconut oil"],
    "cream": ["malai (milk cream)", "cashew paste", "coconut cream"],
    "tomato": ["tamarind paste", "kokum", "amchur (dried mango powder)"],
    "garlic": ["hing (asafoetida)", "ginger-garlic paste"],
    "ginger": ["ginger-garlic paste", "dry ginger powder (soonth)", "amchur (dried mango powder)"],
    "onion": ["fried onions", "shallots", "spring onions"],
    "paneer": ["tofu"],
    "cilantro": ["kasoori methi"],
    "garam masala": ["whole spices"],
    "chicken": ["mutton", "paneer"],
    "yogurt": ["hung curd", "buttermilk (chaas)", "coconut yogurt"],
    "potato": ["sweet potato", "yam (suran)", "raw banana"],
    "cauliflower": ["broccoli", "cabbage", "lotus stem"],
    "cumin": ["caraway seeds (shahi jeera)", "fennel seeds (saunf)", "coriander seeds"],
    "turmeric": ["saffron (for color)", "ginger powder (for slight flavor)"],
    "lentils": ["split chickpeas (chana dal)", "moong dal", "masoor dal"],
    "rice": ["millet (bajra)", "quinoa", "flattened rice (poha)"],
    "cardamom": ["cinnamon", "nutmeg", "fennel seeds (for subtle sweetness)"]
}


def add_sample_data():
    sample_data = [
    {
        "recipe_name": "Butter Chicken",
        "ingredients": "chicken, butter, cream, tomato, garlic, ginger, garam masala,cilantro",
        "instructions": "Marinate the chicken with ginger-garlic paste and garam masala for at least 2 hours. Grill the chicken until partially cooked with a light char. In a pan, melt butter, add garlic, and sauté for a minute. Add pureed tomatoes and cook until the oil separates. Add garam masala. Stir in the grilled chicken and cook for a few minutes. Add cream, stir gently, and let simmer for 10-15 minutes. Garnish with cilantro and serve with naan or basmati rice."
    },
    {
        "recipe_name": "Chicken Tikka Masala",
        "ingredients": "chicken, yogurt, onion, tomato, garlic, ginger, garam masala,yogurt",
        "instructions": "Marinate the chicken with yogurt, ginger-garlic paste, and garam masala. Grill or broil the marinated chicken until lightly charred. In a pan, heat oil, add finely chopped onions, and sauté until golden. Add garlic-ginger paste and cook for 1-2 minutes. Add pureed tomatoes and cook until the oil separates. Stir in garam masala. Add the grilled chicken and mix well. Pour in heavy cream and let it simmer for 10-15 minutes. Garnish with cilantro and serve with steamed rice or naan."
    },
    {
        "recipe_name": "Palak Paneer",
        "ingredients": "spinach, paneer, garlic, onion, cumin, turmeric, garam masala,cilantro",
        "instructions": "Blanch spinach in boiling water for 2 minutes, then transfer to ice water to retain its green color. Puree the spinach. In a pan, heat oil, add cumin seeds, and let them crackle. Add finely chopped onions and sauté until golden. Add garlic and cook for a minute. Pour in the spinach puree and cook for 5-7 minutes. Add turmeric and garam masala, stir well. Add cubed paneer and simmer for 5 minutes. Garnish with cilantro and serve with roti or naan."
    },
    {
        "recipe_name": "Aloo Gobi",
        "ingredients": "potato, cauliflower, garlic, cumin, turmeric, coriander, garam masala,cilantro",
        "instructions": "Cut potatoes and cauliflower into bite-sized pieces. Heat oil in a pan, add cumin seeds, and let them crackle. Add minced garlic and cook for a minute. Add turmeric, coriander powder. Stir well. Add potatoes and sauté for 5 minutes, then add cauliflower and stir to coat with spices. Cover and cook on low heat for 15-20 minutes, stirring occasionally until the vegetables are tender. Sprinkle garam masala and garnish with fresh cilantro. Serve hot with chapati or rice."
    },
    {
        "recipe_name": "Dal Tadka",
        "ingredients": "yellow lentils, onion, garlic, cumin, mustard seeds, turmeric, garam masala,butter",
        "instructions": "Rinse and pressure cook yellow lentils with water, turmeric, and salt until soft. In a pan, heat butter and add mustard seeds and cumin seeds. Once they crackle, add finely chopped onions and sauté until golden. Add garlic and sauté for another minute. Pour in the cooked lentils and stir well. Let the dal simmer for 5 minutes. Garnish with cilantro and serve with steamed rice or roti."
    },
    {
        "recipe_name": "Chole Bhature",
        "ingredients": "chickpeas, flour, onion, garlic, tomato, ginger, garam masala",
        "instructions": "Soak chickpeas overnight and pressure cook them with salt until soft. In a pan, heat oil, add chopped onions, and sauté until golden. Add garlic-ginger paste and cook for 2 minutes. Add pureed tomatoes and cook until the oil separates from the mixture. Add garam masala. Stir in the cooked chickpeas and simmer for 15 minutes. Prepare bhature by mixing flour, and water, letting the dough rest for 1 hour. Roll out and deep fry until golden. Serve the chole with bhature."
    },
    {
        "recipe_name": "Paneer Butter Masala",
        "ingredients": "paneer, butter, cream, tomato, garlic, ginger, garam masala,onion",
        "instructions": "In a pan, melt butter and sauté finely chopped onions until golden. Add garlic-ginger paste and cook for a minute. Add tomato puree and cook until the oil separates. Stir in garam masala. Add cubed paneer and pour in heavy cream. Simmer for 5-7 minutes. Garnish with cilantro and serve with naan or rice."
    },
    {
        "recipe_name": "Biryani",
        "ingredients": "rice, chicken, onion, garlic, ginger, garam masala, saffron,yogurt",
        "instructions": "Marinate the chicken with yogurt, ginger-garlic paste, garam masala for at least 2 hours. Parboil basmati rice with whole spices. In a separate pan, sauté onions until golden, then add the marinated chicken and cook until partially done. In a large pot, layer half of the cooked rice, followed by the chicken mixture, and top with the remaining rice. Sprinkle saffron-infused milk over the top, cover tightly, and cook on low heat for 30 minutes. Serve hot with raita or salad."
    }
]

    for i, recipe in enumerate(sample_data):
        es.index(index=INDEX_NAME, id=i, body=recipe)

#add_sample_data()

@app.route("/", methods=["GET", "POST"])
def home():
    recipes = []
    query_ingredients = []

    if request.method == "POST":
        query_ingredients = request.form.get("ingredients", "").split(',')
        query_ingredients = [ing.strip().lower() for ing in query_ingredients]

        query = {
            "query": {
                "bool": {
                    "should": [
                        {"match": {"ingredients": ing}} for ing in query_ingredients
                    ]
                }
            }
        }

        res = es.search(index=INDEX_NAME, body=query)
        for hit in res['hits']['hits']:
            recipe = hit['_source']
            recipe_ingredients = [ing.strip().lower() for ing in recipe['ingredients'].split(',')]

            # Count the number of matching ingredients
            matched_ingredients = set(recipe_ingredients) & set(query_ingredients)
            count_matches = len(matched_ingredients)

            # Find alternative ingredients for missing ones
            alternative_ingredients = {}
            missing_ingredients = set(recipe_ingredients) - set(query_ingredients)
            for ing in missing_ingredients:
                if ing in ingredient_alternatives:
                    alternative_ingredients[ing] = ingredient_alternatives[ing]

            recipes.append({
                "recipe": recipe,
                "matched_count": count_matches,
                "matched_ingredients": list(matched_ingredients),
                "alternative_ingredients": alternative_ingredients
            })

    return render_template("index.html", recipes=recipes, query_ingredients=query_ingredients)

if __name__ == "__main__":
    app.run(debug=True)
#es.indices.delete(index="recipes", ignore=[400, 404])

