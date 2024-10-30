from pymongo import MongoClient

# Connect to MongoDB (replace 'mongodb://localhost:27017/' with your MongoDB URI)
client = MongoClient("mongodb://localhost:27017/")
db = client["quiz_game"]  # Replace with your database name
collection = db["difficult_questions"]

# List of medium-level general knowledge questions
questions = [
    #question 1-10
    {"question": "What is the capital city of Bhutan?", "answer": "Thimphu"},
    {"question": "Who developed the theory of general relativity?", "answer": "Albert Einstein"},
    {"question": "Which element has the highest melting point?", "answer": "Tungsten"},
    {"question": "Who was the first woman to fly solo across the Atlantic Ocean?", "answer": "Amelia Earhart"},
    {"question": "What is the largest desert in the world?", "answer": "Antarctic Desert"},
    {"question": "Who wrote the philosophical work 'Critique of Pure Reason'?", "answer": "Immanuel Kant"},
    {"question": "Which country is known as the Land of the Rising Sun?", "answer": "Japan"},
    {"question": "What is the longest bone in the human body?", "answer": "Femur"},
    {"question": "Who was the first President of the United States to resign from office?", "answer": "Richard Nixon"},
    {"question": "What is the main ingredient of traditional Japanese miso soup?", "answer": "Miso paste"},
    {"question": "In which year did the Berlin Wall fall?", "answer": "1989"},
    
    #question 11 - 20
    {"question": "What is the capital of Iceland?", "answer": "Reykjavik"},
    {"question": "Who was the first scientist to suggest the heliocentric model of the universe?", "answer": "Nicolaus Copernicus"},
    {"question": "Which organ in the human body is primarily responsible for detoxification?", "answer": "Liver"},
    {"question": "What is the official currency of South Africa?", "answer": "Rand"},
    {"question": "What is the term for a word that is similar in meaning to another word?", "answer": "Synonym"},
    {"question": "Which ocean is the largest by surface area?", "answer": "Pacific Ocean"},
    {"question": "What is the rarest blood type?", "answer": "AB negative"},
    {"question": "Who painted the 'Mona Lisa'?", "answer": "Leonardo da Vinci"},
    {"question": "What is the name of the first artificial Earth satellite?", "answer": "Sputnik 1"},
    {"question": "Which ancient civilization built the Machu Picchu?", "answer": "Inca"},
    
    #question 21-30
    {"question": "What is the second largest planet in our solar system?", "answer": "Saturn"},
    {"question": "Who discovered penicillin?", "answer": "Alexander Fleming"},
    {"question": "Which gas makes up most of the Earth's atmosphere?", "answer": "Nitrogen"},
    {"question": "Who wrote the famous play 'Waiting for Godot'?", "answer": "Samuel Beckett"},
    {"question": "What is the capital of Kazakhstan?", "answer": "Astana"},
    {"question": "Who was the first female Prime Minister of the United Kingdom?", "answer": "Margaret Thatcher"},
    {"question": "Which country was the first to grant women the right to vote?", "answer": "New Zealand"},
    {"question": "What is the hardest natural substance on Earth?", "answer": "Diamond"},
    {"question": "Who is known as the 'Father of Modern Physics'?", "answer": "Albert Einstein"},
    {"question": "What is the currency of South Korea?", "answer": "Won"},
    
    #question 31-40
    {"question": "Who wrote the epic poem 'The Divine Comedy'?", "answer": "Dante Alighieri"},
    {"question": "What is the capital of Libya?", "answer": "Tripoli"},
    {"question": "Which element is represented by the symbol 'Fe' on the periodic table?", "answer": "Iron"},
    {"question": "What is the largest mammal in the world?", "answer": "Blue Whale"},
    {"question": "What is the study of fungi called?", "answer": "Mycology"},
    {"question": "Which country is home to the kangaroo?", "answer": "Australia"},
    {"question": "What is the main language spoken in Brazil?", "answer": "Portuguese"},
    {"question": "Who was the first person to climb Mount Everest?", "answer": "Sir Edmund Hillary and Tenzing Norgay"},
    {"question": "Which planet is known for its rings?", "answer": "Saturn"},
    {"question": "What is the smallest country in the world?", "answer": "Vatican City"},
    
    #question 41-50
    {"question": "Who was the first African-American President of the United States?", "answer": "Barack Obama"},
    {"question": "What is the capital of Portugal?", "answer": "Lisbon"},
    {"question": "Which vitamin is primarily obtained from sunlight?", "answer": "Vitamin D"},
    {"question": "What is the term for animals that only eat plants?", "answer": "Herbivores"},
    {"question": "Who is the author of '1984' and 'Animal Farm'?", "answer": "George Orwell"},
    {"question": "What is the main ingredient in guacamole?", "answer": "Avocado"},
    {"question": "Which planet is known for having a Great Red Spot?", "answer": "Jupiter"},
    {"question": "What is the capital of Egypt?", "answer": "Cairo"},
    {"question": "Who developed the first successful polio vaccine?", "answer": "Jonas Salk"},
    {"question": "What is the longest river in the world?", "answer": "Nile River"},
    
    #question 51-60
    {"question": "What is the capital of Greece?", "answer": "Athens"},
    {"question": "Who is known as the 'Father of Medicine'?", "answer": "Hippocrates"},
    {"question": "What is the most widely spoken language in the world?", "answer": "Mandarin Chinese"},
    {"question": "Who wrote 'The Catcher in the Rye'?", "answer": "J.D. Salinger"},
    {"question": "What is the primary function of the white blood cells?", "answer": "Fight infections"},
    {"question": "What is the capital city of Nepal?", "answer": "Kathmandu"},
    {"question": "Which artist is known for the sculpture 'David'?", "answer": "Michelangelo"},
    {"question": "What is the name of the first successful cloning of a mammal?", "answer": "Dolly the sheep"},
    {"question": "Which treaty ended World War I?", "answer": "Treaty of Versailles"},
    {"question": "What is the scientific study of behavior and mental processes?", "answer": "Psychology"},
    
    #question 61-70
    {"question": "Which country is known for the Pyramids of Giza?", "answer": "Egypt"},
    {"question": "What is the name of the largest ocean on Earth?", "answer": "Pacific Ocean"},
    {"question": "What is the process of converting a solid directly into a gas called?", "answer": "Sublimation"},
    {"question": "Which continent is the Sahara Desert located on?", "answer": "Africa"},
    {"question": "What is the capital of Finland?", "answer": "Helsinki"},
    {"question": "What is the name of the largest coral reef system in the world?", "answer": "Great Barrier Reef"},
    {"question": "Who is known for the theory of evolution by natural selection?", "answer": "Charles Darwin"},
    {"question": "What is the chemical symbol for gold?", "answer": "Au"},
    {"question": "Which planet has the most moons?", "answer": "Saturn"},
    {"question": "What is the capital city of Mongolia?", "answer": "Ulaanbaatar"},
    
    #question 71-80
    {"question": "Which famous scientist developed the laws of motion?", "answer": "Isaac Newton"},
    {"question": "What is the primary purpose of the International Monetary Fund (IMF)?", "answer": "To promote global economic stability"},
    {"question": "Who is the author of the play 'Hamlet'?", "answer": "William Shakespeare"},
    {"question": "Which river runs through the Grand Canyon?", "answer": "Colorado River"},
    {"question": "What is the capital of Turkey?", "answer": "Ankara"},
    {"question": "Who invented the telephone?", "answer": "Alexander Graham Bell"},
    {"question": "What is the name of the device used to measure earthquakes?", "answer": "Seismograph"},
    {"question": "What is the smallest planet in our solar system?", "answer": "Mercury"},
    {"question": "Who wrote the famous book 'The Great Gatsby'?", "answer": "F. Scott Fitzgerald"},
    {"question": "What is the most abundant element in the universe?", "answer": "Hydrogen"},
    
    #question 81-90
    {"question": "Which ocean is the Bermuda Triangle located in?", "answer": "Atlantic Ocean"},
    {"question": "What is the capital city of Malaysia?", "answer": "Kuala Lumpur"},
    {"question": "Which physicist is known for his work on the photoelectric effect?", "answer": "Albert Einstein"},
    {"question": "What is the name of the largest island in the Mediterranean Sea?", "answer": "Sicily"},
    {"question": "Which element has the atomic number 1?", "answer": "Hydrogen"},
    {"question": "Who was the last Tsar of Russia?", "answer": "Nicholas II"},
    {"question": "What is the longest running Broadway show?", "answer": "The Phantom of the Opera"},
    {"question": "What is the largest continent by land area?", "answer": "Asia"},
    {"question": "Who painted the ceiling of the Sistine Chapel?", "answer": "Michelangelo"},
    {"question": "What is the official language of Egypt?", "answer": "Arabic"},
    
    #question 91-100
    
    {"question": "Which physicist is known for the uncertainty principle?", "answer": "Werner Heisenberg"},
    {"question": "What is the capital of Nigeria?", "answer": "Abuja"},
    {"question": "Who wrote the play 'Hamlet'?", "answer": "William Shakespeare"},
    {"question": "What is the primary ingredient in traditional hummus?", "answer": "Chickpeas"},
    {"question": "Which country is known as the Land of the Midnight Sun?", "answer": "Norway"},
    {"question": "What is the largest island in the world?", "answer": "Greenland"},
    {"question": "Who was the first person to walk on the moon?", "answer": "Neil Armstrong"},
    {"question": "What is the capital city of Turkey?", "answer": "Ankara"},
    {"question": "Which gas is most abundant in the Earth's atmosphere?", "answer": "Nitrogen"},
    {"question": "What is the term for the fear of spiders?", "answer": "Arachnophobia"},
   


]

# Insert the questions into the collection
result = collection.insert_many(questions)
print(f"Inserted question IDs: {result.inserted_ids}")
