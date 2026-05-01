function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    sidebar.style.width = sidebar.style.width === "250px" ? "0" : "250px";
}

document.addEventListener("DOMContentLoaded", () => {
    console.log("Search Tasks JS Loaded");

    const form = document.getElementById("search-tasks-form");
    const results = document.querySelector(".search-results");

    form.addEventListener("submit", (e) => {
        e.preventDefault();
        console.log("Form submitted, handling via AJAX");

        const priority = document.getElementById("priority").value;

        $.ajax({
            url: '/teacher/api/search_tasks/',
            method: 'POST',
            headers: {
                'X-CSRFToken': getCsrfToken(),
                'Content-Type': 'application/json'
            },
            data: JSON.stringify({ priority }),
            success: function(response) {
                console.log("AJAX Success:", response);
                if (response.success) {
                    results.innerHTML = response.tasks.map(task => `<li>Task ID: ${task.id} - ${task.name} - Priority: ${task.priority}</li>`).join('');
                } else {
                    results.innerHTML = '<li>No tasks found!</li>';
                }
            },
            error: function(xhr, status, error) {
                console.error("AJAX Error:", status, error);
                results.innerHTML = '<li>An error occurred. Please try again.</li>';
            }
        });
    });

    function getCsrfToken() {
        const cookieValue = document.cookie
            .split('; ')
            .find(row => row.startsWith('csrftoken'))
            ?.split('=')[1];
        return cookieValue || '';
    }
});