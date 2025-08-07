import os
import re

import google
import json
import requests
import warnings
from datetime import timedelta, date, time, datetime
import pandas as pd
from google.cloud import bigquery
from numpy import float64
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import smtplib
import base64
import json
import os
from ast import literal_eval
from pandas.core.dtypes import dtypes
# import db-dtypes
import calendar

# import pyodbc
import pandas as pd
import requests
from Crypto.Cipher import AES
from google.cloud import bigquery
from google.oauth2 import service_account

# pd.set_option('All')
"""----Disable Warnings----"""
warnings.filterwarnings("ignore")
"""-------Connecting to BigQuery-------"""
BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
key = b'Qin$ight@Encrypt'
cwd = os.getcwd()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "{}\qinsights-809e5334043a.json".format(cwd)
Start_Date = "20240606"  # YYMMDD
End_date = "20240606"  # YYMMDD
email_date = datetime.strptime(Start_Date, "%Y%m%d").strftime("%m/%d/%Y")


def configpath():
    encryptedServiceAccount = '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'
    decryptContent = json.dumps(decrypt(encryptedServiceAccount))
    service_account_info = literal_eval(decryptContent.strip('"'))
    # print(service_account_info)
    credentials = service_account.Credentials.from_service_account_info(service_account_info)
    project_id = 'qinsights'
    client = bigquery.Client(credentials=credentials, project=project_id)
    return client


def decrypt(raw):
    encrypted = base64.b64decode(raw)
    IV = encrypted[:BLOCK_SIZE]
    aes = AES.new(key, AES.MODE_CBC, IV)
    decryptdata = unpad(aes.decrypt(encrypted[BLOCK_SIZE:]))
    return decryptdata.decode('utf8')


client = configpath()


def credential():
    query2 = """SELECT Username,Password FROM `qinsights.ma_test.Qinsight_HUB_Crdential`
    """
    client = configpath()
    job_config = bigquery.QueryJobConfig()
    job_config.use_query_cache = True
    result = client.query(query2, location="US", job_config=job_config).result()
    row = next(result)
    username = row['Username']
    password = row['Password']
    return username, password

username, password = credential()
def decrypt(raw):
    encrypted = base64.b64decode(raw)
    IV = encrypted[:BLOCK_SIZE]
    aes = AES.new(key, AES.MODE_CBC, IV)
    decrypted = unpad(aes.decrypt(encrypted[BLOCK_SIZE:]))
    return decrypted.decode('utf-8')  # Ensure correct decoding
password = decrypt(password)

try:
    c_date = date.today() - timedelta(days=1)
    y_date = str(c_date)
    n_date = c_date.strftime("%m/%d/%Y")
    print("This is ndate", n_date)
    d_date = y_date.replace('-', '')
    print("This is d_date", d_date)
    print("****************  Fetching HUB data for: " + str(n_date) + " ************************")

    data = {
        "username": username,
        "password": password
    }
except Exception as e:
    print(e)
try:
    r = requests.post("https://qore.myqone.com/auth/signin", json=data)
    LoginToken = r.json()
    print('yes')
    print(LoginToken)
    LoginToken1 = LoginToken['token']
    token1 = f'Bearer {LoginToken1}'
    jsondata = json.dumps(data)
    print(jsondata)
except Exception as e:
    print(e)
try:
    # url="https://qinsight.myqone.com/restservicehub/FilePayerDetailsByProcessDate"
    url_hub = "https://hub.myqone.com/editranslator/api/Files/GetMasterEraFiles?page=0&size=10000"
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_columns', 25)
    pd.set_option('display.max_rows', None)
    pd.set_option('max_colwidth', 1000)
    headers = {
        'Authorization': token1
    }
    # Jdata1 ={ "processdate":n_date,"bankEnv": "BANQ","clientid": "1"}
    # Jdata1 = {"startdate":"20240530","enddate":"20240530","clientid":1,"searchby":"Filename","searchtext":"","status":"3"}
    Jdata1 = {"startdate": Start_Date, "enddate": End_date, "clientid": 1, "searchby": "Filename", "searchtext": "",
              "status": "3"}
    # Jdata1 = {"startdate": '20240601', "enddate":'20240601' , "clientid": 1, "searchby": "Filename", "searchtext": "",
    #           "status": "3"}
    print(Jdata1)

    r1 = requests.post(url_hub, headers=headers, verify=False, json=Jdata1)
    r1 = json.loads(r1.text)
    df = pd.DataFrame(r1["content"])
    # print(df)
