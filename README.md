Policyholder Data Correction & Claim Calculation (NumPy + Pandas)
📌 Project Description

This project uses NumPy and Pandas to manage and correct insurance policyholder data.
It displays the original policy data, fixes an error by swapping two columns, and then calculates the total claim amount from all policyholders.

✅ Features

Stores policyholder information in a NumPy 2D array

Converts the data into a Pandas DataFrame for better readability

Swaps Premium Amount and Claim Amount columns to correct the dataset

Calculates the total claim amount using NumPy

🛠 Technologies Used

Python

NumPy

Pandas

📦 Installation

Install the required libraries using:

pip install numpy pandas

📊 Data Format

The dataset contains the following columns:

Column Name	Description
Policy Number	Unique policy ID
Premium Amount	Amount paid as premium
Insured Amount	Total insured value
Claim Amount	Amount claimed by the policyholder
⚙️ How the Code Works
1. Create the Policyholder Data

The data is stored as a NumPy array.

2. Display Original Data

The array is converted into a Pandas DataFrame and printed in table format.

3. Correct the Data by Swapping Columns

The program swaps the Premium Amount and Claim Amount columns to fix incorrect values.

4. Display Corrected Data

After swapping, the updated data is displayed again using Pandas.

5. Calculate Total Claim Amount

Finally, the code calculates the total claim amount of all policyholders using NumPy's sum function.

✅ Output

The program prints:

Original policyholder data

Corrected policyholder data (after swapping)

Total claim amount from all policyholders

