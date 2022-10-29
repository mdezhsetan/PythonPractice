from datetime import datetime

import pandas as pd


def current_time_string():
    now = datetime.now()
    return now.strftime("%Y%m%d_%H%M")


new_username = "test" + current_time_string() + "@qa.com"

data = {
    'username': [new_username],
    'password': ['welcome20!']
}

df = pd.DataFrame(data)
df.to_csv('test_accounts.csv', mode='a', index=False, header=False)
