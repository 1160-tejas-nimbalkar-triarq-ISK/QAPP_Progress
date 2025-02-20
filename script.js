let memberData = JSON.parse(localStorage.getItem('memberData')) || [];
let progressData = JSON.parse(localStorage.getItem('progressData')) || [];
let notifications = JSON.parse(localStorage.getItem('notifications')) || [];
let currentPage = 1;
const recordsPerPage = 10;

const tabs = document.querySelectorAll('.tab');
const contentSections = document.querySelectorAll('.content');

tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        const tabId = tab.dataset.tab;

        tabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');

        contentSections.forEach(section => {
            section.classList.remove('show-content');
            if (section.id === tabId) {
                section.classList.add('show-content');
            }
        });
    });
});

document.getElementById('addMember').addEventListener('click', () => {
    document.getElementById('addMemberForm').style.display = 'block';
});

document.getElementById('cancelMember').addEventListener('click', () => {
    document.getElementById('addMemberForm').style.display = 'none';
    document.getElementById('addMemberForm').reset();
});

document.getElementById('submitMember').addEventListener('click', () => {
    const memberName = document.getElementById('memberName').value;
    const memberTeam = document.getElementById('memberTeam').value;

    if (memberName && memberTeam) {
        memberData.push({ name: memberName, team: memberTeam });
        localStorage.setItem('memberData', JSON.stringify(memberData));
        updateMemberTable();
        document.getElementById('addMemberForm').style.display = 'none';
        document.getElementById('addMemberForm').reset();
        updateProgressMemberDropdown();
        updatePraiseMemberDropdown();
        updateTodayDemoDropdown();
        updateMemberFilter();
    } else {
        alert("Please fill in all fields.");
    }
});

document.getElementById('addProgress').addEventListener('click', () => {
    document.getElementById('addProgressForm').style.display = 'block';
});

document.getElementById('cancelProgress').addEventListener('click', () => {
    document.getElementById('addProgressForm').style.display = 'none';
    document.getElementById('addProgressForm').reset();
});

document.getElementById('submitProgress').addEventListener('click', () => {
    const progressTeam = document.getElementById('progressTeam').value;
    const progressMember = document.getElementById('progressMember').value;
    const weekStart = document.getElementById('weekStart').value;
    const weekEnd = document.getElementById('weekEnd').value;

    if (progressTeam && progressMember && weekStart && weekEnd) {
        progressData.push({
            team: progressTeam,
            member: progressMember,
            weekStart: weekStart,
            weekEnd: weekEnd,
            plannedTestCases: parseInt(document.getElementById('plannedTestCases').value),
            completedTestCases: parseInt(document.getElementById('completedTestCases').value),
            plannedTime: parseInt(document.getElementById('plannedTime').value),
            actualTime: parseInt(document.getElementById('actualTime').value),
        });

        localStorage.setItem('progressData', JSON.stringify(progressData));
        updateProgressTable();
        document.getElementById('addProgressForm').style.display = 'none';
        document.getElementById('addProgressForm').reset();
    } else {
        alert("Please fill in all fields.");
    }
});

document.getElementById('updateDetails').addEventListener('click', () => {
    document.getElementById('updateDetailsForm').style.display = 'block';
});

document.getElementById('cancelUpdate').addEventListener('click', () => {
    document.getElementById('updateDetailsForm').style.display = 'none';
    document.getElementById('updateDetailsForm').reset();
});

document.getElementById('submitUpdate').addEventListener('click', () => {
    const todayDemo = document.getElementById('todayDemo').value;
    const praiseMember = document.getElementById('praiseMember').value;
    const praiseMessage = document.getElementById('praiseMessage').value;
    const generalUpdate = document.getElementById('generalUpdate').value;

    if (todayDemo || praiseMember || praiseMessage || generalUpdate) {
        if (praiseMember && praiseMessage) {
            notifications.push({ type: 'praise', member: praiseMember, message: praiseMessage });
        }
        if (generalUpdate) {
            notifications.push({ type: 'update', message: generalUpdate });
        }
        if (todayDemo) {
            notifications.push({ type: 'demo', member: todayDemo, message: 'Demo completed' });
        }
        localStorage.setItem('notifications', JSON.stringify(notifications));
        updateNotificationCards();
        document.getElementById('updateDetailsForm').style.display = 'none';
        document.getElementById('updateDetailsForm').reset();
    } else {
        alert("Please fill in at least one field.");
    }
});

document.getElementById('clearFilters').addEventListener('click', () => {
    document.getElementById('teamFilter').value = '';
    document.getElementById('memberFilter').value = '';
    document.getElementById('dateRangeFilterStart').value = '';
    document.getElementById('dateRangeFilterEnd').value = '';
    currentPage = 1;
    updateProgressTable();
});

