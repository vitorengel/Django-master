import openai


def get_car_ai_bio(brand, model, year):
    prompt = ''' 
    Me mostre uma descrição de venda para o carro {} {} {} em apensa 250 caracteres. Fale coisas específicas desse modelo.
    '''
    openai.api_key = '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'
    prompt = prompt.format(brand, model, year)
    response = openai.completions.create(
        model='gpt-3.5-turbo-instruct',
        prompt=prompt,
        max_tokens=1000,
    )
    return response['choices'][0]['text']