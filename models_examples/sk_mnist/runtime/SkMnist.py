from sklearn.externals import joblib
import os
import json

class SkMnist(object):
    def __init__(self, **kwargs):
        json_conf = os.environ['config_dict'].replace('||','"')
        config = json.loads(json_conf)
        self.clf = joblib.load('/data/{model_id}-{model_version}-{owner_id}-{data_version}/SVM.pkl'.format(**config)) 

    def predict(self,X,feature_names):
        predictions = self.clf.predict(X).reshape(1, -1)
        return predictions