function updateMemberTable() {
    const memberTable = document.getElementById('memberTable').getElementsByTagName('tbody')[0];
    memberTable.innerHTML = '';

    const teamMembers = {};
    for (const member of memberData) {
        if (!teamMembers[member.team]) {
            teamMembers[member.team] = [];
        }
        teamMembers[member.team].push(member);
    }

    for (const team in teamMembers) {
        const row = memberTable.insertRow();
        const teamCell = row.insertCell();
        const membersCell = row.insertCell();

        teamCell.textContent = team;
        membersCell.innerHTML = teamMembers[team].map(member => `
            <span>${member.name}</span>
            <i class="fas fa-trash delete-member" data-name="${member.name}" data-team="${member.team}"></i>
        `).join('<br>');
    }

    document.querySelectorAll('.delete-member').forEach(icon => {
        icon.addEventListener('click', () => {
            const name = icon.dataset.name;
            const team = icon.dataset.team;
            memberData = memberData.filter(member => !(member.name === name && member.team === team));
            localStorage.setItem('memberData', JSON.stringify(memberData));
            updateMemberTable();
            updateProgressMemberDropdown();
            updatePraiseMemberDropdown();
            updateTodayDemoDropdown();
            updateMemberFilter();
        });
    });
}

function updateProgressTable() {
    const progressTable = document.getElementById('progressTable').getElementsByTagName('tbody')[0];
    progressTable.innerHTML = '';

    const filteredData = filterProgressData();
    const paginatedData = paginateData(filteredData);

    if (paginatedData.length === 0) {
        progressTable.innerHTML = `<tr><td colspan="9" style="text-align: center;">No records available</td></tr>`;
        return;
    }

    for (const progress of paginatedData) {
        const row = progressTable.insertRow();
        row.insertCell().textContent = progress.member;
        row.insertCell().textContent = progress.team;
        row.insertCell().textContent = progress.weekStart;
        row.insertCell().textContent = progress.weekEnd;
        row.insertCell().textContent = progress.plannedTestCases;
        row.insertCell().textContent = progress.completedTestCases;
        row.insertCell().textContent = progress.plannedTime;
        row.insertCell().textContent = progress.actualTime;
        const actionsCell = row.insertCell();
        actionsCell.innerHTML = `
            <i class="fas fa-eye view-progress" data-member="${progress.member}" data-team="${progress.team}" data-weekStart="${progress.weekStart}" data-weekEnd="${progress.weekEnd}" data-plannedTestCases="${progress.plannedTestCases}" data-completedTestCases="${progress.completedTestCases}" data-plannedTime="${progress.plannedTime}" data-actualTime="${progress.actualTime}"></i>
            <i class="fas fa-trash delete-progress" data-member="${progress.member}" data-team="${progress.team}" data-weekStart="${progress.weekStart}" data-weekEnd="${progress.weekEnd}"></i>
        `;
    }

    document.querySelectorAll('.view-progress').forEach(icon => {
        icon.addEventListener('click', () => {
            const member = icon.dataset.member;
            const team = icon.dataset.team;
            const weekStart = icon.dataset.weekstart;
            const weekEnd = icon.dataset.weekend;
            const plannedTestCases = icon.dataset.plannedtestcases;
            const completedTestCases = icon.dataset.completedtestcases;
            const plannedTime = icon.dataset.plannedtime;
            const actualTime = icon.dataset.actualtime;

            document.getElementById('popupMember').textContent = member;
            document.getElementById('popupTeam').textContent = team;
            document.getElementById('popupWeekStart').textContent = weekStart;
            document.getElementById('popupWeekEnd').textContent = weekEnd;
            document.getElementById('popupPlannedTestCases').textContent = plannedTestCases;
            document.getElementById('popupCompletedTestCases').textContent = completedTestCases;
            document.getElementById('popupPlannedTime').textContent = plannedTime;
            document.getElementById('popupActualTime').textContent = actualTime;

            document.getElementById('memberPopup').style.display = 'flex';
        });
    });

    document.querySelectorAll('.delete-progress').forEach(icon => {
        icon.addEventListener('click', () => {
            const member = icon.dataset.member;
            const team = icon.dataset.team;
            const weekStart = icon.dataset.weekstart;
            const weekEnd = icon.dataset.weekend;

            progressData = progressData.filter(progress => !(progress.member === member && progress.team === team && progress.weekStart === weekStart && progress.weekEnd === weekEnd));
            localStorage.setItem('progressData', JSON.stringify(progressData));
            updateProgressTable();
        });
    });

    updatePaginationInfo(filteredData.length);
}

