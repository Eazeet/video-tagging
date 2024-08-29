import google.generativeai as genai
video_file_name = "Douchebag Bison.mp4"
genai.configure(api_key='AIzaSyCHpCagd4LqDwu9ERX4mwE5ULoVj6vc2_w')

print(f"Uploading file...")
video_file = genai.upload_file(path=video_file_name)
print(f"Completed upload: {video_file.uri}")

prompt = """Generate a single word tag or if applicable multiple tags that I can upload along with the video, choose from the following options.
    "Comedy",
    "Entertainment Culture",
    "Music",
    "Food & Drink",
    "Sports",
    "Beauty & Style",
    "Fitness & Health",
    "Travel",
    "Science & Education",
    "Gaming",
    "Daily Life",
    "DIY",
    "Family",
    "Anime & Comics",
    "ASMR",
    "Home & Gardens",
    "Auto & Vehicle",
    "Animals",
    "Art",
    "Finance",
    "Technology",
    "Movies",
    "Trending",
    "New",
    "School",
    "Video",
    "Religion & Faith",
    "Fashion",
    "Politics & Current Events",
    "Nature & Environment",
    "Relationships & Dating",
    "Parenting",
    "Career & Professional Development",
    "Language Learning",
    "Dance",
    "Photography & Videography",
    "Books & Literature",
    "Meditation & Mindfulness",
    "Crafts & DIY Projects",
    "Automotive",
    "Activism & Social Causes",
    "Cooking & Recipes",
    "Pranks & Challenges",
    "Nostalgia & Throwbacks",
    "Supernatural & Paranormal",
    "Motivation & Self-Help",
    "Astrology & Horoscopes",
    "True Crime",
    "History"
    """

model = genai.GenerativeModel(model_name="gemini-1.5-pro")

print("Making LLM inference request...")
response = model.generate_content([video_file, prompt],
                                  request_options={"timeout": 600})

print(response.text)