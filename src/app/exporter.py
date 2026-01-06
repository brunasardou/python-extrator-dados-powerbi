import pandas as pd
import logging

def processar_e_exportar(df, filepath, col_zscore=None):
    # Lógica de Z-Score (Mantida)
    if col_zscore and col_zscore in df.columns:
        df[col_zscore] = pd.to_numeric(df[col_zscore], errors='coerce')
        valores = df[col_zscore].dropna()
        if not valores.empty:
            media = valores.mean()
            desvio = valores.std()
            if desvio > 0:
                df[f'zscore_{col_zscore}'] = (df[col_zscore] - media) / desvio
                df['anomalia_detectada'] = df[f'zscore_{col_zscore}'].apply(
                    lambda x: 'Sim' if abs(x) > 2 else 'Não'
                )

    # Lógica de Exportação Inteligente
    try:
        if filepath.lower().endswith('.parquet'):
            # Formato ideal para Big Data: Comprimido e Rápido
            df.to_parquet(filepath, engine='pyarrow', compression='snappy', index=False)
            logging.info(f"Exportação em PARQUET concluída: {filepath}")
            
        elif filepath.lower().endswith('.json'):
            df.to_json(filepath, orient='records', indent=4, force_ascii=False)
            logging.info(f"Exportação em JSON concluída: {filepath}")
            
        else:
            # Padrão CSV para volumes médios/pequenos
            df.to_csv(filepath, index=False, sep=';', encoding='utf-8-sig')
            logging.info(f"Exportação em CSV concluída: {filepath}")
            
    except Exception as e:
        logging.error(f"Erro ao salvar arquivo: {e}")
        raise e