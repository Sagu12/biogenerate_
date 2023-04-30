# import openai
# openai.api_key = "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"

# class BioGen: 
#   def __init__(self):
#     self.messages = [{"role": "system", "content": "You are a short 20 words limit dating bio writer for singles with the keywords provided and also you will not specify the gender, name, city name in any of the bios generated."}]

#   async def main(self, keywords: str) -> None:
#     try:
#       if keywords:
#         self.messages.append(
#           {"role": "user", "content": keywords},
#       )
#       chat = openai.ChatCompletion.create(
#           model="gpt-3.5-turbo", messages=self.messages
#       )
#       reply = chat.choices[0].message.content
#       #optional whether to store the output as a db for training model
#       self.messages.append({"role": "assistant", "content": reply})
#       return {"bio" : reply}  
#     except Exception as e:
#       return {"bio": "bio generated error"}



  