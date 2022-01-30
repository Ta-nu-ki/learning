import math


def margin_to_markup_conversion(margin):
    """
    Calculates markup from margin.
    Margin is [0, 1).
    """
    if 0 <= margin < 1:
        return margin / (1 - margin)
    else:
        print("Input margin is incorrect!")
        return


def markup_to_margin_conversion(markup):
    """
    Calculates margin from markup.
    Markup is [0, 1).
    """
    if 0 <= markup < 1:
        return markup / (1 + markup)
    else:
        print("Input markup is incorrect!")
        return


def log_transformation(number):
    """
    Performs to Log transformation.
    Number is (0, +inf).
    """
    if 0 < number < +math.inf:
        return math.log(1 + number)
    else:
        print("Input number is incorrect!")
        return


def inverse_log_transformation(number):
    """
    Performs from Log transformation.
    Number is (-inf, +inf).
    """
    return math.exp(number) - 1
