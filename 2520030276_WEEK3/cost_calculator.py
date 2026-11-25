
def calculate_tokens(text):
    """Estimate token count using words."""
    if not text:
        return 0

    return len(text.split())


def calculate_cost(input_tokens, output_tokens):
    """Calculate cost for a local Ollama model."""
    input_cost = 0.0
    output_cost = 0.0

    total_cost = input_cost + output_cost

    return round(total_cost, 6)
