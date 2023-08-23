
import pandas as pd
import time
import hashlib
from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
import openai

URL_HOME = 'https://auth.dio.me/'
HASHED_FILE = 'hashed_data.csv'
openai.api_key = '{PUT YOUR OPEN AI KEY HERE!}'

try:
    df = pd.read_csv(HASHED_FILE)
except FileNotFoundError:
    df = pd.DataFrame(columns=['hash'])

def enrich_discussion(text):

    hashed_value = hashlib.sha256(text.encode()).hexdigest()

    if len(df[df['hash'] == hashed_value])==0:
        df.loc[len(df.index)]=[hashed_value]
        return True
    else:
        return False
   
def generate_ai_news(text):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system", 
                "content": "Você é um especialista na área de Tecnologia de Informação e Ciência de Dados."
                },
            {
                "role": "user", 
                "content": f"Crie uma mensagem para um fórum de discussão que responda a dúvida, ou acrescente alguma informação ao tópico abaixo. (Não é necessário escrever saudação no final da resposta, nem meu nome.) {text}."}
        ]
    )
    responseChatGPT = completion.choices[0].message.content
    return responseChatGPT

driver = webdriver.Chrome()
driver.get('https://auth.dio.me/')
uname = driver.find_element(By.ID, "username") 
uname.send_keys("{PUT YOUR EMAIL HERE!}") 
uname = driver.find_element(By.ID, "password") 
uname.send_keys("{PUT YOUR PASSWORD HERE!}") 
uname = driver.find_element(By.ID, "kc-login")
uname.click()
time.sleep(10)
driver.get("https://web.dio.me/track/71477949-f762-43c6-9bf2-9cf3d7f61d4a?page=1&search=&tab=forum")
time.sleep(5)
driver.get("https://web.dio.me/track/71477949-f762-43c6-9bf2-9cf3d7f61d4a?page=1&search=&tab=forum")
time.sleep(14)
i=0
while i < len(discussions := driver.find_elements(By.CLASS_NAME,'topic-link')):
    discussions[i].click()
    time.sleep(5)
    topic = driver.find_element(By.CLASS_NAME,'topic-content')
    if enrich_discussion(topic.text):
        print('----------------',i,'----------------')
        
        new_comment = generate_ai_news(topic.text)
        print(new_comment)
        uname = driver.find_element(By.CLASS_NAME, 'ql-editor')
        uname.send_keys(new_comment)
        uname = driver.find_element(By.CLASS_NAME, 'btn-articles')
        uname.click()
        time.sleep(10)
    uname = driver.find_element(By.CLASS_NAME,'button-back')
    uname.click()
    i+=1
    time.sleep(10)

df.to_csv(HASHED_FILE, index=False)
driver.close()