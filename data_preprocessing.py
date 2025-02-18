import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

def load_and_preprocess_data(file_path):
    # Load data
    data = pd.read_csv(file_path)
    
    # Define preprocessing for numeric features
    numeric_features = ['feature1', 'feature2', 'feature3']
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())])

    # Define preprocessing for categorical features
    categorical_features = ['category_feature']
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))])

    # Combine preprocessing steps
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)])

    # Apply transformations
    features = preprocessor.fit_transform(data)
    target = data['market_demand']
    
    return features, target

if __name__ == "__main__":
    features, target = load_and_preprocess_data('market_data.csv')
    print("Data preprocessed successfully.") 