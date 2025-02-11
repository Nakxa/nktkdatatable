# NkTkDataTable

A modern, feature-rich data table widget for Tkinter applications in Python. NkTkDataTable provides an elegant way to display and interact with tabular data, offering features like sorting, filtering, custom styling, and more.

## Features

- Sortable columns with click-to-sort functionality
- Built-in filtering capability
- Customizable styling with modern defaults
- Row hover effects
- Alternating row colors
- Automatic scrolling for large datasets
- Click event handling for rows
- Dynamic row addition
- Responsive design that adapts to window resizing

## Installation

You can install NkTkDataTable using pip:

```bash
pip install nktkdatatable
```

## Usage

Basic usage example:

```python
import tkinter as tk
from nktkdatatable import NkTkDataTable

# Create root window
root = tk.Tk()
root.geometry('800x500')

# Define columns and data
columns = ['ID', 'Name', 'Email']
data = [
    (1, 'John Doe', 'john@example.com'),
    (2, 'Jane Smith', 'jane@example.com')
]

# Callback function for row clicks
def on_row_click(record):
    print(f"Selected record: {record}")

# Create table
table = NkTkDataTable(root, columns, data, get_data=on_row_click)
table.pack(fill='both', expand=True)

root.mainloop()
```

## Customization

You can customize the table's appearance using the style dictionary:

```python
custom_style = {
    'font': ('Arial', 11),
    'header_bg': '#34495e',
    'header_fg': 'white',
    'row_bg_even': '#ecf0f1',
    'row_bg_odd': '#ffffff',
    'row_hover_bg': '#dcdfe1',
    'border_color': '#bdc3c7',
    'cell_padding': 7,
    'border_width': 2,
    'row_height': 45,
    'header_height': 50,
    'rounded_corners': 6,
    'sort_arrow_up': '▲',
    'sort_arrow_down': '▼'
}

table = NkTkDataTable(root, columns, data, get_data=on_row_click, **custom_style)
```

## Complete Example

Here's a full example demonstrating all features:

```python
import tkinter as tk
from nktkdatatable import NkTkDataTable

root = tk.Tk()
root.title('NkTkDataTable Demo')
root.geometry('800x500')

# Define columns and data
columns = ['ID', 'Name', 'Email', 'Status']
data = [
    (1, 'John Doe', 'john@example.com', 'Active'),
    (2, 'Jane Smith', 'jane@example.com', 'Inactive'),
    (3, 'Bob Wilson', 'bob@example.com', 'Active')
]

def get_data(record):
    print(f"Selected record: {record}")

# Create filter input
filter_frame = tk.Frame(root)
filter_frame.pack(pady=10)

filter_entry = tk.Entry(filter_frame)
filter_entry.pack(side='left', padx=5)

def apply_filter():
    filter_text = filter_entry.get()
    table._on_filter(filter_text)

filter_button = tk.Button(filter_frame, text="Filter", command=apply_filter)
filter_button.pack(side='left')

# Create table with custom style
custom_style = {
    'font': ('Arial', 11),
    'header_bg': '#34495e',
    'header_fg': 'white',
    'row_bg_even': '#ecf0f1',
    'row_bg_odd': '#ffffff',
    'row_hover_bg': '#dcdfe1'
}

table = NkTkDataTable(root, columns, data, get_data=get_data, **custom_style)
table.pack(fill='both', expand=True, padx=10, pady=10)

root.mainloop()
```

## API Reference

### Class: NkTkDataTable

#### Parameters:
- `master`: Tkinter parent widget
- `columns`: List of column headers
- `data`: List of tuples containing row data
- `get_data`: Callback function for row clicks
- `**kwargs`: Style customization options

#### Methods:
- `add_row(row_data)`: Add a new row to the table
- `set_style(**kwargs)`: Update table styling
- `refresh()`: Refresh table display
- `clear()`: Clear filters and reset to original data

#### Style Options:
- `font`: Tuple of (font_family, size)
- `header_bg`: Header background color
- `header_fg`: Header text color
- `row_bg_even`: Even row background color
- `row_bg_odd`: Odd row background color
- `row_hover_bg`: Row hover background color
- `border_color`: Border color
- `cell_padding`: Cell padding in pixels
- `border_width`: Border width in pixels
- `row_height`: Row height in pixels
- `header_height`: Header height in pixels
- `rounded_corners`: Corner radius in pixels
- `sort_arrow_up`: Sort ascending indicator
- `sort_arrow_down`: Sort descending indicator

## License

MIT License

Copyright (c) 2024 NkTkDataTable

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



this is readme file of lib which i have create 
so create mordern authestic documentaion website in react+tailwind for this lib 
i documentation every thing should