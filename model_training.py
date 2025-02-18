import joblib
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, VotingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from data_preprocessing import load_and_preprocess_data

def train_model(features, target):
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
    
    # Define models
    rf = RandomForestRegressor(random_state=42)
    gb = GradientBoostingRegressor(random_state=42)
    
    # Ensemble model
    ensemble_model = VotingRegressor(estimators=[('rf', rf), ('gb', gb)])
    
    # Hyperparameter tuning
    param_grid = {
        'rf__n_estimators': [100, 200],
        'gb__n_estimators': [100, 200],
        'gb__learning_rate': [0.01, 0.1, 0.2]
    }
    grid_search = GridSearchCV(ensemble_model, param_grid, cv=5, scoring='neg_mean_squared_error')
    grid_search.fit(X_train, y_train)
    
    # Best model
    best_model = grid_search.best_estimator_
    
    # Cross-validation
    cv_scores = cross_val_score(best_model, X_train, y_train, cv=5, scoring='neg_mean_squared_error')
    print(f'Cross-validation RMSE: {-cv_scores.mean()}')
    
    # Evaluate model
    predictions = best_model.predict(X_test)
    rmse = mean_squared_error(y_test, predictions, squared=False)
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    print(f'RMSE: {rmse}, MAE: {mae}, R2: {r2}')
    
    # Save model
    joblib.dump(best_model, 'market_demand_model.pkl')
    print("Model trained and saved successfully.")

if __name__ == "__main__":
    features, target = load_and_preprocess_data('market_data.csv')
    train_model(features, target) 