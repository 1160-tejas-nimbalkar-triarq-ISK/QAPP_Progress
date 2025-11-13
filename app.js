// QA Team Members (31 members - can be reordered via drag and drop)
let teamMembers = [
    'Archana Mali',
    'Dhananjay Wagh',
    'Ganesh Nawale',
    'Garima Prasad',
    'Harshal Pawar',
    'Jagdish Bagul',
    'Jayesh Ambekar',
    'Lalita Labhade',
    'Mayur Mate',
    'Mayur Sonawane',
    'Namita Koik',
    'Namrata Borkar',
    'Nikita Dighe',
    'Pooja Sabankar',
    'Poonam Karande',
    'Pournima Ghanmode',
    'Prajakta Ghate',
    'Pravallika Naidu',
    'Pravina Khandbahale',
    'Purva Gadekar',
    'Rachana Mohadikar',
    'Sachin Sanap',
    'Shirish Bhavsar',
    'Somraj Navale',
    'Sunil Chaudhari',
    'Supriya Jethwa',
    'Tejas Nimbalkar',
    'Tulasi Ram Kurapati',
    'Ujwala Gavit',
    'Yogita Nikam'
];

// Data structure to store progress
let progressData = {};

// Chart instances
let testCasesChart = null;
let excelStatusChart = null;
let demoChart = null;
let memberProgressChart = null;

// Current view mode: 'table' or 'graph'
let currentViewMode = 'table';

// Currently searched/filtered members
let filteredMembers = [...teamMembers];

// Drag and drop state
let draggedElement = null;

// Sequence view state
let sequenceViewExpanded = false;

// Sorting state
let sortOrder = 'none'; // 'none', 'asc', 'desc'
let sortedMembers = [...teamMembers];

// Table sorting state
let tableSortColumn = null;
let tableSortDirection = 'asc';

// Admin authentication state
let isAdmin = false;
const ADMIN_PASSWORD = 'QA@2025';

// Data sync state (removed third-party cloud sync)

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    checkAdminStatus(); // Check if user is already logged in as admin
    loadData();
    loadMemberSequence(); // Load saved sequence
    filteredMembers = [...teamMembers]; // Initialize filtered members
    updateAdminUI(); // Update UI based on admin status
    renderDemoSequence();
    setupWeekSelector();
    setupSearchBox();
    setupViewToggle();
    updateViewButtons(); // Initialize view buttons
    updateButtonStates(); // Initialize button states
    renderProgressCards();
    renderCharts();
    
    // Set default week to next Wednesday
    const nextWednesday = getNextWednesday();
    document.getElementById('weekSelect').value = nextWednesday;
    
    // Form submission handler
    document.getElementById('progressForm').addEventListener('submit', saveProgress);
    
    // Update button states when date input changes
    const weekSelect = document.getElementById('weekSelect');
    weekSelect.addEventListener('input', function() {
        updateButtonStates();
    });
    
    // Setup login modal
    setupLoginModal();
});

// Get next Wednesday date
function getNextWednesday() {
    const today = new Date();
    const dayOfWeek = today.getDay();
    const daysUntilWednesday = (3 - dayOfWeek + 7) % 7 || 7;
    const nextWednesday = new Date(today);
    nextWednesday.setDate(today.getDate() + daysUntilWednesday);
    return nextWednesday.toISOString().split('T')[0];
}

// Render demo sequence (with drag and drop)
function renderDemoSequence() {
    const container = document.getElementById('sequenceContainer');
    container.innerHTML = '';
    
    // Apply sorting if needed
    let membersToDisplay = [...teamMembers];
    if (sortOrder !== 'none') {
        membersToDisplay = [...teamMembers].sort((a, b) => {
            const comparison = a.localeCompare(b);
            return sortOrder === 'asc' ? comparison : -comparison;
        });
    }
    
    // Limit to first 5 if not expanded
    const displayCount = sequenceViewExpanded ? membersToDisplay.length : 5;
    const membersToShow = membersToDisplay.slice(0, displayCount);
    
    membersToShow.forEach((member, displayIndex) => {
        const actualIndex = teamMembers.indexOf(member);
        // Use display index + 1 for sequence number when sorted, otherwise use actual index
        const sequenceNumber = sortOrder !== 'none' ? displayIndex + 1 : actualIndex + 1;
        const item = document.createElement('div');
        item.className = 'sequence-item';
        item.draggable = isAdmin; // Only draggable if admin
        item.dataset.index = actualIndex;
        item.dataset.member = member;
        const dragHandle = isAdmin ? '<span class="drag-handle">☰</span>' : '';
        item.innerHTML = `
            ${dragHandle}
            <span class="sequence-number">${sequenceNumber}</span>
            <span>${member}</span>
        `;
        
        // Drag and drop event listeners (only for admin)
        if (isAdmin) {
            item.addEventListener('dragstart', handleDragStart);
            item.addEventListener('dragover', handleDragOver);
            item.addEventListener('drop', handleDrop);
            item.addEventListener('dragend', handleDragEnd);
        }
        
        container.appendChild(item);
    });
    
    // Add "See All" / "See Less" button if there are more than 5 members
    if (membersToDisplay.length > 5) {
        const buttonContainer = document.createElement('div');
        buttonContainer.className = 'see-all-container';
        const seeAllBtn = document.createElement('button');
        seeAllBtn.className = 'btn btn-secondary';
        const icon = sequenceViewExpanded ? '👆' : '👇';
        const text = sequenceViewExpanded ? 'See Less' : `See All (${membersToDisplay.length - 5})`;
        seeAllBtn.innerHTML = `<span class="btn-icon">${icon}</span> ${text}`;
        seeAllBtn.onclick = function() {
            sequenceViewExpanded = !sequenceViewExpanded;
            renderDemoSequence();
        };
        buttonContainer.appendChild(seeAllBtn);
        container.appendChild(buttonContainer);
    }
    
    // Add sorting controls
    const sortContainer = document.createElement('div');
    sortContainer.className = 'sort-controls';
    sortContainer.innerHTML = `
        <label for="sortSelect">Sort:</label>
        <select id="sortSelect" class="sort-select" onchange="handleSortChange(this.value)">
            <option value="none" ${sortOrder === 'none' ? 'selected' : ''}>None</option>
            <option value="asc" ${sortOrder === 'asc' ? 'selected' : ''}>Alphabetically (A-Z)</option>
            <option value="desc" ${sortOrder === 'desc' ? 'selected' : ''}>Alphabetically (Z-A)</option>
        </select>
    `;
    container.appendChild(sortContainer);
}

