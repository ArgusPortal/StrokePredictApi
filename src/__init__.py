"""
Stroke Prediction v3 - Módulos principais
"""

# === CONFIGURAÇÕES ===
from .config import (
    SEED,
    DATA_DIR,
    RAW_PATH,
    INTERIM_PATH,  # ✅ Já presente
    PROC_PATH,     # ✅ Já presente
    MODELS_PATH,
    RESULTS_PATH,
    BASE_DIR
)

# === FUNÇÕES PRINCIPAIS ===
from .feature_engineering import engineer_medical_features


__all__ = [
    # Configs
    'SEED',
    'DATA_DIR',
    'RAW_PATH',
    'INTERIM_PATH',
    'PROC_PATH',
    'MODELS_PATH',
    'RESULTS_PATH',
    'BASE_DIR',
    
    # Funções
    'engineer_medical_features',

]
