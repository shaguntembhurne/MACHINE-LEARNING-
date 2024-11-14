# Matrix Calculator

This Python program performs basic matrix operations using NumPy. It allows users to input two matrices and computes their **addition**, **multiplication**, and the **determinant** (for square matrices). 

## Features
- **Matrix Input**: Users can input matrices of any dimension.
- **Matrix Operations**:
  - **Addition**: Adds two matrices (if they have the same shape).
  - **Multiplication**: Multiplies two matrices (if the number of columns of the first matrix matches the number of rows of the second).
  - **Determinant**: Computes the determinant of a square matrix.
  
## Requirements
- Python 3.x
- NumPy library (`pip install numpy`)

## How to Use
1. Clone or download the repository.
2. Install NumPy: `pip install numpy`.
3. Run the script: `python matrix_calculator.py`.
4. Follow the prompts to enter the matrices:
   - Enter the dimensions (rows and columns).
   - Enter the elements of the matrix row by row.
5. The program will display the result for:
   - **Matrix addition**.
   - **Matrix multiplication**.
   - **Matrix determinant** (for square matrices).

## Code Explanation

The code consists of the following key parts:
1. **`getting_input()`**: A function that collects matrix data from the user. It asks for the number of rows, columns, and the matrix values.
2. **`main()`**: The main function where matrices are collected and the operations are performed:
   - **Addition**: If matrices A and B have the same shape, it adds them together.
   - **Multiplication**: If the number of columns in A matches the number of rows in B, it multiplies the matrices.
   - **Determinant**: Computes the determinant for matrix A if it is square.
3. **Error Handling**: If the matrices' dimensions are incompatible, the program informs the user that the operations can't be performed.

## License
This project is open-source and available under the License.