// Handle sort change
function handleSortChange(value) {
    sortOrder = value;
    renderDemoSequence();
}

// Admin authentication functions
function checkAdminStatus() {
    const adminStatus = localStorage.getItem('qaapAdminLoggedIn');
    isAdmin = adminStatus === 'true';
}

function loginAdmin(password) {
    if (password === ADMIN_PASSWORD) {
        isAdmin = true;
        localStorage.setItem('qaapAdminLoggedIn', 'true');
        updateAdminUI();
        closeLoginModal();
        alert('Admin login successful! You can now add, edit, and delete data.');
        return true;
    } else {
        alert('Incorrect password! Please try again.');
        document.getElementById('adminPassword').value = '';
        document.getElementById('adminPassword').focus();
        return false;
    }
}

function logoutAdmin() {
    isAdmin = false;
    localStorage.removeItem('qaapAdminLoggedIn');
    updateAdminUI();
    renderDemoSequence();
    renderProgressCards();
    alert('Logged out successfully!');
}

function updateAdminUI() {
    // Update login/logout button
    const loginBtn = document.getElementById('adminLoginBtn');
    const logoutBtn = document.getElementById('adminLogoutBtn');
    
    if (isAdmin) {
        if (loginBtn) loginBtn.style.display = 'none';
        if (logoutBtn) logoutBtn.style.display = 'inline-flex';
    } else {
        if (loginBtn) loginBtn.style.display = 'inline-flex';
        if (logoutBtn) logoutBtn.style.display = 'none';
    }
    
    // Update button states
    updateButtonStates();
    
    // Re-render to update edit buttons
    renderProgressCards();
}

function setupLoginModal() {
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const password = document.getElementById('adminPassword').value;
            loginAdmin(password);
        });
    }
}

function openLoginModal() {
    const modal = document.getElementById('loginModal');
    if (modal) {
        modal.style.display = 'block';
        document.getElementById('adminPassword').value = '';
        document.getElementById('adminPassword').focus();
    }
}

function closeLoginModal() {
    const modal = document.getElementById('loginModal');
    if (modal) {
        modal.style.display = 'none';
        document.getElementById('adminPassword').value = '';
    }
}

// Drag and drop handlers
function handleDragStart(e) {
    draggedElement = this;
    this.style.opacity = '0.5';
    e.dataTransfer.effectAllowed = 'move';
    e.dataTransfer.setData('text/html', this.innerHTML);
}

function handleDragOver(e) {
    if (e.preventDefault) {
        e.preventDefault();
    }
    e.dataTransfer.dropEffect = 'move';
    this.style.borderTop = '3px solid #fff';
    return false;
}

function handleDrop(e) {
    if (e.stopPropagation) {
        e.stopPropagation();
    }
    
    this.style.borderTop = '';
    
    if (draggedElement !== this) {
        const draggedIndex = parseInt(draggedElement.dataset.index);
        const targetIndex = parseInt(this.dataset.index);
        
        // Reorder array
        const draggedMember = teamMembers[draggedIndex];
        teamMembers.splice(draggedIndex, 1);
        teamMembers.splice(targetIndex, 0, draggedMember);
        
        // Update filtered members if needed
        if (filteredMembers.length === teamMembers.length) {
            filteredMembers = [...teamMembers];
        }
        
        // Save sequence
        saveMemberSequence();
        
        // Re-render
        renderDemoSequence();
    }
    
    return false;
}

function handleDragEnd(e) {
    this.style.opacity = '1';
    this.style.borderTop = '';
    // Reset all items
    document.querySelectorAll('.sequence-item').forEach(item => {
        item.style.borderTop = '';
    });
    draggedElement = null;
}

// Save member sequence to localStorage
function saveMemberSequence() {
    localStorage.setItem('qaapMemberSequence', JSON.stringify(teamMembers));
}

// Load member sequence from localStorage
function loadMemberSequence() {
    const saved = localStorage.getItem('qaapMemberSequence');
    if (saved) {
        try {
            const savedMembers = JSON.parse(saved);
            // Merge with current members (in case new members were added)
            const allMembers = [...new Set([...savedMembers, ...teamMembers])];
            teamMembers = allMembers;
        } catch (e) {
            console.error('Error loading member sequence:', e);
        }
    }
}

