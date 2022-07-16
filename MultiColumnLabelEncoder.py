import pandas as pd

class MultiColumnLabelEncoder:

    def __init__(self, dataframe= pd.DataFrame() , columns=None):

        self.dataframe = dataframe.copy()
        if columns == None and not self.dataframe.empty:
            self.string_columns = self.get_string_columns()
        else:
            self.string_columns = columns
        if not self.dataframe.empty and self.string_columns!= None:
            self.encoding_params, self.inverse_encoding_params = self.encode_dataframe()
        else:
            self.encoding_params = None
            self.inverse_encoding_params = None

    def get_string_columns(self):
        return(self.dataframe.select_dtypes(include=['object']).columns.tolist())

    
    def encode_dataframe(self):
        encoding_params = {}
        inverse_encoding_params = {}
        for i in self.string_columns:
            categories = list(self.dataframe[i].unique())
            encoding_params[i] = dict(zip(categories,range(len(categories))))
            inverse_encoding_params[i] = dict(zip(range(len(categories)),categories))
        self.inverse_encoding_params = inverse_encoding_params
        self.encoding_params = encoding_params
        return encoding_params, inverse_encoding_params


    def fit_transform(self, dataframe=pd.DataFrame(), columns = None):
        if not dataframe.empty :
            self.dataframe = dataframe.copy()
        if self.string_columns == None and columns == None:
            self.string_columns = self.get_string_columns()
        elif columns != None:
            self.string_columns = columns
        if self.encoding_params == None:
            self.encoding_params, self.inverse_encoding_params = self.encode_dataframe()

        for i in self.string_columns:
            self.dataframe[i] = self.dataframe[i].map(self.encoding_params[i])

        return self.dataframe

    def inverse_fit_transform(self,dataframe,columns=None):

        self.dataframe = dataframe.copy()
        if columns == None:
            self.string_columns = self.get_string_columns()
        else:
            self.string_columns = columns

        if self.encoding_params == None:
            print("Inverse Fit Transform is not possible as previous records are not available")
        
        for i in self.string_columns:
            self.dataframe[i] = self.dataframe[i].map(self.inverse_encoding_params[i])

        return self.dataframe

    
