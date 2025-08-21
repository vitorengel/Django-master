import openai


def get_car_ai_bio(brand, model, year):
    prompt = ''' 
    Me mostre uma descrição de venda para o carro {} {} {} em apensa 250 caracteres. Fale coisas específicas desse modelo.
    '''
    openai.api_key = ''
    prompt = prompt.format(brand, model, year)
    response = openai.completions.create(
        model='gpt-3.5-turbo-instruct',
        prompt=prompt,
        max_tokens=1000,
    )
    return response['choices'][0]['text']