// Setup search box
function setupSearchBox() {
    const searchBox = document.getElementById('memberSearch');
    if (searchBox) {
        searchBox.addEventListener('input', function(e) {
            const searchTerm = e.target.value.toLowerCase().trim();
            if (searchTerm === '') {
                filteredMembers = [...teamMembers];
            } else {
                filteredMembers = teamMembers.filter(member => 
                    member.toLowerCase().includes(searchTerm)
                );
            }
            renderProgressCards();
            renderCharts();
        });
    }
}

// Check if member has any data for the week
function hasMemberData(member, weekDate) {
    return progressData[weekDate] && 
           progressData[weekDate][member] && 
           (progressData[weekDate][member].gaveDemo || 
            progressData[weekDate][member].testCases > 0 || 
            progressData[weekDate][member].excelUpdated);
}

// Helper function to get members to show (handles search filtering)
function getMembersToShow() {
    const searchBox = document.getElementById('memberSearch');
    const hasSearch = searchBox && searchBox.value.trim() !== '';
    return hasSearch && filteredMembers.length > 0 ? filteredMembers : teamMembers;
}

// Setup view toggle
function setupViewToggle() {
    const tableBtn = document.getElementById('tableViewBtn');
    const graphBtn = document.getElementById('graphViewBtn');
    
    if (tableBtn) {
        tableBtn.addEventListener('click', function() {
            currentViewMode = 'table';
            updateViewButtons();
            renderProgressCards();
        });
    }
    
    if (graphBtn) {
        graphBtn.addEventListener('click', function() {
            currentViewMode = 'graph';
            updateViewButtons();
            renderProgressCards();
            renderMemberProgressChart();
        });
    }
}

// Update view toggle buttons
function updateViewButtons() {
    const tableBtn = document.getElementById('tableViewBtn');
    const graphBtn = document.getElementById('graphViewBtn');
    
    if (tableBtn && graphBtn) {
        if (currentViewMode === 'table') {
            tableBtn.classList.add('active');
            graphBtn.classList.remove('active');
        } else {
            graphBtn.classList.add('active');
            tableBtn.classList.remove('active');
        }
    }
}

// Setup week selector
function setupWeekSelector() {
    const weekSelect = document.getElementById('weekSelect');
    updateWeekDropdown();
    weekSelect.addEventListener('change', function() {
        updateButtonStates();
        renderProgressCards();
        renderCharts();
    });
    
    // Also listen to dropdown changes
    setTimeout(() => {
        const weekSelectDropdown = document.getElementById('weekSelectDropdown');
        if (weekSelectDropdown) {
            weekSelectDropdown.addEventListener('change', function() {
                updateButtonStates();
                renderProgressCards();
                renderCharts();
            });
        }
    }, 200);
}

// Update button states based on current selection
function updateButtonStates() {
    const weekDate = getCurrentWeekSelection();
    const deleteBtn = document.getElementById('deleteWeekBtn');
    const exportCSVBtn = document.getElementById('exportCSVBtn');
    const addWeekBtn = document.getElementById('addWeekBtn');
    
    // Delete button: enabled only if admin, week is selected and exists
    if (deleteBtn) {
        if (isAdmin && weekDate && progressData[weekDate]) {
            deleteBtn.disabled = false;
            deleteBtn.classList.remove('disabled');
            deleteBtn.style.display = 'inline-flex';
        } else {
            deleteBtn.disabled = true;
            deleteBtn.classList.add('disabled');
            deleteBtn.style.display = isAdmin ? 'inline-flex' : 'none';
        }
    }
    
    // Export CSV button: enabled only if week is selected and has data (available to all)
    if (exportCSVBtn) {
        if (weekDate && progressData[weekDate]) {
            exportCSVBtn.disabled = false;
            exportCSVBtn.classList.remove('disabled');
        } else {
            exportCSVBtn.disabled = true;
            exportCSVBtn.classList.add('disabled');
        }
    }
    
    // Add Week button: enabled only if admin and date is selected (from date input)
    if (addWeekBtn) {
        if (!isAdmin) {
            addWeekBtn.style.display = 'none';
        } else {
            addWeekBtn.style.display = 'inline-flex';
            const weekSelect = document.getElementById('weekSelect');
            const hasDateInput = weekSelect && weekSelect.value;
            if (hasDateInput) {
                addWeekBtn.disabled = false;
                addWeekBtn.classList.remove('disabled');
            } else {
                // Check if dropdown exists and we can add new week
                const weekSelectDropdown = document.getElementById('weekSelectDropdown');
                if (!weekSelectDropdown || weekSelectDropdown.style.display === 'none') {
                    addWeekBtn.disabled = true;
                    addWeekBtn.classList.add('disabled');
                } else {
                    addWeekBtn.disabled = false;
                    addWeekBtn.classList.remove('disabled');
                }
            }
        }
    }
}

