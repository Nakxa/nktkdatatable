import tkinter as tk
from tkinter import ttk
from nktkdatatable import NkTkDataTable 


if __name__ == '__main__':
    root = tk.Tk()
    root.title('NkTkDataTable Example')
    root.geometry('800x500')

    # Column headers and data
    columns = ['ID', 'Name', 'Email', 'Status', ]
    data = [
        (1, 'John Doe', 'john@example.com', 'Active', ),
        (2, 'Jane Smith', 'jane@example.com', 'Inactive', ),
        (3, 'Bob Wilson', 'bob@example.com', 'Active',  ),
        (4, 'Alice Brown', 'alice@example.com', 'Active',),
    ] * 5  # Multiply data for example

    def get_data(record):
        """Get data callback when a cell is clicked"""
        print("Selected record:", record)

    def filter_data(filter_text):
        """Filter data based on filter input"""
        table._on_filter(filter_text)

    def sort_data(col_idx):
        """Sort data based on the column index"""
        table._on_header_click(col_idx)

    def add_row():
        """Add a new row to the table"""
        new_row = (5, 'Chris Green', 'chris@example.com', 'Active', 'HR', 'Manager', 'Los Angeles')
        table.add_row(new_row)

    def update_style():
        """Update the table style dynamically"""
        new_style = {
            'header_bg': '#2c3e50',  # Change header background
            'row_hover_bg': '#f39c12',  # Change hover background
            'border_color': '#e74c3c',  # Change border color
        }
        table.set_style(**new_style)

    def clear():
        """Clear the filter and reset to the original state"""
        table._on_filter('')  # Reset the table data to the original state
        table.refresh()  # Refresh the table to show the original data

    # Custom styles for the ModernTable
    custom_style = {
        'font': ('Arial', 11),  # Use Arial font
        'header_bg': '#34495e',  # Darker blue for the header
        'header_fg': 'white',  # White text on the header
        'row_bg_even': '#ecf0f1',  # Light gray for even rows
        'row_bg_odd': '#ffffff',  # White for odd rows
        'row_hover_bg': '#dcdfe1',  # Light hover color
        'border_color': '#bdc3c7',  # Lighter border
        'cell_padding': 7,  # Increased padding inside cells
        'border_width': 2,  # Thicker border
        'row_height': 45,  # Increased row height
        'header_height': 50,  # Larger header height
        'rounded_corners': 6,  # Slightly smaller rounded corners
        'sort_arrow_up': '▲',  # Up arrow for sorting
        'sort_arrow_down': '▼',  # Down arrow for sorting
        'header_bg': '#2c3e50',  # Change header background
            'row_hover_bg': '#f39c12',  # Change hover background
            'border_color': '#e74c3c',
    }

    # Create the ModernTable widget with updated style
    table = NkTkDataTable(root, columns, data, get_data, **custom_style)
    table.pack(fill='both', expand=True, padx=10, pady=10)

    # Example filter input box
    filter_entry = tk.Entry(root)
    filter_entry.pack(pady=10, padx=10)
    filter_button = tk.Button(root, text="Apply Filter", command=lambda: filter_data(filter_entry.get()))
    filter_button.pack(pady=5)

    # Example buttons for sorting and adding rows
    sort_button = tk.Button(root, text="Sort by Name", command=lambda: sort_data(1))  # Sort by 'Name' column
    sort_button.pack(pady=5)

    add_button = tk.Button(root, text="Add Row", command=add_row)
    add_button.pack(pady=5)

    style_button = tk.Button(root, text="Update Style", command=update_style)
    style_button.pack(pady=5)

    # Clear Button to reset everything
    clear_button = tk.Button(root, text="Clear", command=clear)
    clear_button.pack(pady=5)

    root.mainloop()
