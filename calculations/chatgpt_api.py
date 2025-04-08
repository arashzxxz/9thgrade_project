import openai  
openai.api_key = 'https://open.wiki-api.ir/apis-1/ChatGPT?q='  
def chat_with_gpt():  
    response = openai.ChatCompletion.create(  
        model="gpt-3.5-turbo",  
        messages=[  
            {"role": "user", "content": "Hello"}  
        ]  
    )  
    print(response.choices[0].message['content'])   
chat_with_gpt()
