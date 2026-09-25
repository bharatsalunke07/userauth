const toggleButtons = document.querySelectorAll(".toggle-password");

toggleButtons.forEach(function (button) {
    button.addEventListener("click", function () {
        const targetId = button.getAttribute("data-target");
        const passwordInput = document.getElementById(targetId);

        if (passwordInput.type === "password") {
            passwordInput.type = "text";
            button.textContent = "🙈";
        } else {
            passwordInput.type = "password";
            button.textContent = "👁";
        }
    });
});