# Customer Membership

## Project Background

MyCommerce is a new e-commerce service that offers a Tier Membership feature where each membership level comes with different benefits and advantages. The available membership tiers are:
- Silver
- Gold
- Platinum

### Membership Benefits
- **Silver Membership**: 8% discount on every payment, plus Food Vouchers.
- **Gold Membership**: 10% discount on every payment, plus benefits from Silver and Online Motorcycle Taxi Vouchers.
- **Platinum Membership**: 15% discount on every payment, plus benefits from Silver and Gold, Holiday Vouchers, and Cashback up to 30%.

To predict user membership, MyCommerce uses a distance-based approach, specifically the Euclidean Distance. The Euclidean Distance is calculated between the user's expense and income and the parameters for each membership tier.

## Project Requirements

### Table 1: Membership Benefits
| **Membership** | **Discount** | **Additional Benefits** |
|:--------------:|:------------:|:-----------------------:|
| Platinum       | 15%          | Silver + Gold + Holiday Vouchers + Cashback up to 30% |
| Gold           | 10%          | Silver + Online Motorcycle Taxi Vouchers |
| Silver         | 8%           | Food Vouchers |

### Table 2: Membership Requirements
| **Membership** | **Monthly Expense (Rp million)** | **Monthly Income (Rp million)** |
|:--------------:|:-------------------------------:|:------------------------------:|
| Platinum       | 8                                | 15                             |
| Gold           | 6                                | 10                             |
| Silver         | 5                                | 7                              |

## Features List
- `show_benefit()`: Shows all membership benefits.
- `show_requirements()`: Shows all requirements to become a member.
- `predict_membership(monthly_expense, monthly_income)`: Predicts which membership a user will be in based on the input parameters and each membership parameter.
- `calculate_price(price_list)`: Calculates the final price to be paid, applying the discount according to the membership provisions.

## Project Solution

The project solution is implemented in the `Membership` class and includes the following methods:

1. `show_benefit()`: Displays a table with membership benefits.
2. `show_requirements()`: Displays a table with membership requirements.
3. `predict_membership(monthly_expense, monthly_income)`: Predicts the user's membership tier using Euclidean distance and updates the membership data.
4. `show_membership()`: Displays the current membership status of the user.
5. `calculate_price(price_list)`: Calculates the final price for the user after applying the membership discount.

### Example Usage

#### 1. Initialization and Display Membership
```python
member = Membership('Sumbul')
member.show_membership()  # Output: Sumbul is a Platinum member

member = Membership('John')
member.show_membership()  # Output: John is not a member yet
```

#### 2. Display Membership Benefits
```python
member = Membership('Ana')
member.show_benefit()  # Output: A table displaying membership benefits
```

#### 3. Display Membership Requirements
```python
member = Membership('Cahya')
member.show_requirements()  # Output: A table displaying membership requirements
```

#### 4. Predict Membership
```python
member = Membership('John')
member.predict_membership(7, 12)  
# Output:
# Predicted Euclidean distances for John are {'Platinum': 3.61, 'Gold': 2.0, 'Silver': 5.0}
# John is predicted to be a Gold member

# Show updated data
print(f'Updated member data: {member.data}')
```

#### 5. Calculate Final Price
```python
member = Membership('Sumbul')
price_list = [100000, 200000, 300000]
member.calculate_price(price_list)  # Output: Sumbul final price is Rp 510,000.0
```

## Repository Contents

The repository contains the following files:
- `customer_membership.ipynb`: Jupyter notebook containing the project code and explanations.
- `main.py`: Python script containing the same code as in the Jupyter notebook for direct execution.

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/customer_membership.git
    cd customer_membership
    ```

2. Install the required dependencies:
    ```bash
    pip install tabulate
    ```

3. Run the Jupyter notebook:
    ```bash
    jupyter notebook customer_membership.ipynb
    ```

4. Alternatively, run the Python script:
    ```bash
    python main.py
    ```
