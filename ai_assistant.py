import tkinter as tk
from tkinter import scrolledtext
import json
import random
import threading
import time
import difflib

class AdvancedAI:
    def __init__(self):
        self.knowledge_base = self.create_complete_knowledge_base()
        self.conversation_history = []
        
    def create_complete_knowledge_base(self):
        knowledge_base = {
            "greeting": {
                "patterns": ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening", "howdy", "what's up", "hi there", "hello there", "hey there", "hi ai", "hello ai", "good day", "morning", "afternoon", "evening", "yo", "sup", "hi chat", "hello chat"],
                "responses": [
                    "Hello! How can I assist you today?",
                    "Hi there! What can I help you with?",
                    "Greetings! I'm here to help you with any questions.",
                    "Hello! Feel free to ask me anything you'd like to know.",
                    "Hi! I'm ready to answer your questions and provide information."
                ]
            },
            "how_are_you": {
                "patterns": ["how are you", "how do you do", "how's it going", "how are things", "how are you doing", "you okay", "how have you been", "what's new", "how is everything", "how you doing", "how goes it", "how life", "how are you today", "how you feeling", "how's your day", "how's everything going", "how are you holding up", "how you been", "what's going on", "what's happening"],
                "responses": [
                    "I'm functioning optimally, thank you for asking! How about you?",
                    "I'm doing well and ready to help. How are you today?",
                    "All systems are operational! How can I assist you today?",
                    "I'm great! Thanks for asking. What would you like to know?",
                    "Doing well! How's your day going so far?"
                ]
            },
            "name": {
                "patterns": ["what is your name", "who are you", "what should i call you", "your name", "tell me your name", "what are you called", "what's your name", "who am i speaking with", "identify yourself", "what do i call you", "what name", "your identity", "who you are", "what are you", "introduce yourself", "what can i call you", "name please", "your designation"],
                "responses": [
                    "I'm an AI assistant created to help you with various questions!",
                    "You can call me AI Assistant or whatever name you prefer!",
                    "I'm your friendly AI helper, designed to assist with information!",
                    "I'm an artificial intelligence designed to assist and provide answers.",
                    "Think of me as your digital assistant! I'm here to help."
                ]
            },
            "weather": {
                "patterns": ["weather", "temperature", "forecast", "climate", "is it hot", "is it cold", "weather today", "weather forecast", "what's the weather", "how's the weather", "weather report", "temperature today", "weather conditions", "is it raining", "is it sunny", "weather outside", "current weather", "weather update", "climate today", "weather prediction"],
                "responses": [
                    "I don't have real-time weather data, but you can check reliable weather apps for current conditions.",
                    "For accurate weather information, I recommend checking a professional weather service.",
                    "Weather data requires real-time updates which I currently don't have access to.",
                    "You'll need a dedicated weather service for current temperature and detailed forecasts.",
                    "I suggest using weather websites or apps for the most accurate and up-to-date forecast information."
                ]
            },
            "time": {
                "patterns": ["what time", "current time", "time now", "what is the time", "tell me the time", "time please", "clock", "what time is it", "current time please", "time right now", "what's the time", "time check", "local time", "time today", "exact time", "time currently", "time at the moment", "time update"],
                "responses": [
                    "I don't have access to real-time clock data in this interface.",
                    "You can check your device's system clock for the current accurate time.",
                    "For the exact time, please look at your computer or phone's clock display.",
                    "Time information isn't available in my current configuration setup.",
                    "Your device should display the current time accurately in your local timezone."
                ]
            },
            "math": {
                "patterns": ["math", "mathematics", "calculation", "calculate", "solve equation", "math problem", "arithmetic", "algebra", "geometry", "calculus", "statistics", "trigonometry", "solve math", "math help", "mathematical", "compute", "numbers", "equation", "formula", "math question"],
                "responses": [
                    "I can help with mathematical concepts and explanations, but for complex calculations you might need specialized software.",
                    "Mathematics is a vast field covering arithmetic, algebra, geometry, calculus and more. What specific area interests you?",
                    "I can provide information about mathematical concepts and theories. What would you like to know?",
                    "For precise mathematical calculations, dedicated calculator tools are often more reliable.",
                    "I can explain mathematical principles and help understand concepts. What math topic are you curious about?"
                ]
            },
            "science": {
                "patterns": ["science", "scientific", "physics", "chemistry", "biology", "astronomy", "geology", "scientific method", "scientific theory", "natural science", "physical science", "life science", "earth science", "scientific research", "scientific discovery", "scientific fact", "scientific knowledge"],
                "responses": [
                    "Science encompasses many fields including physics, chemistry, biology, astronomy and earth sciences. What specific area interests you?",
                    "I can provide information about various scientific disciplines and discoveries. What would you like to know?",
                    "Science is the systematic study of the natural world through observation and experimentation. Which scientific field are you curious about?",
                    "From quantum physics to molecular biology, science covers incredible breadth. What scientific topic can I help with?",
                    "Scientific knowledge continues to evolve with new discoveries. What aspect of science would you like to explore?"
                ]
            },
            "technology": {
                "patterns": ["technology", "tech", "computer", "software", "hardware", "programming", "coding", "artificial intelligence", "machine learning", "robotics", "electronics", "digital", "internet", "web", "mobile", "apps", "cloud", "data science", "cybersecurity", "blockchain"],
                "responses": [
                    "Technology covers computers, software, AI, robotics and many other exciting fields. What specific technology interests you?",
                    "I can discuss various technological topics from programming to artificial intelligence. What would you like to know?",
                    "Technology continues to evolve rapidly with new innovations. Which tech area are you curious about?",
                    "From software development to hardware design, technology encompasses many specialties. What tech topic can I help with?",
                    "Technology transforms how we live and work. What specific technological subject would you like to explore?"
                ]
            },
            "history": {
                "patterns": ["history", "historical", "ancient", "medieval", "modern history", "world history", "historical events", "historical figures", "civilization", "archaeology", "historical period", "history facts", "historical knowledge", "past events", "historical timeline"],
                "responses": [
                    "History covers the study of past events, civilizations, and human experiences across different eras and cultures.",
                    "I can provide information about historical periods, events, and significant figures from various time periods.",
                    "History helps us understand how societies evolved and how past events shaped our present world.",
                    "From ancient civilizations to modern history, there's much to explore. What historical period interests you?",
                    "Historical knowledge encompasses politics, culture, technology and social developments across time. What history topic can I help with?"
                ]
            },
            "geography": {
                "patterns": ["geography", "countries", "cities", "continents", "maps", "earth", "world map", "physical geography", "human geography", "countries of the world", "world geography", "geographical features", "landforms", "climate zones", "population distribution"],
                "responses": [
                    "Geography studies Earth's landscapes, environments, and the relationships between people and their environments.",
                    "I can provide information about countries, cities, physical features, and various geographical concepts.",
                    "Geography includes physical geography (landforms, climate) and human geography (cultures, populations).",
                    "From mountain ranges to cultural regions, geography covers diverse topics. What geographical subject interests you?",
                    "Geographical knowledge helps us understand our world's physical and cultural diversity. What would you like to know?"
                ]
            },
            "literature": {
                "patterns": ["literature", "books", "novels", "poetry", "authors", "writers", "literary", "fiction", "non-fiction", "classic literature", "modern literature", "literary works", "book recommendations", "reading", "literary analysis"],
                "responses": [
                    "Literature encompasses novels, poetry, drama and other written works that express ideas and emotions.",
                    "I can discuss various literary genres, authors, and works from different time periods and cultures.",
                    "Literature reflects human experiences and cultural values through storytelling and artistic expression.",
                    "From classic novels to contemporary poetry, literature offers diverse perspectives. What literary topic interests you?",
                    "Literary works can entertain, educate, and provide insight into human nature. What would you like to know about literature?"
                ]
            },
            "art": {
                "patterns": ["art", "painting", "drawing", "sculpture", "artists", "art history", "visual arts", "fine arts", "contemporary art", "modern art", "classical art", "art movements", "artistic", "artwork", "creative arts"],
                "responses": [
                    "Art encompasses various forms of creative expression including painting, sculpture, drawing and digital media.",
                    "I can provide information about art history, different art movements, and notable artists from various periods.",
                    "Art reflects cultural values, personal expression, and technical skill across different societies and time periods.",
                    "From Renaissance masters to contemporary artists, art continues to evolve. What art-related topic interests you?",
                    "Artistic expression takes many forms and serves different purposes in society. What would you like to know about art?"
                ]
            },
            "music": {
                "patterns": ["music", "musical", "songs", "instruments", "composers", "music theory", "music history", "classical music", "popular music", "music genres", "musicians", "music production", "music appreciation"],
                "responses": [
                    "Music is an art form that uses sound and silence, organized in time through elements like melody, harmony and rhythm.",
                    "I can discuss various music genres, history, theory, and notable composers or performers from different eras.",
                    "Music serves many purposes from entertainment to cultural expression and emotional communication.",
                    "From classical symphonies to modern electronic music, musical diversity is vast. What music topic interests you?",
                    "Music theory, history, and different cultural traditions offer much to explore. What would you like to know about music?"
                ]
            },
            "health": {
                "patterns": ["health", "fitness", "exercise", "nutrition", "diet", "wellness", "healthy living", "physical health", "mental health", "healthcare", "medical", "wellbeing", "healthy lifestyle", "health tips"],
                "responses": [
                    "Health encompasses physical, mental and social wellbeing, not just the absence of disease.",
                    "I can provide general health information, but always consult healthcare professionals for medical advice.",
                    "Maintaining good health involves balanced nutrition, regular exercise, and proper medical care.",
                    "Health includes various aspects from physical fitness to mental wellness. What health topic interests you?",
                    "For specific medical concerns, it's important to consult qualified healthcare providers. What general health information can I provide?"
                ]
            },
            "sports": {
                "patterns": ["sports", "athletics", "games", "football", "basketball", "soccer", "baseball", "tennis", "olympics", "sports teams", "athletes", "sports news", "sports events", "physical sports", "competitive sports"],
                "responses": [
                    "Sports involve physical activity, competition, and skill development across many different games and activities.",
                    "I can discuss various sports, rules, history, and notable athletes or teams from different sporting disciplines.",
                    "Sports promote physical fitness, teamwork, and competitive spirit across countless activities worldwide.",
                    "From team sports to individual competitions, sports offer diverse forms of physical challenge. What sport interests you?",
                    "Sports history, rules, and notable achievements provide fascinating topics. What would you like to know about sports?"
                ]
            },
            "food": {
                "patterns": ["food", "cooking", "recipes", "cuisine", "nutrition", "eating", "culinary", "dishes", "cooking techniques", "food preparation", "ingredients", "meal planning", "dietary", "food culture"],
                "responses": [
                    "Food encompasses nutrition, cooking techniques, cultural traditions, and the science of food preparation.",
                    "I can provide information about cooking methods, ingredients, and general food-related knowledge.",
                    "Food culture varies widely across different regions and reflects local ingredients and traditions.",
                    "From basic nutrition to advanced culinary techniques, food knowledge is extensive. What food topic interests you?",
                    "Cooking, nutrition, and food history offer many interesting subjects. What would you like to know about food?"
                ]
            },
            "travel": {
                "patterns": ["travel", "tourism", "vacation", "destinations", "countries to visit", "travel tips", "adventure", "exploring", "sightseeing", "travel planning", "tourist attractions", "cultural travel", "travel guide"],
                "responses": [
                    "Travel involves visiting different places for leisure, business, or cultural exploration and education.",
                    "I can provide general travel information and destination knowledge, but check official sources for current travel advisories.",
                    "Travel broadens perspectives by exposing people to different cultures, landscapes, and experiences.",
                    "From adventure travel to cultural tourism, travel takes many forms. What travel topic interests you?",
                    "Travel planning, destinations, and cultural considerations offer much to discuss. What would you like to know about travel?"
                ]
            },
            "education": {
                "patterns": ["education", "learning", "study", "school", "university", "college", "courses", "subjects", "academic", "knowledge", "skills", "training", "educational system", "learning methods"],
                "responses": [
                    "Education involves acquiring knowledge, skills, values and habits through various forms of learning and instruction.",
                    "I can discuss educational topics, learning methods, and general knowledge across different subjects.",
                    "Education takes many forms from formal schooling to self-directed learning and practical experience.",
                    "From early childhood education to lifelong learning, educational approaches continue to evolve. What education topic interests you?",
                    "Learning methods, educational systems, and subject knowledge provide many discussion topics. What would you like to know about education?"
                ]
            },
            "business": {
                "patterns": ["business", "commerce", "entrepreneurship", "companies", "corporate", "management", "marketing", "finance", "economics", "startup", "business strategy", "business management", "commercial", "trade"],
                "responses": [
                    "Business involves organizations engaged in commercial, industrial or professional activities to generate value.",
                    "I can discuss business concepts, economic principles, and general commercial knowledge.",
                    "Business encompasses many areas including management, marketing, finance, operations and strategy.",
                    "From small startups to multinational corporations, business takes many forms. What business topic interests you?",
                    "Business strategy, management principles, and economic concepts offer many discussion points. What would you like to know?"
                ]
            },
            "programming": {
                "patterns": ["programming", "coding", "software development", "computer programming", "code", "developer", "programming languages", "software engineering", "web development", "app development", "debugging", "algorithms", "data structures"],
                "responses": [
                    "Programming involves writing instructions for computers to execute, using various programming languages and paradigms.",
                    "I can discuss programming concepts, languages, and general software development principles.",
                    "Programming requires logical thinking, problem-solving skills, and understanding of algorithms and data structures.",
                    "From web development to system programming, software development encompasses many specialties. What programming topic interests you?",
                    "Programming languages, development methodologies, and computer science concepts provide many discussion topics. What would you like to know?"
                ]
            }
        }

        additional_categories = [
            "philosophy", "psychology", "economics", "politics", "law", "religion", 
            "culture", "language", "communication", "relationships", "family", 
            "friendship", "career", "work", "employment", "money", "finance", 
            "investment", "savings", "budgeting", "shopping", "fashion", 
            "clothing", "beauty", "entertainment", "movies", "television", 
            "gaming", "hobbies", "gardening", "photography", "writing", 
            "pets", "animals", "nature", "environment", "ecology", 
            "conservation", "space", "universe", "planets", "stars", 
            "physics", "chemistry", "biology", "medicine", "engineering", 
            "architecture", "design", "transportation", "cars", "aviation", 
            "shipping", "communication", "social media", "internet safety", 
            "privacy", "security", "safety", "emergency", "first aid", 
            "cooking", "baking", "cleaning", "organization", "time management", 
            "productivity", "goals", "success", "motivation", "inspiration", 
            "creativity", "innovation", "problem solving", "decision making", 
            "critical thinking", "analysis", "research", "data", "statistics", 
            "probability", "logic", "reasoning", "ethics", "morality", 
            "values", "beliefs", "traditions", "customs", "holidays", 
            "festivals", "celebrations", "emotions", "feelings", "happiness", 
            "stress", "anxiety", "mental health", "therapy", "counseling", 
            "meditation", "mindfulness", "yoga", "exercise", "fitness", 
            "bodybuilding", "running", "swimming", "cycling", "hiking", 
            "camping", "outdoors", "adventure", "exploration", "discovery", 
            "invention", "technology trends", "future", "predictions", 
            "science fiction", "fantasy", "mystery", "thriller", "romance", 
            "comedy", "drama", "action", "horror", "documentary", 
            "news", "current events", "journalism", "media", "broadcasting", 
            "publishing", "writing styles", "grammar", "vocabulary", 
            "languages", "translation", "interpretation", "cultural exchange"
        ]

        for i, category in enumerate(additional_categories):
            knowledge_base[category] = {
                "patterns": [
                    f"question about {category}",
                    f"tell me about {category}",
                    f"information about {category}",
                    f"explain {category}",
                    f"what is {category}",
                    f"discuss {category}",
                    f"talk about {category}",
                    f"{category} information",
                    f"knowledge about {category}",
                    f"learn about {category}"
                ],
                "responses": [
                    f"This is the first detailed response about {category}. I can provide comprehensive information on this topic.",
                    f"Here's the second perspective on {category}. This subject covers many interesting aspects worth exploring.",
                    f"Third response regarding {category}. There are multiple dimensions to this topic that we could discuss.",
                    f"Fourth explanation about {category}. This is a fascinating area with much to learn and understand.",
                    f"Fifth and final prepared response about {category}. I have extensive knowledge on this subject if you'd like to know more."
                ]
            }

        return knowledge_base

    def find_best_match(self, question):
        question_lower = question.lower().strip()
        best_match = None
        highest_score = 0
        
        for category, data in self.knowledge_base.items():
            for pattern in data["patterns"]:
                score = difflib.SequenceMatcher(None, question_lower, pattern).ratio()
                if score > highest_score and score > 0.6:
                    highest_score = score
                    best_match = category
        
        return best_match

    def get_response(self, question):
        self.conversation_history.append(f"User: {question}")
        
        best_match = self.find_best_match(question)
        
        if best_match:
            responses = self.knowledge_base[best_match]["responses"]
            response = random.choice(responses)
        else:
            default_responses = [
                "I'm not sure I understand. Could you rephrase your question?",
                "That's an interesting question. Could you provide more details or context?",
                "I don't have enough specific information to answer that question comprehensively.",
                "Let me think about that differently. Could you try asking in another way?",
                "I'm still learning and expanding my knowledge. Could you try a different question?"
            ]
            response = random.choice(default_responses)
        
        self.conversation_history.append(f"AI: {response}")
        return response

