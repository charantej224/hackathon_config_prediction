import pandas as pd
from datetime import datetime
from apps.models.data_model import Data
from apps.models.config_model import ConfigData
from apps.models.collective_reliability_model import Collective
from apps.models.reliability_model import Reliability
from apps.models.efficiency_model import Efficiency
from apps.models.retention_model import Retention

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
        print(start_time)
        start_dt_time = datetime.strptime(start_time, "%m/%d/%y %H:%M")
        end_dt_time = datetime.strptime(end_time, "%m/%d/%y %H:%M")

        response_data_deployment = pd.DataFrame(self.deployment_data_frame, columns=['created_time', 'product_name'])
        response_expansion_data_frame = pd.DataFrame(self.expansion_data_frame,
                                                     columns=['created_time', 'product_name'])
        response_updated_data_frame = pd.DataFrame(self.updated_data_frame, columns=['created_time', 'product_name'])
        frames = [response_data_deployment, response_expansion_data_frame, response_updated_data_frame]
        result = pd.concat(frames)
        result = result[(result["created_time"] > start_dt_time) & (result["created_time"] < end_dt_time)]
        # result['month'] = result['created_time'].apply(lambda x: x.month)
        # result['day'] = result['created_time'].apply(lambda x: x.day)
        # grouped_values1 = pd.DataFrame({'count': result.groupby(['product_name', 'month', 'day']).size()}).reset_index()
        grouped_values1 = pd.DataFrame({'count': result.groupby(['product_name']).size()}).reset_index()
        print(grouped_values1)
        return_list = []
        for index, row in grouped_values1.iterrows():
            return_list.append(Data(row['product_name'], row['count']).to_json())
            print(grouped_values1.index[index])

        return json.dumps(return_list)

    def get_all_config_data(self, start_time, end_time):
        start_dt_time = datetime.strptime(start_time, "%m/%d/%y %H:%M")
        end_dt_time = datetime.strptime(end_time, "%m/%d/%y %H:%M")
        response_data_deployment = pd.DataFrame(self.deployment_data_frame,
                                                columns=['created_time', 'product_name', 'cores', 'storage'])
        response_expansion_data_frame = pd.DataFrame(self.expansion_data_frame,
                                                     columns=['created_time', 'product_name', 'cores', 'storage'])
        result = pd.concat([response_data_deployment, response_expansion_data_frame])
        result = result[(result["created_time"] > start_dt_time) & (result["created_time"] < end_dt_time)]
        grouped_values1 = pd.DataFrame(
            {'count': result.groupby(['product_name', 'cores', 'storage']).size()}).reset_index()
        print(grouped_values1)

        return_list = []
        for index, row in grouped_values1.iterrows():
            return_list.append(
                ConfigData(row['product_name'], row['count'], str(row['cores']) + "," + str(row['storage'])).to_json())
            print(grouped_values1.index[index])

        return json.dumps(return_list)

    def get_reliability_info(self, start_time, end_time):
        start_dt_time = datetime.strptime(start_time, "%m/%d/%y %H:%M")
        end_dt_time = datetime.strptime(end_time, "%m/%d/%y %H:%M")
        response_data_deployment = pd.DataFrame(self.deployment_data_frame,
                                                columns=['product_name', 'created_time', 'completed_time', 'result'])
        response_expansion_data_frame = pd.DataFrame(self.expansion_data_frame,
                                                     columns=['product_name', 'created_time', 'completed_time',
                                                              'result'])
        response_updated_data_frame = pd.DataFrame(self.updated_data_frame,
                                                   columns=['product_name', 'created_time', 'completed_time', 'result'])

        response_data_deployment = response_data_deployment[
            (response_data_deployment["created_time"] > start_dt_time) & (
                    response_data_deployment["created_time"] < end_dt_time)]
        response_data_deployment['difference'] = response_data_deployment.apply(self.data_diff, axis=1)

        response_expansion_data_frame = response_expansion_data_frame[
            (response_expansion_data_frame["created_time"] > start_dt_time) & (
                    response_expansion_data_frame["created_time"] < end_dt_time)]
        response_expansion_data_frame['difference'] = response_expansion_data_frame.apply(self.data_diff, axis=1)

        response_updated_data_frame = response_updated_data_frame[
            (response_updated_data_frame["created_time"] > start_dt_time) & (
                    response_updated_data_frame["created_time"] < end_dt_time)]
        response_updated_data_frame['difference'] = response_updated_data_frame.apply(self.data_diff, axis=1)
        print(response_expansion_data_frame)
        deployment_response = []
        expansion_response = []
        update_response = []
        for index, row in response_data_deployment.iterrows():
            deployment_response.append(Reliability(row['product_name'], row['result'], row['difference']).to_json())
        for index, row in response_expansion_data_frame.iterrows():
            expansion_response.append(Reliability(row['product_name'], row['result'], row['difference']).to_json())
        for index, row in response_updated_data_frame.iterrows():
            update_response.append(Reliability(row['product_name'], row['result'], row['difference']).to_json())
        return json.dumps(Collective(deployment_response, expansion_response, update_response).to_json())

    def data_diff(self, x):
        return (x['completed_time'] - x['created_time']).seconds

    def get_efficiency_data(self, start_time, end_time):
        print(start_time)
        start_dt_time = datetime.strptime(start_time, "%m/%d/%y %H:%M")
        end_dt_time = datetime.strptime(end_time, "%m/%d/%y %H:%M")

        response_data_deployment = pd.DataFrame(self.deployment_data_frame,
                                                columns=['created_time', 'result', 'product_name'])
        response_expansion_data_frame = pd.DataFrame(self.expansion_data_frame,
                                                     columns=['created_time', 'result', 'product_name'])
        response_updated_data_frame = pd.DataFrame(self.updated_data_frame,
                                                   columns=['created_time', 'result', 'product_name'])
        frames = [response_data_deployment, response_expansion_data_frame, response_updated_data_frame]
        result = pd.concat(frames)
        result = result[(result["created_time"] > start_dt_time) & (result["created_time"] < end_dt_time)]
        grouped_values1 = pd.DataFrame({'count': result.groupby(['result', 'product_name']).size()}).reset_index()
        print(grouped_values1)
        return_list = []
        for index, row in grouped_values1.iterrows():
            return_list.append(Efficiency(row['product_name'], row['result'], row['count']).to_json())
        return json.dumps(return_list)

    def get_retention_data(self, start_time, end_time):
        print(start_time)
        start_dt_time = datetime.strptime(start_time, "%m/%d/%y %H:%M")
        end_dt_time = datetime.strptime(end_time, "%m/%d/%y %H:%M")
        response_expansion_data_frame = pd.DataFrame(self.expansion_data_frame,
                                                     columns=['created_time', 'result', 'customer_id'])
        response_updated_data_frame = pd.DataFrame(self.updated_data_frame,
                                                   columns=['created_time', 'result', 'customer_id'])
        frames = [response_expansion_data_frame, response_updated_data_frame]
        result = pd.concat(frames)
        result = result[(result["created_time"] > start_dt_time) & (result["created_time"] < end_dt_time)]
        grouped_values1 = pd.DataFrame({'count': result.groupby(['customer_id', 'result']).size()}).reset_index()
        return_list = []
        for index, row in grouped_values1.iterrows():
            return_list.append(Retention(row['customer_id'], row['result'], row['count']).to_json())
        return json.dumps(return_list)
