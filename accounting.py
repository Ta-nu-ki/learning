def margin_to_markup_conversion(margin):
	"""
	Calculates markup from margin.
	"""
    return margin / (1 - margin)


def markup_to_margin_conversion(markup):
	"""
	Calculates margin from markup.
	"""
    return markup / (1 + markup)
