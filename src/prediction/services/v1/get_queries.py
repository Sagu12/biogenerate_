# import random

# pr= """write dating bios with keywords

#         Keywords: inquisitive, intentional, reflective
#         Sentences: I'm an inquisitive and reflective person who is always looking to learn and grow. I'm intentional in my relationships and value honesty and communication. I'm looking for someone who shares similar values and is open to exploring new ideas and experiences together.

#         Keywords: daydreamer, uses internet, derping
#         Sentences: I'm a daydreamer who loves to use the internet to explore new ideas and connect with others. When I'm not lost in my own thoughts, you can usually find me derping around online or trying out new hobbies. Looking for someone who shares a similar sense of curiosity and adventure.

#         Keywords: romantic, woman, faithful, fun loving
#         Sentences: I'm a romantic woman who is looking for a faithful and fun-loving partner to share my life with. I value honesty, trust, and mutual respect in a relationship, and I'm excited to find someone who shares these values. Whether we're exploring new places or cuddling up at home, I want to find someone who is ready to enjoy every moment with me.

#         Keywords: tall, curly, introvert
#         Sentences: I'm a tall, curly-haired introvert who loves to curl up with a good book or spend time in nature. I'm looking for someone who is kind, understanding, and respectful, and who is willing to take the time to get to know me. Whether we're exploring new places or just enjoying each other's company at home, I'm excited to find someone who shares my love of meaningful connections and deep conversations.

#         Keywords: singer, duet, bathroom
#         Sentences: I'm a singer who loves nothing more than belting out a good duet with my partner. I'm looking for someone who is kind, passionate, and confident, and who isn't afraid to let their true self shine. Whether we're performing on stage or singing in the bathroom, I'm excited to find someone who shares my love of music and adventure.

#         Keywords: travel, music, gym
#         Sentences: I'm a adventurous person who loves to travel and discover new music. When I'm not exploring new places, you can usually find me at the gym or trying out new hobbies. I'm looking for someone who is kind, spontaneous, and open-minded, and who is ready to join me on new adventures and share new experiences together.

#         Keywords: catch, fall, love
#         Sentences: I'm looking for someone to catch me when I fall and to share the ups and downs of life with. I believe in love at first sight and in taking risks for the things that matter most. I'm looking for someone who is kind, sincere, and passionate, and who is ready to take the journey of love with me.

#         Keywords: writer, techie, boxer
#         Sentences: I'm a writer and techie who loves to explore new ideas and push the boundaries of what's possible. When I'm not busy coding or creating, you can usually find me boxing at the gym or trying out new hobbies. I'm looking for someone who is intelligent, driven, and physically fit, and who is ready to join me on new adventures and share new experiences together.

#         Keywords: chai, dance, weather
#         Sentences: I'm a chai-loving dancer who is always ready to embrace whatever the weather has in store. Whether it's raining or shining, I'm always up for a new adventure and trying out new things. I'm looking for someone who is spontaneous, fun-loving, and adventurous, and who is ready to join me on new adventures and share new experiences together.

#         Keywords: dreams, creating life, day time
#         Sentences: I'm a dreamer who loves nothing more than creating a life that I love. Whether it's exploring new places or spending a quiet day at home, I'm always looking for new ways to grow and learn. I'm looking for someone who is kind, curious, and open-minded, and who is ready to join me on new adventures and share new experiences together.

#         Keywords: netflix, night, talk
#         Sentences: I'm a Netflix-loving night owl who loves nothing more than staying up late talking about everything and nothing. Whether we're snuggling up on the couch or exploring the city, I'm always up for a new adventure and trying out new things. I'm looking for someone who is kind, open-minded, and up for anything, and who is ready to join me on new adventures and share new experiences together.

#         Keywords: {}
#         Sentences:"""

# prompt= '''Paraphrase the given sentence into a different sentence.

#                         Input: Hi there! I'm a kind and gentle person who loves kids and dogs. I'm always seeking out adventure and being outdoors, and love getting away for the weekend. If you're someone who is passionate about the outdoors, pets, and staying active, I'd love to chat and get to know you better.
#                         Output: I'm a kind and adventurous person who enjoys the outdoors and pets. I'm looking to chat with someone who shares my passions.

#                         Input: Hi there! I'm a kind and gentle person who loves caring for others. I'm also the type to keep what I say to a minimum. I'm a big music and art fan, and I'm always up to new experiences and exploring new places. If you're someone who is an easygoing and fun-loving partner who is ready to commit and grow old with, I'd love to chat and get to know you better.
#                         Output: I am a kind, gentle person who enjoys caring for others. A fan of music and art and enjoy experiencing new things. Looking for an easygoing, fun loving partner who is ready to commit and grow old together.
                        
#                         Input: {}
#                         Output:'''


# substrings= ["father", "mother", "sister", "brother", "dad", "mom", "siblings", "husband", "wife"]

# url= "https://staging.together.xyz/api/inference"

# model= "Together-gpt-JT-6B-v1"

# space= 'GPT-JT HuggingFace Space'

# temperature= random.uniform(0.9, 1)

# agent= 'User-Agent'