function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    sidebar.style.width = sidebar.style.width === "250px" ? "0" : "250px";
}

document.addEventListener("DOMContentLoaded", () => {
    console.log("Mark Task Completed JS Loaded");

    const taskList = document.getElementById("task-list");
    const markButtons = document.querySelectorAll(".mark-btn");
    
    markButtons.forEach(button => {
        button.addEventListener("click", () => {
            const taskItem = button.parentElement;
            const taskName = taskItem.getAttribute("data-task-name");

            if (!taskName) {
                alert("Task name not found!");
                return;
            }

            $.ajax({
                url: '/teacher/api/mark_task_completed/',
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCsrfToken(),
                    'Content-Type': 'application/json'
                },
                data: JSON.stringify({ task_name: taskName }),
                success: function(response) {
                    console.log("AJAX Success:", response);
                    if (response.success) {
                        alert(response.message);
                        taskItem.remove();
                        if (!taskList.querySelector(".task-item")) {
                            taskList.innerHTML = '<p>No Tasks Available</p>';
                        }
                    } else {
                        alert(response.message);
                    }
                },
                error: function(xhr, status, error) {
                    console.error("AJAX Error:", status, error);
                    alert("An error occurred. Please try again.");
                }
            });
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