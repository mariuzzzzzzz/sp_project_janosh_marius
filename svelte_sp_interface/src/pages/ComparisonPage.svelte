<script>
    let selectedOption = {
      option1: "",
      option2: "",
    };
  
    function updateSelectedOption1() {
      let selectElement = document.getElementById("employeeData");
      selectedOption.option1 = selectElement.options[selectElement.selectedIndex].value;
      console.log(selectedOption);
    }
  
    function updateSelectedOption2() {
      let selectElement = document.getElementById("covidData");
      selectedOption.option2 = selectElement.options[selectElement.selectedIndex].value;
      console.log(selectedOption);
    }
  
    function handleCommit() {
      let x = 0;
      let y = 0;
  
      if (selectedOption.option1 === "overtime" && selectedOption.option2 === "cases") {
        x = 1;
        y = 1;
      } else if (selectedOption.option1 === "overtime" && selectedOption.option2 === "hospitalisation") {
        x = 1;
        y = 2;
      } else if (selectedOption.option1 === "sollist" && selectedOption.option2 === "cases") {
        x = 6;
        y = 1;
      } else {
        x = 6;
        y = 2;
      }

      console.log("x:", x, "y:", y);
    }
  </script>
  
  <h1>Comparison Page</h1>
  
  <select id="employeeData" on:change={updateSelectedOption1}>
    <option value="">data employee</option>
    <option value="overtime">overtime</option>
    <option value="sollist">soll-ist</option>
  </select>
  
  <select id="covidData" on:change={updateSelectedOption2}>
    <option value="">data covid</option>
    <option value="cases">cases</option>
    <option value="hospitalisation">hospitalisation</option>
  </select>
  
  <button on:click={handleCommit}>Commit</button>
  
  {selectedOption.option1}
  {selectedOption.option2}
  
  <style>
    h1 {
      padding-top: 50px;
      padding-bottom: 20px;
    }
  </style>
  