// Update week dropdown with all available weeks
function updateWeekDropdown() {
    const weekSelect = document.getElementById('weekSelect');
    const allWeeks = Object.keys(progressData).sort().reverse(); // Most recent first
    
    // Store current selection
    const currentValue = weekSelect.value;
    
    // Clear existing options except the first one (date input)
    // Actually, we'll replace the date input with a select dropdown
    const weekSelectorContainer = weekSelect.parentElement;
    const label = weekSelectorContainer.querySelector('label');
    
    // Create select dropdown
    let weekSelectDropdown = document.getElementById('weekSelectDropdown');
    if (!weekSelectDropdown) {
        weekSelectDropdown = document.createElement('select');
        weekSelectDropdown.id = 'weekSelectDropdown';
        weekSelectDropdown.className = 'date-input';
        weekSelectDropdown.style.display = 'none'; // Hide initially if no weeks
        weekSelectDropdown.innerHTML = '<option value="">Select a week...</option>';
        
        // Add change handler
        weekSelectDropdown.addEventListener('change', function() {
            const selectedWeek = this.value;
            if (selectedWeek) {
                document.getElementById('weekSelect').value = selectedWeek;
                updateButtonStates();
                renderProgressCards();
                renderCharts();
            } else {
                updateButtonStates();
            }
        });
        
        weekSelect.parentNode.insertBefore(weekSelectDropdown, weekSelect.nextSibling);
    }
    
    // Update dropdown options
    weekSelectDropdown.innerHTML = '<option value="">Select a week...</option>';
    allWeeks.forEach(week => {
        const option = document.createElement('option');
        option.value = week;
        option.textContent = formatDate(week);
        if (week === currentValue) {
            option.selected = true;
        }
        weekSelectDropdown.appendChild(option);
    });
    
    // Show/hide based on whether weeks exist
    if (allWeeks.length > 0) {
        weekSelectDropdown.style.display = 'block';
        weekSelect.style.display = 'none';
        // Set the date input value to match dropdown
        if (weekSelectDropdown.value) {
            weekSelect.value = weekSelectDropdown.value;
        }
    } else {
        weekSelectDropdown.style.display = 'none';
        weekSelect.style.display = 'block';
    }
    
    // Update button states after dropdown update
    updateButtonStates();
}

// Delete week function
function deleteWeek(weekDateParam) {
    let weekDate = weekDateParam || getCurrentWeekSelection();
    if (!weekDate) {
        alert('Please select a week to delete!');
        return;
    }
    
    if (confirm(`Are you sure you want to delete all progress data for ${formatDate(weekDate)}? This action cannot be undone.`)) {
        delete progressData[weekDate];
        saveData();
        updateWeekDropdown();
        
        // Clear selection if deleted week was selected
        const weekSelect = document.getElementById('weekSelect');
        const weekSelectDropdown = document.getElementById('weekSelectDropdown');
        if (weekSelect.value === weekDate || (weekSelectDropdown && weekSelectDropdown.value === weekDate)) {
            weekSelect.value = '';
            if (weekSelectDropdown) {
                weekSelectDropdown.value = '';
            }
        }
        
        updateButtonStates();
        renderProgressCards();
        renderCharts();
        alert('Week deleted successfully!');
    }
}

// Add new week
function addNewWeek() {
    let weekDate = getCurrentWeekSelection();
    if (!weekDate) {
        // Try to get from date input if dropdown is empty
        const weekSelect = document.getElementById('weekSelect');
        weekDate = weekSelect.value;
        if (!weekDate) {
            alert('Please select a date first!');
            return;
        }
    }
    
    if (!progressData[weekDate]) {
        progressData[weekDate] = {};
        teamMembers.forEach(member => {
            progressData[weekDate][member] = {
                gaveDemo: false,
                testCases: 0,
                excelUpdated: false
            };
        });
        saveData();
        updateWeekDropdown();
        updateButtonStates();
        renderProgressCards();
        renderCharts();
        alert('New week added successfully!');
    } else {
        alert('This week already exists!');
    }
}

// Helper function to get current week selection
function getCurrentWeekSelection() {
    const weekSelect = document.getElementById('weekSelect');
    const weekSelectDropdown = document.getElementById('weekSelectDropdown');
    return weekSelect.value || (weekSelectDropdown && weekSelectDropdown.value) || '';
}

// Render progress cards (table or graph view)
function renderProgressCards() {
    const weekDate = getCurrentWeekSelection();
    const container = document.getElementById('progressGrid');
    container.innerHTML = '';
    
    if (!weekDate) {
        container.innerHTML = '<p style="text-align: center; color: #999; padding: 20px;">Please select a week to view progress</p>';
        return;
    }
    
    if (!progressData[weekDate]) {
        container.innerHTML = '<p style="text-align: center; color: #999; padding: 20px;">No data for this week. Click "Add New Week" to start tracking.</p>';
        return;
    }
    
    // Filter members based on search
    const membersToShow = getMembersToShow();
    
    if (currentViewMode === 'table') {
        renderTableView(container, weekDate, membersToShow);
    } else {
        container.innerHTML = '<div id="memberProgressChartContainer" style="width: 100%; height: 400px;"><canvas id="memberProgressChart"></canvas></div>';
        // Small delay to ensure DOM is ready
        setTimeout(() => renderMemberProgressChart(), 50);
    }
}