except Exception as e:
    print(e)
hubdict = {}
bqdict = {}
filename_list = []
checkno_list = []
hubpaid = []
bqpaid = []
statuslist = []
hubplbdict = []


def unmapped_claim():
    # global count
    print("inside unmapped_claim")
    # unmapped_df = pd.DataFrame()
    # for index,row in df.iterrows():
    file_id = str(tuple(df['nmastererafileid'].values)).replace(",)", ")")

    print(file_id)
    # hub_Unmatched_PLB_count=row["unmatchedplbcount"]
    job_config = bigquery.QueryJobConfig()
    job_config.use_query_cache = True

    query1 = """select
            fileid ,filename ,
            count
            (claimno)Qinsight_unmapped_claim_cnt
            from
             BANQ.SubModel_erain_claims
            where
            subclientid
            is
            null
            and
            cast (fileid as string) in
            """ + file_id + """
            group
            by
            fileid ,filename """
    # print(query1)
    unmapped_df = client.query(query1, location="US", job_config=job_config).to_dataframe()
    unmapped_df.sort_values(by=["filename", "fileid"])
    # print(df1)

    # unmapped_df=unmapped_df.append(df1)

    # print("unmapped_df",unmapped_df)
    df2_data = {
        "file_id": [],
        "filename": [],
        "hub_unmapped_claim_count": []
    }

    for index, row in df.iterrows():
        file_id = row["nmastererafileid"]
        filename = row["sfilename"]
        hub_unmapped_claim_count = row["unmatchedclaimcount"]
        hub_unmapped_plb_count = row["unmatchedplbcount"]
        df2_data["file_id"].append(file_id)
        df2_data["filename"].append(filename)
        df2_data["hub_unmapped_claim_count"].append(hub_unmapped_claim_count)
    df2 = pd.DataFrame(df2_data)
    df2 = df2.sort_values(by=["filename", "file_id"])

    # print(df2)
    # print(type(df2["file_id"]))
    # print(type(unmapped_df["fileid"]))
    df_merged = pd.merge(unmapped_df, df2, left_on="filename", right_on="filename")
    # print(df_merged)
    for index, row in df_merged.iterrows():
        Qinsight_unmapped_claim_cnt = row["Qinsight_unmapped_claim_cnt"]  # Assuming this is a single value, not a list
        hub_unmapped_claim_count = row["hub_unmapped_claim_count"]  # Assuming this is a single value, not a list
        if int(Qinsight_unmapped_claim_cnt) == int(hub_unmapped_claim_count):
            df_merged.at[index, "Difference"] = "Matched"
        else:
            df_merged.at[index, "Difference"] = "Unmatched"
    print("unmapped claim", df_merged)
    df_merged.to_csv("UnMapped_Claim.csv")


unmapped_claim()


