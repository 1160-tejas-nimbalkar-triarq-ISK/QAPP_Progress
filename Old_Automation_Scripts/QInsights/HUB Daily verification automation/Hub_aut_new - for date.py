import traceback

import datetime as datetime
import google.oauth2
import pandas as pd
import requests
import json
import numpy as np
from datetime import datetime, timedelta, date
import smtplib, ssl
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import os
from email.message import EmailMessage
from email import encoders
from datetime import timedelta, date, time, datetime
from google.cloud import bigquery
from ast import literal_eval
from google.oauth2 import service_account
import base64
from concurrent import futures

# from Crypto import Randomm
from Crypto.Cipher import AES


current_date= date.today()
y_date=current_date-timedelta(days=1)
Start_Date=datetime.strftime(y_date,"%Y%m%d")#"20240613"
End_date=datetime.strftime(y_date,"%Y%m%d")

Email_date=datetime.strptime(Start_Date, "%Y%m%d").strftime("%m/%d/%Y")

Query_date=datetime.strptime(Start_Date, "%Y%m%d").strftime("%Y-%m-%d")




import logging
logging.basicConfig(filename="logs.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')

logger = logging.getLogger()
logger.setLevel(logging.INFO)
y_date = date.today()- timedelta(days = 1)#Yesterdays date in YYYY-MM-DD
y_date_int = y_date.strftime("%Y%m%d")#Yesterdays date in YYYYMMDD
y_date_slash = y_date.strftime("%m/%d/%Y")#Yesterdays date in MMDDYYYY
BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
key = b'Qin$ight@Encrypt'
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


############################ Comparing amount between Qinsight and HUB   ###########################

#download report from Qinsight HUb-file distribution
query_string = r"""
              SELECT
  DISTINCT checkdata.importdate,
  checkdata.filename,
  checkdata.fileid,
  checkdata.fileshareid,
  CONCAT(EFTMonth,'-',EFTYear) AS EFTMonthYear,
  checkdata.payername,
  checkdata.plancode AS payerid,
  checkdata.paymentmethodcode AS payment_method,
  CASE
    WHEN SUM(checkdata.TotalPaid) = 0 AND SUM(SubModel_erain_plb.PLBamount) =0 THEN 0
  ELSE
  ROUND(SUM(checkdata.TotalPaid - ROUND(CAST(IFNULL(SubModel_erain_plb.PLBamount,0) AS float64),2)),2)
END
  AS check_amount,
  SUM(chk.checkamount)checkamount,
  ROUND(SUM(TotalPaid),2) AS TotalPaid
FROM (
  SELECT
    SubModel_erain_claims.clientid,
    clientname,
    fileshareid,
    FORMAT_DATE("%m/%d/%Y",CAST(cast(CAST(SubModel_erain_claims.importdate AS date) AS String) AS date)) AS importdate,
    CAST(SubModel_erain_claims.fileid AS string) AS fileid,
    SubModel_erain_claims.filename,
    FORMAT_DATE("%m/%d/%Y", CAST(FORMAT_DATE("%F",PARSE_DATE('%Y%m%d', CAST(checkdate AS STRING))) AS date)) AS checkdate,
    CAST(FORMAT_DATE("%F",PARSE_DATE('%Y%m%d', CAST(EFTEffectiveDate AS STRING))) AS date)AS EFTEffectiveDate,
    FORMAT_DATE("%B",PARSE_DATE('%Y%m%d', CAST(EFTEffectiveDate AS STRING)))AS EFTMonth,
    FORMAT_DATE("%Y",PARSE_DATE('%Y%m%d', CAST(EFTEffectiveDate AS STRING)))AS EFTyear,
    CAST(SubModel_erain_claims.checknumber AS string) AS checknumber,
    ROUND(SUM(IFNULL(SubModel_erain_claims.claimpaidamount,0)),2) AS TotalPaid,
    SubModel_erain_claims.payername,
    SubModel_erain_claims.payeridentificationcode,
    SubModel_erain_claims.plancode,
    SubModel_erain_claims.paymentmethodcode,
    SubModel_erain_claims.paymentmethoddesc
  FROM (
    SELECT
      DISTINCT clientid,
      clientname,
      fileid,
      COUNT(DISTINCT renderingid) AS Providercount,
      ROUND(SUM(CAST(claimpaidamount AS NUMERIC)),2) AS claimpaidamount,
      subclientid,
      subclientname,
      subclientdivisioncode,
      COUNT(DISTINCT claimno) AS claimcount,
      fileshareid,
      COUNT(DISTINCT subclientid) AS divisioncount,
      checknumber,
      payername,
      payeridentificationcode,
      plancode,
      paymentmethodcode,
      paymentmethoddesc,
      importdate,
      filename,
      checkamount,
      EFTEffectiveDate,
      checkdate,
      subclientcode
    FROM (
      SELECT
        clientid,
        clientname,
        subclientid,
        subclientname,
        subclientdivisioncode,
        claimpaidamount,
        claimno,
        checknumber,
        fileshareid,
        fileid,
        renderingid,
        payername,
        payeridentificationcode,
        plancode,
        paymentmethodcode,
        paymentmethoddesc,
        CheckIssueorEFTEffectiveDate_16 AS EFTEffectiveDate,
        checkdate,
        subclientcode,
        importdate,
        filename,
        checkamount
      FROM
        BANQ.SubModel_erain_claims
      WHERE
        statusid = 1
      ORDER BY
        subclientname )
    GROUP BY
      clientid,
      fileid,
      checknumber,
      subclientid,
      subclientname,
      subclientdivisioncode,
      fileshareid,
      payername,
      payeridentificationcode,
      plancode,
      paymentmethodcode,
      paymentmethoddesc,
      importdate,
      filename,
      checkamount,
      subclientcode,
      EFTEffectiveDate,
      checkdate,
      clientname )SubModel_erain_claims
  LEFT OUTER JOIN (
    SELECT
      DISTINCT fileid,
      subclientname,
      SUM(CAST (amount AS FLOAT64))AS adjustment
    FROM
      BANQ.SubModel_erain_claimadjustment
    WHERE
      statusid = 1
    GROUP BY
      fileid,
      subclientname )SubModel_erain_claimadjustment
  ON
    SubModel_erain_claimadjustment.fileid = SubModel_erain_claims.fileid
    AND SubModel_erain_claimadjustment.subclientname = SubModel_erain_claims.subclientname
  WHERE
    CAST(SubModel_erain_claims.importdate AS date) = '"""+Query_date+"""'
    AND clientid = 1
  GROUP BY
    SubModel_erain_claims.clientid,
    clientname,
    SubModel_erain_claims.importdate,
    SubModel_erain_claims.fileid,
    fileshareid,
    SubModel_erain_claims.filename,
    checkdate,
    EFTEffectiveDate,
    checknumber,
    SubModel_erain_claims.payername,
    payeridentificationcode,
    plancode,
    SubModel_erain_claims.paymentmethodcode,
    SubModel_erain_claims.paymentmethoddesc,
    EFTMonth,
    EFTyear )checkdata
LEFT OUTER JOIN (
  SELECT
    SUM(checkamount)checkamount,
    fileid,
    checknumber
  FROM
    BANQ.SubModel_erain_check
  GROUP BY
    fileid,
    checknumber )chk
ON
  chk.fileid=CAST(checkdata.fileid AS int64)
  AND chk.checknumber=checkdata.checknumber
LEFT OUTER JOIN (
  SELECT
    DISTINCT fileid,
    fileshareid,
    Filename,
    checknumber,
    SUM(CAST(PLBAmount AS FLOAT64)) AS PLBamount
  FROM
    BANQ.SubModel_erain_plb
  WHERE
    status = 1
  GROUP BY
    fileid,
    Filename,
    checknumber,
    fileshareid )SubModel_erain_plb
ON
  SubModel_erain_plb.fileid = CAST(checkdata.fileid AS INT64)
  AND SubModel_erain_plb.fileshareid = checkdata.fileshareid
  AND SubModel_erain_plb.checknumber = checkdata.checknumber
WHERE
  EFTMonth IS NOT NULL
  AND EFTYear IS NOT NULL
GROUP BY
  fileid,
  filename,
  importdate,
  EFTMonthYear,
  payername,
  payerid,
  payment_method,
  fileshareid
ORDER BY
  importdate ASC,
  EFTMonthYear ASC,
  fileid ASC,
  payerid asc
            """

# query for user name and password



def QInsight_HUB(query_string):
    """
    :return: dataframe obtained from Bigquery for given SQL query
    :rtype: dataframe
    """

    client=configpath()
    job_config = bigquery.QueryJobConfig()
    job_config.use_query_cache = True
    query_job = client.query(query_string, location="US", job_config=job_config)
    # credentials, project_id = google.auth.default(
    #     scopes=["https://www.googleapis.com/auth/cloud-platform"]
    # )
    # # bqclient = bigquery.Client(project="qinsights")
    # # bqstorageclient = bigquery_storage.BigQueryReadClient(credentials=credentials)
    #
    # project_id = 'qinsights'
    # client = bigquery.Client(credentials=credentials, project=project_id)
    # # client = bigquery.Client(project=project_id)
    #
    dataframe = query_job.to_dataframe()
    return dataframe

df1= QInsight_HUB(query_string)
df1["TotalPaid"]=abs(df1["TotalPaid"].astype(np.float64))
# print("df1",df1)
pd.set_option('display.max_columns', 1000)
# print(df1.filename=="P77910D0H60216 G9999DU134.RMT")
df3 = (df1.groupby(["filename"], as_index=False).sum())
pd.set_option('display.max_columns', 1000)
# print("This is df3",df3.head(3))
Qinight_file_count=df1["filename"].nunique()
# print(Qinight_file_count)
# print("This is df3",df3)
#for checking the missing payer in QInsightr
Empty_payer_name=[]
for i, row in df1.iterrows():
    payer_name=row["payername"]
    file_name=row["filename"]
    if len(payer_name)==0:
        Empty_payer_name.append(file_name)




def credential():
    query2="""SELECT Username,Password FROM `qinsights.ma_test.Qinsight_HUB_Crdential`
    """
    client=configpath()
    job_config = bigquery.QueryJobConfig()
    job_config.use_query_cache = True
    result = client.query(query2, location="US", job_config=job_config).result()
    row=next(result)
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
# Download report from HUB
url ="https://qore.myqone.com/auth/signin"
url_hub= "https://hub.myqone.com/editranslator/api/Reports/getFileSummary?pagesize=3000&pagenumber=0"
def logintoken(url, username, password):
    try:
        data = {
            "username": username,
            "password": password
        }
        r = requests.post(url, json=data)
        LoginToken = r.json()
        # print('yes')
        # print(LoginToken)
        LoginToken1 = LoginToken['token']
        token1 = f'Bearer {LoginToken1}'
        # token1="Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MTY4OTc4MDgsImV4cCI6MTcxOTQ4OTgwOCwiaXNzIjoiY2xvdWQtZW5kcG9pbnRzLXFhQHFwYXRod2F5cy1xYS5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsImF1ZCI6Imh0dHBzOi8vcW9yZS1xYS5teXFvbmUuY29tIiwic3ViIjoiY2xvdWQtZW5kcG9pbnRzLXFhQHFwYXRod2F5cy1xYS5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsImVtYWlsIjoidGVqcGFsLmJhbnNvZGVAdHJpYXJxaGVhbHRoLmNvbSIsInVzZXJpZCI6IjlhNTg5YmVhLTM2ZWQtMTFlYy05MzA5LWFkNjYyMjE1NmQ2MCIsImZpcnN0bmFtZSI6IlRlanBhbCIsImxhc3RuYW1lIjoiQmFuc29kZSJ9.FC2Y5ACZF4RCsbpiAMeKypxXrvGSEHdnaBINNT7UG5h8UtfEVAzX9vbm1aou0aIJJ8QZ8RwBIVvC1nFFZ3k-_AF2mVgTz0YLcQMXiIUo9hd0tWu3dhiczVZWK9Vyw1gA1-Dym_l4sovoOKI99yHRkE2AxLWSloxoshpS8WHQoUsFGI3VB6hC9n7urKvDrGmOgb0VwnwpRKsvkiNu9FQRUfdtMN6dKl24zBKJ9c5VrINfgn3-GnqS25uq_KL8LWclRMrAEok7J1azvXx4aPUWyuGW1JerTK0JOIDn3zw1Bq95Q5k8x4v_amTw4OaKlrq_QcRhJVBsowxda6oiJKMXZw"
        headers = {
            'Authorization': token1
        }
        return {'status': 'success', 'message': headers}
    except Exception as e:
        print(e)
        return {'status': 'error', 'message': e}

headers = logintoken(url, username, password)['message']
# Jdata = {"nmastererafileid":"0","splitfileflag":False,"dtstartdate":"20240307","dtenddate":"20240307","nclientid":1,"searchby":"Filename","searchtext":"","nsubclientid":"0","status":"3","userid":"0","divisioncode":""}
Jdata={"nmastererafileid":"0","splitfileflag":False,"dtstartdate":Start_Date,"dtenddate":End_date,"nclientid":1,"searchby":"Filename","searchtext":"","nsubclientid":"0","status":"3","userid":"0","divisioncode":""}
# Jdata = {"nmastererafileid":"0","splitfileflag":False,"dtstartdate":y_date_int,"dtenddate":y_date_int,"nclientid":1,"searchby":"Filename","searchtext":"","nsubclientid":"0","status":"3","userid":"0","divisioncode":""}
pd.set_option('display.max_columns', None)
print(Jdata)
try:
    StopStatus = requests.post(url_hub, headers=headers, verify=False, json=Jdata)
    StopStatus = json.loads(StopStatus.text)
    #print(StopStatus)

except Exception as e:
    print(e)

    StopStatus = None

if StopStatus is not None:
    df = pd.DataFrame(StopStatus['content'])
    # df2 = df.sort_values(by=["filename"]).reset_index(drop=True)
    # df2["totalcheckamount"]= df2["totalcheckamount"].str.replace("$","")
    # df2["totalcheckamount"] = df2["totalcheckamount"].str.replace(",", "")
    # df2["totalcheckamount"]= df2["totalcheckamount"].str.replace('%',"").astype(np.float64)
# print("This is df",df)
HUB_File_count=df["filename"].nunique()
# print("This is df2",df)
# print("This id df",df)
# print(df.columns)
try:

    checks=[]
    row_number=0
    for i,row in df.iterrows():
        file_id=row["fileid"]
        filename=row["filename"]
        # print(file_id)
        url= "https://qore.myqone.com/auth/signin"
        url_check ="https://hub.myqone.com/editranslator/api/Reports/getCheckSummary?pagesize=3000&pagenumber=0"
        # cors(app)

        # Jdata = {"nmastererafileid":"0","splitfileflag":False,"dtstartdate":"20240307","dtenddate":"20240307","nclientid":1,"searchby":"Filename","searchtext":"","nsubclientid":"0","status":"3","userid":"0","divisioncode":""}
        Jdata = {"nmastererafileid":file_id,"v_ts835id":"0","splitfileflag":False,"splitid":"0","searchby":"Check","searchtext":""}
        # print("This is json",Jdata)
        # Jdata = {"nmastererafileid":"0","splitfileflag":False,"dtstartdate":y_date_int,"dtenddate":y_date_int,"nclientid":1,"searchby":"Filename","searchtext":"","nsubclientid":"0","status":"3","userid":"0","divisioncode":""}
        pd.set_option('display.max_columns', None)
        try:
            row_number=row_number+1
            print("File_number",row_number)
            print(filename)
            StopStatus = requests.post(url_check, headers=headers, verify=False, json=Jdata)
            StopStatus = json.loads(StopStatus.text)
            # print(StopStatus)

        except Exception as e:
            print(e)

            StopStatus = None

        if StopStatus is not None:
            df2 = pd.DataFrame(StopStatus['content'])
            # print("this is df 2",df2)
            # HUB_check_amt+=df2["totalpayment"].replace("$","").astype(float)
            # # HUB_check_amt=df2["totalpayment"].sum()
            # print("HUB_check_amt",HUB_check_amt)
            df2['totalpayment'] = pd.to_numeric(df2['totalpayment'].replace('[^\d.]', '', regex=True))

            # Now, you can calculate the sum of the numeric column
            HUB_check_amt = df2['totalpayment'].sum()
            # print("HUB_check_amt",HUB_check_amt)
            # HUB_check_amt=HUB_check_amt.replace("$","")
            # HUB_check_amt = df2["totalpayment"].astype(str).str.replace('$', '')
            # print(type(HUB_check_amt))
            # HUB_total_paid+=df2["totalpaidamt"].replace("$","").astype(float)
            # HUB_total_paid=df2["totalpaidamt"].sum()
            df2['totalpaidamt'] = pd.to_numeric(df2['totalpaidamt'].replace('[^\d.]', '', regex=True))
            HUB_total_paid = df2['totalpaidamt'].sum()
            # HUB_total_paid=HUB_total_paid.replace("$","")
            # HUB_total_paid = df2["totalpaidamt"].astype(str).str.replace('$', '')
            # print("HUB_total_paid",HUB_total_paid)
            # Payer_name=df2["payername"]
            # print(Payer_name)
            # checks={"File_Name":file_name,"HUB_check_amt":HUB_check_amt,"HUB_total_paid":HUB_total_paid}
            # print(df2["totalpaidamt"])
            checks.append({
                "filename": filename,

                "HUB_check_amt": abs(HUB_check_amt),  # Convert to list if needed
                "HUB_total_paid": abs(HUB_total_paid)  # Convert to list if needed

            })
            # print(df2["totalpayment"])
    # print(HUB_File_count)
    # Comparing two excels
    # df4 = pd.merge(df2, df3, left_on="filename", right_on="filename")
    # print("This is checks ",checks)
    df4=pd.DataFrame(checks)
    print("this is df4 before changes ",df4)
    df4 = df4.sort_values(by=["filename"]).reset_index(drop=True)
    print("this sorted df4",df4)
    # df4["HUB_check_amt"]= df4["HUB_check_amt"].str.replace("$","",)
    # df4["HUB_check_amt"] = df4["HUB_check_amt"].str.replace(",", "")
    # # df4["HUB_total_paid"] = df4["HUB_total_paid"].str.replace("$", "", )
    # df4["HUB_total_paid"] = df4["HUB_total_paid"].str.replace(",", "")
    df4 = (df4.groupby(["filename"], as_index=False).sum())

    # df4_new["HUB_check_amt"]= df4["HUB_check_amt"].str.replace('%',"").astype(np.float64)
    # print(df4_new.columns)
    print("this is df4 after changes ",df4)
except Exception as e:
    print(traceback.print_exc())
df_merged=pd.merge(df4, df3, left_on="filename", right_on="filename")
print("DF merged",df_merged)

file_name=[]
payer_name=[]
check_amount_diff1=[]
Totalpaid_amt_diff1=[]
for i,row in df_merged.iterrows():

    filename = row["filename"]
    # payername=row["payername"]
    HUB_check_amt=row['HUB_check_amt']
    HUB_total_paid=row["HUB_total_paid"]
    Qinsight_check_amt=row["check_amount"]
    Qinsight_totalpaid_amt=row["TotalPaid"]
    # print("HUB_check_amt",HUB_check_amt)
    # print("Qinsight_check_amt",Qinsight_check_amt)

    check_amount_diff = round(float(HUB_check_amt),2)- round(float(Qinsight_check_amt),2)
    # check_amount_diff = HUB_check_amt -Qinsight_check_amt
    Totalpaid_amt_diff = round(float(HUB_total_paid),2) - round(float(Qinsight_totalpaid_amt),2)
    # Totalpaid_amt_diff = HUB_total_paid - Qinsight_totalpaid_amt


    file_name.append(filename)
    check_amount_diff1.append(check_amount_diff)
    Totalpaid_amt_diff1.append(Totalpaid_amt_diff)
    # payer_name.append(payername)

df_final= {"Filename":file_name, "Difference for Check Amount":check_amount_diff1,"Difference for Total Paid":Totalpaid_amt_diff1}

df_final1= pd.DataFrame.from_dict(df_final)
# print(df_final1)

df_final1.to_csv("HUB Mismatch.csv",index=False)



###########################    Testing of file opening issue    ####################################
# Dowloading all file data
# url ="https://qore.myqone.com/auth/signin"
# url_hub= "https://qinsight.myqone.com/restservice/FilePayerDetailsByProcessDate"

# def logintoken(url, username, password):
#     try:
#         data = {
#             "username": username,
#             "password": password
#         }
#         r = requests.post(url, json=data)
#         LoginToken = r.json()
#         # print('yes')
#         print(LoginToken)
#         LoginToken1 = LoginToken['token']
#         token1 = f'Bearer {LoginToken1}'
#         headers = {
#             'Authorization': token1
#         }
#         return {'status': 'success', 'message': headers}
#     except Exception as e:
#         print(e)
#         return {'status': 'error', 'message': e}
#
# headers = logintoken(url, username, password)['message']
# Jdata ={ "processdate":"03/19/2024" ,"bankEnv": "BANQ","clientid": "1"}
# # Jdata ={ "processdate":y_date_slash ,"bankEnv": "BANQ","clientid": "1"}
# r = requests.post(url_hub, headers=headers, verify=False, json=Jdata)
# r = json.loads(r.text)
#
# df = pd.DataFrame(r)
# print(df)
# pd.options.display.max_columns = None
# df['payername']
# #print('#################')
# #print(r)
# # print(df)
#
# # Creating URl from files data and sending get request
# for index, row in df.iterrows():
#     row["payername"]=row["payername"].replace(' ', '%')
#     df.loc[index,"payername"]=row["payername"]
# print("This id df")
# print(df)
#
# dict = {}
# filename_list = []
# payername_list = []
# status_list = []
# for index, row in df.iterrows():
#     # print(row['filename'],row['payername'])
#     url='https://qinsight.myqone.com/restservice/FileDistributionmailservice'
#     # url = 'https://qinsight.myqone.com/restservice/FileDistributionmailservice/BANQ/{}/338877/{}/{}/{}/{}'.format(row['fileid'], row['payment_method'], row['payerid'], row['EFTMonthYear'], row['payername'])
#     Jdata={"getbankEnv":"BANQ","getfileid":row['fileid'],"randomno":936653,"paymenttype":row['payment_method'],"payerid":row['payerid'],"EFTMonthYear":row['EFTMonthYear'],"payername":row['payername']}
#
#
#     # print(Jdata)
#     # print(url)
#     # "''' + operationtype + '''",
#     x = requests.post(url, headers=headers, verify=False,json=Jdata)
#     #print(x.status_code)
#     y = x.status_code
#     # print(y)
#     filename_list.append(row['filename'])
#     payername_list.append(row['payername'])
#     status_list.append(y)
#     #print(status_list)
# dict = {
#     "filename": filename_list,
#     "payername": payername_list,
#     "Status": status_list
# }
#
# df1 = pd.DataFrame(dict)
# df1.to_csv("Hub File Opening Issue.csv",index=False)


# sending mail
# TodaysDate = time.strftime("%b %d,%Y")
def email():
    fromaddr = "noreply@triarqhealth.com"
    # toaddr="jagdish.bagul@triarqhealth.com;sachin.sanap@triarqhealth.com"
    # nikita.dighe@triarqhealth.com;"
    toaddr = "jagdish.bagul@triarqhealth.com;nikita.dighe@triarqhealth.com;namrata.borkar@triarqhealth.com;sachin.sanap@triarqhealth.com;dhananjay.wagh@triarqhealth.com;namrata.borkar@triarqhealth.com"
    tocc=""
    rcpt = fromaddr.split(";") + toaddr.split(";") +tocc.split(";")
    #instance of MIMEMultipart
    msg = MIMEMultipart()
    # storing the senders email address
    msg['From'] = fromaddr
    # storing the receivers email address
    msg['To'] = toaddr
    # storing the subject
    msg['Subject'] =f"""HUB Mismatch for {Email_date} """#+y_date
    # string to store the body of the mail
    if len(Empty_payer_name) > 0:
        body = f"Hello Team\nPlease find attached HUB mismatch files. Qinsight file count is {Qinight_file_count} and HUB file count is {HUB_File_count} for date {y_date_slash} and found missing payer for file {Empty_payer_name}"#+y_date
    else:
        body=f"Hello Team\nPlease find attached HUB mismatch files. Qinsight file count is {Qinight_file_count} and HUB file count is {HUB_File_count} for date {y_date_slash} and found no missing payer "
    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
    # open the file to be sent
    filename1="HUB Mismatch.csv"
    # filename2="UnMapped_PLB.csv"
    attachment1 = open("HUB Mismatch.csv", "rb")
    # attachment2 = open("UnMapped_PLB.csv", "rb")
    # instance of MIMEBase and named as p
    p1 = MIMEBase('application', 'octet-stream')
    # p2 = MIMEBase('application', 'octet-stream')
    # To change the payload into encoded form
    p1.set_payload((attachment1).read())
    # p2.set_payload((attachment2).read())
    # encode into base64
    encoders.encode_base64(p1)
    # encoders.encode_base64(p2)
    p1.add_header('Content-Disposition', "attachment1; filename= %s" % filename1)
    # p2.add_header('Content-Disposition', "attachment2; filename= %s" % filename2)
    # attach the instance 'p' to instance 'msg'
    msg.attach(p1)
    # msg.attach(p2)
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
