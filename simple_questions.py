from pymongo import MongoClient

# Connect to MongoDB (replace 'mongodb://localhost:27017/' with your MongoDB URI)
client = MongoClient("mongodb://localhost:27017/")
db = client["quiz_game"]  # Replace with your database name
collection = db["simple_questions"]

# List of questions
questions = [
    # question 1- 10
    {"question": "Who is the President of the United States in 2024?", "answer": "Joe Biden"},
    {"question": "Which country hosted the 2024 Summer Olympics?", "answer": "France"},
    {"question": "What is the name of the world's largest ocean?", "answer": "Pacific Ocean"},
    {"question": "What new space telescope did NASA launch recently?", "answer": "James Webb Space Telescope"},
    {"question": "What is the capital city of Canada?", "answer": "Ottawa"},
    {"question": "Which animal is known for the highest land speed?", "answer": "Cheetah"},
    {"question": "What is the main function of red blood cells?", "answer": "Carrying oxygen"},
    {"question": "What is the name of the most widely spoken language in the world?", "answer": "Mandarin Chinese"},
    {"question": "Who wrote the novel 'Pride and Prejudice'?", "answer": "Jane Austen"},
    {"question": "What is the national currency of Japan?", "answer": "Yen"},
    
    #question 10-20 
    {"question": "What is the smallest planet in our solar system?", "answer": "Mercury"},
    {"question": "Who was the first woman to fly solo across the Atlantic?", "answer": "Amelia Earhart"},
    {"question": "Which element has the chemical symbol 'O'?", "answer": "Oxygen"},
    {"question": "What is the capital of Italy?", "answer": "Rome"},
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "What is the largest mammal on Earth?", "answer": "Blue Whale"},
    {"question": "Which planet is known as the 'Red Planet'?", "answer": "Mars"},
    {"question": "What is the boiling point of water in Celsius?", "answer": "100 degrees Celsius"},
    {"question": "Who discovered penicillin?", "answer": "Alexander Fleming"},
    {"question": "What is the main ingredient in traditional Japanese miso soup?", "answer": "Soybean paste"},
    
    #question 21-30 
    {"question": "What is the capital city of Australia?", "answer": "Canberra"},
    {"question": "In which year did the Titanic sink?", "answer": "1912"},
    {"question": "Who is known as the 'Father of Computers'?", "answer": "Charles Babbage"},
    {"question": "Which planet is closest to the sun?", "answer": "Mercury"},
    {"question": "What is the largest desert in the world?", "answer": "Sahara Desert"},
    {"question": "What is the hardest natural substance on Earth?", "answer": "Diamond"},
    {"question": "Which country is known as the Land of the Rising Sun?", "answer": "Japan"},
    {"question": "What is the longest river in the world?", "answer": "Nile River"},
    {"question": "Which country gifted the Statue of Liberty to the USA?", "answer": "France"},
    {"question": "In which continent is the Amazon Rainforest located?", "answer": "South America"},
    
    #question 31-40 
    
    {"question": "Who developed the theory of relativity?", "answer": "Albert Einstein"},
    {"question": "Which element is said to keep bones strong?", "answer": "Calcium"},
    {"question": "Which city is known as the 'Big Apple'?", "answer": "New York City"},
    {"question": "What is the national sport of Canada?", "answer": "Lacrosse"},
    {"question": "What planet is known for its rings?", "answer": "Saturn"},
    {"question": "What is the longest bone in the human body?", "answer": "Femur"},
    {"question": "Who was the first person to reach the summit of Mount Everest?", "answer": "Sir Edmund Hillary and Tenzing Norgay"},
    {"question": "What is the primary ingredient in guacamole?", "answer": "Avocado"},
    {"question": "Which planet is known as the 'Blue Planet'?", "answer": "Earth"},
    {"question": "Who invented the telephone?", "answer": "Alexander Graham Bell"},
    
    #question 41-50
    {"question": "Which country has the largest population?", "answer": "China"},
    {"question": "What is the name of the closest star to Earth?", "answer": "The Sun"},
    {"question": "What is the freezing point of water in Fahrenheit?", "answer": "32 degrees Fahrenheit"},
    {"question": "Who wrote the play 'Romeo and Juliet'?", "answer": "William Shakespeare"},
    {"question": "Which planet is the hottest in our solar system?", "answer": "Venus"},
    {"question": "What is the chemical symbol for gold?", "answer": "Au"},
    {"question": "Who was the first person to walk on the moon?", "answer": "Neil Armstrong"},
    {"question": "What is the largest organ in the human body?", "answer": "Skin"},
    {"question": "In which year did World War II end?", "answer": "1945"},
    {"question": "What is the tallest mountain in the world?", "answer": "Mount Everest"},
    
    #question 51-60
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "Which gas do plants absorb from the atmosphere?", "answer": "Carbon dioxide"},
    {"question": "What is the hardest rock?", "answer": "Diamond"},
    {"question": "What is the main language spoken in Brazil?", "answer": "Portuguese"},
    {"question": "Who painted the ceiling of the Sistine Chapel?", "answer": "Michelangelo"},
    {"question": "What is the currency of the United Kingdom?", "answer": "Pound Sterling"},
    {"question": "What is the largest continent on Earth?", "answer": "Asia"},
    {"question": "Who is known as the 'King of Pop'?", "answer": "Michael Jackson"},
    {"question": "What is the main ingredient in bread?", "answer": "Flour"},
    {"question": "Which ocean is the largest?", "answer": "Pacific Ocean"},
    
    #question 61-70
    {"question": "What is the capital city of Italy?", "answer": "Rome"},
    {"question": "Which planet is known for having a Great Red Spot?", "answer": "Jupiter"},
    {"question": "What is the chemical symbol for water?", "answer": "H2O"},
    {"question": "Who wrote 'The Odyssey'?", "answer": "Homer"},
    {"question": "What is the largest island in the world?", "answer": "Greenland"},
    {"question": "Who was the first female Prime Minister of the United Kingdom?", "answer": "Margaret Thatcher"},
    {"question": "Which vitamin is produced when a person is exposed to sunlight?", "answer": "Vitamin D"},
    {"question": "What is the name of the longest river in South America?", "answer": "Amazon River"},
    {"question": "Who is known as the 'Father of Medicine'?", "answer": "Hippocrates"},
    {"question": "Which country is famous for the Great Wall?", "answer": "China"},
    
    #question 71-80
    
    {"question": "What is the smallest country in the world?", "answer": "Vatican City"},
    {"question": "Which animal is known as the 'Ship of the Desert'?", "answer": "Camel"},
    {"question": "What is the main ingredient in sushi?", "answer": "Rice"},
    {"question": "Who discovered penicillin?", "answer": "Alexander Fleming"},
    {"question": "What is the capital city of Egypt?", "answer": "Cairo"},
    {"question": "Which metal is liquid at room temperature?", "answer": "Mercury"},
    {"question": "What is the name of the first artificial Earth satellite?", "answer": "Sputnik"},
    {"question": "What is the currency used in the European Union?", "answer": "Euro"},
    {"question": "Which planet is known as the 'Red Planet'?", "answer": "Mars"},
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
    
    #question 81-90
    
    {"question": "What is the tallest waterfall in the world?", "answer": "Angel Falls"},
    {"question": "What is the primary language spoken in Argentina?", "answer": "Spanish"},
    {"question": "Who is the author of the Harry Potter series?", "answer": "J.K. Rowling"},
    {"question": "Which gas is most abundant in the Earth's atmosphere?", "answer": "Nitrogen"},
    {"question": "What is the largest organ in the human body?", "answer": "Skin"},
    {"question": "Who painted 'The Starry Night'?", "answer": "Vincent van Gogh"},
    {"question": "What is the fastest land animal?", "answer": "Cheetah"},
    {"question": "Which planet has the most moons?", "answer": "Jupiter"},
    {"question": "What is the capital of Australia?", "answer": "Canberra"},
    {"question": "What is the currency of India?", "answer": "Indian Rupee (INR)"},
    
    #question 91-100 
    
    {"question": "What is the main ingredient of hummus?", "answer": "Chickpeas"},
    {"question": "Which ocean is the smallest?", "answer": "Arctic Ocean"},
    {"question": "Who wrote the novel '1984'?", "answer": "George Orwell"},
    {"question": "What is the chemical symbol for silver?", "answer": "Ag"},
    {"question": "In which continent is the Sahara Desert located?", "answer": "Africa"},
    {"question": "Who is known as the 'Father of Geometry'?", "answer": "Euclid"},
    {"question": "What is the longest river in the world?", "answer": "Nile River"},
    {"question": "Which element has the atomic number 1?", "answer": "Hydrogen"},
    {"question": "What year did the Titanic sink?", "answer": "1912"},
    {"question": "Which country is known as the Land of the Rising Sun?", "answer": "Japan"},

]

# Insert questions into the collection
result = collection.insert_many(questions)
print(f"Inserted question IDs: {result.inserted_ids}")
