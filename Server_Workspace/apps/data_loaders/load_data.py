import pandas as pd
from datetime import datetime


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
        grouped_values = result.groupby(['product_name', 'month', 'day'])
        #grouped_values['count'] = result.groupby(['product_name', 'created_time']).count()
        print(grouped_values.get_group('Product 3'))

        return result