def unmapped_plb():
    # global count
    print("inside unmapped_plb")
    # unmapped_df = pd.DataFrame()
    # for index,row in df.iterrows():
    file_id = str(tuple(df['nmastererafileid'].values)).replace(",)", ")")

    print(file_id)
    # hub_Unmatched_PLB_count=row["unmatchedplbcount"]
    job_config = bigquery.QueryJobConfig()
    job_config.use_query_cache = True

    query_plb = """
     SELECT  fileid , filename , count(c042id)Qinsight_unmapped_plb_cnt

FROM `BANQ.SubModel_erain_plb`

        where                
       cast(Fileid as string) in  """ + file_id + """

        and subclientname = 'Unmatch PLB' and CheckNumber != ''
        group by fileid , filename
     """
    # print(query1)
    unmapped_plb_df = client.query(query_plb, location="US", job_config=job_config).to_dataframe()
    unmapped_plb_df.sort_values(by=["filename", "fileid"])
    # print(df1)

    # unmapped_df=unmapped_df.append(df1)

    # print("unmapped_plb_df",unmapped_plb_df)
    df3_data = {
        "file_id": [],
        "filename": [],
        "hub_unmapped_plb_count": []
    }

    for index, row in df.iterrows():
        file_id = row["nmastererafileid"]
        filename = row["sfilename"]

        hub_unmapped_plb_count = row["unmatchedplbcount"]
        df3_data["file_id"].append(file_id)
        df3_data["filename"].append(filename)
        df3_data["hub_unmapped_plb_count"].append(hub_unmapped_plb_count)
    df3 = pd.DataFrame(df3_data)
    df3 = df3.sort_values(by=["filename", "file_id"])

    # print(df2)
    # print(type(df2["file_id"]))
    # print(type(unmapped_df["fileid"]))
    df_merged = pd.merge(unmapped_plb_df, df3, left_on="filename", right_on="filename")
    # print(df_merged)
    for index, row in df_merged.iterrows():
        Qinsight_unmapped_plb_cnt = row["Qinsight_unmapped_plb_cnt"]  # Assuming this is a single value, not a list
        hub_unmapped_plb_count = row["hub_unmapped_plb_count"]  # Assuming this is a single value, not a list
        if int(Qinsight_unmapped_plb_cnt) == int(hub_unmapped_plb_count):
            df_merged.at[index, "Difference"] = "Matched"
        else:
            df_merged.at[index, "Difference"] = "Unmatched"
    print(df_merged)
    df_merged.to_csv("UnMapped_PLB.csv")


unmapped_plb()


def email():
    fromaddr = "noreply@triarqhealth.com"
    toaddr = "nikita.dighe@triarqhealth.com;sachin.sanap@triarqhealth.com;rohini.wadekar@triarqhealth.com;sheetal.ghuge@triarqhealth.com"
    tocc = ""
    rcpt = fromaddr.split(";") + toaddr.split(";") + tocc.split(";")
    # instance of MIMEMultipart
    msg = MIMEMultipart()
    # storing the senders email address
    msg['From'] = fromaddr
    # storing the receivers email address
    msg['To'] = toaddr
    # storing the subject
    msg['Subject'] = f"""Unmapped Claims and UnmappedPLB for  {email_date}"""  # +y_date
    # string to store the body of the mail
    body = f"""Hi,
              Please find attached the Unmapped Claims and UnmapppedPLB file for {email_date}  """  # +y_date
    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
    # open the file to be sent
    filename1 = "UnMapped_claim.csv"
    filename2 = "UnMapped_PLB.csv"
    attachment1 = open("UnMapped_Claim.csv", "rb")
    attachment2 = open("UnMapped_PLB.csv", "rb")
    # instance of MIMEBase and named as p
    p1 = MIMEBase('application', 'octet-stream')
    p2 = MIMEBase('application', 'octet-stream')
    # To change the payload into encoded form
    p1.set_payload((attachment1).read())
    p2.set_payload((attachment2).read())
    # encode into base64
    encoders.encode_base64(p1)
    encoders.encode_base64(p2)
    p1.add_header('Content-Disposition', "attachment1; filename= %s" % filename1)
    p2.add_header('Content-Disposition', "attachment2; filename= %s" % filename2)
    # attach the instance 'p' to instance 'msg'
    msg.attach(p1)
    msg.attach(p2)
    # creates SMTP session
    s = smtplib.SMTP('smtp.office365.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login(fromaddr, "RWv~rq;hzC3b=Xtp")
    # Converts the Multipart msg into a string
    text = msg.as_string()
    # sending the mail
    s.sendmail(fromaddr, rcpt, text)
    # terminating the session
    s.quit()


email()