// Render table view
function renderTableView(container, weekDate, membersToShow) {
    const searchBox = document.getElementById('memberSearch');
    const hasSearch = searchBox && searchBox.value.trim() !== '';
    
    // If searching, show weekly progress details
    if (hasSearch && filteredMembers.length > 0) {
        renderWeeklyProgressTable(container, membersToShow);
        return;
    }
    
    // Regular single week table
    const table = document.createElement('table');
    table.className = 'progress-table';
    table.innerHTML = `
        <thead>
            <tr>
                <th onclick="sortTable('name')" class="sortable">Member Name <span class="sort-icon"></span></th>
                <th onclick="sortTable('demo')" class="sortable">Gave Demo <span class="sort-icon"></span></th>
                <th onclick="sortTable('testCases')" class="sortable">Test Cases <span class="sort-icon"></span></th>
                <th onclick="sortTable('excel')" class="sortable">Excel Updated <span class="sort-icon"></span></th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            ${membersToShow.map(member => {
                const memberData = progressData[weekDate][member] || {
                    gaveDemo: false,
                    testCases: 0,
                    excelUpdated: false
                };
                const hasData = hasMemberData(member, weekDate);
                const buttonText = hasData ? 'Edit' : 'Add';
                const buttonClass = hasData ? 'btn-primary' : 'btn-success';
                return `
                    <tr>
                        <td><strong>${member}</strong></td>
                        <td>
                            <span class="status-badge ${memberData.gaveDemo ? 'status-yes' : 'status-no'}">
                                ${memberData.gaveDemo ? 'Yes' : 'No'}
                            </span>
                        </td>
                        <td><span class="progress-value">${memberData.testCases}</span></td>
                        <td>
                            <span class="status-badge ${memberData.excelUpdated ? 'status-yes' : 'status-no'}">
                                ${memberData.excelUpdated ? 'Yes' : 'No'}
                            </span>
                        </td>
                        <td>
                            ${isAdmin ? `
                                <button class="btn ${buttonClass} btn-small" onclick="openEditModal('${member.replace(/'/g, "\\'")}', '${weekDate}')">
                                    ${buttonText}
                                </button>
                            ` : '<span class="view-only-badge">View Only</span>'}
                        </td>
                    </tr>
                `;
            }).join('')}
        </tbody>
    `;
    container.appendChild(table);
    updateSortIcons();
}

// Render weekly progress table for searched members
function renderWeeklyProgressTable(container, membersToShow) {
    const allWeeks = Object.keys(progressData).sort().reverse(); // Most recent first
    
    if (allWeeks.length === 0) {
        container.innerHTML = '<p style="text-align: center; color: #999; padding: 20px;">No weekly data available. Add a week first.</p>';
        return;
    }
    
    const table = document.createElement('table');
    table.className = 'progress-table weekly-progress-table';
    table.innerHTML = `
        <thead>
            <tr>
                <th onclick="sortWeeklyTable('name')" class="sortable">Member Name <span class="sort-icon"></span></th>
                ${allWeeks.map(week => `
                    <th onclick="sortWeeklyTable('week-${week}')" class="sortable">
                        ${formatDate(week)} <span class="sort-icon"></span>
                    </th>
                `).join('')}
            </tr>
        </thead>
        <tbody>
            ${membersToShow.map(member => {
                return `
                    <tr>
                        <td><strong>${member}</strong></td>
                        ${allWeeks.map(week => {
                            const weekData = progressData[week] || {};
                            const memberData = weekData[member] || {
                                gaveDemo: false,
                                testCases: 0,
                                excelUpdated: false
                            };
                            const clickHandler = isAdmin ? `onclick="openEditModal('${member.replace(/'/g, "\\'")}', '${week}')"` : '';
                            const cursorStyle = isAdmin ? 'cursor: pointer;' : 'cursor: default;';
                            return `
                                <td class="weekly-cell" ${clickHandler} style="${cursorStyle}">
                                    <div class="weekly-progress">
                                        <div class="weekly-item">
                                            <span class="weekly-label">Demo:</span>
                                            <span class="status-badge ${memberData.gaveDemo ? 'status-yes' : 'status-no'}">
                                                ${memberData.gaveDemo ? 'Yes' : 'No'}
                                            </span>
                                        </div>
                                        <div class="weekly-item">
                                            <span class="weekly-label">Cases:</span>
                                            <span class="progress-value">${memberData.testCases}</span>
                                        </div>
                                        <div class="weekly-item">
                                            <span class="weekly-label">Excel:</span>
                                            <span class="status-badge ${memberData.excelUpdated ? 'status-yes' : 'status-no'}">
                                                ${memberData.excelUpdated ? 'Yes' : 'No'}
                                            </span>
                                        </div>
                                    </div>
                                </td>
                            `;
                        }).join('')}
                    </tr>
                `;
            }).join('')}
        </tbody>
    `;
    container.appendChild(table);
    updateSortIcons();
}

// Sort table function
function sortTable(column) {
    const weekDate = getCurrentWeekSelection();
    if (!weekDate || !progressData[weekDate]) return;
    
    if (tableSortColumn === column) {
        tableSortDirection = tableSortDirection === 'asc' ? 'desc' : 'asc';
    } else {
        tableSortColumn = column;
        tableSortDirection = 'asc';
    }
    
    const membersToShow = getMembersToShow();
    const sorted = [...membersToShow].sort((a, b) => {
        const dataA = progressData[weekDate][a] || { gaveDemo: false, testCases: 0, excelUpdated: false };
        const dataB = progressData[weekDate][b] || { gaveDemo: false, testCases: 0, excelUpdated: false };
        
        let comparison = 0;
        switch(column) {
            case 'name':
                comparison = a.localeCompare(b);
                break;
            case 'demo':
                comparison = (dataA.gaveDemo ? 1 : 0) - (dataB.gaveDemo ? 1 : 0);
                break;
            case 'testCases':
                comparison = dataA.testCases - dataB.testCases;
                break;
            case 'excel':
                comparison = (dataA.excelUpdated ? 1 : 0) - (dataB.excelUpdated ? 1 : 0);
                break;
        }
        return tableSortDirection === 'asc' ? comparison : -comparison;
    });
    
    // Update filtered members temporarily for rendering
    const originalFiltered = [...filteredMembers];
    filteredMembers = sorted;
    renderProgressCards();
    filteredMembers = originalFiltered;
    updateSortIcons();
}

