import anthropic
import os
import cv2
import base64
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)

image_media_type = "image/jpeg"

video_path = "Douchebag Bison.mp4"
video = cv2.VideoCapture(video_path)

if not video.isOpened():
    print(f"Error: Could not open video file {video_path}")
    exit()

base64_frames = []
frame_count = 0
n = 50  # Adjust to process every 50th frame
while video.isOpened():
    success, frame = video.read()
    if not success:
        break
    if frame_count % n == 0:
        _, buffer = cv2.imencode(".jpg", frame)
        base64_frames.append(base64.b64encode(buffer).decode("utf-8"))
    frame_count += 1

video.release()
print(f"{len(base64_frames)} frames read and encoded.")

messages_content = []
for i, base64_image in enumerate(base64_frames):
    messages_content.append({"type": "text", "text": f"Frame {i + 1}:"})
    messages_content.append({
        "type": "image",
        "source": {
            "type": "base64",
            "media_type": image_media_type,
            "data": base64_image,
        },
    })

messages_content.append({"type": "text", "text": """Generate a single word tag or if applicable multiple tags that I can upload along with the video, choose from the following options.
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
    """})

message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": messages_content
        }
    ],
)

print(message.text)
