const { getUserRepos } = require("./github");

// TODO: Enter your GitHub username
const gitHubUser = "JasmineRowe";

getUserRepos(gitHubUser).then((repos) => {
  console.log(repos);
});