// Sort weekly table
function sortWeeklyTable(column) {
    // Toggle sort direction if same column, otherwise set to ascending
    if (tableSortColumn === column) {
        tableSortDirection = tableSortDirection === 'asc' ? 'desc' : 'asc';
    } else {
        tableSortColumn = column;
        tableSortDirection = 'asc';
    }
    
    // Get current members to sort - use getMembersToShow() to get the right list
    let membersToSort = getMembersToShow();
    
    if (column === 'name') {
        // Sort by member name
        membersToSort = membersToSort.sort((a, b) => {
            const comparison = a.localeCompare(b);
            return tableSortDirection === 'asc' ? comparison : -comparison;
        });
    } else if (column.startsWith('week-')) {
        // Sort by week column - extract week date
        const weekDate = column.replace('week-', '');
        membersToSort = membersToSort.sort((a, b) => {
            const weekData = progressData[weekDate] || {};
            const dataA = weekData[a] || { gaveDemo: false, testCases: 0, excelUpdated: false };
            const dataB = weekData[b] || { gaveDemo: false, testCases: 0, excelUpdated: false };
            
            // Sort by test cases (primary), then demo status, then excel status
            let comparison = 0;
            if (dataA.testCases !== dataB.testCases) {
                comparison = dataA.testCases - dataB.testCases;
            } else if (dataA.gaveDemo !== dataB.gaveDemo) {
                comparison = (dataA.gaveDemo ? 1 : 0) - (dataB.gaveDemo ? 1 : 0);
            } else {
                comparison = (dataA.excelUpdated ? 1 : 0) - (dataB.excelUpdated ? 1 : 0);
            }
            
            return tableSortDirection === 'asc' ? comparison : -comparison;
        });
    }
    
    // Update filtered members with sorted order (preserve search state)
    const searchBox = document.getElementById('memberSearch');
    const hasSearch = searchBox && searchBox.value.trim() !== '';
    if (hasSearch) {
        filteredMembers = membersToSort;
    } else {
        // If no search, update teamMembers order for display
        // But we need to maintain the sorted order in filteredMembers for rendering
        filteredMembers = membersToSort;
    }
    
    renderProgressCards();
    updateSortIcons();
}

// Update sort icons
function updateSortIcons() {
    document.querySelectorAll('.sortable').forEach(th => {
        const icon = th.querySelector('.sort-icon');
        if (icon) {
            icon.textContent = '';
            if (th.onclick && tableSortColumn) {
                const onclickAttr = th.getAttribute('onclick');
                if (onclickAttr) {
                    const columnName = onclickAttr.match(/'([^']+)'/)?.[1];
                    if (columnName) {
                        // Check for exact match or if it's a week column match
                        if (columnName === tableSortColumn || 
                            (columnName.startsWith('week-') && tableSortColumn.startsWith('week-') && columnName === tableSortColumn)) {
                            icon.textContent = tableSortDirection === 'asc' ? ' ▲' : ' ▼';
                        }
                    }
                }
            }
        }
    });
}

// Render member progress chart
function renderMemberProgressChart() {
    const weekDate = getCurrentWeekSelection();
    if (!weekDate || !progressData[weekDate]) {
        return;
    }
    
    const membersToShow = getMembersToShow();
    const weekData = progressData[weekDate];
    
    const ctx = document.getElementById('memberProgressChart');
    if (!ctx) {
        // Wait a bit for DOM to update
        setTimeout(renderMemberProgressChart, 100);
        return;
    }
    
    if (memberProgressChart) {
        memberProgressChart.destroy();
    }
    
    memberProgressChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: membersToShow,
            datasets: [
                {
                    label: 'Test Cases',
                    data: membersToShow.map(member => weekData[member]?.testCases || 0),
                    backgroundColor: 'rgba(102, 126, 234, 0.8)',
                    borderColor: 'rgba(102, 126, 234, 1)',
                    borderWidth: 2
                },
                {
                    label: 'Gave Demo (Yes=1, No=0)',
                    data: membersToShow.map(member => weekData[member]?.gaveDemo ? 1 : 0),
                    backgroundColor: 'rgba(76, 175, 80, 0.8)',
                    borderColor: 'rgba(76, 175, 80, 1)',
                    borderWidth: 2
                },
                {
                    label: 'Excel Updated (Yes=1, No=0)',
                    data: membersToShow.map(member => weekData[member]?.excelUpdated ? 1 : 0),
                    backgroundColor: 'rgba(255, 152, 0, 0.8)',
                    borderColor: 'rgba(255, 152, 0, 1)',
                    borderWidth: 2
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            },
            onClick: (event, elements) => {
                if (elements.length > 0) {
                    const index = elements[0].index;
                    const member = membersToShow[index];
                    openEditModal(member, weekDate);
                }
            }
        }
    });
}

// Open edit modal
function openEditModal(member, weekDate) {
    const modal = document.getElementById('editModal');
    const memberData = progressData[weekDate][member] || {
        gaveDemo: false,
        testCases: 0,
        excelUpdated: false
    };
    
    document.getElementById('memberName').value = member;
    document.getElementById('weekDate').value = formatDate(weekDate);
    document.getElementById('gaveDemo').checked = memberData.gaveDemo;
    document.getElementById('testCases').value = memberData.testCases;
    document.getElementById('excelUpdated').checked = memberData.excelUpdated;
    
    modal.style.display = 'block';
}

// Close modal
function closeModal() {
    document.getElementById('editModal').style.display = 'none';
}

