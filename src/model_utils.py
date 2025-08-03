from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_absolute_error
import numpy as np

print("✅ model_utils.py başarıyla import edildi.")
def evaluate_model(model, X, y, n_splits=5):
    """
    Verilen regresyon modelini zaman serisi verisi üzerinde TimeSeriesSplit kullanarak değerlendirir.

    Parameters
    ----------
    model : object
        fit() ve predict() metodlarına sahip bir regresyon modeli (örneğin: LinearRegression, XGBoost, LightGBM, CatBoost).
    
    X : pd.DataFrame veya np.ndarray
        Bağımsız değişkenleri içeren giriş veri kümesi.
    
    y : pd.Series veya np.ndarray
        Bağımlı değişken (hedef değişken).
    
    n_splits : int, default=5
        TimeSeriesSplit kullanılarak verinin kaç parçaya bölüneceği.

    Returns
    -------
    float
        Ortalama MAE (Mean Absolute Error) skoru. Daha düşük değer, daha iyi model performansını gösterir.
    """

    tscv = TimeSeriesSplit(n_splits=n_splits)
    scores = []

    for train_idx, val_idx in tscv.split(X):
        X_train_cv, X_val_cv = X.iloc[train_idx], X.iloc[val_idx]
        y_train_cv, y_val_cv = y.iloc[train_idx], y.iloc[val_idx]

        model.fit(X_train_cv, y_train_cv)
        y_pred = model.predict(X_val_cv)
        score = mean_absolute_error(y_val_cv, y_pred)
        scores.append(score)

    return np.mean(scores)