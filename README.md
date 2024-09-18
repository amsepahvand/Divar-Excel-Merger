# Data Enrichment Script

This Python script enriches an output list with additional information from an information list. It matches names from the information list with descriptions in the output list and adds corresponding details.

## Requirements

To run this script, you need to have Python installed along with the following package:

- `pandas`

You can install the required package using pip:

```bash
pip install pandas
```
## Usage

1. **Prepare Your Files**: Place the following files in the same directory as the script:
   - `information_list.xlsx`: This file should contain at least the following columns:
     - `First Name`
     - `Surname`
     - `Personal ID`
     - `Company`
   - `output_list.xlsx`: This file should contain a column named `Description` where the full names will be matched.

2. **Run the Script**: Execute the script using Python:

```bash
python your_script_name.py

3. **Output**: The script will create a new file named `updated_output_list.xlsx` in the same directory. This file will contain the original data from `output_list.xlsx` along with the matched `First Name And Surname`, `Personal ID`, and `Company` from `information_list.xlsx`.

## Example

### information_list.xlsx
| First Name | Surname | Personal ID | Company      |
|------------|---------|-------------|--------------|
| John       | Doe     | 12345       | Example Inc. |
| Jane       | Smith   | 67890       | Sample LLC   |

### output_list.xlsx
| Description                |
|----------------------------|
| John Doe is a developer.   |
| Jane Smith is a manager.   |

### Result in updated_output_list.xlsx
| Description                | First Name And Surname | Personal ID | Company      |
|----------------------------|------------------------|-------------|--------------|
| John Doe is a developer.   | John Doe               | 12345       | Example Inc. |
| Jane Smith is a manager.   | Jane Smith             | 67890       | Sample LLC   |

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Pandas Documentation](https://pandas.pydata.org/docs/) for data manipulation.