// Save progress
function saveProgress(e) {
    e.preventDefault();
    
    const member = document.getElementById('memberName').value;
    const weekDate = document.getElementById('weekSelect').value;
    
    if (!progressData[weekDate]) {
        progressData[weekDate] = {};
    }
    
    progressData[weekDate][member] = {
        gaveDemo: document.getElementById('gaveDemo').checked,
        testCases: parseInt(document.getElementById('testCases').value) || 0,
        excelUpdated: document.getElementById('excelUpdated').checked
    };
    
    saveData();
    renderProgressCards();
    renderCharts();
    closeModal();
}

// Render charts
function renderCharts() {
    const weekDate = getCurrentWeekSelection();
    
    if (!weekDate || !progressData[weekDate]) {
        // Clear charts if no data
        if (testCasesChart) testCasesChart.destroy();
        if (excelStatusChart) excelStatusChart.destroy();
        if (demoChart) demoChart.destroy();
        return;
    }
    
    const weekData = progressData[weekDate];
    const membersToShow = getMembersToShow();
    
    // Test Cases Chart
    const testCasesCtx = document.getElementById('testCasesChart').getContext('2d');
    if (testCasesChart) testCasesChart.destroy();
    testCasesChart = new Chart(testCasesCtx, {
        type: 'bar',
        data: {
            labels: membersToShow,
            datasets: [{
                label: 'Test Cases Covered',
                data: membersToShow.map(member => weekData[member]?.testCases || 0),
                backgroundColor: 'rgba(102, 126, 234, 0.8)',
                borderColor: 'rgba(102, 126, 234, 1)',
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
    
    // Excel Status Chart
    const excelCtx = document.getElementById('excelStatusChart').getContext('2d');
    if (excelStatusChart) excelStatusChart.destroy();
    const excelUpdated = membersToShow.filter(member => weekData[member]?.excelUpdated).length;
    const excelNotUpdated = membersToShow.length - excelUpdated;
    
    excelStatusChart = new Chart(excelCtx, {
        type: 'doughnut',
        data: {
            labels: ['Updated', 'Not Updated'],
            datasets: [{
                data: [excelUpdated, excelNotUpdated],
                backgroundColor: ['#4caf50', '#f44336'],
                borderWidth: 2,
                borderColor: '#fff'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true
        }
    });
    
    // Demo Completion Chart
    const demoCtx = document.getElementById('demoChart').getContext('2d');
    if (demoChart) demoChart.destroy();
    const gaveDemo = membersToShow.filter(member => weekData[member]?.gaveDemo).length;
    const notGaveDemo = membersToShow.length - gaveDemo;
    
    demoChart = new Chart(demoCtx, {
        type: 'pie',
        data: {
            labels: ['Completed', 'Pending'],
            datasets: [{
                data: [gaveDemo, notGaveDemo],
                backgroundColor: ['#667eea', '#ff9800'],
                borderWidth: 2,
                borderColor: '#fff'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true
        }
    });
    
    // Update member progress chart if in graph view
    if (currentViewMode === 'graph') {
        renderMemberProgressChart();
    }
}

// Format date for display
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', { 
        weekday: 'long', 
        year: 'numeric', 
        month: 'long', 
        day: 'numeric' 
    });
}

// Save data to localStorage
function saveData() {
    localStorage.setItem('qaapProgressData', JSON.stringify(progressData));
    saveMemberSequence();
    updateWeekDropdown(); // Update dropdown after saving
}

// Load data from localStorage
function loadData() {
    const saved = localStorage.getItem('qaapProgressData');
    if (saved) {
        progressData = JSON.parse(saved);
    }
    // Update week dropdown after loading
    setTimeout(() => updateWeekDropdown(), 100);
}

// Export to CSV
function exportToCSV() {
    const weekDate = getCurrentWeekSelection();
    if (!weekDate || !progressData[weekDate]) {
        alert('No data available for the selected week!');
        return;
    }
    
    const weekData = progressData[weekDate];
    let csv = 'Member,Gave Demo,Test Cases Covered,Excel Updated\n';
    
    teamMembers.forEach(member => {
        const data = weekData[member] || { gaveDemo: false, testCases: 0, excelUpdated: false };
        csv += `"${member}",${data.gaveDemo ? 'Yes' : 'No'},${data.testCases},${data.excelUpdated ? 'Yes' : 'No'}\n`;
    });
    
    // Create download link
    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    const url = URL.createObjectURL(blob);
    link.setAttribute('href', url);
    link.setAttribute('download', `QAAP_Progress_${weekDate}.csv`);
    link.style.visibility = 'hidden';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

// Export to JSON
function exportToJSON() {
    const dataStr = JSON.stringify(progressData, null, 2);
    const blob = new Blob([dataStr], { type: 'application/json' });
    const link = document.createElement('a');
    const url = URL.createObjectURL(blob);
    link.setAttribute('href', url);
    link.setAttribute('download', 'qaap_progress_data.json');
    link.style.visibility = 'hidden';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

// Import from JSON
function importFromJSON(event) {
    const file = event.target.files[0];
    if (!file) return;
    
    const reader = new FileReader();
    reader.onload = function(e) {
        try {
            progressData = JSON.parse(e.target.result);
            saveData();
            renderProgressCards();
            renderCharts();
            alert('Data imported successfully!');
        } catch (error) {
            alert('Error importing file. Please check the file format.');
        }
    };
    reader.readAsText(file);
}

// Close modal when clicking outside
window.onclick = function(event) {
    const editModal = document.getElementById('editModal');
    const loginModal = document.getElementById('loginModal');
    if (event.target == editModal) {
        closeModal();
    }
    if (event.target == loginModal) {
        closeLoginModal();
    }
}

// Note: Third-party cloud sync removed for office PC compatibility
// Data sharing is done via export/import JSON files

// Removed cloud sync functions - using export/import instead
/*
function loadCloudSyncConfig() {
    const config = localStorage.getItem('qaapCloudSyncConfig');
    if (config) {
        try {
            const parsed = JSON.parse(config);
            cloudSyncEnabled = parsed.enabled || false;
            jsonbinId = parsed.binId || null;
            jsonbinApiKey = parsed.apiKey || null;
        } catch (e) {
            console.error('Error loading cloud sync config:', e);
        }
    }
}

function saveCloudSyncConfig() {
    const binId = document.getElementById('jsonbinId').value.trim();
    const apiKey = document.getElementById('jsonbinApiKey').value.trim();
    
    if (!binId || !apiKey) {
        alert('Please enter both Bin ID and API Key!');
        return;
    }
    
    jsonbinId = binId;
    jsonbinApiKey = apiKey;
    cloudSyncEnabled = true;
    
    localStorage.setItem('qaapCloudSyncConfig', JSON.stringify({
        enabled: true,
        binId: binId,
        apiKey: apiKey
    }));
    
    updateCloudSyncUI();
    startAutoSync();
    syncToCloud(); // Initial sync
    
    document.getElementById('cloudSyncSetup').style.display = 'none';
    alert('Cloud sync enabled! Data will be synced automatically.');
}

function enableCloudSync() {
    document.getElementById('cloudSyncSetup').style.display = 'block';
}

function disableCloudSync() {
    if (confirm('Are you sure you want to disable cloud sync? Data will only be stored locally.')) {
        cloudSyncEnabled = false;
        jsonbinId = null;
        jsonbinApiKey = null;
        
        localStorage.setItem('qaapCloudSyncConfig', JSON.stringify({
            enabled: false
        }));
        
        stopAutoSync();
        updateCloudSyncUI();
        alert('Cloud sync disabled. Data will only be stored locally.');
    }
}

function updateCloudSyncUI() {
    const enableBtn = document.getElementById('enableCloudSyncBtn');
    const disableBtn = document.getElementById('disableCloudSyncBtn');
    const syncNowBtn = document.getElementById('syncNowBtn');
    const syncStatus = document.getElementById('syncStatus');
    const setupDiv = document.getElementById('cloudSyncSetup');
    
    if (cloudSyncEnabled && jsonbinId && jsonbinApiKey) {
        if (enableBtn) enableBtn.style.display = 'none';
        if (disableBtn) disableBtn.style.display = 'inline-flex';
        if (syncNowBtn) syncNowBtn.style.display = 'inline-flex';
        if (syncStatus) syncStatus.textContent = '☁️ Cloud sync enabled';
        if (setupDiv) setupDiv.style.display = 'none';
    } else {
        if (enableBtn) enableBtn.style.display = 'inline-flex';
        if (disableBtn) disableBtn.style.display = 'none';
        if (syncNowBtn) syncNowBtn.style.display = 'none';
        if (syncStatus) syncStatus.textContent = '';
        if (setupDiv) setupDiv.style.display = 'none';
    }
}

async function syncToCloud() {
    if (!cloudSyncEnabled || !jsonbinId || !jsonbinApiKey) return;
    
    const syncStatus = document.getElementById('syncStatus');
    if (syncStatus) syncStatus.textContent = '🔄 Syncing...';
    
    try {
        const dataToSync = {
            progressData: progressData,
            memberSequence: teamMembers,
            lastUpdated: new Date().toISOString()
        };
        
        const response = await fetch(`https://api.jsonbin.io/v3/b/${jsonbinId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'X-Master-Key': jsonbinApiKey
            },
            body: JSON.stringify(dataToSync)
        });
        
        if (response.ok) {
            if (syncStatus) syncStatus.textContent = '✅ Synced ' + new Date().toLocaleTimeString();
            setTimeout(() => {
                if (syncStatus) syncStatus.textContent = '☁️ Cloud sync enabled';
            }, 3000);
        } else {
            throw new Error('Sync failed');
        }
    } catch (error) {
        console.error('Cloud sync error:', error);
        if (syncStatus) syncStatus.textContent = '❌ Sync failed';
        setTimeout(() => {
            if (syncStatus) syncStatus.textContent = '☁️ Cloud sync enabled';
        }, 3000);
    }
}

async function syncFromCloud() {
    if (!cloudSyncEnabled || !jsonbinId || !jsonbinApiKey) return;
    
    try {
        const response = await fetch(`https://api.jsonbin.io/v3/b/${jsonbinId}/latest`, {
            headers: {
                'X-Master-Key': jsonbinApiKey
            }
        });
        
        if (response.ok) {
            const result = await response.json();
            const cloudData = result.record;
            
            if (cloudData.progressData) {
                progressData = cloudData.progressData;
                localStorage.setItem('qaapProgressData', JSON.stringify(progressData));
            }
            
            if (cloudData.memberSequence) {
                teamMembers = cloudData.memberSequence;
                saveMemberSequence();
            }
            
            // Reload UI
            updateWeekDropdown();
            renderDemoSequence();
            renderProgressCards();
            renderCharts();
        }
    } catch (error) {
        console.error('Cloud load error:', error);
    }
}

function startAutoSync() {
    // Sync every 30 seconds
    if (syncInterval) clearInterval(syncInterval);
    syncInterval = setInterval(() => {
        syncFromCloud();
    }, 30000); // 30 seconds
}

function stopAutoSync() {
    if (syncInterval) {
        clearInterval(syncInterval);
        syncInterval = null;
    }
}
*/


