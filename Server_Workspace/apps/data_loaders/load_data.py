import pandas as pd
from datetime import datetime
from apps.models.data_model import Data
import json


class DataLoader:
    is_loaded = False

    def __init__(self):
        self.deployment_data_frame = pd.read_csv("dataset/Anonymized Deployment Job Data.csv")
        self.deployment_data_frame['created_time'] = self.deployment_data_frame[
            'created_time'].apply(lambda x: datetime.strptime(x, "%m/%d/%y %H:%M"))
        self.deployment_data_frame['completed_time'] = self.deployment_data_frame[
            'completed_time'].apply(lambda x: datetime.strptime(x, "%m/%d/%y %H:%M"))
        self.expansion_data_frame = pd.read_csv("dataset/Anonymized Expansion Job Data.csv")
        self.expansion_data_frame['created_time'] = self.expansion_data_frame[
            'created_time'].apply(lambda x: datetime.strptime(x, "%m/%d/%y %H:%M"))
        self.expansion_data_frame['completed_time'] = self.expansion_data_frame[
            'completed_time'].apply(lambda x: datetime.strptime(x, "%m/%d/%y %H:%M"))
        self.updated_data_frame = pd.read_csv("dataset/Anonymized Update Job Data.csv")
        self.updated_data_frame['created_time'] = self.updated_data_frame[
            'created_time'].apply(lambda x: datetime.strptime(x, "%m/%d/%y %H:%M"))
        self.updated_data_frame['completed_time'] = self.updated_data_frame[
            'completed_time'].apply(lambda x: datetime.strptime(x, "%m/%d/%y %H:%M"))
        self.is_loaded = True

    def get_all_data(self, start_time, end_time):
        response_data_deployment = pd.DataFrame(self.deployment_data_frame, columns=['created_time', 'product_name'])
        response_expansion_data_frame = pd.DataFrame(self.expansion_data_frame,
                                                     columns=['created_time', 'product_name'])
        response_updated_data_frame = pd.DataFrame(self.updated_data_frame, columns=['created_time', 'product_name'])
        frames = [response_data_deployment, response_expansion_data_frame, response_updated_data_frame]
        result = pd.concat(frames)
        result['month'] = result['created_time'].apply(lambda x: x.month)
        result['day'] = result['created_time'].apply(lambda x: x.day)
        grouped_values = result.groupby(['product_name', 'month', 'day']).count()
        grouped_values1 = pd.DataFrame({'count': result.groupby(['product_name', 'month', 'day']).size()}).reset_index()
        print(grouped_values1)
        return_list = []
        for index, row in grouped_values1.iterrows():
            return_list.append(Data(row['product_name'], row['month'], row['day'], row['count']))
            print(grouped_values1.index[index])

        return json.dumps(return_list)
