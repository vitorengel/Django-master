from openai import OpenAI


client = OpenAI(
    api_key='API_KEY'
)


def get_car_ai_bio(brand, model, year):
    message = '''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas sobre este carro.
    '''

    response = client.chat.completions.create(
        messages=[
            {
                'role' : 'user',
                'content' : message
            }
        ],
        max_tokens=1000,
        model='gpt-3.5-turbo',
    )
    
    return response.choices[0].message.content