def clean_logistics_data(logistics_data: dict) -> dict:
    """Remove entregas inválidas para garantir a segurança da rota."""
    return {
        k: v for k, v in logistics_data.items()
        if all([v.get('lat'), v.get('long'), v.get('zona_voo')])
    }
