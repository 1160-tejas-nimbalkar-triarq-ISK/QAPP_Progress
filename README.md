# QAAP Demo Tracker

A beautiful web application for tracking QA team progress and demo sequences for weekly QAAP calls.

## Features

- **Demo Sequence Tracker**: Automatically displays team members in alphabetical order for demo sequence
- **Weekly Progress Tracking**: Track each team member's progress including:
  - Whether they gave demo
  - Number of test cases covered
  - Excel sheet update status
- **Visual Analytics**: Interactive charts showing:
  - Test cases covered per member
  - Excel update status distribution
  - Demo completion status
- **Data Export**: Export progress data to CSV (Excel) or JSON format
- **Data Import**: Import previously saved data from JSON files
- **Beautiful UI**: Modern, responsive design with smooth animations

## Team Members

The application tracks progress for the following QA team members (in alphabetical order):
1. Somraj Navale
2. Sunil Chaudhari
3. Supriya Jethwa
4. Tejas Nimbalkar
5. Tulasi Ram Kurapati
6. Ujwala Gavit
7. Yogita Nikam

## How to Use

1. **Open the Application**: Simply open `index.html` in a web browser
2. **Select Week**: Choose the date for the QAAP call (defaults to next Wednesday)
3. **Add New Week**: Click "Add New Week" to start tracking for a new week
4. **Update Progress**: Click on any team member's card to update their progress
5. **View Analytics**: Charts automatically update based on the selected week
6. **Export Data**: Use the export buttons to save data as CSV or JSON

## Data Storage

All data is stored in the browser's localStorage, so it persists between sessions. You can also export and import data using the JSON format for backup or sharing.

## Browser Compatibility

Works on all modern browsers (Chrome, Firefox, Safari, Edge).


