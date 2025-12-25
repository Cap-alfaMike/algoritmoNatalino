def get_invalid_deliveries(logistics_data: dict) -> list:
    """Identifica IDs com coordenadas ou zona de voo ausentes."""
    return [
        delivery_id for delivery_id, info in logistics_data.items()
        if not all([info.get('lat'), info.get('long'), info.get('zona_voo')])
    ]
