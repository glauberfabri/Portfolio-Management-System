def export_to_powerbi(data, file_path):
    data.to_csv(file_path, index=False)
    print(f"Exported to {file_path}")