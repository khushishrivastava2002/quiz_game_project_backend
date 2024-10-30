from pymongo import MongoClient

# Connect to MongoDB (replace 'mongodb://localhost:27017/' with your MongoDB URI)
client = MongoClient("mongodb://localhost:27017/")
db = client["quiz_game"]  # Replace with your database name
collection = db["very_difficult_question"]

# List of medium-level general knowledge questions
questions = [
    
    #question 1-10
    {"question": "What is the rarest blood type in humans?", "answer": "AB negative"},
    {"question": "Who wrote the philosophical work 'Critique of Pure Reason'?", "answer": "Immanuel Kant"},
    {"question": "What is the longest river in the world?", "answer": "Nile River"},
    {"question": "Which planet has the most moons?", "answer": "Jupiter"},
    {"question": "Who discovered the structure of DNA?", "answer": "James Watson and Francis Crick"},
    {"question": "What is the capital of Bhutan?", "answer": "Thimphu"},
    {"question": "Who is the only U.S. President to serve more than two terms?", "answer": "Franklin D. Roosevelt"},
    {"question": "What is the term for a word that is spelled the same backward as forward?", "answer": "Palindrome"},
    {"question": "Which element has the atomic number 1?", "answer": "Hydrogen"},
    {"question": "What is the hardest natural substance on Earth?", "answer": "Diamond"},
    
    #question 11-20
    {"question": "Who painted 'The Last Supper'?", "answer": "Leonardo da Vinci"},
    {"question": "What is the smallest country in the world?", "answer": "Vatican City"},
    {"question": "Who was the first person to win two Nobel Prizes?", "answer": "Marie Curie"},
    {"question": "What is the capital of the Maldives?", "answer": "Malé"},
    {"question": "What is the world's largest desert?", "answer": "Antarctic Desert"},
    {"question": "Who was the first female Prime Minister of the United Kingdom?", "answer": "Margaret Thatcher"},
    {"question": "What is the name of the longest bone in the human body?", "answer": "Femur"},
    {"question": "Which gas is most abundant in the Earth's atmosphere?", "answer": "Nitrogen"},
    {"question": "What is the main ingredient in a traditional moussaka?", "answer": "Eggplant"},
    {"question": "Who wrote 'War and Peace'?", "answer": "Leo Tolstoy"},
    
    #question 21-30
    {"question": "What is the capital of Iceland?", "answer": "Reykjavik"},
    {"question": "Who developed the theory of general relativity?", "answer": "Albert Einstein"},
    {"question": "Which organ is responsible for producing insulin?", "answer": "Pancreas"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "Which famous battle took place in 1066?", "answer": "Battle of Hastings"},
    {"question": "What is the official language of Brazil?", "answer": "Portuguese"},
    {"question": "Which animal is known for its ability to change color?", "answer": "Chameleon"},
    {"question": "What is the only continent without reptiles or snakes?", "answer": "Antarctica"},
    {"question": "What is the largest mammal in the world?", "answer": "Blue whale"},
    {"question": "Who invented the printing press?", "answer": "Johannes Gutenberg"},
    
    #question 31-40
    {"question": "What is the chemical symbol for lead?", "answer": "Pb"},
    {"question": "What is the main language spoken in Argentina?", "answer": "Spanish"},
    {"question": "Which organelle is known as the powerhouse of the cell?", "answer": "Mitochondria"},
    {"question": "What is the capital city of Australia?", "answer": "Canberra"},
    {"question": "What is the world's deepest lake?", "answer": "Lake Baikal"},
    {"question": "Who was the first astronaut to orbit the Earth?", "answer": "Yuri Gagarin"},
    {"question": "What is the name of the world's largest rainforest?", "answer": "Amazon Rainforest"},
    {"question": "Which physicist is known for the uncertainty principle?", "answer": "Werner Heisenberg"},
    {"question": "What is the capital of Uzbekistan?", "answer": "Tashkent"},
    {"question": "Who wrote 'The Odyssey'?", "answer": "Homer"},
    
    #question 41-50
    {"question": "What is the currency of Switzerland?", "answer": "Swiss Franc"},
    {"question": "Who is known as the 'Father of Geometry'?", "answer": "Euclid"},
    {"question": "What is the name of the first artificial satellite?", "answer": "Sputnik"},
    {"question": "What is the capital of Kenya?", "answer": "Nairobi"},
    {"question": "Which ancient civilization built the pyramids?", "answer": "Egyptians"},
    {"question": "What is the most spoken language in the world?", "answer": "Mandarin Chinese"},
    {"question": "What is the capital city of Azerbaijan?", "answer": "Baku"},
    {"question": "Who discovered penicillin?", "answer": "Alexander Fleming"},
    {"question": "What is the capital of South Korea?", "answer": "Seoul"},
    {"question": "Which country gifted the Statue of Liberty to the USA?", "answer": "France"},
    
    #question 51-60
    {"question": "What is the chemical formula for ozone?", "answer": "O3"},
    {"question": "Who was the first woman to fly solo across the Atlantic Ocean?", "answer": "Amelia Earhart"},
    {"question": "What is the name of the galaxy that contains our solar system?", "answer": "Milky Way"},
    {"question": "Which artist is famous for the painting 'The Starry Night'?", "answer": "Vincent van Gogh"},
    {"question": "What is the most expensive painting ever sold?", "answer": "Salvator Mundi"},
    {"question": "What is the largest species of shark?", "answer": "Whale shark"},
    {"question": "Who was the last Tsar of Russia?", "answer": "Nicholas II"},
    {"question": "What is the capital city of Mongolia?", "answer": "Ulaanbaatar"},
    {"question": "Who painted the ceiling of the Sistine Chapel?", "answer": "Michelangelo"},
    {"question": "What is the hardest rock?", "answer": "Diamond"},
   
    #question 61-70
    {"question": "Who was the first woman to win a Nobel Prize?", "answer": "Marie Curie"},
    {"question": "What is the main ingredient in traditional hummus?", "answer": "Chickpeas"},
    {"question": "What is the capital of Norway?", "answer": "Oslo"},
    {"question": "Which chemical element has the symbol 'K'?", "answer": "Potassium"},
    {"question": "Who wrote the novel '1984'?", "answer": "George Orwell"},
    {"question": "What is the name of the largest volcano in the solar system?", "answer": "Olympus Mons"},
    {"question": "What is the main language spoken in Tibet?", "answer": "Tibetan"},
    {"question": "Who developed the theory of evolution by natural selection?", "answer": "Charles Darwin"},
    {"question": "What is the capital of Finland?", "answer": "Helsinki"},
    {"question": "Which country is known as the Land of the Rising Sun?", "answer": "Japan"},
    
    #question 71-80 
    {"question": "What is the name of the world's largest coral reef system?", "answer": "Great Barrier Reef"},
    {"question": "Which famous scientist developed the laws of motion?", "answer": "Isaac Newton"},
    {"question": "What is the capital of Vietnam?", "answer": "Hanoi"},
    {"question": "Which city is known as the City of Love?", "answer": "Paris"},
    {"question": "What is the largest organ in the human body?", "answer": "Skin"},
    {"question": "Who invented the light bulb?", "answer": "Thomas Edison"},
    {"question": "What is the term for a word that has the opposite meaning?", "answer": "Antonym"},
    {"question": "Which element is used in batteries?", "answer": "Lithium"},
    {"question": "Who was the first African American President of the United States?", "answer": "Barack Obama"},
    {"question": "What is the largest land animal?", "answer": "African elephant"},
    
    #question 81-90
    {"question": "What is the capital of Egypt?", "answer": "Cairo"},
    {"question": "Which gas do plants absorb from the atmosphere?", "answer": "Carbon dioxide"},
    {"question": "What is the currency of India?", "answer": "Indian Rupee"},
    {"question": "Who discovered the law of gravity?", "answer": "Isaac Newton"},
    {"question": "What is the most abundant gas in the Earth's atmosphere?", "answer": "Nitrogen"},
    {"question": "Which organ is responsible for detoxifying chemicals in the body?", "answer": "Liver"},
    {"question": "What is the capital of Portugal?", "answer": "Lisbon"},
    {"question": "Which philosopher is known for the quote 'I think, therefore I am'?", "answer": "René Descartes"},
    {"question": "What is the main ingredient in traditional sushi?", "answer": "Rice"},
    {"question": "What is the capital of Saudi Arabia?", "answer": "Riyadh"},
    
    #question 91-100
    
    {"question": "Who is known as the 'Father of Modern Physics'?", "answer": "Albert Einstein"},
    {"question": "What is the capital of Greece?", "answer": "Athens"},
    {"question": "Who wrote the 'Divine Comedy'?", "answer": "Dante Alighieri"},
    {"question": "Which country is known for the Great Wall?", "answer": "China"},
    {"question": "What is the largest island in the world?", "answer": "Greenland"},
    {"question": "Who was the first person to climb Mount Everest?", "answer": "Sir Edmund Hillary and Tenzing Norgay"},
    {"question": "What is the main ingredient in guacamole?", "answer": "Avocado"},
    {"question": "What is the chemical symbol for gold?", "answer": "Au"},
    {"question": "What is the capital of Argentina?", "answer": "Buenos Aires"},
    {"question": "Who invented the telephone?", "answer": "Alexander Graham Bell"},
    

]

# Insert the questions into the collection
result = collection.insert_many(questions)
print(f"Inserted question IDs: {result.inserted_ids}")
