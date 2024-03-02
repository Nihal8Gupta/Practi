import requests,json,pandas as pd

# Get the id of your facbook page
# https://www.facebook.com/profile.php?id=61556830713788   - it is page url

page_id = "61556830713788"

# Get the post id of your page

post_id = '122101981556227690'

# Graph API
# It is way of intracting with facebook in any language
access_token = ''

url =f'https://graph.facebook.com/v19.0/{page_id}_{post_id}/comments?access_token={access_token}'

response = requests.request('GET',url)

#save name , message in excel file
data = json.loads(response.text)

#create object with only name , time , message

def get_comment(comment):
    return {
        'name' : comment['from']['name'],
        'time' : comment['created_time'],
        'message' : comment['message'],

    }

excel_data = list(map(get_comment,data['data']))
df = pd.DataFrame(excel_data)
df.to_excel('comments.xlsx',index=False)