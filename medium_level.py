from pymongo import MongoClient

# Connect to MongoDB (replace 'mongodb://localhost:27017/' with your MongoDB URI)
client = MongoClient("mongodb://localhost:27017/")
db = client["quiz_game"]  # Replace with your database name
collection = db["medium_questions"]

# List of medium-level general knowledge questions
questions = [
    #question 1-10
    {"question": "What is the capital of Bhutan?", "answer": "Thimphu"},
    {"question": "In which year did the Berlin Wall fall?", "answer": "1989"},
    {"question": "What is the chemical formula for table salt?", "answer": "NaCl"},
    {"question": "Which planet is known for its rings?", "answer": "Saturn"},
    {"question": "What is the hardest natural substance on Earth?", "answer": "Diamond"},
    {"question": "Who invented the telephone?", "answer": "Alexander Graham Bell"},
    {"question": "Which organ in the human body produces insulin?", "answer": "Pancreas"},
    {"question": "What is the largest desert in the world?", "answer": "Antarctic Desert"},
    {"question": "In which country would you find the ancient city of Petra?", "answer": "Jordan"},
    {"question": "Who wrote 'The Great Gatsby'?", "answer": "F. Scott Fitzgerald"},
    
    #question 11-20
    {"question": "What is the primary language spoken in Egypt?", "answer": "Arabic"},
    {"question": "What is the currency of South Africa?", "answer": "Rand"},
    {"question": "Which famous scientist developed the theory of relativity?", "answer": "Albert Einstein"},
    {"question": "What is the smallest country in Asia?", "answer": "Maldives"},
    {"question": "In which year did World War I begin?", "answer": "1914"},
    {"question": "Which vitamin is produced when the skin is exposed to sunlight?", "answer": "Vitamin D"},
    {"question": "What is the longest river in Asia?", "answer": "Yangtze River"},
    {"question": "Who was the first person to walk on the moon?", "answer": "Neil Armstrong"},
    {"question": "What is the name of the largest ocean on Earth?", "answer": "Pacific Ocean"},
    {"question": "Which city is known as the Big Apple?", "answer": "New York City"},
    
    #queestion 21-30
    {"question": "Who discovered the law of gravity?", "answer": "Isaac Newton"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "Which country is home to the kangaroo?", "answer": "Australia"},
    {"question": "What is the most spoken language in the world?", "answer": "Mandarin Chinese"},
    {"question": "Which organ is responsible for pumping blood throughout the body?", "answer": "Heart"},
    {"question": "What is the capital of Canada?", "answer": "Ottawa"},
    {"question": "In which continent is the country of Kenya located?", "answer": "Africa"},
    {"question": "What is the name of the largest bone in the human body?", "answer": "Femur"},
    {"question": "Which famous landmark is located in Paris?", "answer": "Eiffel Tower"},
    {"question": "What is the main ingredient in guacamole?", "answer": "Avocado"},
    
    #question 31-40
    {"question": "What is the currency used in Japan?", "answer": "Yen"},
    {"question": "Who was the first woman to fly solo across the Atlantic Ocean?", "answer": "Amelia Earhart"},
    {"question": "What is the capital of Italy?", "answer": "Rome"},
    {"question": "Which gas do plants use for photosynthesis?", "answer": "Carbon dioxide"},
    {"question": "Who painted the Last Supper?", "answer": "Leonardo da Vinci"},
    {"question": "What is the most widely consumed beverage in the world?", "answer": "Water"},
    {"question": "Which instrument has keys, pedals, and strings?", "answer": "Piano"},
    {"question": "What is the tallest mountain in the world?", "answer": "Mount Everest"},
    {"question": "Who is the author of 'To Kill a Mockingbird'?", "answer": "Harper Lee"},
    {"question": "What is the name of the galaxy that contains our solar system?", "answer": "Milky Way"},
    
    #question 41-50
    {"question": "What is the boiling point of water at sea level in degrees Celsius?", "answer": "100"},
    {"question": "Who is known as the 'Father of Modern Physics'?", "answer": "Albert Einstein"},
    {"question": "Which country has the most natural lakes?", "answer": "Canada"},
    {"question": "What is the name of the longest river in the United States?", "answer": "Missouri River"},
    {"question": "What is the capital city of Brazil?", "answer": "Brasília"},
    {"question": "Who was the first African-American president of the United States?", "answer": "Barack Obama"},
    {"question": "What is the primary ingredient in chocolate?", "answer": "Cocoa"},
    {"question": "Which planet is known as the Earth's twin?", "answer": "Venus"},
    {"question": "What is the term for an animal that primarily eats plants?", "answer": "Herbivore"},
    {"question": "Which scientist is known for his theory of evolution?", "answer": "Charles Darwin"},
    
    #question 51-60
    {"question": "What is the capital of Russia?", "answer": "Moscow"},
    {"question": "Which element has the chemical symbol 'O'?", "answer": "Oxygen"},
    {"question": "What is the largest country in the world by area?", "answer": "Russia"},
    {"question": "What is the main function of the liver?", "answer": "Detoxification"},
    {"question": "Who was the first emperor of Rome?", "answer": "Augustus"},
    {"question": "What is the capital city of Egypt?", "answer": "Cairo"},
    {"question": "What is the most popular sport in the world?", "answer": "Soccer (Football)"},
    {"question": "What is the currency of the European Union?", "answer": "Euro"},
    {"question": "Which planet is known for its prominent ring system?", "answer": "Saturn"},
    {"question": "What is the hardest natural mineral?", "answer": "Diamond"},
    
    #question 61-70
    {"question": "What is the capital of Australia?", "answer": "Canberra"},
    {"question": "Which chemical element has the symbol 'Fe'?", "answer": "Iron"},
    {"question": "Who wrote 'The Catcher in the Rye'?", "answer": "J.D. Salinger"},
    {"question": "What is the primary ingredient in traditional Japanese sake?", "answer": "Rice"},
    {"question": "Which country is known as the Land of the Rising Sun?", "answer": "Japan"},
    {"question": "What is the name of the largest ocean on Earth?", "answer": "Pacific Ocean"},
    {"question": "Who is the Greek god of war?", "answer": "Ares"},
    {"question": "What is the capital of Spain?", "answer": "Madrid"},
    {"question": "What is the main language spoken in Brazil?", "answer": "Portuguese"},
    {"question": "Who painted the Sistine Chapel ceiling?", "answer": "Michelangelo"},
    
    #question 71-80
    {"question": "What is the capital of Norway?", "answer": "Oslo"},
    {"question": "In which year did the Titanic sink?", "answer": "1912"},
    {"question": "What is the primary ingredient in pesto?", "answer": "Basil"},
    {"question": "Which country is known for the Great Pyramid of Giza?", "answer": "Egypt"},
    {"question": "What is the capital of Thailand?", "answer": "Bangkok"},
    {"question": "What is the term for a baby kangaroo?", "answer": "Joey"},
    {"question": "What is the name of the famous clock tower in London?", "answer": "Big Ben"},
    {"question": "Which gas is most commonly used in balloons?", "answer": "Helium"},
    {"question": "What is the most populous city in the world?", "answer": "Tokyo"},
    {"question": "What is the largest island in the Mediterranean Sea?", "answer": "Sicily"},
    
    #question 81-90
    {"question": "What is the capital of Sweden?", "answer": "Stockholm"},
    {"question": "Who was the first woman to win a Nobel Prize?", "answer": "Marie Curie"},
    {"question": "What is the largest land mammal?", "answer": "African Elephant"},
    {"question": "In which year did the first manned moon landing occur?", "answer": "1969"},
    {"question": "Which city is known as the City of Light?", "answer": "Paris"},
    {"question": "What is the most abundant gas in the Earth's atmosphere?", "answer": "Nitrogen"},
    {"question": "Who wrote the play 'Romeo and Juliet'?", "answer": "William Shakespeare"},
    {"question": "What is the primary ingredient in hummus?", "answer": "Chickpeas"},
    {"question": "What is the currency of Switzerland?", "answer": "Swiss Franc"},
    {"question": "Which country is known for the Great Wall?", "answer": "China"},
    
    #question 91-100
    {"question": "What is the largest continent on Earth?", "answer": "Asia"},
    {"question": "What is the capital of New Zealand?", "answer": "Wellington"},
    {"question": "Which gas is essential for human respiration?", "answer": "Oxygen"},
    {"question": "Who painted 'Starry Night'?", "answer": "Vincent van Gogh"},
    {"question": "What is the name of the longest river in Africa?", "answer": "Nile River"},
    {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
    {"question": "Who wrote the 'Iliad' and the 'Odyssey'?", "answer": "Homer"},
    {"question": "What is the capital of Argentina?", "answer": "Buenos Aires"},
    {"question": "What is the name of the largest moon of Saturn?", "answer": "Titan"},
    {"question": "Which scientist is known for the laws of motion?", "answer": "Isaac Newton"},

]

# Insert the questions into the collection
result = collection.insert_many(questions)
print(f"Inserted question IDs: {result.inserted_ids}")
