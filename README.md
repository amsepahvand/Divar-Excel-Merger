# Data Enrichment Script


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
     - `Personal ID`
     - `Title`
     - `First Name`
     - `Surname`
     - `Company`
   - `output_list.xlsx`: This file should contain a column named `Description` where the full names will be matched.

2. **Run the Script**: Execute the script using Python:

```bash
python3 merger.py
```

3. **Output**: The script will create a new file named `updated_output_list.xlsx` in the same directory. This file will contain the original data from `output_list.xlsx` along with the matched `First Name And Surname`, `Personal ID`, and `Company` from `information_list.xlsx`.

## Example

### information_list.xlsx
| First Name | Surname |   Title    | Personal ID  |   Company    |
|------------|---------|------------|--------------|--------------|
| John       | Doe     |     MR     | 2f66e42f66e4 | Example Inc. |
| Jane       | Smith   |     MRS    | 2f66e42f66e4 |  Sample LLC   |

### output_list.xlsx
| Description                |
|----------------------------|
| Paid by, John Doe          |
| Paid by, Jane Smith        |

### Result in updated_output_list.xlsx
| Description                | First Name And Surname | Personal ID | Company      |
|----------------------------|------------------------|-------------|--------------|
| Paid by, John Doe          |      John Doe          |2f66e42f66e4 | Example Inc. |
| Paid by, Jane Smith        |      Jane Smith        |2f66e42f66e4 | Sample LLC   |

