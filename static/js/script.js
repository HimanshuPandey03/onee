// Smooth scroll for nav links
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".nav-links a").forEach(link => {
    link.addEventListener("click", function(e) {
      if(this.hash !== "") {
        e.preventDefault();
        document.querySelector(this.hash).scrollIntoView({ behavior: "smooth" });
      }
    });
  });
});
