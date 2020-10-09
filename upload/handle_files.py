import pandas as pd
import datetime as dt
from upload.models import DataReport
import csv, codecs
import threading
import sys

class ReportThread(threading.Thread):
    def __init__(self, dataframe):
        self.dataframe = dataframe
        threading.Thread.__init__(self)
    
    def run(self):
        print('file was loaded successfully.')
        for index, row in self.dataframe.iterrows():
            save_data = DataReport(
                date=row['DATE'], 
                market_code=row['MARKET_CODE'], 
                room_night=row['ROOM_NIGHT'], 
                room_revenue=row['ROOM_REVENUE'],
                # file_name=row['FILE_NAME'],
                )
            save_data.save()
        

# function to return VALUE for any KEY 
def get_key(key):
    dict_ = {'REPORT_ID': 'res_forecast', 'RESORT': 'res_statistics'}
    for k, v in dict_.items(): 
         if k == key: 
             return True

    return False

# file_name = R'C:\Users\maalh836\Desktop\temp\2. R122 Schedule.txt'
def handle_uploaded_file(file_name):
    
    try:
        # if file_name.name.endswith('.txt'):
        data = pd.read_csv(file_name, low_memory=False, sep='\t', lineterminator='\r')
        # is_valid = get_key(data.columns[0])
        
        # if file_name.name.endswith('.csv'):
        #     data = pd.DataFrame(csv.reader(codecs.iterdecode(file_name, 'utf-8')))
        #     data.columns = data.iloc[0]
        #     data.drop([0], inplace=True)

        # print(data.columns)

        if data.columns.values[0] == 'RESORT':
            room_revenue = 'REVENUE'
            date = 'BUSINESS_DATE'

        if data.columns.values[0] == 'REPORT_ID':
            room_revenue = 'TOTAL_REVENUE'
            date = 'RESERVATION_DATE'

        data.rename(columns={
            f'{date}':'DATE',
            f'{room_revenue}':'ROOM_REVENUE',
            'MARKET_CODE':'MARKET_CODE',
            'NO_DEFINITE_ROOMS':'ROOM_NIGHT',
            }, inplace=True)

        data = data[:-3]
        data = data[['DATE','MARKET_CODE','ROOM_NIGHT','ROOM_REVENUE']].copy()
        data['DATE'] = pd.to_datetime(data['DATE'])
        # data['FILE_NAME'] = 'test'
        
        data['ROOM_REVENUE'] = data['ROOM_REVENUE'].astype(float)
        data['ROOM_NIGHT'] = data['ROOM_NIGHT'].astype(float)

        # df['DATE'] = pd.to_datetime(pd.Series(df['DATE']))
        # df['month']= df['DATE'].apply(lambda x: x.month)
        # df['year']= df['DATE'].apply(lambda x: x.year)
        # df['day']= df['DATE'].apply(lambda x: x.day)
        # df['DDMMMYY'] = df['DATE'].map(lambda x: dt.datetime(x.year, x.month, 1))
        # df['timestamp'] = dt.datetime.now()
        ReportThread(data).start()

    except Exception as ex:
        print("Failed to process", ex, '\n', "Error on line {}".format(sys.exc_info()[-1].tb_lineno))

    # return is_valid
   


# # save data frame to database
# def add_data(dataframe):
#     for index, row in dataframe.iterrows():
#         print(row['MARKET_CODE'])
#         save_data = DataReport(
#             date=row['DATE'], 
#             market_code=row['MARKET_CODE'], 
#             room_night=row['ROOM_NIGHT'], 
#             room_revenue=row['ROOM_REVENUE']
#             )
#         save_data.save()




def is_file_valid(file_name):
    try:
        if file_name.name.endswith('.txt'):
            data = pd.read_csv(file_name, low_memory=False, sep='\t', lineterminator='\r')

        return get_key(data.columns[0])

    
    except Exception as ex:
        print("Failed to process", ex, '\n', "Error on line {}".format(sys.exc_info()[-1].tb_lineno))
        
        return False, 'Not_Valid'

# is_file_valid(R'C:\Users\maalh836\Desktop\temp\test_data\2. F126.txt')

# with open(R'C:\Users\maalh836\Desktop\temp\test_data\2. F126.txt', ) as file:
#     line1 = file.readline()

#     for last_line in line1:
#         pass
#     print(line1)