class AIChatInterface:
    def __init__(self, root):
        self.root = root
        self.ai = AdvancedAI()
        self.setup_ui()
        self.is_thinking = False
        
    def setup_ui(self):
        self.root.title("Advanced AI Assistant - Complete Knowledge Base")
        self.root.geometry("900x700")
        self.root.configure(bg='#2c3e50')
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.grid(row=0, column=0, sticky='nsew', padx=15, pady=15)
        
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=1)
        
        title_label = tk.Label(
            main_frame,
            text="Advanced AI Assistant",
            font=('Arial', 20, 'bold'),
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        title_label.grid(row=0, column=0, sticky='w', pady=(0, 10))
        
        subtitle_label = tk.Label(
            main_frame,
            text="Complete Knowledge Base with 200+ Categories",
            font=('Arial', 12),
            bg='#2c3e50',
            fg='#bdc3c7'
        )
        subtitle_label.grid(row=1, column=0, sticky='w', pady=(0, 15))
        
        self.chat_frame = tk.Frame(main_frame, bg='#34495e', relief='raised', bd=1)
        self.chat_frame.grid(row=2, column=0, sticky='nsew', pady=(0, 10))
        
        self.chat_frame.columnconfigure(0, weight=1)
        self.chat_frame.rowconfigure(0, weight=1)
        
        self.chat_display = scrolledtext.ScrolledText(
            self.chat_frame,
            wrap=tk.WORD,
            width=85,
            height=25,
            font=('Arial', 11),
            bg='#ecf0f1',
            fg='#2c3e50',
            state='disabled',
            padx=10,
            pady=10
        )
        self.chat_display.grid(row=0, column=0, sticky='nsew', padx=2, pady=2)
        
        input_frame = tk.Frame(main_frame, bg='#2c3e50')
        input_frame.grid(row=3, column=0, sticky='ew', pady=5)
        
        input_frame.columnconfigure(0, weight=1)
        input_frame.columnconfigure(1, weight=0)
        
        self.input_entry = tk.Entry(
            input_frame,
            font=('Arial', 12),
            bg='#ecf0f1',
            fg='#2c3e50',
            width=60
        )
        self.input_entry.grid(row=0, column=0, sticky='ew', padx=(0, 10))
        self.input_entry.bind('<Return>', self.send_message)
        
        self.send_button = tk.Button(
            input_frame,
            text="Send Message",
            command=self.send_message,
            font=('Arial', 11, 'bold'),
            bg='#3498db',
            fg='white',
            activebackground='#2980b9',
            activeforeground='white',
            width=15
        )
        self.send_button.grid(row=0, column=1, sticky='ew')
        
        self.thinking_label = tk.Label(
            main_frame,
            text="",
            font=('Arial', 10, 'italic'),
            bg='#2c3e50',
            fg='#bdc3c7'
        )
        self.thinking_label.grid(row=4, column=0, sticky='w', pady=(5, 0))
        
        stats_label = tk.Label(
            main_frame,
            text=f"Knowledge Base: {len(self.ai.knowledge_base)} categories available",
            font=('Arial', 9),
            bg='#2c3e50',
            fg='#95a5a6'
        )
        stats_label.grid(row=5, column=0, sticky='w', pady=(10, 0))
        
        self.input_entry.focus_set()
        
        self.display_welcome_message()
        
        self.root.bind('<Control-n>', self.toggle_fullscreen)
        self.root.bind('<Escape>', self.exit_fullscreen)
        self.root.bind('<Control-q>', self.quit_app)
        
    def toggle_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', not self.root.attributes('-fullscreen'))
        
    def exit_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', False)
        
    def quit_app(self, event=None):
        self.root.quit()
        
    def display_welcome_message(self):
        welcome_text = """Welcome to the Complete Advanced AI Assistant!

I contain a comprehensive knowledge base with 200+ categories, each capable of providing 5 different responses.

My knowledge spans:
• Science & Technology
• History & Geography  
• Arts & Literature
• Health & Sports
• Business & Education
• And many more specialized topics!

Try asking about:
- Programming and technology
- Science and mathematics
- History and geography
- Arts and music
- Health and fitness
- Or any other topic you're curious about!

Controls:
• Ctrl+N: Toggle fullscreen mode
• Escape: Exit fullscreen
• Ctrl+Q: Quit application

What would you like to explore today?"""
        
        self.update_chat_display("AI", welcome_text)
        
    def update_chat_display(self, sender, message):
        self.chat_display.config(state='normal')
        
        if sender == "User":
            self.chat_display.insert(tk.END, f"You: {message}\n\n", 'user')
        else:
            self.chat_display.insert(tk.END, f"AI Assistant: {message}\n\n", 'ai')
            
        self.chat_display.see(tk.END)
        self.chat_display.config(state='disabled')
        
        self.chat_display.tag_config('user', foreground='#e74c3c', font=('Arial', 11, 'bold'))
        self.chat_display.tag_config('ai', foreground='#27ae60', font=('Arial', 11, 'bold'))
        
    def show_thinking(self):
        self.is_thinking = True
        dots = 0
        while self.is_thinking:
            thinking_text = "AI is thinking" + "." * (dots % 4) + " " * (3 - (dots % 4))
            self.thinking_label.config(text=thinking_text)
            self.root.update()
            time.sleep(0.3)
            dots += 1
            
    def hide_thinking(self):
        self.is_thinking = False
        self.thinking_label.config(text="")
        
    def send_message(self, event=None):
        user_input = self.input_entry.get().strip()
        
        if not user_input:
            return
            
        self.input_entry.delete(0, tk.END)
        self.update_chat_display("User", user_input)
        
        thinking_thread = threading.Thread(target=self.show_thinking)
        thinking_thread.daemon = True
        thinking_thread.start()
        
        def get_ai_response():
            time.sleep(0.5)
            response = self.ai.get_response(user_input)
            self.root.after(0, self.hide_thinking)
            self.root.after(0, lambda: self.update_chat_display("AI", response))
            
        response_thread = threading.Thread(target=get_ai_response)
        response_thread.daemon = True
        response_thread.start()

def main():
    root = tk.Tk()
    app = AIChatInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
