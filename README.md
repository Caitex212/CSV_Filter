# CSV Filter

This Python script processes CSV files located in the `input` folder based on the configuration provided in `config.py`. It filters rows based on specific criteria and saves the filtered data into the `output` folder.

## Usage

1. **Configuration:**
    - Modify `config.py` to specify which columns to include (`True`) or exclude (`False`) from the output.
    - Optionally, set phone number filters in `phone_filter_include` or `phone_filter_exclude` lists.

2. **Input:**
    - Place CSV files to be processed in the `input` folder.

3. **Output:**
    - Filtered CSV files will be saved in the `output` folder.

4. **Execution:**
    - Run `main.py` to start the processing. 

## Requirements

- Python 3.x
- `csv` module

## Example

```python
# Process CSV files in the input folder and save filtered data in the output folder
process_folder(input_folder, output_folder)
```

## Configuration (`config.py`)

Adjust the configuration to include or exclude specific columns from the output.

```python
config = {
    "email_first": False,
    "email_second": False,
    "phone": True,
    # Add or remove fields as needed
}

phone_filter_include = []  # Include only numbers specified here
phone_filter_exclude = ["04"]  # Exclude numbers beginning with strings specified here
```

**Note:** Ensure Python script files (`main.py` and `config.py`) are in the same directory.

---
