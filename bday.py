import pandas as pd
import datetime
# import smtplib

# GMAIL_ID = ''
# GAMIL_PSWD = ''

def sendEmails(to, sub, msg):
    print(f"Email to {to} sent with subject '{sub}' & message '{msg}'")
    # s = smtplib.SMTP('smtp.gmail.com', 587)
    # s.starttls()
    # s.login(GMAIL_ID, GAMIL_PSWD)
    # s.sendmail(GMAIL_ID, to, f"Subject: {sub}\n\n{msg}")
    # s.quit()
    # Turn on less secure apps in gmail to send from here

if __name__ == "__main__":
    df = pd.read_excel("data.xlsx")
    today = datetime.datetime.now().strftime("%d-%m")
    thisYear = datetime.datetime.now().strftime("%Y")
    writeInd = []
    for index, item in df.iterrows():
        bday = item['Birthday'].strftime("%d-%m")
        # print(bday)
        if (today == bday) and thisYear not in str(item['Year']):
            sendEmails(item['Email'], "Happy Birthday", item['Dialogue'])
            writeInd.append(index)
    for i in writeInd:
        yr = df.loc[i, 'Year']
        df.loc[i, 'Year'] = str(yr) + ',' + str(thisYear)
        print(df.loc[i, 'Year'])
    
    df.to_excel('data.xlsx', index = False)