import requests
import pandas as pd

headers = {
    'authority': 'www.behance.net',
    'accept': '*/*',
    'x-bcp': '0e94cad1-98bc-4948-9193-434abe97f815',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'sec-gpc': '1',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.behance.net/search/projects?field=architecture',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'gk_suid=29269953; gki=%7B%22feature_stock_rail%22%3Afalse%7D; bcp=0e94cad1-98bc-4948-9193-434abe97f815; AMCVS_9E1005A551ED61CA0A490D45%40AdobeOrg=1; gpv=behance.net:search:projects; s_cc=true; OptanonConsent=isIABGlobal=false&datestamp=Fri+Jan+21+2022+18%3A50%3A24+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.9.0&hosts=&consentId=d0a29a75-eba3-4af9-93aa-6089e0c21cec&interactionCount=0&landingPath=https%3A%2F%2Fwww.behance.net%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1; feds_privacy_consent={"hasUserProvidedConsent":true,"userHasCustomConsent":false}; s_sq=%5B%5BB%5D%5D; sign_up_prompt=true; AMCV_9E1005A551ED61CA0A490D45%40AdobeOrg=870038026%7CMCMID%7C56586488518047349773733653051510070332%7CMCAID%7CNONE%7CMCOPTOUT-1642787470s%7CNONE%7CvVersion%7C5.0.0',
}

params = (
    ('content', 'projects'),
    ('field', 'architecture'),
    ('ordinal', '0'),
)

response = requests.get('https://www.behance.net/search', headers=headers, params=params)

# Create Json Object
results_json = response.json()

# result items (total: 48)
result_items = results_json['search']['content']['projects']

# Put everything together - Loop through results and append data inside a list

name = []
first_name = []
last_name = []
username = []
country = []
views = []
appreciations = []
comments = []
url = []

for result in result_items:
    # name
    name.append(result['name'])
    
    # first name
    first_name.append(result['owners'][0]['first_name'])
    
    # last name
    last_name.append(result['owners'][0]['last_name'])
    
    # username
    username.append(result['owners'][0]['username'])
    
    # country
    country.append(result['owners'][0]['country'])
    
    # views
    views.append(result['owners'][0]['stats']['views'])
    
    # appreciations
    appreciations.append(result['owners'][0]['stats']['appreciations'])
    
    # comments
    comments.append(result['owners'][0]['stats']['comments'])
    
    # url
    url.append(result['owners'][0]['url'])

# Pandas Dataframe - Single Page
df = pd.DataFrame({'name': name, 'first name': first_name, 'last name': last_name,
                   'username': username, 'country': country, 'views': views,
                   'appreciations': appreciations, 'comments': comments, 'url': url})

# Scraping Multiple Pages
headers = {
    'authority': 'www.behance.net',
    'accept': '*/*',
    'x-bcp': '0e94cad1-98bc-4948-9193-434abe97f815',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'sec-gpc': '1',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.behance.net/search/projects?field=architecture',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'gk_suid=29269953; gki=%7B%22feature_stock_rail%22%3Afalse%7D; bcp=0e94cad1-98bc-4948-9193-434abe97f815; AMCVS_9E1005A551ED61CA0A490D45%40AdobeOrg=1; gpv=behance.net:search:projects; s_cc=true; OptanonConsent=isIABGlobal=false&datestamp=Fri+Jan+21+2022+18%3A50%3A24+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.9.0&hosts=&consentId=d0a29a75-eba3-4af9-93aa-6089e0c21cec&interactionCount=0&landingPath=https%3A%2F%2Fwww.behance.net%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1; feds_privacy_consent={"hasUserProvidedConsent":true,"userHasCustomConsent":false}; s_sq=%5B%5BB%5D%5D; sign_up_prompt=true; AMCV_9E1005A551ED61CA0A490D45%40AdobeOrg=870038026%7CMCMID%7C56586488518047349773733653051510070332%7CMCAID%7CNONE%7CMCOPTOUT-1642787470s%7CNONE%7CvVersion%7C5.0.0',
}

name = []
first_name = []
last_name = []
username = []
country = []
views = []
appreciations = []
comments = []
url = []

# scrape 10 pages

for i in range(0, 480, 48):
    params = (
        ('content', 'projects'),
        ('field', 'architecture'),
        ('ordinal', str(i)),
    )

    # response variable for the get request
    response = requests.get('https://www.behance.net/search', headers=headers, params=params)

    # json object
    results_json = response.json()

    # list of results
    result_items = results_json['search']['content']['projects']

    for result in result_items:
        # name
        name.append(result['name'])
        
        # first name
        first_name.append(result['owners'][0]['first_name'])
        
        # last name
        last_name.append(result['owners'][0]['last_name'])
        
        # username
        username.append(result['owners'][0]['username'])
        
        # country
        country.append(result['owners'][0]['country'])
        
        # views
        views.append(result['owners'][0]['stats']['views'])
        
        # appreciations
        appreciations.append(result['owners'][0]['stats']['appreciations'])
        
        # comments
        comments.append(result['owners'][0]['stats']['comments'])
        
        # url
        url.append(result['owners'][0]['url'])

df = pd.DataFrame({'name': name, 'first name': first_name, 'last name': last_name,
                   'username': username, 'country': country, 'views': views,
                   'appreciations': appreciations, 'comments': comments, 'url': url})

# Store Results in Excel 
df.to_excel('pictures_multiple_pages.xlsx', engine='xlsxwriter', index=False)