function filterProgressData() {
    const teamFilter = document.getElementById('teamFilter').value;
    const memberFilter = document.getElementById('memberFilter').value;
    const dateStart = document.getElementById('dateRangeFilterStart').value;
    const dateEnd = document.getElementById('dateRangeFilterEnd').value;

    return progressData.filter(progress => {
        const teamMatch = teamFilter ? progress.team === teamFilter : true;
        const memberMatch = memberFilter ? progress.member === memberFilter : true;
        const dateMatch = (!dateStart || progress.weekStart >= dateStart) && (!dateEnd || progress.weekEnd <= dateEnd);
        return teamMatch && memberMatch && dateMatch;
    });
}

function paginateData(data) {
    const startIndex = (currentPage - 1) * recordsPerPage;
    return data.slice(startIndex, startIndex + recordsPerPage);
}

function updatePaginationInfo(totalRecords) {
    const totalPages = Math.ceil(totalRecords / recordsPerPage);
    document.getElementById('pageInfo').textContent = `Page ${currentPage} of ${totalPages}`;
}

document.getElementById('applyFilters').addEventListener('click', () => {
    currentPage = 1;
    updateProgressTable();
});

document.getElementById('prevPage').addEventListener('click', () => {
    if (currentPage > 1) {
        currentPage--;
        updateProgressTable();
    }
});

document.getElementById('nextPage').addEventListener('click', () => {
    const totalPages = Math.ceil(filterProgressData().length / recordsPerPage);
    if (currentPage < totalPages) {
        currentPage++;
        updateProgressTable();
    }
});

function updateProgressMemberDropdown() {
    const progressMemberDropdown = document.getElementById('progressMember');
    progressMemberDropdown.innerHTML = '<option value="">Select Member</option>';

    for (const member of memberData) {
        const option = document.createElement('option');
        option.value = member.name;
        option.text = member.name;
        progressMemberDropdown.add(option);
    }
}

function updatePraiseMemberDropdown() {
    const praiseMemberDropdown = document.getElementById('praiseMember');
    praiseMemberDropdown.innerHTML = '<option value="">Select Member</option>';

    for (const member of memberData) {
        const option = document.createElement('option');
        option.value = member.name;
        option.text = member.name;
        praiseMemberDropdown.add(option);
    }
}

function updateTodayDemoDropdown() {
    const todayDemoDropdown = document.getElementById('todayDemo');
    todayDemoDropdown.innerHTML = '<option value="">Select Member</option>';

    for (const member of memberData) {
        const option = document.createElement('option');
        option.value = member.name;
        option.text = member.name;
        todayDemoDropdown.add(option);
    }
}

function updateMemberFilter() {
    const memberFilterDropdown = document.getElementById('memberFilter');
    memberFilterDropdown.innerHTML = '<option value="">All Members</option>';

    for (const member of memberData) {
        const option = document.createElement('option');
        option.value = member.name;
        option.text = member.name;
        memberFilterDropdown.add(option);
    }
}

function updateNotificationCards() {
    const notificationContent = document.getElementById('notificationContent');
    const updateContent = document.getElementById('updateContent');
    const thisWeekDemoContent = document.getElementById('thisWeekDemoContent');
    const lastWeekDemoContent = document.getElementById('lastWeekDemoContent');

    notificationContent.innerHTML = '';
    updateContent.innerHTML = '';
    thisWeekDemoContent.innerHTML = '';
    lastWeekDemoContent.innerHTML = '';

    notifications.forEach(notification => {
        const card = document.createElement('div');
        card.className = 'notification-card';
        if (notification.type === 'praise') {
            card.innerHTML = `
                <h4>Praise for ${notification.member}</h4>
                <p>${notification.message}</p>
            `;
            notificationContent.appendChild(card);
        } else if (notification.type === 'update') {
            card.innerHTML = `
                <h4>Update</h4>
                <p>${notification.message}</p>
            `;
            updateContent.appendChild(card);
        } else if (notification.type === 'demo') {
            if (notification.message === 'Demo completed') {
                card.innerHTML = `
                    <h4>This Week Demo</h4>
                    <p>${notification.member}</p>
                `;
                thisWeekDemoContent.appendChild(card);
            } else {
                card.innerHTML = `
                    <h4>Last Week Demo</h4>
                    <p>${notification.member}</p>
                `;
                lastWeekDemoContent.appendChild(card);
            }
        }
    });
}

document.querySelector('.close-popup').addEventListener('click', () => {
    document.getElementById('memberPopup').style.display = 'none';
});

// Initial load
updateMemberTable();
updateProgressTable();
updateNotificationCards();
updateProgressMemberDropdown();
updatePraiseMemberDropdown();
updateTodayDemoDropdown();
updateMemberFilter();