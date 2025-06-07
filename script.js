document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('budget-form');
    const nameInput = document.getElementById('name');
    const amountInput = document.getElementById('amount');
    const budgetList = document.getElementById('budget-list');
    const monthlyIncomeInput = document.getElementById('monthly-income');
    const monthlyExpensesInput = document.getElementById('monthly-expenses');
    const startPlanBtn = document.getElementById('start-plan-btn');
    const budgetSection = document.getElementById('budget-section');
    const incomeExpensesSection = document.getElementById('income-expenses-section');
    const startSection = document.getElementById('start-section');
    const savingsDisplay = document.getElementById('monthly-savings');

    let monthlyIncome = 0;
    let monthlyExpenses = 0;

    function fetchBudgetItems() {
        fetch('/api/budget')
            .then(response => response.json())
            .then(data => {
                budgetList.innerHTML = '';
                let totalBudget = 0;
                data.forEach(item => {
                    const li = document.createElement('li');
                    li.textContent = `${item.name}: $${item.amount.toFixed(2)}`;
                    const deleteBtn = document.createElement('button');
                    deleteBtn.textContent = 'Delete';
                    deleteBtn.className = 'delete-btn';
                    deleteBtn.onclick = () => deleteBudgetItem(item.id);
                    li.appendChild(deleteBtn);
                    budgetList.appendChild(li);
                    totalBudget += item.amount;
                });
                updateSavings(totalBudget);
            });
    }

    function addBudgetItem(name, amount) {
        fetch('/api/budget', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, amount: parseFloat(amount) })
        })
        .then(response => {
            if (response.ok) {
                nameInput.value = '';
                amountInput.value = '';
                fetchBudgetItems();
            }
        });
    }

    function deleteBudgetItem(id) {
        fetch(`/api/budget/${id}`, {
            method: 'DELETE'
        })
        .then(response => {
            if (response.ok) {
                fetchBudgetItems();
            }
        });
    }

    function updateSavings(totalBudget) {
        const savings = monthlyIncome - monthlyExpenses - totalBudget;
        savingsDisplay.textContent = savings.toFixed(2);
    }

    startPlanBtn.addEventListener('click', () => {
        startSection.style.display = 'none';
        incomeExpensesSection.style.display = 'flex';
    });

    monthlyIncomeInput.addEventListener('input', updateSavingsOnInput);
    monthlyExpensesInput.addEventListener('input', updateSavingsOnInput);

    function updateSavingsOnInput() {
        const income = parseFloat(monthlyIncomeInput.value);
        const expenses = parseFloat(monthlyExpensesInput.value);
        if (!isNaN(income) && !isNaN(expenses) && income >= 0 && expenses >= 0) {
            monthlyIncome = income;
            monthlyExpenses = expenses;
            budgetSection.style.display = 'block';
            updateSavings(0);
        } else {
            budgetSection.style.display = 'none';
        }
    }

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const name = nameInput.value.trim();
        const amount = amountInput.value.trim();
        if (name && amount) {
            addBudgetItem(name, amount);
        }
    });

    // Initially hide income-expenses and budget sections
    incomeExpensesSection.style.display = 'none';
    budgetSection.style.display = 'none';
});
