def get_circle_dimensions(rows):
    if rows < 2 or rows > 10:
        raise ValueError("Rows must be between 2 and 10.")

    # Anchored values for rows = 5
    base_object_size = 30
    base_row_spacing = 75
    base_vertical_offset = 40

    # Scaling factors for rows above and below 5
    size_delta = 10  # Total change in size from 2 rows to 10 rows
    spacing_delta = 20  # Total change in spacing from 2 rows to 10 rows
    vertical_offset_delta = 10  # Total change in vertical offset from 2 rows to 10 rows

    # Calculate proportional scaling
    object_size = base_object_size + (5 - rows) * (size_delta / 3)
    row_spacing = base_row_spacing + (5 - rows) * (spacing_delta / 3)
    row_vertical_offset = base_vertical_offset + (5 - rows) * (
        vertical_offset_delta / 3
    )

    return {
        "object_size": int(object_size),
        "row_spacing": int(row_spacing),
        "row_vertical_offset": int(row_vertical_offset),
    }
