document.addEventListener("DOMContentLoaded", function() {
  var repo = "AvizNetworks/ncp-sdk-agents"; // <--- Your 2nd Repo Name
  var container = document.getElementById("second-repo-facts");

  if (container) {
    fetch("https://api.github.com/repos/" + repo)
      .then(function(response) {
        return response.json();
      })
      .then(function(data) {
        // 1. Format Stars
        var stars = data.stargazers_count;
        if (stars > 1000) stars = (stars / 1000).toFixed(1) + "k";

        // 2. Format Forks
        var forks = data.forks_count;
        if (forks > 1000) forks = (forks / 1000).toFixed(1) + "k";

        // 3. Inject HTML (using Material Theme classes)
        container.innerHTML = 
          '<li class="md-source__fact md-source__fact--stars">' + stars + '</li>' +
          '<li class="md-source__fact md-source__fact--forks">' + forks + '</li>';
      })
      .catch(function(error) {
        console.log("Error fetching repo stats:", error);
      });
  }
});