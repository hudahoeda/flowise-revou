from flowise_test import Flowise, FlowiseClientOptions, PredictionData

def test_non_streaming():
    # Set the base URL and API key for the Flowise API
    options = FlowiseClientOptions(
        base_url="https://flowise.revou.tech/api/v1",
        api_key="qSm0h-wPVhl8EgLzDRXLrNlt7SzQd3Dy5bw5we3d1fk"  # Replace with your actual API key
    )
    client = Flowise(options=options)

    # Test non-streaming prediction
    completion = client.create_prediction(
        PredictionData(
            chatflowId="1a10a40b-1cb4-4b79-88d6-e616481aaffc",
            question="What is the capital of France?",
            streaming=False
        )
    )

    # Process and print the response
    print("Non-streaming response:")
    for response in completion:
        print(response)

def test_streaming():
    options = FlowiseClientOptions(
        base_url="https://flowise.revou.tech/api/v1",
        api_key="qSm0h-wPVhl8EgLzDRXLrNlt7SzQd3Dy5bw5we3d1fk"  # Replace with your actual API key
    )
    client = Flowise(options=options)

    # Test streaming prediction
    completion = client.create_prediction(
        PredictionData(
            chatflowId="1a10a40b-1cb4-4b79-88d6-e616481aaffc",
            question="Tell me a joke!",
            streaming=True
        )
    )

    # Process and print each streamed chunk
    print("Streaming response:")
    for chunk in completion:
        print(chunk)

if __name__ == "__main__":
    # Run non-streaming test
    test_non_streaming()

    # Run streaming test
    test_streaming()
