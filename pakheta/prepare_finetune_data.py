import json
import os
import glob
from datetime import datetime


def clean_text_for_training(text):
    """
    Clean and format text for training data.
    Removes extra whitespace and ensures proper formatting.
    """
    # Remove excessive newlines and spaces
    text = ' '.join(text.split())
    # Ensure text ends with a period if it doesn't already
    if text and not text.endswith(('.', '!', '?')):
        text += '.'
    return text


def prepare_finetune_data(input_file=None, output_file=None):
    """
    Convert bird data from JSON to JSONL format for OpenAI fine-tuning.

    Args:
        input_file (str): Path to input JSON file. If None, uses latest file in data directory
        output_file (str): Path to output JSONL file. If None, generates timestamped filename
    """
    # If no input file specified, get the most recent JSON file from data directory
    if input_file is None:
        data_files = glob.glob('data/birds_*.json')
        if not data_files:
            raise FileNotFoundError("No bird data JSON files found in data directory")
        input_file = max(data_files, key=os.path.getctime)
        print(f"Using most recent data file: {input_file}")

    # If no output file specified, create timestamped filename
    if output_file is None:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f'data/finetune_birds_{timestamp}.jsonl'

    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)

    try:
        # Read the JSON data
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        finetune_data = []

        # Prepare training examples
        for bird in data:
            # Clean and prepare the text
            name = clean_text_for_training(bird['name'])
            description = clean_text_for_training(bird['description'])

            # Create multiple prompt variations for better training
            prompts = [
                f"Tell me about {name}:",
                f"What can you tell me about {name}?",
                f"Describe the {name}:",
                f"What is a {name}?"
            ]

            # Create a training example for each prompt variation
            for prompt in prompts:
                finetune_data.append({
                    "prompt": prompt,
                    "completion": f" {description}"
                })

        # Write the JSONL file
        with open(output_file, 'w', encoding='utf-8') as f:
            for entry in finetune_data:
                f.write(json.dumps(entry, ensure_ascii=False) + '\n')

        # Print statistics
        print(f"\nFine-tuning data preparation completed successfully:")
        print(f"Input file: {input_file}")
        print(f"Output file: {output_file}")
        print(f"Number of birds: {len(data)}")
        print(f"Number of training examples: {len(finetune_data)}")
        print(
            f"Average completion length: {sum(len(entry['completion']) for entry in finetune_data) // len(finetune_data)} characters")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found")
    except json.JSONDecodeError:
        print(f"Error: '{input_file}' contains invalid JSON")
    except Exception as e:
        print(f"Error preparing fine-tuning data: {str(e)}")


if __name__ == "__main__":
    # The script can be run directly and will use the latest JSON file
    prepare_finetune_data()
