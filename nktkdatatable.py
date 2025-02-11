
import tkinter as tk  # Import the tkinter module for GUI creation
from tkinter import ttk  # Import ttk for additional styling (like Scrollbars)

class NkTkDataTable(tk.Frame):
    def __init__(self, master, columns, data=None, get_data=None, **kwargs):
        super().__init__(master)  # Initialize the parent class (Frame)
        
        # Default style configuration for table appearance
        self.style = {
            'font': ('Segoe UI', 10),
            'header_bg': '#2c3e50',  # Header background color
            'header_fg': 'white',  # Header text color
            'row_bg_even': '#f8f9fa',  # Even row background color
            'row_bg_odd': 'white',  # Odd row background color
            'row_hover_bg': '#e9ecef',  # Hover effect for rows
            'border_color': '#dee2e6',  # Border color
            'cell_padding': 5,  # Padding inside cells
            'border_width': 1,  # Border width for the cells
            'row_height': 40,  # Height for rows
            'header_height': 45,  # Height for header
            'rounded_corners': 8,  # Rounded corners for the table
            'sort_arrow_up': '▲',  # Sort up arrow
            'sort_arrow_down': '▼'  # Sort down arrow
        }
        
        self.style.update(kwargs)  # Update the default style with any custom styles passed in kwargs
        self.columns = columns  # Set the column headers
        self.original_data = list(data or [])  # Initialize original data, if provided
        self.data = list(data or [])  # Initialize table data to the same as original data
        self.sort_column = None  # No sorting column initially
        self.sort_ascending = True  # Default sorting is ascending
        self.get_data = get_data  # Function to handle row click data
        
        # Create a toolbar for the filter input
        self._create_toolbar()
        
        # Create main container for the table
        self.main_container = tk.Frame(self)
        self.main_container.pack(fill="both", expand=True)  # Expand the main container in both directions
        
        # Create header container for header widgets
        self.header_container = tk.Frame(self.main_container)
        self.header_container.pack(fill="x", side="top")
        
        # Create a frame for the header and a dummy scrollbar for spacing
        self.header_frame = tk.Frame(self.header_container)
        self.dummy_scrollbar = tk.Frame(self.header_container, width=17)  # Dummy scrollbar
        
        self.header_frame.pack(side="left", fill="x", expand=True)  # Pack header frame to the left
        
        # Create a container for the table content that is scrollable
        self.container = tk.Frame(self.main_container)
        self.container.pack(fill="both", expand=True)
        
        # Create a canvas to hold the table's content and a vertical scrollbar for it
        self.canvas = tk.Canvas(self.container)
        self.vsb = ttk.Scrollbar(self.container, orient="vertical", command=self.canvas.yview)  # Vertical Scrollbar
        
        # Configure the canvas to use the vertical scrollbar for scrolling
        self.canvas.configure(yscrollcommand=self._on_vsb)
        
        # Create the table frame where the actual data will be displayed
        self.table_frame = tk.Frame(self.canvas)
        
        # Pack the canvas and vertical scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        
        # Create a window inside the canvas to hold the table content
        self.canvas_window = self.canvas.create_window(
            (0, 0), 
            window=self.table_frame, 
            anchor="nw",  # North-West corner
            tags="table"  # Tag the window as 'table'
        )
        
        # Configure column weights for both the header and table content (makes columns resize evenly)
        for i in range(len(columns)):
            self.header_frame.grid_columnconfigure(i, weight=1, uniform='column')
            self.table_frame.grid_columnconfigure(i, weight=1, uniform='column')
        
        # Bind events to handle resizing and mouse scrolling
        self.table_frame.bind("<Configure>", self._on_frame_configure)
        self.canvas.bind("<Configure>", self._on_canvas_configure)
        self._bind_mouse_scroll()
        
        # Create the table header and table rows
        self._create_header()
        self._create_table()

    def _create_toolbar(self):
        """Create toolbar for filter input"""
        self.toolbar = tk.Frame(self)
        self.toolbar.pack(fill="x", pady=(0, 5))  # Create and pack toolbar
        
        filter_frame = tk.Frame(self.toolbar)  # Frame for filter input
        filter_frame.pack(side="left")  # Pack filter frame to the left

    def _create_header(self):
        """Create sticky header with sort functionality"""
        for col_idx, col in enumerate(self.columns):  # Loop through column headers
            header_text = col
            # Add sort arrows if the column is being sorted
            if self.sort_column == col_idx:
                header_text += ' ' + (
                    self.style['sort_arrow_up'] 
                    if self.sort_ascending 
                    else self.style['sort_arrow_down']
                )
            
            # Create header label with sorting indicator
            header = tk.Label(
                self.header_frame,
                text=header_text,
                bg=self.style['header_bg'],
                fg=self.style['header_fg'],
                font=(self.style['font'][0], self.style['font'][1], 'bold'),
                pady=self.style['cell_padding'],
                padx=self.style['cell_padding'],
                cursor='hand2'  # Show hand cursor for sortable columns
            )
            header.grid(row=0, column=col_idx, sticky='nsew', padx=1, pady=1)  # Grid the header
            
            # Bind click event for sorting functionality
            header.bind('<Button-1>', lambda e, col=col_idx: self._on_header_click(col))

    def _create_table(self):
        """Create table rows and make them scrollable"""
        for row_idx, row_data in enumerate(self.data):  # Loop through table rows
            bg_color = self.style['row_bg_even'] if row_idx % 2 == 0 else self.style['row_bg_odd']  # Alternate row colors
            
            for col_idx, cell_data in enumerate(row_data):  # Loop through each cell in the row
                if isinstance(cell_data, (int, float)):  # Align numerical data to the right
                    anchor = 'e'
                elif isinstance(cell_data, str):  # Align string data to the left
                    anchor = 'w'
                else:
                    anchor = 'center'  # Center other data types
                
                # Create a label for each cell in the table
                cell = tk.Label(
                    self.table_frame,
                    text=str(cell_data),
                    bg=bg_color,  # Background color for rows
                    font=self.style['font'],
                    pady=self.style['cell_padding'],
                    padx=self.style['cell_padding'],
                    anchor=anchor,
                    wraplength=150  # Wrap text in the cell if it's too long
                )
                cell.grid(row=row_idx, column=col_idx, sticky='nsew', padx=1, pady=1)  # Grid the cell
                
                # Store row index on the cell for hover functionality
                cell.row_index = row_idx
                cell.bind('<Enter>', lambda e, r=row_idx: self._on_row_hover(r, True))  # Bind hover event (Enter)
                cell.bind('<Leave>', lambda e, r=row_idx: self._on_row_hover(r, False))  # Bind hover event (Leave)

                # Bind click event on the cell to fetch data when clicked
                cell.bind('<Button-1>', lambda e, r=row_idx, c=col_idx: self._on_cell_click(r, c))

    def _on_header_click(self, col_idx):
        """Handle header click to sort the table"""
        if self.sort_column == col_idx:  # Toggle ascending/descending if the column is clicked again
            self.sort_ascending = not self.sort_ascending
        else:
            self.sort_column = col_idx  # Sort by new column
            self.sort_ascending = True
        
        # Sort data based on the clicked column
        self.data.sort(
            key=lambda x: (x[col_idx] is None, x[col_idx]),
            reverse=not self.sort_ascending
        )
        self.refresh()  # Refresh the table display

    def _on_filter(self, filter_val, *args):
        """Filter rows based on the input"""
        filter_text = filter_val
        if filter_text:
            # Filter the data by matching any cell in a row with the filter text
            self.data = [
                row for row in self.original_data
                if any(str(cell).lower().find(filter_text) >= 0 for cell in row)
            ]
        else:
            self.data = list(self.original_data)  # Reset data if no filter text
        
        # Maintain sorting order after filtering
        if self.sort_column is not None:
            self.data.sort(
                key=lambda x: (x[self.sort_column] is None, x[self.sort_column]),
                reverse=not self.sort_ascending
            )
        
        self.refresh()  # Refresh table to show filtered data

    def _on_vsb(self, *args):
        """Handle vertical scrollbar visibility and movement"""
        if self.table_frame.winfo_height() > self.canvas.winfo_height():
            self.vsb.pack(side="right", fill="y")  # Show scrollbar
            self.dummy_scrollbar.pack(side="right", fill="y")
            self.vsb.set(*args)  # Update scrollbar position
        else:
            self.vsb.pack_forget()  # Hide scrollbar if content fits
            self.dummy_scrollbar.pack_forget()
            self.canvas.yview_moveto(0)  # Reset canvas view

    def _on_row_hover(self, row_idx, entering):
        """Handle row hover effect"""
        bg_color = self.style['row_hover_bg'] if entering else \
                   (self.style['row_bg_even'] if row_idx % 2 == 0 else self.style['row_bg_odd'])
        
        for widget in self.table_frame.grid_slaves(row=row_idx):  # Update row background color on hover
            widget.configure(bg=bg_color)

    def _on_cell_click(self, row_idx, entering):
        """Handle click on a table cell"""
        selected_record = (self.data[row_idx], row_idx)  # Get the selected row data
        self.get_data(selected_record)  # Callback function with selected data

    def _bind_mouse_scroll(self):
        """Bind mouse scroll for the canvas"""
        def _on_mousewheel(event):
            if self.table_frame.winfo_height() > self.canvas.winfo_height():
                if event.num == 4 or event.num == 5:
                    delta = -1 if event.num == 5 else 1
                else:
                    delta = event.delta // 120
                self.canvas.yview_scroll(-delta, "units")  # Scroll the table on mouse wheel event
        
        self.bind_all("<MouseWheel>", _on_mousewheel)  # Bind mouse wheel events
        self.bind_all("<Button-4>", _on_mousewheel)
        self.bind_all("<Button-5>", _on_mousewheel)

    def _on_frame_configure(self, event=None):
        """Handle frame configuration changes (resize, etc.)"""
        bbox = self.canvas.bbox("all")  # Get bounding box of canvas content
        if bbox:
            x1, y1, x2, y2 = bbox
            self.canvas.configure(scrollregion=(x1, y1, x2, y2 + 5))  # Update scroll region
        self.canvas.after(100, lambda: self._on_vsb(*self.canvas.yview()))  # Update vertical scrollbar

    def _on_canvas_configure(self, event):
        """Handle canvas resizing"""
        self.canvas.itemconfig(self.canvas_window, width=event.width)  # Resize the window inside the canvas
        self.canvas.after(100, lambda: self._on_vsb(*self.canvas.yview()))  # Update vertical scrollbar

    def refresh(self):
        """Refresh the entire table (e.g., after sorting or filtering)"""
        for widget in self.header_frame.winfo_children():  # Destroy all header widgets
            widget.destroy()
        for widget in self.table_frame.winfo_children():  # Destroy all table widgets
            widget.destroy()
        
        self._create_header()  # Recreate the header
        self._create_table()  # Recreate the table

    def add_row(self, row_data):
        """Add a new row to the table"""
        self.original_data.append(row_data)  # Add to original data
        self.data.append(row_data)  # Add to current table data
        self.refresh()  # Refresh table display with new data

    def set_style(self, **kwargs):
        """Update the style of the table"""
        self.style.update(kwargs)  # Update the style dictionary with new styles
        self.refresh()  # Refresh table display with updated styles

    def clear(self):
        """Clear the filter and reset the table data"""
        self._on_filter('')  # Reset the table data to the original state
        self.refresh()  # Refresh the table to show the original data

