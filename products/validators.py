from django.core.validators import ValidationError

BLOCKED_WORDS_LIST = ['cheap','bad']

def validate_blocked_words(value):
    """
    Django Model/Forms
    """
    init_value = f"{value}".lower()
    init_items = set(init_value.split())
    blocked = set([x.lower() for x in BLOCKED_WORDS_LIST])

    invalid_items = list(init_items & blocked)
    has_error = len(invalid_items)>0

    if has_error:
        validation_errors = []
        for i, invalid in enumerate(invalid_items):
            validation_errors.append(
                ValidationError("%(value)s is a blocked word",params={'value':invalid},code=f'blocked-word-{i}'))
        raise ValidationError(validation_errors)




