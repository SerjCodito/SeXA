import openai
import random

openai.api_key = "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"
engine = "text-davinci-003"

industry_options = ["Finance", "Technology", "Healthcare", "Retail", "Education", "Energy", "Hospitality", "Real Estate", "Entertainment", "Transportation", "Manufacturing", "Construction", "Agriculture",
                    "Telecommunications", "Automotive", "Fashion", "Sports", "Media", "Gaming", "Food", "Beauty", "Fitness", "Home Improvement", "Insurance", "Legal Services", "Pet", "Non-profit", "Travel", "Gaming"]

greek_names = ["Alexandros", "Andreas", "Christina", "Dimitrios", "Eleni", "George", "Ioanna", "Katerina", "Kostas", "Maria", "Michalis", "Nikolas", "Panagiotis", "Paraskevi",
               "Sofia", "Stavros", "Stella", "Thalia", "Thodoris", "Vasilis", "Yannis", "Yiannis", "Eva", "Klio", "Nikoletta", "Orestis", "Vasiliki", "Anastasia", "Nikos", "Ilias"]

# Prompt user for required information
industry = input(f"Choose an industry from {industry_options}: ")

service_info = input("Enter information about your services or product: ")
industry_name = input("Enter the business name: ")

prompt = f"Generate 10 unique examples of ideal customers for a company in the {industry} industry that offers similar solutions to this information: {service_info}. The ideal customers should suffer a lot from not having the solution to their problem."
response = openai.Completion.create(
    engine=engine, prompt=prompt, max_tokens=1024, temperature=0.5)

choices = response.choices[0].text.strip().split("\n")

# Store generated examples in an array
generated_examples = []
for choice in choices:
    generated_examples.append(choice.strip())


target_audience = ""
for i, choice in enumerate(generated_examples):
    print(f"{i+1}. {choice.strip()}")
choice_index = input(
    f"Please select one of the above options (enter a number from 1-{len(generated_examples)}): ")


prompt2 = f"Do a competitor research to understand better what problems does the product/service solve, on 5 top brands in the {industry} industry similar to the information provided here, {service_info} Then act as a professional website copywriter and write an about us section for {industry_name}, explaining exactly what they do and what problems they help solve. I need you to combine the information the user will prompt and the information you will find online."
response = openai.Completion.create(
    engine=engine, prompt=prompt2, max_tokens=1024, n=10, stop=None, temperature=0.5)


# Generate 10 examples of ideal customers using OpenAI's GPT-3 API


character_name = random.choice(greek_names)
story_prompt = (
    f"Behave as a professional writer and brand storyteller, and as a sales person for a content marketing company. I will give you the parameters to write a story about how {industry_name} addresses the problems, desires and pain of {target_audience}. \n"
    f"The first thing you must do before write the story is to research the next 10 books I will write in order to understand better how to craft amazing stories and how to use those stories to increase brand awareness, build trust and increase sales. You will take the 5 keypoints from each book in order to write the story with the parameters I will give you. You will try to combine the stories in the books that are real with the stories that you will create. Here are the books names, MADE TO STICK: WHY SOME IDEAS SURVIVE AND OTHERS DIE BY CHIP HEATH & DAN HEATH, STEVE JOBS BY WALTER ISAACSON, ONWARD: HOW STARBUCKS FOUGHT FOR ITS LIFE WITHOUT LOSING ITS SOUL BY HOWARD SCHULTZ & JOANNE GORDON,ELON MUSK: TESLA, SPACEX AND THE QUEST FOR A FANTASTIC FUTURE BY ASHLEE VANCE,START WITH WHY: HOW GREAT LEADERS INSPIRE OTHERS TO TAKE ACTION BY SIMON SINEK,THE DOODLE REVOLUTION BY SUNNI BROWN,ALL MARKETERS ARE LIARS: THE UNDERGROUND CLASSIC THAT EXPLAINS HOW MARKETING REALLY WORKS–AND WHY AUTHENTICITY IS THE BEST MARKETING OF ALL BY SETH GODIN,The Storytelling Animal: How Stories Make Us Human by Jonathan Gottschall,The Story Factor: Inspiration, Influence, and Persuasion throught the Art of Storytelling by Annette Simmons and Doug Lipman,Writing for Story: Craft Secrets of Dramatic Nonfiction by Jon Franklin,Resonate: Present Visual Stories that Transform Audiences by Nancy Duarte,Made to Stick: Why Some Ideas Survive and Others Die by Chip Heath and Dan Heath \n"
    f"Use the following information to better understand {industry_name} and what they do, here's more information about them, {prompt2}. \n"
    f"The story you will write will be used to create a brand storytelling video for {industry_name} with the goal to help them attract more {target_audience} clients, increase brand awareness and brand loyalty.\n"
    f"The first chapter is about setting up the protagonist environment, details to personal life like weaknesses and advantages. \n"
    f"Then story must continue with how the protagonist, {character_name}  is psychologically suffering from a problem that {industry_name} solves.\n"
    f"Then the story will continue with how {character_name} feels not having the solution of {industry_name} and how it is impacting {character_name} family, business or personal life. \n"
    f"The second chapter is focused on adding the neccesary details to the story to make the story feel real, this part must build conflict with {character_name} thoughts or environment. \n"
    f"The third chapter follows with how {character_name} discovers {industry_name} by either randomly meeting with a friend, or surfing online, or from a family member. \n"
    f"The final chapter of the story must finish with how {character_name}'s pain points have vanished and it helped me solve his big problem that was hurting him, then continue with how after using {industry_name} service/product a new opportunity arrised"
)

generated_story = openai.Completion.create(
    engine=engine,
    prompt=story_prompt,
    max_tokens=2000,
    temperature=0.5,
)["choices"][0]["text"]

print(generated_story)
