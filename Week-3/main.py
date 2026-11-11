
from llm_client import generate_response
from mongo_logger import MongoLogger
from cost_calculator import calculate_cost


def main():

    print("\n===== LLM MONITORING SYSTEM =====")

    logger = MongoLogger()

    try:
        prompt = input("\nEnter your question: ")

        print("\nGenerating AI response...")

        result = generate_response(prompt)

        response = result["response"]
        input_tokens = result["input_tokens"]
        output_tokens = result["output_tokens"]
        response_time = result["response_time"]

        total_tokens = input_tokens + output_tokens

        cost = calculate_cost(
            input_tokens,
            output_tokens
        )

        print("\n===== AI RESPONSE =====")
        print(response)

        print("\n===== USAGE DETAILS =====")
        print("Input Tokens:", input_tokens)
        print("Output Tokens:", output_tokens)
        print("Total Tokens:", total_tokens)
        print("Estimated Cost: $", cost)
        print("Response Time:", response_time, "seconds")

        log_data = {
            "prompt": prompt,
            "response": response,
            "model": "llama3.2",
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": total_tokens,
            "cost": cost,
            "response_time": response_time
        }

        logger.log_call(log_data)

    except Exception as error:
        print("Error:", error)

    finally:
        logger.close()


if __name__ == "__main__":
    main()
